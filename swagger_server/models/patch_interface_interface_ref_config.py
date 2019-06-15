# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref_config import AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig  # noqa: F401,E501
from swagger_server.models.interface_interface_ref_config import InterfaceInterfaceRefConfig  # noqa: F401,E501
from swagger_server import util


class PatchInterfaceInterfaceRefConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig=None):  # noqa: E501
        """PatchInterfaceInterfaceRefConfig - a model defined in Swagger

        :param openconfig_aclconfig: The openconfig_aclconfig of this PatchInterfaceInterfaceRefConfig.  # noqa: E501
        :type openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        """
        self.swagger_types = {
            'openconfig_aclconfig': AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        }

        self.attribute_map = {
            'openconfig_aclconfig': 'openconfig-acl:config'
        }

        self._openconfig_aclconfig = openconfig_aclconfig

    @classmethod
    def from_dict(cls, dikt) -> 'PatchInterfaceInterfaceRefConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patch_interface_interface_ref_config of this PatchInterfaceInterfaceRefConfig.  # noqa: E501
        :rtype: PatchInterfaceInterfaceRefConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclconfig(self) -> AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig:
        """Gets the openconfig_aclconfig of this PatchInterfaceInterfaceRefConfig.


        :return: The openconfig_aclconfig of this PatchInterfaceInterfaceRefConfig.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        """
        return self._openconfig_aclconfig

    @openconfig_aclconfig.setter
    def openconfig_aclconfig(self, openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig):
        """Sets the openconfig_aclconfig of this PatchInterfaceInterfaceRefConfig.


        :param openconfig_aclconfig: The openconfig_aclconfig of this PatchInterfaceInterfaceRefConfig.
        :type openconfig_aclconfig: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        """

        self._openconfig_aclconfig = openconfig_aclconfig
