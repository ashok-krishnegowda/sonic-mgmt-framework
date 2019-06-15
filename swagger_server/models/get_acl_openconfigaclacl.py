# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_acl_openconfigaclacl_aclsets import GetAclOpenconfigaclaclAclsets  # noqa: F401,E501
from swagger_server.models.get_acl_openconfigaclacl_interfaces import GetAclOpenconfigaclaclInterfaces  # noqa: F401,E501
from swagger_server.models.get_acl_openconfigaclacl_state import GetAclOpenconfigaclaclState  # noqa: F401,E501
from swagger_server import util


class GetAclOpenconfigaclacl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, state: GetAclOpenconfigaclaclState=None, acl_sets: GetAclOpenconfigaclaclAclsets=None, interfaces: GetAclOpenconfigaclaclInterfaces=None):  # noqa: E501
        """GetAclOpenconfigaclacl - a model defined in Swagger

        :param state: The state of this GetAclOpenconfigaclacl.  # noqa: E501
        :type state: GetAclOpenconfigaclaclState
        :param acl_sets: The acl_sets of this GetAclOpenconfigaclacl.  # noqa: E501
        :type acl_sets: GetAclOpenconfigaclaclAclsets
        :param interfaces: The interfaces of this GetAclOpenconfigaclacl.  # noqa: E501
        :type interfaces: GetAclOpenconfigaclaclInterfaces
        """
        self.swagger_types = {
            'state': GetAclOpenconfigaclaclState,
            'acl_sets': GetAclOpenconfigaclaclAclsets,
            'interfaces': GetAclOpenconfigaclaclInterfaces
        }

        self.attribute_map = {
            'state': 'state',
            'acl_sets': 'acl-sets',
            'interfaces': 'interfaces'
        }

        self._state = state
        self._acl_sets = acl_sets
        self._interfaces = interfaces

    @classmethod
    def from_dict(cls, dikt) -> 'GetAclOpenconfigaclacl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_acl_openconfigaclacl of this GetAclOpenconfigaclacl.  # noqa: E501
        :rtype: GetAclOpenconfigaclacl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> GetAclOpenconfigaclaclState:
        """Gets the state of this GetAclOpenconfigaclacl.


        :return: The state of this GetAclOpenconfigaclacl.
        :rtype: GetAclOpenconfigaclaclState
        """
        return self._state

    @state.setter
    def state(self, state: GetAclOpenconfigaclaclState):
        """Sets the state of this GetAclOpenconfigaclacl.


        :param state: The state of this GetAclOpenconfigaclacl.
        :type state: GetAclOpenconfigaclaclState
        """

        self._state = state

    @property
    def acl_sets(self) -> GetAclOpenconfigaclaclAclsets:
        """Gets the acl_sets of this GetAclOpenconfigaclacl.


        :return: The acl_sets of this GetAclOpenconfigaclacl.
        :rtype: GetAclOpenconfigaclaclAclsets
        """
        return self._acl_sets

    @acl_sets.setter
    def acl_sets(self, acl_sets: GetAclOpenconfigaclaclAclsets):
        """Sets the acl_sets of this GetAclOpenconfigaclacl.


        :param acl_sets: The acl_sets of this GetAclOpenconfigaclacl.
        :type acl_sets: GetAclOpenconfigaclaclAclsets
        """

        self._acl_sets = acl_sets

    @property
    def interfaces(self) -> GetAclOpenconfigaclaclInterfaces:
        """Gets the interfaces of this GetAclOpenconfigaclacl.


        :return: The interfaces of this GetAclOpenconfigaclacl.
        :rtype: GetAclOpenconfigaclaclInterfaces
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces: GetAclOpenconfigaclaclInterfaces):
        """Sets the interfaces of this GetAclOpenconfigaclacl.


        :param interfaces: The interfaces of this GetAclOpenconfigaclacl.
        :type interfaces: GetAclOpenconfigaclaclInterfaces
        """

        self._interfaces = interfaces
