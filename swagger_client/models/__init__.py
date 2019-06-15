# coding: utf-8

# flake8: noqa
"""
    Sonic NMS

    Network management Open APIs for Broadcom's Sonic.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: mohammed.faraaz@broadcom.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.acl import Acl
from swagger_client.models.acl_acl_sets import AclAclSets
from swagger_client.models.acl_acl_sets_acl_set import AclAclSetsAclSet
from swagger_client.models.acl_acl_sets_acl_set_openconfigaclaclset import AclAclSetsAclSetOpenconfigaclaclset
from swagger_client.models.acl_entry_actions import AclEntryActions
from swagger_client.models.acl_entry_config import AclEntryConfig
from swagger_client.models.acl_entry_config_description import AclEntryConfigDescription
from swagger_client.models.acl_entry_input_interface import AclEntryInputInterface
from swagger_client.models.acl_entry_ipv4 import AclEntryIpv4
from swagger_client.models.acl_entry_ipv6 import AclEntryIpv6
from swagger_client.models.acl_entry_l2 import AclEntryL2
from swagger_client.models.acl_entry_transport import AclEntryTransport
from swagger_client.models.acl_interfaces import AclInterfaces
from swagger_client.models.acl_interfaces_interface import AclInterfacesInterface
from swagger_client.models.acl_interfaces_interface_openconfigaclinterface import AclInterfacesInterfaceOpenconfigaclinterface
from swagger_client.models.acl_openconfigaclacl import AclOpenconfigaclacl
from swagger_client.models.acl_openconfigaclacl_aclsets import AclOpenconfigaclaclAclsets
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries import AclOpenconfigaclaclAclsetsAclentries
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_aclentry import AclOpenconfigaclaclAclsetsAclentriesAclentry
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_actions import AclOpenconfigaclaclAclsetsAclentriesActions
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_actions_config import AclOpenconfigaclaclAclsetsAclentriesActionsConfig
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_config import AclOpenconfigaclaclAclsetsAclentriesConfig
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface import AclOpenconfigaclaclAclsetsAclentriesInputinterface
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref import AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref_config import AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_ipv4 import AclOpenconfigaclaclAclsetsAclentriesIpv4
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_ipv4_config import AclOpenconfigaclaclAclsetsAclentriesIpv4Config
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_ipv6 import AclOpenconfigaclaclAclsetsAclentriesIpv6
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_ipv6_config import AclOpenconfigaclaclAclsetsAclentriesIpv6Config
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_l2 import AclOpenconfigaclaclAclsetsAclentriesL2
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_l2_config import AclOpenconfigaclaclAclsetsAclentriesL2Config
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_transport import AclOpenconfigaclaclAclsetsAclentriesTransport
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_transport_config import AclOpenconfigaclaclAclsetsAclentriesTransportConfig
from swagger_client.models.acl_openconfigaclacl_aclsets_aclset import AclOpenconfigaclaclAclsetsAclset
from swagger_client.models.acl_openconfigaclacl_aclsets_config import AclOpenconfigaclaclAclsetsConfig
from swagger_client.models.acl_openconfigaclacl_interfaces import AclOpenconfigaclaclInterfaces
from swagger_client.models.acl_openconfigaclacl_interfaces_config import AclOpenconfigaclaclInterfacesConfig
from swagger_client.models.acl_openconfigaclacl_interfaces_egressaclsets import AclOpenconfigaclaclInterfacesEgressaclsets
from swagger_client.models.acl_openconfigaclacl_interfaces_ingressaclsets import AclOpenconfigaclaclInterfacesIngressaclsets
from swagger_client.models.acl_openconfigaclacl_interfaces_ingressaclsets_config import AclOpenconfigaclaclInterfacesIngressaclsetsConfig
from swagger_client.models.acl_openconfigaclacl_interfaces_ingressaclsets_ingressaclset import AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset
from swagger_client.models.acl_openconfigaclacl_interfaces_interface import AclOpenconfigaclaclInterfacesInterface
from swagger_client.models.acl_set_acl_entries import AclSetAclEntries
from swagger_client.models.acl_set_acl_entries_acl_entry import AclSetAclEntriesAclEntry
from swagger_client.models.acl_set_acl_entries_acl_entry_openconfigaclaclentry import AclSetAclEntriesAclEntryOpenconfigaclaclentry
from swagger_client.models.acl_set_config import AclSetConfig
from swagger_client.models.actions_config import ActionsConfig
from swagger_client.models.config_description import ConfigDescription
from swagger_client.models.config_destination_address import ConfigDestinationAddress
from swagger_client.models.config_destination_flow_label import ConfigDestinationFlowLabel
from swagger_client.models.config_destination_mac import ConfigDestinationMac
from swagger_client.models.config_destination_mac_mask import ConfigDestinationMacMask
from swagger_client.models.config_destination_port import ConfigDestinationPort
from swagger_client.models.config_dscp import ConfigDscp
from swagger_client.models.config_ethertype import ConfigEthertype
from swagger_client.models.config_forwarding_action import ConfigForwardingAction
from swagger_client.models.config_hop_limit import ConfigHopLimit
from swagger_client.models.config_id import ConfigId
from swagger_client.models.config_interface import ConfigInterface
from swagger_client.models.config_log_action import ConfigLogAction
from swagger_client.models.config_name import ConfigName
from swagger_client.models.config_protocol import ConfigProtocol
from swagger_client.models.config_sequence_id import ConfigSequenceId
from swagger_client.models.config_set_name import ConfigSetName
from swagger_client.models.config_source_address import ConfigSourceAddress
from swagger_client.models.config_source_flow_label import ConfigSourceFlowLabel
from swagger_client.models.config_source_mac import ConfigSourceMac
from swagger_client.models.config_source_mac_mask import ConfigSourceMacMask
from swagger_client.models.config_source_port import ConfigSourcePort
from swagger_client.models.config_subinterface import ConfigSubinterface
from swagger_client.models.config_tcp_flags import ConfigTcpFlags
from swagger_client.models.config_type import ConfigType
from swagger_client.models.egress_acl_set_config import EgressAclSetConfig
from swagger_client.models.egress_acl_set_config_set_name import EgressAclSetConfigSetName
from swagger_client.models.egress_acl_set_config_type import EgressAclSetConfigType
from swagger_client.models.get_acl import GetAcl
from swagger_client.models.get_acl_acl_sets import GetAclAclSets
from swagger_client.models.get_acl_acl_sets_acl_set import GetAclAclSetsAclSet
from swagger_client.models.get_acl_acl_sets_acl_set_openconfigaclaclset import GetAclAclSetsAclSetOpenconfigaclaclset
from swagger_client.models.get_acl_entries_acl_entry_state import GetAclEntriesAclEntryState
from swagger_client.models.get_acl_entries_acl_entry_state_matched_octets import GetAclEntriesAclEntryStateMatchedOctets
from swagger_client.models.get_acl_entries_acl_entry_state_matched_packets import GetAclEntriesAclEntryStateMatchedPackets
from swagger_client.models.get_acl_entries_acl_entry_state_sequence_id import GetAclEntriesAclEntryStateSequenceId
from swagger_client.models.get_acl_entry_actions import GetAclEntryActions
from swagger_client.models.get_acl_entry_config import GetAclEntryConfig
from swagger_client.models.get_acl_entry_config_description import GetAclEntryConfigDescription
from swagger_client.models.get_acl_entry_input_interface import GetAclEntryInputInterface
from swagger_client.models.get_acl_entry_ipv4 import GetAclEntryIpv4
from swagger_client.models.get_acl_entry_ipv6 import GetAclEntryIpv6
from swagger_client.models.get_acl_entry_l2 import GetAclEntryL2
from swagger_client.models.get_acl_entry_state import GetAclEntryState
from swagger_client.models.get_acl_entry_state_description import GetAclEntryStateDescription
from swagger_client.models.get_acl_entry_state_matched_octets import GetAclEntryStateMatchedOctets
from swagger_client.models.get_acl_entry_state_matched_packets import GetAclEntryStateMatchedPackets
from swagger_client.models.get_acl_entry_state_sequence_id import GetAclEntryStateSequenceId
from swagger_client.models.get_acl_entry_transport import GetAclEntryTransport
from swagger_client.models.get_acl_interfaces import GetAclInterfaces
from swagger_client.models.get_acl_interfaces_interface import GetAclInterfacesInterface
from swagger_client.models.get_acl_interfaces_interface_openconfigaclinterface import GetAclInterfacesInterfaceOpenconfigaclinterface
from swagger_client.models.get_acl_openconfigaclacl import GetAclOpenconfigaclacl
from swagger_client.models.get_acl_openconfigaclacl_aclsets import GetAclOpenconfigaclaclAclsets
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries import GetAclOpenconfigaclaclAclsetsAclentries
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_aclentry import GetAclOpenconfigaclaclAclsetsAclentriesAclentry
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_actions import GetAclOpenconfigaclaclAclsetsAclentriesActions
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_inputinterface import GetAclOpenconfigaclaclAclsetsAclentriesInputinterface
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref import GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_ipv4 import GetAclOpenconfigaclaclAclsetsAclentriesIpv4
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_ipv6 import GetAclOpenconfigaclaclAclsetsAclentriesIpv6
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_l2 import GetAclOpenconfigaclaclAclsetsAclentriesL2
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_state import GetAclOpenconfigaclaclAclsetsAclentriesState
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_transport import GetAclOpenconfigaclaclAclsetsAclentriesTransport
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclset import GetAclOpenconfigaclaclAclsetsAclset
from swagger_client.models.get_acl_openconfigaclacl_interfaces import GetAclOpenconfigaclaclInterfaces
from swagger_client.models.get_acl_openconfigaclacl_interfaces_egressaclsets import GetAclOpenconfigaclaclInterfacesEgressaclsets
from swagger_client.models.get_acl_openconfigaclacl_interfaces_ingressaclsets import GetAclOpenconfigaclaclInterfacesIngressaclsets
from swagger_client.models.get_acl_openconfigaclacl_interfaces_ingressaclsets_aclentries import GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentries
from swagger_client.models.get_acl_openconfigaclacl_interfaces_ingressaclsets_aclentries_aclentry import GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesAclentry
from swagger_client.models.get_acl_openconfigaclacl_interfaces_ingressaclsets_aclentries_state import GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState
from swagger_client.models.get_acl_openconfigaclacl_interfaces_ingressaclsets_ingressaclset import GetAclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset
from swagger_client.models.get_acl_openconfigaclacl_interfaces_interface import GetAclOpenconfigaclaclInterfacesInterface
from swagger_client.models.get_acl_openconfigaclacl_state import GetAclOpenconfigaclaclState
from swagger_client.models.get_acl_set_acl_entries import GetAclSetAclEntries
from swagger_client.models.get_acl_set_acl_entries_acl_entry import GetAclSetAclEntriesAclEntry
from swagger_client.models.get_acl_set_acl_entries_acl_entry_openconfigaclaclentry import GetAclSetAclEntriesAclEntryOpenconfigaclaclentry
from swagger_client.models.get_acl_set_config import GetAclSetConfig
from swagger_client.models.get_acl_set_state import GetAclSetState
from swagger_client.models.get_acl_state import GetAclState
from swagger_client.models.get_actions_config import GetActionsConfig
from swagger_client.models.get_actions_state import GetActionsState
from swagger_client.models.get_config_description import GetConfigDescription
from swagger_client.models.get_config_destination_address import GetConfigDestinationAddress
from swagger_client.models.get_config_destination_flow_label import GetConfigDestinationFlowLabel
from swagger_client.models.get_config_destination_mac import GetConfigDestinationMac
from swagger_client.models.get_config_destination_mac_mask import GetConfigDestinationMacMask
from swagger_client.models.get_config_destination_port import GetConfigDestinationPort
from swagger_client.models.get_config_dscp import GetConfigDscp
from swagger_client.models.get_config_ethertype import GetConfigEthertype
from swagger_client.models.get_config_forwarding_action import GetConfigForwardingAction
from swagger_client.models.get_config_hop_limit import GetConfigHopLimit
from swagger_client.models.get_config_id import GetConfigId
from swagger_client.models.get_config_interface import GetConfigInterface
from swagger_client.models.get_config_log_action import GetConfigLogAction
from swagger_client.models.get_config_name import GetConfigName
from swagger_client.models.get_config_protocol import GetConfigProtocol
from swagger_client.models.get_config_sequence_id import GetConfigSequenceId
from swagger_client.models.get_config_set_name import GetConfigSetName
from swagger_client.models.get_config_source_address import GetConfigSourceAddress
from swagger_client.models.get_config_source_flow_label import GetConfigSourceFlowLabel
from swagger_client.models.get_config_source_mac import GetConfigSourceMac
from swagger_client.models.get_config_source_mac_mask import GetConfigSourceMacMask
from swagger_client.models.get_config_source_port import GetConfigSourcePort
from swagger_client.models.get_config_subinterface import GetConfigSubinterface
from swagger_client.models.get_config_tcp_flags import GetConfigTcpFlags
from swagger_client.models.get_config_type import GetConfigType
from swagger_client.models.get_egress_acl_set_acl_entries import GetEgressAclSetAclEntries
from swagger_client.models.get_egress_acl_set_acl_entries_acl_entry_state import GetEgressAclSetAclEntriesAclEntryState
from swagger_client.models.get_egress_acl_set_config import GetEgressAclSetConfig
from swagger_client.models.get_egress_acl_set_config_set_name import GetEgressAclSetConfigSetName
from swagger_client.models.get_egress_acl_set_config_type import GetEgressAclSetConfigType
from swagger_client.models.get_egress_acl_set_state import GetEgressAclSetState
from swagger_client.models.get_egress_acl_set_state_set_name import GetEgressAclSetStateSetName
from swagger_client.models.get_egress_acl_set_state_type import GetEgressAclSetStateType
from swagger_client.models.get_egress_acl_sets_egress_acl_set_acl_entries_acl_entry import GetEgressAclSetsEgressAclSetAclEntriesAclEntry
from swagger_client.models.get_ingress_acl_set_acl_entries import GetIngressAclSetAclEntries
from swagger_client.models.get_ingress_acl_set_config import GetIngressAclSetConfig
from swagger_client.models.get_ingress_acl_set_config_type import GetIngressAclSetConfigType
from swagger_client.models.get_ingress_acl_set_state import GetIngressAclSetState
from swagger_client.models.get_ingress_acl_set_state_type import GetIngressAclSetStateType
from swagger_client.models.get_ingress_acl_sets_ingress_acl_set_acl_entries_acl_entry import GetIngressAclSetsIngressAclSetAclEntriesAclEntry
from swagger_client.models.get_ingress_acl_sets_ingress_acl_set_acl_entries_acl_entry_openconfigaclaclentry import GetIngressAclSetsIngressAclSetAclEntriesAclEntryOpenconfigaclaclentry
from swagger_client.models.get_input_interface_interface_ref import GetInputInterfaceInterfaceRef
from swagger_client.models.get_interface_config import GetInterfaceConfig
from swagger_client.models.get_interface_egress_acl_sets import GetInterfaceEgressAclSets
from swagger_client.models.get_interface_egress_acl_sets_egress_acl_set import GetInterfaceEgressAclSetsEgressAclSet
from swagger_client.models.get_interface_ingress_acl_sets import GetInterfaceIngressAclSets
from swagger_client.models.get_interface_ingress_acl_sets_ingress_acl_set import GetInterfaceIngressAclSetsIngressAclSet
from swagger_client.models.get_interface_ingress_acl_sets_ingress_acl_set_openconfigaclingressaclset import GetInterfaceIngressAclSetsIngressAclSetOpenconfigaclingressaclset
from swagger_client.models.get_interface_interface_ref import GetInterfaceInterfaceRef
from swagger_client.models.get_interface_interface_ref_config import GetInterfaceInterfaceRefConfig
from swagger_client.models.get_interface_interface_ref_state import GetInterfaceInterfaceRefState
from swagger_client.models.get_interface_ref_config import GetInterfaceRefConfig
from swagger_client.models.get_interface_ref_config_interface import GetInterfaceRefConfigInterface
from swagger_client.models.get_interface_ref_config_subinterface import GetInterfaceRefConfigSubinterface
from swagger_client.models.get_interface_ref_state import GetInterfaceRefState
from swagger_client.models.get_interface_ref_state_interface import GetInterfaceRefStateInterface
from swagger_client.models.get_interface_ref_state_subinterface import GetInterfaceRefStateSubinterface
from swagger_client.models.get_interface_state import GetInterfaceState
from swagger_client.models.get_ipv4_config import GetIpv4Config
from swagger_client.models.get_ipv4_state import GetIpv4State
from swagger_client.models.get_ipv6_config import GetIpv6Config
from swagger_client.models.get_ipv6_config_destination_address import GetIpv6ConfigDestinationAddress
from swagger_client.models.get_ipv6_config_dscp import GetIpv6ConfigDscp
from swagger_client.models.get_ipv6_config_hop_limit import GetIpv6ConfigHopLimit
from swagger_client.models.get_ipv6_config_protocol import GetIpv6ConfigProtocol
from swagger_client.models.get_ipv6_config_source_address import GetIpv6ConfigSourceAddress
from swagger_client.models.get_ipv6_state import GetIpv6State
from swagger_client.models.get_ipv6_state_destination_address import GetIpv6StateDestinationAddress
from swagger_client.models.get_ipv6_state_dscp import GetIpv6StateDscp
from swagger_client.models.get_ipv6_state_hop_limit import GetIpv6StateHopLimit
from swagger_client.models.get_ipv6_state_protocol import GetIpv6StateProtocol
from swagger_client.models.get_ipv6_state_source_address import GetIpv6StateSourceAddress
from swagger_client.models.get_l2_config import GetL2Config
from swagger_client.models.get_l2_state import GetL2State
from swagger_client.models.get_list_base_acl_entries_acl_entry import GetListBaseAclEntriesAclEntry
from swagger_client.models.get_list_base_acl_sets_acl_set import GetListBaseAclSetsAclSet
from swagger_client.models.get_list_base_egress_acl_set_acl_entries_acl_entry import GetListBaseEgressAclSetAclEntriesAclEntry
from swagger_client.models.get_list_base_egress_acl_sets_egress_acl_set import GetListBaseEgressAclSetsEgressAclSet
from swagger_client.models.get_list_base_ingress_acl_set_acl_entries_acl_entry import GetListBaseIngressAclSetAclEntriesAclEntry
from swagger_client.models.get_list_base_ingress_acl_sets_ingress_acl_set import GetListBaseIngressAclSetsIngressAclSet
from swagger_client.models.get_list_base_interfaces_interface import GetListBaseInterfacesInterface
from swagger_client.models.get_state_counter_capability import GetStateCounterCapability
from swagger_client.models.get_state_description import GetStateDescription
from swagger_client.models.get_state_destination_address import GetStateDestinationAddress
from swagger_client.models.get_state_destination_flow_label import GetStateDestinationFlowLabel
from swagger_client.models.get_state_destination_mac import GetStateDestinationMac
from swagger_client.models.get_state_destination_mac_mask import GetStateDestinationMacMask
from swagger_client.models.get_state_destination_port import GetStateDestinationPort
from swagger_client.models.get_state_dscp import GetStateDscp
from swagger_client.models.get_state_ethertype import GetStateEthertype
from swagger_client.models.get_state_forwarding_action import GetStateForwardingAction
from swagger_client.models.get_state_hop_limit import GetStateHopLimit
from swagger_client.models.get_state_id import GetStateId
from swagger_client.models.get_state_interface import GetStateInterface
from swagger_client.models.get_state_log_action import GetStateLogAction
from swagger_client.models.get_state_matched_octets import GetStateMatchedOctets
from swagger_client.models.get_state_matched_packets import GetStateMatchedPackets
from swagger_client.models.get_state_name import GetStateName
from swagger_client.models.get_state_protocol import GetStateProtocol
from swagger_client.models.get_state_sequence_id import GetStateSequenceId
from swagger_client.models.get_state_set_name import GetStateSetName
from swagger_client.models.get_state_source_address import GetStateSourceAddress
from swagger_client.models.get_state_source_flow_label import GetStateSourceFlowLabel
from swagger_client.models.get_state_source_mac import GetStateSourceMac
from swagger_client.models.get_state_source_mac_mask import GetStateSourceMacMask
from swagger_client.models.get_state_source_port import GetStateSourcePort
from swagger_client.models.get_state_subinterface import GetStateSubinterface
from swagger_client.models.get_state_tcp_flags import GetStateTcpFlags
from swagger_client.models.get_state_type import GetStateType
from swagger_client.models.get_transport_config import GetTransportConfig
from swagger_client.models.get_transport_state import GetTransportState
from swagger_client.models.ingress_acl_set_config import IngressAclSetConfig
from swagger_client.models.ingress_acl_set_config_type import IngressAclSetConfigType
from swagger_client.models.input_interface_interface_ref import InputInterfaceInterfaceRef
from swagger_client.models.interface_config import InterfaceConfig
from swagger_client.models.interface_egress_acl_sets import InterfaceEgressAclSets
from swagger_client.models.interface_egress_acl_sets_egress_acl_set import InterfaceEgressAclSetsEgressAclSet
from swagger_client.models.interface_ingress_acl_sets import InterfaceIngressAclSets
from swagger_client.models.interface_ingress_acl_sets_ingress_acl_set import InterfaceIngressAclSetsIngressAclSet
from swagger_client.models.interface_ingress_acl_sets_ingress_acl_set_openconfigaclingressaclset import InterfaceIngressAclSetsIngressAclSetOpenconfigaclingressaclset
from swagger_client.models.interface_interface_ref import InterfaceInterfaceRef
from swagger_client.models.interface_interface_ref_config import InterfaceInterfaceRefConfig
from swagger_client.models.interface_ref_config import InterfaceRefConfig
from swagger_client.models.interface_ref_config_interface import InterfaceRefConfigInterface
from swagger_client.models.interface_ref_config_subinterface import InterfaceRefConfigSubinterface
from swagger_client.models.ipv4_config import Ipv4Config
from swagger_client.models.ipv6_config import Ipv6Config
from swagger_client.models.ipv6_config_destination_address import Ipv6ConfigDestinationAddress
from swagger_client.models.ipv6_config_dscp import Ipv6ConfigDscp
from swagger_client.models.ipv6_config_hop_limit import Ipv6ConfigHopLimit
from swagger_client.models.ipv6_config_protocol import Ipv6ConfigProtocol
from swagger_client.models.ipv6_config_source_address import Ipv6ConfigSourceAddress
from swagger_client.models.l2_config import L2Config
from swagger_client.models.list_base_acl_entries_acl_entry import ListBaseAclEntriesAclEntry
from swagger_client.models.list_base_acl_sets_acl_set import ListBaseAclSetsAclSet
from swagger_client.models.list_base_egress_acl_sets_egress_acl_set import ListBaseEgressAclSetsEgressAclSet
from swagger_client.models.list_base_ingress_acl_sets_ingress_acl_set import ListBaseIngressAclSetsIngressAclSet
from swagger_client.models.list_base_interfaces_interface import ListBaseInterfacesInterface
from swagger_client.models.patch_acl import PatchAcl
from swagger_client.models.patch_acl_acl_sets import PatchAclAclSets
from swagger_client.models.patch_acl_acl_sets_acl_set import PatchAclAclSetsAclSet
from swagger_client.models.patch_acl_entry_actions import PatchAclEntryActions
from swagger_client.models.patch_acl_entry_config import PatchAclEntryConfig
from swagger_client.models.patch_acl_entry_config_description import PatchAclEntryConfigDescription
from swagger_client.models.patch_acl_entry_input_interface import PatchAclEntryInputInterface
from swagger_client.models.patch_acl_entry_ipv4 import PatchAclEntryIpv4
from swagger_client.models.patch_acl_entry_ipv6 import PatchAclEntryIpv6
from swagger_client.models.patch_acl_entry_l2 import PatchAclEntryL2
from swagger_client.models.patch_acl_entry_transport import PatchAclEntryTransport
from swagger_client.models.patch_acl_interfaces import PatchAclInterfaces
from swagger_client.models.patch_acl_interfaces_interface import PatchAclInterfacesInterface
from swagger_client.models.patch_acl_set_acl_entries import PatchAclSetAclEntries
from swagger_client.models.patch_acl_set_acl_entries_acl_entry import PatchAclSetAclEntriesAclEntry
from swagger_client.models.patch_acl_set_config import PatchAclSetConfig
from swagger_client.models.patch_actions_config import PatchActionsConfig
from swagger_client.models.patch_config_description import PatchConfigDescription
from swagger_client.models.patch_config_destination_address import PatchConfigDestinationAddress
from swagger_client.models.patch_config_destination_flow_label import PatchConfigDestinationFlowLabel
from swagger_client.models.patch_config_destination_mac import PatchConfigDestinationMac
from swagger_client.models.patch_config_destination_mac_mask import PatchConfigDestinationMacMask
from swagger_client.models.patch_config_destination_port import PatchConfigDestinationPort
from swagger_client.models.patch_config_dscp import PatchConfigDscp
from swagger_client.models.patch_config_ethertype import PatchConfigEthertype
from swagger_client.models.patch_config_forwarding_action import PatchConfigForwardingAction
from swagger_client.models.patch_config_hop_limit import PatchConfigHopLimit
from swagger_client.models.patch_config_id import PatchConfigId
from swagger_client.models.patch_config_interface import PatchConfigInterface
from swagger_client.models.patch_config_log_action import PatchConfigLogAction
from swagger_client.models.patch_config_name import PatchConfigName
from swagger_client.models.patch_config_protocol import PatchConfigProtocol
from swagger_client.models.patch_config_sequence_id import PatchConfigSequenceId
from swagger_client.models.patch_config_set_name import PatchConfigSetName
from swagger_client.models.patch_config_source_address import PatchConfigSourceAddress
from swagger_client.models.patch_config_source_flow_label import PatchConfigSourceFlowLabel
from swagger_client.models.patch_config_source_mac import PatchConfigSourceMac
from swagger_client.models.patch_config_source_mac_mask import PatchConfigSourceMacMask
from swagger_client.models.patch_config_source_port import PatchConfigSourcePort
from swagger_client.models.patch_config_subinterface import PatchConfigSubinterface
from swagger_client.models.patch_config_tcp_flags import PatchConfigTcpFlags
from swagger_client.models.patch_config_type import PatchConfigType
from swagger_client.models.patch_egress_acl_set_config import PatchEgressAclSetConfig
from swagger_client.models.patch_egress_acl_set_config_set_name import PatchEgressAclSetConfigSetName
from swagger_client.models.patch_egress_acl_set_config_type import PatchEgressAclSetConfigType
from swagger_client.models.patch_ingress_acl_set_config import PatchIngressAclSetConfig
from swagger_client.models.patch_ingress_acl_set_config_type import PatchIngressAclSetConfigType
from swagger_client.models.patch_input_interface_interface_ref import PatchInputInterfaceInterfaceRef
from swagger_client.models.patch_interface_config import PatchInterfaceConfig
from swagger_client.models.patch_interface_egress_acl_sets import PatchInterfaceEgressAclSets
from swagger_client.models.patch_interface_egress_acl_sets_egress_acl_set import PatchInterfaceEgressAclSetsEgressAclSet
from swagger_client.models.patch_interface_ingress_acl_sets import PatchInterfaceIngressAclSets
from swagger_client.models.patch_interface_ingress_acl_sets_ingress_acl_set import PatchInterfaceIngressAclSetsIngressAclSet
from swagger_client.models.patch_interface_interface_ref import PatchInterfaceInterfaceRef
from swagger_client.models.patch_interface_interface_ref_config import PatchInterfaceInterfaceRefConfig
from swagger_client.models.patch_interface_ref_config import PatchInterfaceRefConfig
from swagger_client.models.patch_interface_ref_config_interface import PatchInterfaceRefConfigInterface
from swagger_client.models.patch_interface_ref_config_subinterface import PatchInterfaceRefConfigSubinterface
from swagger_client.models.patch_ipv4_config import PatchIpv4Config
from swagger_client.models.patch_ipv6_config import PatchIpv6Config
from swagger_client.models.patch_ipv6_config_destination_address import PatchIpv6ConfigDestinationAddress
from swagger_client.models.patch_ipv6_config_dscp import PatchIpv6ConfigDscp
from swagger_client.models.patch_ipv6_config_hop_limit import PatchIpv6ConfigHopLimit
from swagger_client.models.patch_ipv6_config_protocol import PatchIpv6ConfigProtocol
from swagger_client.models.patch_ipv6_config_source_address import PatchIpv6ConfigSourceAddress
from swagger_client.models.patch_l2_config import PatchL2Config
from swagger_client.models.patch_list_base_acl_entries_acl_entry import PatchListBaseAclEntriesAclEntry
from swagger_client.models.patch_list_base_acl_sets_acl_set import PatchListBaseAclSetsAclSet
from swagger_client.models.patch_list_base_egress_acl_sets_egress_acl_set import PatchListBaseEgressAclSetsEgressAclSet
from swagger_client.models.patch_list_base_ingress_acl_sets_ingress_acl_set import PatchListBaseIngressAclSetsIngressAclSet
from swagger_client.models.patch_list_base_interfaces_interface import PatchListBaseInterfacesInterface
from swagger_client.models.patch_transport_config import PatchTransportConfig
from swagger_client.models.post_acl import PostAcl
from swagger_client.models.post_acl_acl_sets import PostAclAclSets
from swagger_client.models.post_acl_entry_config import PostAclEntryConfig
from swagger_client.models.post_acl_set_config import PostAclSetConfig
from swagger_client.models.post_actions_config import PostActionsConfig
from swagger_client.models.post_config_forwarding_action import PostConfigForwardingAction
from swagger_client.models.post_config_id import PostConfigId
from swagger_client.models.post_config_interface import PostConfigInterface
from swagger_client.models.post_config_name import PostConfigName
from swagger_client.models.post_config_sequence_id import PostConfigSequenceId
from swagger_client.models.post_config_set_name import PostConfigSetName
from swagger_client.models.post_config_source_address import PostConfigSourceAddress
from swagger_client.models.post_config_source_mac import PostConfigSourceMac
from swagger_client.models.post_config_source_port import PostConfigSourcePort
from swagger_client.models.post_egress_acl_set_config import PostEgressAclSetConfig
from swagger_client.models.post_egress_acl_set_config_set_name import PostEgressAclSetConfigSetName
from swagger_client.models.post_ingress_acl_set_config import PostIngressAclSetConfig
from swagger_client.models.post_input_interface_interface_ref import PostInputInterfaceInterfaceRef
from swagger_client.models.post_interface_config import PostInterfaceConfig
from swagger_client.models.post_interface_interface_ref_config import PostInterfaceInterfaceRefConfig
from swagger_client.models.post_interface_ref_config import PostInterfaceRefConfig
from swagger_client.models.post_interface_ref_config_interface import PostInterfaceRefConfigInterface
from swagger_client.models.post_ipv4_config import PostIpv4Config
from swagger_client.models.post_ipv6_config import PostIpv6Config
from swagger_client.models.post_ipv6_config_source_address import PostIpv6ConfigSourceAddress
from swagger_client.models.post_l2_config import PostL2Config
from swagger_client.models.post_list_base_acl_entries_acl_entry import PostListBaseAclEntriesAclEntry
from swagger_client.models.post_list_base_acl_sets_acl_set import PostListBaseAclSetsAclSet
from swagger_client.models.post_list_base_egress_acl_sets_egress_acl_set import PostListBaseEgressAclSetsEgressAclSet
from swagger_client.models.post_list_base_ingress_acl_sets_ingress_acl_set import PostListBaseIngressAclSetsIngressAclSet
from swagger_client.models.post_list_base_interfaces_interface import PostListBaseInterfacesInterface
from swagger_client.models.post_transport_config import PostTransportConfig
from swagger_client.models.put_acl import PutAcl
from swagger_client.models.put_acl_acl_sets import PutAclAclSets
from swagger_client.models.put_acl_acl_sets_acl_set import PutAclAclSetsAclSet
from swagger_client.models.put_acl_entry_actions import PutAclEntryActions
from swagger_client.models.put_acl_entry_config import PutAclEntryConfig
from swagger_client.models.put_acl_entry_config_description import PutAclEntryConfigDescription
from swagger_client.models.put_acl_entry_input_interface import PutAclEntryInputInterface
from swagger_client.models.put_acl_entry_ipv4 import PutAclEntryIpv4
from swagger_client.models.put_acl_entry_ipv6 import PutAclEntryIpv6
from swagger_client.models.put_acl_entry_l2 import PutAclEntryL2
from swagger_client.models.put_acl_entry_transport import PutAclEntryTransport
from swagger_client.models.put_acl_interfaces import PutAclInterfaces
from swagger_client.models.put_acl_interfaces_interface import PutAclInterfacesInterface
from swagger_client.models.put_acl_set_acl_entries import PutAclSetAclEntries
from swagger_client.models.put_acl_set_acl_entries_acl_entry import PutAclSetAclEntriesAclEntry
from swagger_client.models.put_acl_set_config import PutAclSetConfig
from swagger_client.models.put_actions_config import PutActionsConfig
from swagger_client.models.put_config_description import PutConfigDescription
from swagger_client.models.put_config_destination_address import PutConfigDestinationAddress
from swagger_client.models.put_config_destination_flow_label import PutConfigDestinationFlowLabel
from swagger_client.models.put_config_destination_mac import PutConfigDestinationMac
from swagger_client.models.put_config_destination_mac_mask import PutConfigDestinationMacMask
from swagger_client.models.put_config_destination_port import PutConfigDestinationPort
from swagger_client.models.put_config_dscp import PutConfigDscp
from swagger_client.models.put_config_ethertype import PutConfigEthertype
from swagger_client.models.put_config_forwarding_action import PutConfigForwardingAction
from swagger_client.models.put_config_hop_limit import PutConfigHopLimit
from swagger_client.models.put_config_id import PutConfigId
from swagger_client.models.put_config_interface import PutConfigInterface
from swagger_client.models.put_config_log_action import PutConfigLogAction
from swagger_client.models.put_config_name import PutConfigName
from swagger_client.models.put_config_protocol import PutConfigProtocol
from swagger_client.models.put_config_sequence_id import PutConfigSequenceId
from swagger_client.models.put_config_set_name import PutConfigSetName
from swagger_client.models.put_config_source_address import PutConfigSourceAddress
from swagger_client.models.put_config_source_flow_label import PutConfigSourceFlowLabel
from swagger_client.models.put_config_source_mac import PutConfigSourceMac
from swagger_client.models.put_config_source_mac_mask import PutConfigSourceMacMask
from swagger_client.models.put_config_source_port import PutConfigSourcePort
from swagger_client.models.put_config_subinterface import PutConfigSubinterface
from swagger_client.models.put_config_tcp_flags import PutConfigTcpFlags
from swagger_client.models.put_config_type import PutConfigType
from swagger_client.models.put_egress_acl_set_config import PutEgressAclSetConfig
from swagger_client.models.put_egress_acl_set_config_set_name import PutEgressAclSetConfigSetName
from swagger_client.models.put_egress_acl_set_config_type import PutEgressAclSetConfigType
from swagger_client.models.put_ingress_acl_set_config import PutIngressAclSetConfig
from swagger_client.models.put_ingress_acl_set_config_type import PutIngressAclSetConfigType
from swagger_client.models.put_input_interface_interface_ref import PutInputInterfaceInterfaceRef
from swagger_client.models.put_interface_config import PutInterfaceConfig
from swagger_client.models.put_interface_egress_acl_sets import PutInterfaceEgressAclSets
from swagger_client.models.put_interface_egress_acl_sets_egress_acl_set import PutInterfaceEgressAclSetsEgressAclSet
from swagger_client.models.put_interface_ingress_acl_sets import PutInterfaceIngressAclSets
from swagger_client.models.put_interface_ingress_acl_sets_ingress_acl_set import PutInterfaceIngressAclSetsIngressAclSet
from swagger_client.models.put_interface_interface_ref import PutInterfaceInterfaceRef
from swagger_client.models.put_interface_interface_ref_config import PutInterfaceInterfaceRefConfig
from swagger_client.models.put_interface_ref_config import PutInterfaceRefConfig
from swagger_client.models.put_interface_ref_config_interface import PutInterfaceRefConfigInterface
from swagger_client.models.put_interface_ref_config_subinterface import PutInterfaceRefConfigSubinterface
from swagger_client.models.put_ipv4_config import PutIpv4Config
from swagger_client.models.put_ipv6_config import PutIpv6Config
from swagger_client.models.put_ipv6_config_destination_address import PutIpv6ConfigDestinationAddress
from swagger_client.models.put_ipv6_config_dscp import PutIpv6ConfigDscp
from swagger_client.models.put_ipv6_config_hop_limit import PutIpv6ConfigHopLimit
from swagger_client.models.put_ipv6_config_protocol import PutIpv6ConfigProtocol
from swagger_client.models.put_ipv6_config_source_address import PutIpv6ConfigSourceAddress
from swagger_client.models.put_l2_config import PutL2Config
from swagger_client.models.put_list_base_acl_entries_acl_entry import PutListBaseAclEntriesAclEntry
from swagger_client.models.put_list_base_acl_sets_acl_set import PutListBaseAclSetsAclSet
from swagger_client.models.put_list_base_egress_acl_sets_egress_acl_set import PutListBaseEgressAclSetsEgressAclSet
from swagger_client.models.put_list_base_ingress_acl_sets_ingress_acl_set import PutListBaseIngressAclSetsIngressAclSet
from swagger_client.models.put_list_base_interfaces_interface import PutListBaseInterfacesInterface
from swagger_client.models.put_transport_config import PutTransportConfig
from swagger_client.models.transport_config import TransportConfig
