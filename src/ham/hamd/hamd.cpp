// Host Account Management
#include <glib.h>               // g_file_test()
#include <glib/gstdio.h>        // g_chdir()
#include <stdio.h>
#include <stdlib.h>             // system()
#include <sys/types.h>          // getpwnam(), getpid()
#include <pwd.h>                // fgetpwent()
#include <string>               // std::string
#include <sstream>              // std::ostringstream
#include <systemd/sd-journal.h> // sd_journal_print()
#include <pwd.h>                // getpwnam(), getpwuid()
#include <grp.h>                // getgrnam(), getgrgid()
#include <shadow.h>             // getspnam()
#include <unistd.h>             // getpid()

#include "hamd.h"               // hamd_c
#include "../shared/utils.h"    // startswith(), streq()
#include "siphash24.h"          // siphash24()

typedef struct
{
    uid_t   euid;
    gid_t   egid;
} credentials_t;

int change_credentials_by_id(uid_t uid, gid_t gid)
{
    int rv;
    rv = setegid(gid);
    if (rv == -1)
    {
        sd_journal_print(LOG_WARNING, "change_credentials_by_id() - Error! setegid() failed");
    }
    else
    {
        rv = seteuid(uid);
        if (rv == -1)
        {
            sd_journal_print(LOG_WARNING, "change_credentials_by_id() - Error! seteuid() failed");
        }
    }

    return rv;
}

int change_credentials_by_name(credentials_t  * original_cred_p, /* Structure to hold old User and Group IDs */
                               const char     * user_p,          /* New user name  */
                               const char     * group_p)         /* New group name */
{
    int              rv;
    struct passwd  * pwd_p;
    struct group   * grp_p;

    // Save old User and Group IDs. This can later be used with
    // change_credentials_by_id() to restore the old credentials.
    original_cred_p->euid = geteuid();
    original_cred_p->egid = getegid();

    pwd_p = getpwnam(user_p); // Get User ID associated with user name.
    if (NULL == pwd_p)
    {
        sd_journal_print(LOG_EMERG, "change_credentials_by_name() - Error! Unable to getpwnam() for user %s.", user_p);
        rv = -1;
    }
    else
    {
        grp_p = getgrnam(group_p); // Get Group ID associated with group name.
        if (NULL == grp_p)
        {
            sd_journal_print(LOG_EMERG, "change_credentials_by_name() - Error! Unable to getgrnam() for user %s.", group_p);
            rv = -1;
        }
        else
        {
            rv = change_credentials_by_id(pwd_p->pw_uid, grp_p->gr_gid);
        }
    }

    return rv;
}


/**
 * @brief DBus adaptor class constructor
 *
 * @param config_r Structure containing configuration parameters
 * @param conn_r
 */
hamd_c::hamd_c(hamd_config_c & config_r, DBus::Connection & conn_r) :
    DBus::ObjectAdaptor(conn_r, DBUS_OBJ_PATH_BASE),
    config_rm(config_r),
    poll_timer_m((double)config_rm.poll_period_sec_m, hamd_c::on_poll_timeout, this)
{
    apply_config();
}

/**
 * @brief This is called when the poll_timer_m expires.
 *
 * @param user_data_p Pointer to user data. In this case this point to the
 *                    hamd_c object.
 * @return bool
 */
bool hamd_c::on_poll_timeout(gpointer user_data_p)
{
    hamd_c * p = static_cast<hamd_c *>(user_data_p);
    LOG_CONDITIONAL(p->is_tron(), LOG_INFO, "hamd_c::on_poll_timeout()");
    p->rm_unconfirmed_users();
    return true; // Return true to repeat timer
}

/**
 * @brief reload configuration and apply to running daemon.
 */
void hamd_c::reload()
{
    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::reload()");
    config_rm.reload();
    apply_config();
}

/**
 * @brief Apply the configuration to the running daemon
 */
void hamd_c::apply_config()
{
    if (config_rm.poll_period_sec_m > 0)
        poll_timer_m.start((double)config_rm.poll_period_sec_m);
    else
        poll_timer_m.stop();
}

/**
 * @brief This is called just before the destructor is called and is used
 *        to clean up all resources in use by the class instance.
 */
