#!/usr/bin/python
###########################################################################
#
# Copyright 2019 Dell, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###########################################################################

import sys
import cli_client as cc
from rpipe_utils import pipestr
from scripts.render_cli import show_cli_output

import urllib3
urllib3.disable_warnings()

#For interface to VRF mapping
vrfDict = {}

def get_keypath(func,args):
    keypath = None
    instance = None
    body = None

    if func == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors':
        keypath = cc.Path('/restconf/data/openconfig-interfaces:interfaces/interface={name}/subinterfaces/subinterface={index}/openconfig-if-ip:ipv4/neighbors', name=args[1], index="0")
    elif func == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors':
        keypath = cc.Path('/restconf/data/openconfig-interfaces:interfaces/interface={name}/subinterfaces/subinterface={index}/openconfig-if-ip:ipv6/neighbors', name=args[1], index="0")
    elif func == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor':
        keypath = cc.Path('/restconf/data/openconfig-interfaces:interfaces/interface={name}/subinterfaces/subinterface={index}/openconfig-if-ip:ipv4/neighbors/neighbor={ip}', name=args[1], index="0", ip=args[3])
    elif func == 'get_openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor':
        keypath = cc.Path('/restconf/data/openconfig-interfaces:interfaces/interface={name}/subinterfaces/subinterface={index}/openconfig-if-ip:ipv6/neighbors/neighbor={ip}',name=args[1], index="0", ip=args[3])
    elif func == 'get_sonic_neigh_sonic_neigh_neigh_table':
        keypath = cc.Path('/restconf/data/sonic-neighbor:sonic-neighbor/NEIGH_TABLE')
    elif func == 'rpc_sonic_clear_neighbors':
        keypath = cc.Path('/restconf/operations/sonic-neighbor:clear-neighbors')
        if (len (args) == 2):
            body = {"sonic-neighbor:input":{"family": args[0], "force": args[1], "ip": "", "ifname": ""}}
        elif (len (args) == 3):
            body = {"sonic-neighbor:input":{"family": args[0], "force": args[1], "ip": args[2], "ifname": ""}}
        elif (len (args) == 4):
            body = {"sonic-neighbor:input":{"family": args[0], "force": args[1], "ip": "", "ifname": args[3]}}

    return keypath, body

def get_egress_port(macAddr, vlanName):
    aa = cc.ApiClient()

    vlanId = vlanName[len("Vlan"):]
    macAddr = macAddr.strip()

    keypath = cc.Path('/restconf/data/openconfig-network-instance:network-instances/network-instance={name}/fdb/mac-table/entries/entry={macaddress},{vlan}', name='default', macaddress=macAddr, vlan=vlanId)

    try:
        response = aa.get(keypath)
        response = response.content

        if 'openconfig-network-instance:entry' in response.keys():
                instance = response['openconfig-network-instance:entry'][0]['interface']['interface-ref']['state']['interface']

        if instance is not None:
                return instance
        return "-"

    except:
        return "-"

def build_vrf_list():
    aa = cc.ApiClient()

    tIntf = ("/restconf/data/sonic-interface:sonic-interface/INTERFACE/", "sonic-interface:INTERFACE", "INTERFACE_LIST","portname")
    tVlanIntf = ("/restconf/data/sonic-vlan-interface:sonic-vlan-interface/VLAN_INTERFACE/", "sonic-vlan-interface:VLAN_INTERFACE", "VLAN_INTERFACE_LIST","vlanName")
    tPortChannelIntf = ("/restconf/data/sonic-portchannel-interface:sonic-portchannel-interface/PORTCHANNEL_INTERFACE/", "sonic-portchannel-interface:PORTCHANNEL_INTERFACE", "PORTCHANNEL_INTERFACE_LIST", "pch_name")
    tMgmtIntf = ("/restconf/data/sonic-mgmt-interface:sonic-mgmt-interface/MGMT_INTERFACE/", "sonic-mgmt-interface:MGMT_INTERFACE", "MGMT_INTERFACE_LIST", "portname")

    requests = [tIntf, tVlanIntf, tPortChannelIntf, tMgmtIntf]

    for request in requests:
        keypath = cc.Path(request[0])

        try:
            response = aa.get(keypath)
            response = response.content

            intfsContainer = response.get(request[1])
            if intfsContainer is None:
                continue

            intfsList = intfsContainer.get(request[2])
            if intfsList is None:
                continue

            for intf in intfsList:
                portName = intf.get(request[3])
                vrfName = intf.get('vrf_name')
                if len(portName) > 0 and len(vrfName) > 0:
                    vrfDict[portName] = vrfName

        except Exception as e:
            print "Error in getting interfaces: ", e

