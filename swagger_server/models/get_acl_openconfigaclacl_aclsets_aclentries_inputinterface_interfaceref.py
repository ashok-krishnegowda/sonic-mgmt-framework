# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref_config import AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig  # noqa: F401,E501
from swagger_server import util


class GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, config: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig=None, state: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig=None):  # noqa: E501
        """GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref - a model defined in Swagger

        :param config: The config of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.  # noqa: E501
        :type config: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        :param state: The state of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.  # noqa: E501
        :type state: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        """
        self.swagger_types = {
            'config': AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig,
            'state': AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        }

        self.attribute_map = {
            'config': 'config',
            'state': 'state'
        }

        self._config = config
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.  # noqa: E501
        :rtype: GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config(self) -> AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig:
        """Gets the config of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.


        :return: The config of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        """
        return self._config

    @config.setter
    def config(self, config: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig):
        """Sets the config of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.


        :param config: The config of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.
        :type config: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        """

        self._config = config

    @property
    def state(self) -> AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig:
        """Gets the state of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.


        :return: The state of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        """
        return self._state

    @state.setter
    def state(self, state: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig):
        """Sets the state of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.


        :param state: The state of this GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref.
        :type state: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfacerefConfig
        """

        self._state = state