void hamd_c::cleanup()
{
    poll_timer_m.stop();
}

#if (0)
/**
 * @brief Scan "/etc/passwd" looking for user. If found, return a pointer
 *        to a "struct passwd" containing all the data related to user.
 *
 * @param fn E.g. /etc/passwd
 * @param user The user we're looking for
 *
 * @return If user found, return a pointer to a struct passwd.
 */
static struct passwd * fgetpwname(const char * login, const char * fname_p="/etc/passwd");
static struct passwd * fgetpwname(const char * login, const char * fname_p)
{
    struct passwd * pwd = NULL;
    FILE          * f   = fopen(fname_p, "re");
    if (f)
    {
        struct passwd * ent;
        while (NULL != (ent = fgetpwent(f)))
        {
            if (streq(ent->pw_name, login))
            {
                pwd = ent;
                break;
            }
        }
        fclose(f);
    }

    return pwd;
}
#endif

std::string hamd_c::certgen(const std::string  & login) const
{
    std::string errmsg = "";

    // Generate certificates
    gchar * certdir = g_build_filename("/home", login.c_str(), ".cert", nullptr);
    if (certdir != nullptr)
    {
        // We're going to run the certificate generation with the user's
        // credentials so that file/dir ownership is reflected properly.
        credentials_t  original_cred;
        if (0 == change_credentials_by_name(&original_cred, login.c_str(), login.c_str()))
        {
            // Make sure certificate directory exists and set permissions to
            // 700 so that only "user" (or root) can access the certificates.
            if (0 == g_mkdir_with_parents(certdir, S_IRWXU)) // 0700
            {
                std::string cmd = config_rm.certgen_cmd(login, certdir);
                LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::certgen() - Generate user \"%s\" certificates [%s]", login.c_str(), cmd.c_str());

                int  rc          = system(cmd.c_str());
                bool term_normal = WIFEXITED(rc);
                int  exit_status = WEXITSTATUS(rc);
                bool success     = term_normal && (exit_status == 0);

                LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::certgen() - Generate user \"%s\" certificates [%s]", login.c_str(), success ? "OK" : "ERROR");

                // Restore credentials
                change_credentials_by_id(original_cred.euid, original_cred.egid);

                if (success)
                {
                    // Set permissions on newly created certificates
                    GDir * dir = g_dir_open(certdir, 0, nullptr);
                    if (dir != nullptr)
                    {
                        gchar       * fullname;
                        const gchar * name;
                        while ((name = g_dir_read_name(dir)) != nullptr)
                        {
                            fullname = g_build_filename(certdir, name, nullptr);
                            if (fullname != nullptr)
                            {
                                g_chmod(fullname, S_IRUSR | S_IWUSR); // 0600
                                g_free(fullname);
                            }
                        }
                        g_dir_close(dir);
                    }
                }
                else
                {
                    errmsg = "Failed to generate certificates for: " + login;
                }
            }
            else
            {
                errmsg = "Failed to create certificate directory: " + std::string(certdir);
            }
        }
        else
        {
            errmsg = "Failed to switch to user " + login;
        }

        g_free(certdir);
    }
    else
    {
        errmsg = "Failed to build certificate directory name";
    }

    return errmsg;
}

/**
 * @brief Create a new user
 */
