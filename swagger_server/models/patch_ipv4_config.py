# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_ipv4_config import AclOpenconfigaclaclAclsetsAclentriesIpv4Config  # noqa: F401,E501
from swagger_server.models.ipv4_config import Ipv4Config  # noqa: F401,E501
from swagger_server import util


class PatchIpv4Config(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesIpv4Config=None):  # noqa: E501
        """PatchIpv4Config - a model defined in Swagger

        :param openconfig_aclconfig: The openconfig_aclconfig of this PatchIpv4Config.  # noqa: E501
        :type openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesIpv4Config
        """
        self.swagger_types = {
            'openconfig_aclconfig': AclOpenconfigaclaclAclsetsAclentriesIpv4Config
        }

        self.attribute_map = {
            'openconfig_aclconfig': 'openconfig-acl:config'
        }

        self._openconfig_aclconfig = openconfig_aclconfig

    @classmethod
    def from_dict(cls, dikt) -> 'PatchIpv4Config':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patch_ipv4_config of this PatchIpv4Config.  # noqa: E501
        :rtype: PatchIpv4Config
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclconfig(self) -> AclOpenconfigaclaclAclsetsAclentriesIpv4Config:
        """Gets the openconfig_aclconfig of this PatchIpv4Config.


        :return: The openconfig_aclconfig of this PatchIpv4Config.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesIpv4Config
        """
        return self._openconfig_aclconfig

    @openconfig_aclconfig.setter
    def openconfig_aclconfig(self, openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesIpv4Config):
        """Sets the openconfig_aclconfig of this PatchIpv4Config.


        :param openconfig_aclconfig: The openconfig_aclconfig of this PatchIpv4Config.
        :type openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesIpv4Config
        """

        self._openconfig_aclconfig = openconfig_aclconfig
