# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_acl_openconfigaclacl_interfaces_egressaclsets import GetAclOpenconfigaclaclInterfacesEgressaclsets  # noqa: F401,E501
from swagger_server import util


class GetInterfaceEgressAclSets(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclegress_acl_sets: GetAclOpenconfigaclaclInterfacesEgressaclsets=None):  # noqa: E501
        """GetInterfaceEgressAclSets - a model defined in Swagger

        :param openconfig_aclegress_acl_sets: The openconfig_aclegress_acl_sets of this GetInterfaceEgressAclSets.  # noqa: E501
        :type openconfig_aclegress_acl_sets: GetAclOpenconfigaclaclInterfacesEgressaclsets
        """
        self.swagger_types = {
            'openconfig_aclegress_acl_sets': GetAclOpenconfigaclaclInterfacesEgressaclsets
        }

        self.attribute_map = {
            'openconfig_aclegress_acl_sets': 'openconfig-acl:egress-acl-sets'
        }

        self._openconfig_aclegress_acl_sets = openconfig_aclegress_acl_sets

    @classmethod
    def from_dict(cls, dikt) -> 'GetInterfaceEgressAclSets':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_interface_egress_acl_sets of this GetInterfaceEgressAclSets.  # noqa: E501
        :rtype: GetInterfaceEgressAclSets
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclegress_acl_sets(self) -> GetAclOpenconfigaclaclInterfacesEgressaclsets:
        """Gets the openconfig_aclegress_acl_sets of this GetInterfaceEgressAclSets.


        :return: The openconfig_aclegress_acl_sets of this GetInterfaceEgressAclSets.
        :rtype: GetAclOpenconfigaclaclInterfacesEgressaclsets
        """
        return self._openconfig_aclegress_acl_sets

    @openconfig_aclegress_acl_sets.setter
    def openconfig_aclegress_acl_sets(self, openconfig_aclegress_acl_sets: GetAclOpenconfigaclaclInterfacesEgressaclsets):
        """Sets the openconfig_aclegress_acl_sets of this GetInterfaceEgressAclSets.


        :param openconfig_aclegress_acl_sets: The openconfig_aclegress_acl_sets of this GetInterfaceEgressAclSets.
        :type openconfig_aclegress_acl_sets: GetAclOpenconfigaclaclInterfacesEgressaclsets
        """

        self._openconfig_aclegress_acl_sets = openconfig_aclegress_acl_sets
