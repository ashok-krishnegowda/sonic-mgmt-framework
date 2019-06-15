# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_interfaces_ingressaclsets import AclOpenconfigaclaclInterfacesIngressaclsets  # noqa: F401,E501
from swagger_server.models.interface_ingress_acl_sets import InterfaceIngressAclSets  # noqa: F401,E501
from swagger_server import util


class PutInterfaceIngressAclSets(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclingress_acl_sets: AclOpenconfigaclaclInterfacesIngressaclsets=None):  # noqa: E501
        """PutInterfaceIngressAclSets - a model defined in Swagger

        :param openconfig_aclingress_acl_sets: The openconfig_aclingress_acl_sets of this PutInterfaceIngressAclSets.  # noqa: E501
        :type openconfig_aclingress_acl_sets: AclOpenconfigaclaclInterfacesIngressaclsets
        """
        self.swagger_types = {
            'openconfig_aclingress_acl_sets': AclOpenconfigaclaclInterfacesIngressaclsets
        }

        self.attribute_map = {
            'openconfig_aclingress_acl_sets': 'openconfig-acl:ingress-acl-sets'
        }

        self._openconfig_aclingress_acl_sets = openconfig_aclingress_acl_sets

    @classmethod
    def from_dict(cls, dikt) -> 'PutInterfaceIngressAclSets':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The put_interface_ingress_acl_sets of this PutInterfaceIngressAclSets.  # noqa: E501
        :rtype: PutInterfaceIngressAclSets
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclingress_acl_sets(self) -> AclOpenconfigaclaclInterfacesIngressaclsets:
        """Gets the openconfig_aclingress_acl_sets of this PutInterfaceIngressAclSets.


        :return: The openconfig_aclingress_acl_sets of this PutInterfaceIngressAclSets.
        :rtype: AclOpenconfigaclaclInterfacesIngressaclsets
        """
        return self._openconfig_aclingress_acl_sets

    @openconfig_aclingress_acl_sets.setter
    def openconfig_aclingress_acl_sets(self, openconfig_aclingress_acl_sets: AclOpenconfigaclaclInterfacesIngressaclsets):
        """Sets the openconfig_aclingress_acl_sets of this PutInterfaceIngressAclSets.


        :param openconfig_aclingress_acl_sets: The openconfig_aclingress_acl_sets of this PutInterfaceIngressAclSets.
        :type openconfig_aclingress_acl_sets: AclOpenconfigaclaclInterfacesIngressaclsets
        """

        self._openconfig_aclingress_acl_sets = openconfig_aclingress_acl_sets
