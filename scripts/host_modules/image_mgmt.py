""" Image management handler"""
import host_service
import subprocess

MOD_NAME= 'image_mgmt'

class IMAGE_MGMT(host_service.HostModule):
    """DBus endpoint that executes CFG_MGMT related commands """

    @staticmethod
    def _run_command(options):
        """ Run config mgmt command """
        cmd = ['/usr/bin/sonic_installer']
        for x in options:
            if x == "-mgmt":
                cmd.insert(0, 'cgexec')
                cmd.insert(1, '-g')
                cmd.insert(2, 'l3mdev:mgmt')
            else :
                cmd.append(str(x))
            
        output =""
        try:
            print("cmd", cmd)
            rc = 0
            output= subprocess.check_output(cmd)
            print('Output -> ',output)

        except subprocess.CalledProcessError as err:
            print("Exception when calling get_sonic_error -> %s\n" %(err))
            rc = err.returncode
            output = err.output
            
        return rc, output

    @host_service.method(host_service.bus_name(MOD_NAME), in_signature='as', out_signature='is')
    def action(self, options):
        return IMAGE_MGMT._run_command(options)
        
def register():
    """Return class name"""
    return IMAGE_MGMT, MOD_NAME
