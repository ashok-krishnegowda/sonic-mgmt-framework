# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_transport_config import AclOpenconfigaclaclAclsetsAclentriesTransportConfig  # noqa: F401,E501
from swagger_server import util


class GetTransportState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclstate: AclOpenconfigaclaclAclsetsAclentriesTransportConfig=None):  # noqa: E501
        """GetTransportState - a model defined in Swagger

        :param openconfig_aclstate: The openconfig_aclstate of this GetTransportState.  # noqa: E501
        :type openconfig_aclstate: AclOpenconfigaclaclAclsetsAclentriesTransportConfig
        """
        self.swagger_types = {
            'openconfig_aclstate': AclOpenconfigaclaclAclsetsAclentriesTransportConfig
        }

        self.attribute_map = {
            'openconfig_aclstate': 'openconfig-acl:state'
        }

        self._openconfig_aclstate = openconfig_aclstate

    @classmethod
    def from_dict(cls, dikt) -> 'GetTransportState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_transport_state of this GetTransportState.  # noqa: E501
        :rtype: GetTransportState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclstate(self) -> AclOpenconfigaclaclAclsetsAclentriesTransportConfig:
        """Gets the openconfig_aclstate of this GetTransportState.


        :return: The openconfig_aclstate of this GetTransportState.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesTransportConfig
        """
        return self._openconfig_aclstate

    @openconfig_aclstate.setter
    def openconfig_aclstate(self, openconfig_aclstate: AclOpenconfigaclaclAclsetsAclentriesTransportConfig):
        """Sets the openconfig_aclstate of this GetTransportState.


        :param openconfig_aclstate: The openconfig_aclstate of this GetTransportState.
        :type openconfig_aclstate: AclOpenconfigaclaclAclsetsAclentriesTransportConfig
        """

        self._openconfig_aclstate = openconfig_aclstate