::DBus::Struct< bool, std::string > hamd_c::useradd(const std::string                & login,
                                                    const std::vector< std::string > & roles,
                                                    const std::string                & hashed_pw)
{
    ::DBus::Struct< bool,       /* success */
                    std::string /* errmsg  */ > ret;

    ret._1 = true; // Let's be optimistic
    ret._2 = "";   // ..and set returned value to success.

    std::string cmd = "/usr/sbin/useradd"
                      " --create-home"
                      " --user-group"
                      " --shell " + config_rm.shell() +
                      " --password '" + hashed_pw + "'"
                      " --groups " + join(roles.cbegin(), roles.cend(), ",", " ") +
                      login;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::useradd() - Create user \"%s\" [%s]", login.c_str(), cmd.c_str());

    int  rc          = system(cmd.c_str());
    bool term_normal = WIFEXITED(rc);

    if (term_normal)
    {
        int  exit_status = WEXITSTATUS(rc);
        bool success     = exit_status == 0;
        if (success)
        {
            LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::useradd() - Create user \"%s\" [OK]", login.c_str());

            ret._2  = certgen(login);
            success = ret._2.length() == 0;
        }
        else
        {
            switch (exit_status)
            {
            case 0:  break;
            case 1:  ret._2 = "can't update password file";               break;
            case 2:  ret._2 = "invalid command syntax";                   break;
            case 3:  ret._2 = "invalid argument to option";               break;
            case 4:  ret._2 = "UID already in use (and no -o)";           break;
            case 6:  ret._2 = "specified group (role) doesn't exist";     break;
            case 9:  ret._2 = "username already in use";                  break;
            case 10: ret._2 = "can't update group (role) file";           break;
            case 12: ret._2 = "can't create home directory";              break;
            case 14: ret._2 = "can't update SELinux user mapping";        break;
            default: ret._2 = "unknown error code " + std::to_string(rc); break;
            }
            LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::useradd() - Create user \"%s\" [%s]", login.c_str(), ret._2.c_str());
        }

        ret._1 = success;
    }
    else
    {
        ret._1 = false;
        ret._2 = strerror(errno);
        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::useradd() - Abnornal command termination, errno=%d (%s)",
                        errno, ret._2.c_str());
    }

    return ret;
}

/**
 * @brief Delete a user account
 */
::DBus::Struct< bool, std::string > hamd_c::userdel(const std::string& login)
{
    std::string  cmd = "/usr/sbin/userdel --force --remove " + login;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::userdel() - executing command \"%s\"", cmd.c_str());

    int  rc          = system(cmd.c_str());
    bool term_normal = WIFEXITED(rc);

    ::DBus::Struct< bool,       /* success */
                    std::string /* errmsg  */ > ret;

    if (term_normal)
    {
        int  exit_status = WEXITSTATUS(rc);

        ret._1 = (exit_status == 0) || (exit_status == 6);

        switch (exit_status)
        {
        case 0:  ret._2 = "";                                         break;
        case 1:  ret._2 = "can't update password file";               break;
        case 2:  ret._2 = "invalid command syntax";                   break;
        case 8:  ret._2 = "user currently logged in";                 break;
        case 10: ret._2 = "can't update group (role) file";           break;
        case 12: ret._2 = "can't remove home directory";              break;
        default: ret._2 = "unknown error code " + std::to_string(rc); break;
        }

        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::userdel() - command returned exit_status=%d (%s)",
                        exit_status, ret._2.c_str());
    }
    else
    {
        ret._1 = false;
        ret._2 = strerror(errno);
        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::userdel() - Abnornal command termination, errno=%d (%s)",
                        errno, ret._2.c_str());
    }

    return ret;
}

/**
 * @brief Change user password
 */
::DBus::Struct< bool, std::string > hamd_c::passwd(const std::string& login, const std::string& hashed_pw)
{
    std::string  cmd = "/usr/sbin/usermod --password " + hashed_pw + ' ' + login;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::passwd() - executing command \"%s\"", cmd.c_str());

    int  rc          = system(cmd.c_str());
    bool term_normal = WIFEXITED(rc);

    ::DBus::Struct< bool,       /* success */
                    std::string /* errmsg  */ > ret;

    if (term_normal)
    {
        int  exit_status = WEXITSTATUS(rc);

        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::passwd() - command returned exit_status=%d",
                        login.c_str(), exit_status);

        ret._1 = exit_status == 0;

        switch (exit_status)
        {
        case 0:  ret._2 = "";                                         break;
        case 1:  ret._2 = "can't update password file";               break;
        case 2:  ret._2 = "invalid command syntax";                   break;
        case 3:  ret._2 = "invalid argument to option";               break;
        case 4:  ret._2 = "UID already in use (and no -o)";           break;
        case 6:  ret._2 = "specified user/group doesn't exist";       break;
        case 8:  ret._2 = "user to modify is logged in";              break;
        case 9:  ret._2 = "username already in use";                  break;
        case 10: ret._2 = "can't update group file";                  break;
        case 12: ret._2 = "unable to complete home dir move";         break;
        case 14: ret._2 = "can't update SELinux user mapping";        break;
        default: ret._2 = "unknown error code " + std::to_string(rc); break;
        }

        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::passwd() - command returned exit_status=%d (%s)",
                        exit_status, ret._2.c_str());
    }
    else
    {
        ret._1 = false;
        ret._2 = strerror(errno);
        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::passwd() - Abnornal command termination, errno=%d (%s)",
                        errno, ret._2.c_str());
    }

    return ret;
}

