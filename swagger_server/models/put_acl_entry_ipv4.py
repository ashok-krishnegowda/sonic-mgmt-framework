# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_entry_ipv4 import AclEntryIpv4  # noqa: F401,E501
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_ipv4 import AclOpenconfigaclaclAclsetsAclentriesIpv4  # noqa: F401,E501
from swagger_server import util


class PutAclEntryIpv4(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclipv4: AclOpenconfigaclaclAclsetsAclentriesIpv4=None):  # noqa: E501
        """PutAclEntryIpv4 - a model defined in Swagger

        :param openconfig_aclipv4: The openconfig_aclipv4 of this PutAclEntryIpv4.  # noqa: E501
        :type openconfig_aclipv4: AclOpenconfigaclaclAclsetsAclentriesIpv4
        """
        self.swagger_types = {
            'openconfig_aclipv4': AclOpenconfigaclaclAclsetsAclentriesIpv4
        }

        self.attribute_map = {
            'openconfig_aclipv4': 'openconfig-acl:ipv4'
        }

        self._openconfig_aclipv4 = openconfig_aclipv4

    @classmethod
    def from_dict(cls, dikt) -> 'PutAclEntryIpv4':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The put_acl_entry_ipv4 of this PutAclEntryIpv4.  # noqa: E501
        :rtype: PutAclEntryIpv4
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclipv4(self) -> AclOpenconfigaclaclAclsetsAclentriesIpv4:
        """Gets the openconfig_aclipv4 of this PutAclEntryIpv4.


        :return: The openconfig_aclipv4 of this PutAclEntryIpv4.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesIpv4
        """
        return self._openconfig_aclipv4

    @openconfig_aclipv4.setter
    def openconfig_aclipv4(self, openconfig_aclipv4: AclOpenconfigaclaclAclsetsAclentriesIpv4):
        """Sets the openconfig_aclipv4 of this PutAclEntryIpv4.


        :param openconfig_aclipv4: The openconfig_aclipv4 of this PutAclEntryIpv4.
        :type openconfig_aclipv4: AclOpenconfigaclaclAclsetsAclentriesIpv4
        """

        self._openconfig_aclipv4 = openconfig_aclipv4
