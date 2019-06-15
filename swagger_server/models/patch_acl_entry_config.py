# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_entry_config import AclEntryConfig  # noqa: F401,E501
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_config import AclOpenconfigaclaclAclsetsAclentriesConfig  # noqa: F401,E501
from swagger_server import util


class PatchAclEntryConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesConfig=None):  # noqa: E501
        """PatchAclEntryConfig - a model defined in Swagger

        :param openconfig_aclconfig: The openconfig_aclconfig of this PatchAclEntryConfig.  # noqa: E501
        :type openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesConfig
        """
        self.swagger_types = {
            'openconfig_aclconfig': AclOpenconfigaclaclAclsetsAclentriesConfig
        }

        self.attribute_map = {
            'openconfig_aclconfig': 'openconfig-acl:config'
        }

        self._openconfig_aclconfig = openconfig_aclconfig

    @classmethod
    def from_dict(cls, dikt) -> 'PatchAclEntryConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patch_acl_entry_config of this PatchAclEntryConfig.  # noqa: E501
        :rtype: PatchAclEntryConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclconfig(self) -> AclOpenconfigaclaclAclsetsAclentriesConfig:
        """Gets the openconfig_aclconfig of this PatchAclEntryConfig.


        :return: The openconfig_aclconfig of this PatchAclEntryConfig.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesConfig
        """
        return self._openconfig_aclconfig

    @openconfig_aclconfig.setter
    def openconfig_aclconfig(self, openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesConfig):
        """Sets the openconfig_aclconfig of this PatchAclEntryConfig.


        :param openconfig_aclconfig: The openconfig_aclconfig of this PatchAclEntryConfig.
        :type openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesConfig
        """

        self._openconfig_aclconfig = openconfig_aclconfig