/**
 * @brief Set user's roles (supplementary groups)
 */
::DBus::Struct< bool, std::string > hamd_c::set_roles(const std::string& login, const std::vector< std::string >& roles)
{
    std::string  cmd = "/usr/sbin/usermod --groups " + join(roles.cbegin(), roles.cend(), ",", " ") + login;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::set_roles() - executing command \"%s\"", cmd.c_str());

    int  rc          = system(cmd.c_str());
    bool term_normal = WIFEXITED(rc);

    ::DBus::Struct< bool,       /* success */
                    std::string /* errmsg  */ > ret;

    if (term_normal)
    {
        int  exit_status = WEXITSTATUS(rc);

        ret._1 = exit_status == 0;

        switch (exit_status)
        {
        case 0:  ret._2 = "";                                         break;
        case 1:  ret._2 = "can't update password file";               break;
        case 2:  ret._2 = "invalid command syntax";                   break;
        case 3:  ret._2 = "invalid argument to option";               break;
        case 4:  ret._2 = "UID already in use (and no -o)";           break;
        case 6:  ret._2 = "specified user/group doesn't exist";       break;
        case 8:  ret._2 = "user to modify is logged in";              break;
        case 9:  ret._2 = "username already in use";                  break;
        case 10: ret._2 = "can't update group file";                  break;
        case 12: ret._2 = "unable to complete home dir move";         break;
        case 14: ret._2 = "can't update SELinux user mapping";        break;
        default: ret._2 = "unknown error code " + std::to_string(rc); break;
        }

        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::set_roles() - command returned exit_status=%d (%s)",
                        exit_status, ret._2.c_str());
    }
    else
    {
        ret._1 = false;
        ret._2 = strerror(errno);
        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::set_roles() - Abnornal command termination, errno=%d (%s)",
                        errno, ret._2.c_str());
    }

    return ret;
}

/**
 * @brief Create a group
 */
::DBus::Struct< bool, std::string > hamd_c::groupadd(const std::string& group)
{
    ::DBus::Struct< bool, std::string > ret;
    ret._1 = false;
    ret._2 = "Not implemented";
    return ret;
}

/**
 * @brief Delete a group
 */
::DBus::Struct< bool, std::string > hamd_c::groupdel(const std::string& group)
{
    ::DBus::Struct< bool, std::string > ret;
    ret._1 = false;
    ret._2 = "Not implemented";
    return ret;
}

::DBus::Struct< bool, std::string, std::string, uint32_t, uint32_t, std::string, std::string, std::string > hamd_c::getpwnam(const std::string& name)
{
    ::DBus::Struct< bool,         /* success   */
                    std::string,  /* pw_name   */
                    std::string,  /* pw_passwd */
                    uint32_t,     /* pw_uid    */
                    uint32_t,     /* pw_gid    */
                    std::string,  /* pw_gecos  */
                    std::string,  /* pw_dir    */
                    std::string > /* pw_shell  */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getpwnam(%s)", name.c_str());

    struct passwd * p = ::getpwnam(name.c_str());

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2 = p->pw_name;
        ret._3 = p->pw_passwd;
        ret._4 = p->pw_uid;
        ret._5 = p->pw_gid;
        ret._6 = p->pw_gecos;
        ret._7 = p->pw_dir;
        ret._8 = p->pw_shell;
    }

    return ret;
}