def process_single_nbr(response, args):
    nbr_list = []
    ext_intf_name = "-"
    nbr = response['openconfig-if-ip:neighbor']

    if nbr[0]['state'] is None:
      return

    ipAddr = nbr[0]['state']['ip']
    if ipAddr is None:
        return

    macAddr = nbr[0]['state']['link-layer-address']
    if macAddr is None:
        return

    if args[1].startswith('Vlan'):
      ext_intf_name = get_egress_port(macAddr, args[1])

    nbr_table_entry = {'ipAddr':ipAddr,
                       'macAddr':macAddr,
                       'intfName':args[1],
                       'extIntfName':ext_intf_name
                     }
    nbr_list.append(nbr_table_entry)
    return nbr_list

def process_nbrs_intf(response, args):
    nbr_list = []
    if response['openconfig-if-ip:neighbors'] is None:
        return

    nbrs = response['openconfig-if-ip:neighbors']['neighbor']
    if nbrs is None:
        return

    for nbr in nbrs:
        ext_intf_name = "-"
        ipAddr = nbr['state']['ip']
        if ipAddr is None:
            return[]

        macAddr = nbr['state']['link-layer-address']
        if macAddr is None:
            return[]

        if args[1].startswith('Vlan'):
            ext_intf_name = get_egress_port(macAddr, args[1])

        nbr_table_entry = {'ipAddr':ipAddr,
                            'macAddr':macAddr,
                            'intfName':args[1],
                            'extIntfName':ext_intf_name
                          }
        nbr_list.append(nbr_table_entry)

    return nbr_list

def process_sonic_nbrs(response, args):
    nbr_list = []
    vrfName = ""

    if response['sonic-neighbor:NEIGH_TABLE'] is None:
        return

    nbrs = response['sonic-neighbor:NEIGH_TABLE']['NEIGH_TABLE_LIST']
    if nbrs is None:
        return

    if len(args) == 4 and args[2] == "vrf":
	    build_vrf_list()

    for nbr in nbrs:
        ext_intf_name = "-"

        family = nbr.get('family')
        if family is None:
            return []

        if family != args[1]:
            continue

        ifName = nbr.get('ifname')
        if ifName is None:
            return []

        ipAddr = nbr.get('ip')
        if ipAddr is None:
            return []

        macAddr = nbr.get('neigh')
        if macAddr is None:
            return []

        if len(args) == 4 and args[2] == "vrf":
            vrfName = vrfDict.get(ifName)

        if ifName.startswith('Vlan'):
            ext_intf_name = get_egress_port(macAddr, ifName)

        nbr_table_entry = {'ipAddr':ipAddr,
                           'macAddr':macAddr,
                           'intfName':ifName,
                           'extIntfName':ext_intf_name
                        }
        if (len(args) == 4):
            if (args[2] == "mac" and args[3] == macAddr):
                nbr_list.append(nbr_table_entry)
            if (args[2] == "vrf" and args[3] == vrfName):
                nbr_list.append(nbr_table_entry)
        elif (len(args) == 3 and args[2] != "summary"):
            if args[2] == ipAddr:
                nbr_list.append(nbr_table_entry)
        else:
            nbr_list.append(nbr_table_entry)

    return nbr_list

def run(func, args):
    aa = cc.ApiClient()

    # create a body block
    keypath, body = get_keypath(func, args)
    nbr_list = []

    try:
        if (func == 'rpc_sonic_clear_neighbors'):
            api_response = aa.post(keypath, body)
        else:
            api_response = aa.get(keypath)
    except:
        # system/network error
        print "Error: Unable to connect to the server"

    try:
        if api_response.ok():
            response = api_response.content
        else:
            return

        if response is None:
            return

        if 'openconfig-if-ip:neighbor' in response.keys():
            nbr_list = process_single_nbr(response, args)
        elif 'openconfig-if-ip:neighbors' in response.keys():
            nbr_list = process_nbrs_intf(response, args)
        elif 'sonic-neighbor:NEIGH_TABLE' in response.keys():
            nbr_list = process_sonic_nbrs(response, args)
        elif 'sonic-neighbor:output' in response.keys():
            status = response['sonic-neighbor:output']
            status = status['response']
            if (status != "Success"):
                print status
            return
        else:
            return
	if (len(args) == 3 and args[2] == "summary"):
            show_cli_output(args[0], len(nbr_list))
	else:
            show_cli_output(args[0], nbr_list)
        return
    except Exception as e:
        print "Error: ",  e

if __name__ == '__main__':
    pipestr().write(sys.argv)
    run(sys.argv[1], sys.argv[2:])


