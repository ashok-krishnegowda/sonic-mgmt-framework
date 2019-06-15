# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_aclentry import AclOpenconfigaclaclAclsetsAclentriesAclentry  # noqa: F401,E501
from swagger_server import util


class ListBaseAclEntriesAclEntry(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclacl_entry: List[AclOpenconfigaclaclAclsetsAclentriesAclentry]=None):  # noqa: E501
        """ListBaseAclEntriesAclEntry - a model defined in Swagger

        :param openconfig_aclacl_entry: The openconfig_aclacl_entry of this ListBaseAclEntriesAclEntry.  # noqa: E501
        :type openconfig_aclacl_entry: List[AclOpenconfigaclaclAclsetsAclentriesAclentry]
        """
        self.swagger_types = {
            'openconfig_aclacl_entry': List[AclOpenconfigaclaclAclsetsAclentriesAclentry]
        }

        self.attribute_map = {
            'openconfig_aclacl_entry': 'openconfig-acl:acl-entry'
        }

        self._openconfig_aclacl_entry = openconfig_aclacl_entry

    @classmethod
    def from_dict(cls, dikt) -> 'ListBaseAclEntriesAclEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The list_base_acl_entries_acl_entry of this ListBaseAclEntriesAclEntry.  # noqa: E501
        :rtype: ListBaseAclEntriesAclEntry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclacl_entry(self) -> List[AclOpenconfigaclaclAclsetsAclentriesAclentry]:
        """Gets the openconfig_aclacl_entry of this ListBaseAclEntriesAclEntry.


        :return: The openconfig_aclacl_entry of this ListBaseAclEntriesAclEntry.
        :rtype: List[AclOpenconfigaclaclAclsetsAclentriesAclentry]
        """
        return self._openconfig_aclacl_entry

    @openconfig_aclacl_entry.setter
    def openconfig_aclacl_entry(self, openconfig_aclacl_entry: List[AclOpenconfigaclaclAclsetsAclentriesAclentry]):
        """Sets the openconfig_aclacl_entry of this ListBaseAclEntriesAclEntry.


        :param openconfig_aclacl_entry: The openconfig_aclacl_entry of this ListBaseAclEntriesAclEntry.
        :type openconfig_aclacl_entry: List[AclOpenconfigaclaclAclsetsAclentriesAclentry]
        """

        self._openconfig_aclacl_entry = openconfig_aclacl_entry