::DBus::Struct< bool, std::string, std::string, uint32_t, uint32_t, std::string, std::string, std::string > hamd_c::getpwuid(const uint32_t& uid)
{
    ::DBus::Struct< bool,         /* success   */
                    std::string,  /* pw_name   */
                    std::string,  /* pw_passwd */
                    uint32_t,     /* pw_uid    */
                    uint32_t,     /* pw_gid    */
                    std::string,  /* pw_gecos  */
                    std::string,  /* pw_dir    */
                    std::string > /* pw_shell  */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getpwuid(%u)", uid);

    struct passwd * p = ::getpwuid(uid);

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2 = p->pw_name;
        ret._3 = p->pw_passwd;
        ret._4 = p->pw_uid;
        ret._5 = p->pw_gid;
        ret._6 = p->pw_gecos;
        ret._7 = p->pw_dir;
        ret._8 = p->pw_shell;
    }

    return ret;
}

::DBus::Struct< bool, std::string, std::string, uint32_t, std::vector< std::string > > hamd_c::getgrnam(const std::string& name)
{
    ::DBus::Struct< bool,                        /* success   */
                    std::string,                 /* gr_name   */
                    std::string,                 /* gr_passwd */
                    uint32_t,                    /* gr_gid    */
                    std::vector< std::string > > /* gr_mem    */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getgrnam(%s)", name.c_str());

    struct group * p = ::getgrnam(name.c_str());

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2 = p->gr_name;
        ret._3 = p->gr_passwd;
        ret._4 = p->gr_gid;

        for (unsigned i = 0; p->gr_mem[i] != NULL; i++)
            ret._5.push_back(p->gr_mem[i]);
    }

    return ret;
}

::DBus::Struct< bool, std::string, std::string, uint32_t, std::vector< std::string > > hamd_c::getgrgid(const uint32_t& gid)
{
    ::DBus::Struct< bool,                        /* success   */
                    std::string,                 /* gr_name   */
                    std::string,                 /* gr_passwd */
                    uint32_t,                    /* gr_gid    */
                    std::vector< std::string > > /* gr_mem    */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getgrgid(%u)", gid);

    struct group * p = ::getgrgid(gid);

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2 = p->gr_name;
        ret._3 = p->gr_passwd;
        ret._4 = p->gr_gid;

        for (unsigned i = 0; p->gr_mem[i] != NULL; i++)
            ret._5.push_back(p->gr_mem[i]);
    }

    return ret;
}

::DBus::Struct< bool, std::string, std::string, int32_t, int32_t, int32_t, int32_t, int32_t, int32_t, uint32_t > hamd_c::getspnam(const std::string& name)
{
    ::DBus::Struct< bool,        /* success   */
                    std::string, /* sp_namp   */
                    std::string, /* sp_pwdp   */
                    int32_t,     /* sp_lstchg */
                    int32_t,     /* sp_min    */
                    int32_t,     /* sp_max    */
                    int32_t,     /* sp_warn   */
                    int32_t,     /* sp_inact  */
                    int32_t,     /* sp_expire */
                    uint32_t >   /* sp_flag   */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getspnam(%s)", name.c_str());

    struct spwd * p = ::getspnam(name.c_str());

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2  = p->sp_namp;
        ret._3  = p->sp_pwdp;
        ret._4  = p->sp_lstchg;
        ret._5  = p->sp_min;
        ret._6  = p->sp_max;
        ret._7  = p->sp_warn;
        ret._8  = p->sp_inact;
        ret._9  = p->sp_expire;
        ret._10 = p->sp_flag;
    }

    return ret;
}

/**
 * @brief Remove unconfirmed users from /etc/passwd. Unconfirmed users have
 *        the string "Unconfirmed sac user [PID]" in their GECOS string and
 *        the PID does not exist anymore.
 */
void hamd_c::rm_unconfirmed_users() const
{
    FILE  * f = fopen("/etc/passwd", "re");
    if (f)
    {
        struct passwd * ent;
        std::string     base_cmd("/usr/sbin/userdel --remove ");
        std::string     full_cmd;
        g_chdir("/proc");
        while (NULL != (ent = fgetpwent(f)))
        {
            const char * pid_p;
            if ((ent->pw_uid >= (uid_t)config_rm.sac_uid_min_m) && (ent->pw_uid <= (uid_t)config_rm.sac_uid_max_m) &&
                (NULL != (pid_p = startswith(ent->pw_gecos, "Unconfirmed system-assigned credentials "))))
            {
                if (!g_file_test(pid_p, G_FILE_TEST_EXISTS))
                {
                    // Directory does not exist, which means process does not
                    // exist either. Let's remove this user which was never
                    // confirmed by PAM authentification.
                    full_cmd = base_cmd + ent->pw_name;
                    int ret = system(full_cmd.c_str());
                    if (!WIFEXITED(ret) || (WEXITSTATUS(ret) != 0))
                    {
                        sd_journal_print(LOG_ERR, "User \"%s\": Failed to removed unconfirmed user UID=%d",
                                         ent->pw_name, ent->pw_uid);
                    }
                }
            }
        }
        fclose(f);
    }
}

