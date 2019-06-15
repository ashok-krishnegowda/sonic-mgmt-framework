# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_acl_openconfigaclacl_interfaces_ingressaclsets_aclentries_state import GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState  # noqa: F401,E501
from swagger_server import util


class GetAclEntriesAclEntryState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclstate: GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState=None):  # noqa: E501
        """GetAclEntriesAclEntryState - a model defined in Swagger

        :param openconfig_aclstate: The openconfig_aclstate of this GetAclEntriesAclEntryState.  # noqa: E501
        :type openconfig_aclstate: GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState
        """
        self.swagger_types = {
            'openconfig_aclstate': GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState
        }

        self.attribute_map = {
            'openconfig_aclstate': 'openconfig-acl:state'
        }

        self._openconfig_aclstate = openconfig_aclstate

    @classmethod
    def from_dict(cls, dikt) -> 'GetAclEntriesAclEntryState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_acl_entries_acl_entry_state of this GetAclEntriesAclEntryState.  # noqa: E501
        :rtype: GetAclEntriesAclEntryState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclstate(self) -> GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState:
        """Gets the openconfig_aclstate of this GetAclEntriesAclEntryState.


        :return: The openconfig_aclstate of this GetAclEntriesAclEntryState.
        :rtype: GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState
        """
        return self._openconfig_aclstate

    @openconfig_aclstate.setter
    def openconfig_aclstate(self, openconfig_aclstate: GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState):
        """Sets the openconfig_aclstate of this GetAclEntriesAclEntryState.


        :param openconfig_aclstate: The openconfig_aclstate of this GetAclEntriesAclEntryState.
        :type openconfig_aclstate: GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentriesState
        """

        self._openconfig_aclstate = openconfig_aclstate
