# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_interfaces_config import AclOpenconfigaclaclInterfacesConfig  # noqa: F401,E501
from swagger_server import util


class InterfaceConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclconfig: AclOpenconfigaclaclInterfacesConfig=None):  # noqa: E501
        """InterfaceConfig - a model defined in Swagger

        :param openconfig_aclconfig: The openconfig_aclconfig of this InterfaceConfig.  # noqa: E501
        :type openconfig_aclconfig: AclOpenconfigaclaclInterfacesConfig
        """
        self.swagger_types = {
            'openconfig_aclconfig': AclOpenconfigaclaclInterfacesConfig
        }

        self.attribute_map = {
            'openconfig_aclconfig': 'openconfig-acl:config'
        }

        self._openconfig_aclconfig = openconfig_aclconfig

    @classmethod
    def from_dict(cls, dikt) -> 'InterfaceConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The interface_config of this InterfaceConfig.  # noqa: E501
        :rtype: InterfaceConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclconfig(self) -> AclOpenconfigaclaclInterfacesConfig:
        """Gets the openconfig_aclconfig of this InterfaceConfig.


        :return: The openconfig_aclconfig of this InterfaceConfig.
        :rtype: AclOpenconfigaclaclInterfacesConfig
        """
        return self._openconfig_aclconfig

    @openconfig_aclconfig.setter
    def openconfig_aclconfig(self, openconfig_aclconfig: AclOpenconfigaclaclInterfacesConfig):
        """Sets the openconfig_aclconfig of this InterfaceConfig.


        :param openconfig_aclconfig: The openconfig_aclconfig of this InterfaceConfig.
        :type openconfig_aclconfig: AclOpenconfigaclaclInterfacesConfig
        """

        self._openconfig_aclconfig = openconfig_aclconfig