/**
 * @brief This is a DBus interface used by remote programs to add an
 *        unconfirmed user.
 *
 * @param username  Username to be added
 * @param pid       PID of the caller.
 *
 * @return bool     true if user was added successfully,
 *                  false otherwise.
 */
bool hamd_c::add_unconfirmed_user(const std::string& username, const uint32_t& pid)
{
    // First, let's check if there are any
    // unconfirmed users that could be removed.
    rm_unconfirmed_users();

    // Next, add <username> as an unconfirmed user.
    static const uint8_t hash_key[] =
    {
        0x37, 0x53, 0x7e, 0x31, 0xcf, 0xce, 0x48, 0xf5,
        0x8a, 0xbb, 0x39, 0x57, 0x8d, 0xd9, 0xec, 0x59
    };

    unsigned     n_tries;
    uid_t        candidate;
    std::string  name(username);
    std::string  full_cmd;
    std::string  base_cmd = "/usr/sbin/useradd"
                            " --create-home"
                            " --no-user-group"
                            " --shell /usr/bin/klish"
                            " --user-group"
                            " --comment \"Unconfirmed system-assigned credentials " + std::to_string(pid) + '"';

    for (n_tries = 0; n_tries < 100; n_tries++) /* Give up retrying eventually */
    {
        // Find a unique UID in the range sac_uid_min_m..sac_uid_max_m.
        // We use a hash function to always get the same ID for a given user
        // name. Hash collisions (i.e. two user names with the same hash) will
        // be handled by trying with a slightly different username.
        candidate = config_rm.uid_fit_into_range(siphash24(name.c_str(), name.length(), hash_key));

        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": attempt %d using name \"%s\", candidate UID=%lu",
                        username.c_str(), n_tries, name.c_str(), (unsigned long)candidate);

        // Note: The range 60000-64999 is reserved on Debian platforms
        //       and should be avoided and the value 65535 is traditionally
        //       reserved as an "error" code.
        if (!((candidate >= 60000) && (candidate <= 64999)) &&
             (candidate != 65535) &&
            !::getpwuid(candidate)) /* make sure not already allocated */
        {
            full_cmd = base_cmd + " --uid " + std::to_string(candidate) + ' ' + username;

            LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": executing \"%s\"", username.c_str(), full_cmd.c_str());

            int  rc          = system(full_cmd.c_str());
            bool term_normal = WIFEXITED(rc);
            int  exit_status = WEXITSTATUS(rc);

            LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": command returned term_normal=%s, exit_status=%d, errno=%d (%s)",
                            username.c_str(), term_normal ? "true" : "false", exit_status, errno, strerror(errno));

            return term_normal && (0 == exit_status) ? true : false;
        }
        else
        {
            // Try with a slightly different name
            name = username + std::to_string(n_tries);
            LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": candidate UID=%lu already in use. Retry with name = \"%s\"",
                            username.c_str(), (unsigned long)candidate, name.c_str());
        }
    }

    sd_journal_print(LOG_ERR, "User \"%s\": unable to create unconfirmed user after %d attempts",
                     username.c_str(), n_tries);

    return false;
}

/**
 * @brief  Generate ssh keys
 *
 * @param  username_p   user name
 *
 * @return true if successful, false otherwise.
 */
static bool generate_certs(const std::string username)
{
    static const char * fname_p = "/usr/bin/certgen";
    if (!g_file_test(fname_p, G_FILE_TEST_EXISTS))
        return false;

    std::string cmd         = "/bin/sh " + (fname_p + (' ' + username));
    int         ret         = system(cmd.c_str());
    bool        term_normal = WIFEXITED(ret);
    int         exit_status = WEXITSTATUS(ret);
    bool        ok          = term_normal && (exit_status == 0) ? true : false;

    if (!ok)
    {
        sd_journal_print(LOG_ERR, "User %s: Failed to run \"%s\". term_normal=%s, exit_status=%d, errno=%d (%s)",
                         username.c_str(), cmd.c_str(), term_normal ? "true" : "false", exit_status,
                         errno, strerror(errno));
    }

    return ok;
}

