# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries import AclOpenconfigaclaclAclsetsAclentries  # noqa: F401,E501
from swagger_server.models.acl_set_acl_entries import AclSetAclEntries  # noqa: F401,E501
from swagger_server import util


class PatchAclSetAclEntries(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclacl_entries: AclOpenconfigaclaclAclsetsAclentries=None):  # noqa: E501
        """PatchAclSetAclEntries - a model defined in Swagger

        :param openconfig_aclacl_entries: The openconfig_aclacl_entries of this PatchAclSetAclEntries.  # noqa: E501
        :type openconfig_aclacl_entries: AclOpenconfigaclaclAclsetsAclentries
        """
        self.swagger_types = {
            'openconfig_aclacl_entries': AclOpenconfigaclaclAclsetsAclentries
        }

        self.attribute_map = {
            'openconfig_aclacl_entries': 'openconfig-acl:acl-entries'
        }

        self._openconfig_aclacl_entries = openconfig_aclacl_entries

    @classmethod
    def from_dict(cls, dikt) -> 'PatchAclSetAclEntries':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patch_acl_set_acl_entries of this PatchAclSetAclEntries.  # noqa: E501
        :rtype: PatchAclSetAclEntries
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclacl_entries(self) -> AclOpenconfigaclaclAclsetsAclentries:
        """Gets the openconfig_aclacl_entries of this PatchAclSetAclEntries.


        :return: The openconfig_aclacl_entries of this PatchAclSetAclEntries.
        :rtype: AclOpenconfigaclaclAclsetsAclentries
        """
        return self._openconfig_aclacl_entries

    @openconfig_aclacl_entries.setter
    def openconfig_aclacl_entries(self, openconfig_aclacl_entries: AclOpenconfigaclaclAclsetsAclentries):
        """Sets the openconfig_aclacl_entries of this PatchAclSetAclEntries.


        :param openconfig_aclacl_entries: The openconfig_aclacl_entries of this PatchAclSetAclEntries.
        :type openconfig_aclacl_entries: AclOpenconfigaclaclAclsetsAclentries
        """

        self._openconfig_aclacl_entries = openconfig_aclacl_entries
