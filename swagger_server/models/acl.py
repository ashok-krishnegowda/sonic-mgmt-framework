# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl import AclOpenconfigaclacl  # noqa: F401,E501
from swagger_server import util


class Acl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclacl: AclOpenconfigaclacl=None):  # noqa: E501
        """Acl - a model defined in Swagger

        :param openconfig_aclacl: The openconfig_aclacl of this Acl.  # noqa: E501
        :type openconfig_aclacl: AclOpenconfigaclacl
        """
        self.swagger_types = {
            'openconfig_aclacl': AclOpenconfigaclacl
        }

        self.attribute_map = {
            'openconfig_aclacl': 'openconfig-acl:acl'
        }

        self._openconfig_aclacl = openconfig_aclacl

    @classmethod
    def from_dict(cls, dikt) -> 'Acl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The acl of this Acl.  # noqa: E501
        :rtype: Acl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclacl(self) -> AclOpenconfigaclacl:
        """Gets the openconfig_aclacl of this Acl.


        :return: The openconfig_aclacl of this Acl.
        :rtype: AclOpenconfigaclacl
        """
        return self._openconfig_aclacl

    @openconfig_aclacl.setter
    def openconfig_aclacl(self, openconfig_aclacl: AclOpenconfigaclacl):
        """Sets the openconfig_aclacl of this Acl.


        :param openconfig_aclacl: The openconfig_aclacl of this Acl.
        :type openconfig_aclacl: AclOpenconfigaclacl
        """

        self._openconfig_aclacl = openconfig_aclacl