/**
 * @brief This is a DBus interface used by remote programs to confirm a
 *        user.
 *
 * @param username  Username to be confirmed
 * @param groupname User's Primary group
 * @param groups    User's Supplementory groups (comma-separated list)
 * @param label     Label to be added in the comment (e.g. "RADIUS",
 *                  "TACACS+", "AAA", etc...)
 *
 * @return bool     true if user was confirmed successfully,
 *                  false otherwise.
 */
bool hamd_c::confirm_user(const std::string& username, const std::string& groupname, const std::string& groups, const std::string& label)
{
    std::string  cmd("/usr/sbin/usermod --comment \"Automagic user");

    if (label.length() != 0)
        cmd += ' ' + label;

    cmd += '"';

    if (groups.length() != 0)
        cmd += " --append --groups " + groups;

    cmd += " --gid " + groupname + ' ' + username;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": executing \"%s\"", username.c_str(), cmd.c_str());

    int  rc          = system(cmd.c_str());
    bool term_normal = WIFEXITED(rc);
    int  exit_status = WEXITSTATUS(rc);

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": command returned term_normal=%s, exit_status=%d, errno=%d (%s)",
                    username.c_str(), term_normal ? "true" : "false", exit_status, errno, strerror(errno));

    bool ok = term_normal && (0 == exit_status);

    if (ok)
        ok = generate_certs(username);

    return ok;
}

/**
 * @brief This is a DBus interface used to turn tracing on. This allows
 *        the daemon to run with verbosity turned on.
 *
 * @return std::string
 */
std::string hamd_c::tron()
{
    config_rm.tron_m = true;
    return "Tracing is now ON";
}

/**
 * @brief This is a DBus interface used to turn tracing off. This allows
 *        the daemon to run with verbosity turned off.
 *
 * @return std::string
 */
std::string hamd_c::troff()
{
    config_rm.tron_m = false;
    return "Tracing is now OFF";
}

/**
 * @brief This is a DBus interface used to retrieve daemon running info
 *
 * @return std::string
 */
std::string hamd_c::show()
{
    std::ostringstream  dbg;
    dbg << "PID                       = " << getpid() << '\n'
        << "conf_file_pm              = " << config_rm.conf_file_pm << '\n'
        << "certgen_cmd_m             = " << config_rm.certgen_cmd_m << '\n'
        << "poll_period_sec_m         = " << std::to_string(config_rm.poll_period_sec_m)  << "s\n"
        << "poll_timer_m              = " << poll_timer_m << '\n'
        << "sac_uid_min_m             = " << std::to_string(config_rm.sac_uid_min_m) << '\n'
        << "sac_uid_max_m             = " << std::to_string(config_rm.sac_uid_max_m) << '\n'
        << "sac_uid_range_m           = " << std::to_string(config_rm.sac_uid_range_m)  << '\n'
        << "shell_m                   = " << config_rm.shell_m << '\n'
        << "tron_m                    = " << true_false(config_rm.tron_m) << '\n';
        //<< "\n"
        //<< "Defaults:                 = "
        //<< "conf_file_default_pm      = " << config_rm.conf_file_default_pm << '\n'
        //<< "certgen_cmd_default_m     = " << config_rm.certgen_cmd_default_m << '\n'
        //<< "poll_period_sec_default_m = " << std::to_string(config_rm.poll_period_sec_default_m)  << "s\n"
        //<< "sac_uid_min_default_m     = " << std::to_string(config_rm.sac_uid_min_default_m) << '\n'
        //<< "sac_uid_max_default_m     = " << std::to_string(config_rm.sac_uid_max_default_m) << '\n'
        //<< "shell_default_m           = " << config_rm.shell_default_m << '\n'
        //<< "tron_default_m            = " << (config_rm.tron_default_m ? "true" : "false") << '\n';

    return dbg.str();
}