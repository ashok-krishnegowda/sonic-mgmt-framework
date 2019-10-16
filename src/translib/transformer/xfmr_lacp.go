package transformer

import (
        "encoding/json"
	"translib/ocbinds"
        "os/exec"

	log "github.com/golang/glog"
	"github.com/openconfig/ygot/ygot"
)

func init () {
    XlateFuncBind("DbToYang_lacp_get_specific_xfmr", DbToYang_lacp_get_specific_xfmr)
}

func getLacpRoot (s *ygot.GoStruct) *ocbinds.OpenconfigLacp_Lacp {
    deviceObj := (*s).(*ocbinds.Device)
    return deviceObj.Lacp
}

func populateLacpData(ifKey string, state *ocbinds.OpenconfigLacp_Lacp_Interfaces_Interface_State,
                                    members *ocbinds.OpenconfigLacp_Lacp_Interfaces_Interface_Members) bool {
    cmd := exec.Command("docker", "exec", "teamd", "teamdctl", ifKey, "state", "dump")
    out_stream, err := cmd.StdoutPipe()
    if err != nil {
        log.Fatalf("Can't get stdout pipe: %s\n", err)
        return false
    }
    err = cmd.Start()
    if err != nil {
        log.Fatalf("cmd.Start() failed with %s\n", err)
        return false
    }

    var TeamdJson map[string]interface{}

    err = json.NewDecoder(out_stream).Decode(&TeamdJson)
    if err != nil {
        log.Fatalf("Not able to decode teamd json output: %s\n", err)
        return false
    }

    err = cmd.Wait()
    if err != nil {
        log.Fatalf("Command execution completion failed with %s\n", err)
        return false
    }

    runner_map := TeamdJson["runner"].(map[string]interface{})

    prio := runner_map["sys_prio"].(float64)
    sys_prio := uint16(prio)
    state.SystemPriority = &sys_prio

    fast_rate := runner_map["fast_rate"].(bool)
    if fast_rate {
	state.Interval = ocbinds.OpenconfigLacp_LacpPeriodType_FAST
    } else {
        state.Interval = ocbinds.OpenconfigLacp_LacpPeriodType_SLOW
    }

    active := runner_map["active"].(bool)
    if active {
        state.LacpMode = ocbinds.OpenconfigLacp_LacpActivityType_ACTIVE
    } else {
        state.LacpMode = ocbinds.OpenconfigLacp_LacpActivityType_PASSIVE
    }

    team_device := TeamdJson["team_device"].(map[string]interface{})
    team_device_ifinfo := team_device["ifinfo"].(map[string]interface{})
    SystemIdMac := team_device_ifinfo["dev_addr"].(string)
    state.SystemIdMac = &SystemIdMac

    var lacpMemberObj *ocbinds.OpenconfigLacp_Lacp_Interfaces_Interface_Members_Member

    ygot.BuildEmptyTree(members)

    ports_map := TeamdJson["ports"].(map[string]interface{})
    for ifKey := range ports_map {
        lacpMemberObj, _ = members.NewMember(ifKey)
        ygot.BuildEmptyTree(lacpMemberObj)

       member_map := ports_map[ifKey].(map[string]interface{})
       port_runner := member_map["runner"].(map[string]interface{})
       actor := port_runner["actor_lacpdu_info"].(map[string]interface{})

       port_num := actor["port"].(float64)
       pport_num := uint16(port_num)
       lacpMemberObj.State.PortNum = &pport_num

       system_id := actor["system"].(string)
       lacpMemberObj.State.SystemId = &system_id

       oper_key := actor["key"].(float64)
       ooper_key := uint16(oper_key)
       lacpMemberObj.State.OperKey = &ooper_key

       partner := port_runner["partner_lacpdu_info"].(map[string]interface{})
       partner_port_num := partner["port"].(float64)
       ppartner_num := uint16(partner_port_num)
       lacpMemberObj.State.PartnerPortNum = &ppartner_num

       partner_system_id := partner["system"].(string)
       lacpMemberObj.State.PartnerId = &partner_system_id

       partner_oper_key := partner["key"].(float64)
       ppartner_key := uint16(partner_oper_key)
       lacpMemberObj.State.PartnerKey = &ppartner_key

    }

    return true
}

var DbToYang_lacp_get_specific_xfmr  SubTreeXfmrDbToYang = func(inParams XfmrParams) error {

    lacpIntfsObj := getLacpRoot(inParams.ygRoot)
    pathInfo := NewPathInfo(inParams.uri)
    ifKey := pathInfo.Var("name")

    targetUriPath, err := getYangPathFromUri(pathInfo.Path)

    log.Infof("Received GET for path: %s; template: %s vars: %v targetUriPath: %s ifKey: %s", pathInfo.Path, pathInfo.Template, pathInfo.Vars, targetUriPath, ifKey)

    var ok bool
    var lacpintfObj *ocbinds.OpenconfigLacp_Lacp_Interfaces_Interface

    /* Request for a specific portchannel */
    if lacpIntfsObj.Interfaces.Interface != nil && len(lacpIntfsObj.Interfaces.Interface) > 0 {
        lacpintfObj, ok = lacpIntfsObj.Interfaces.Interface[ifKey]
        if !ok {
            lacpintfObj, _ = lacpIntfsObj.Interfaces.NewInterface(ifKey)
        }

    } else {
        ygot.BuildEmptyTree(lacpIntfsObj)
        lacpintfObj, _ = lacpIntfsObj.Interfaces.NewInterface(ifKey)
    }
    ygot.BuildEmptyTree(lacpintfObj)

    populateLacpData(ifKey, lacpintfObj.State, lacpintfObj.Members)

    return err

}
