# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_entry_input_interface import AclEntryInputInterface  # noqa: F401,E501
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface import AclOpenconfigaclaclAclsetsAclentriesInputinterface  # noqa: F401,E501
from swagger_server import util


class PutAclEntryInputInterface(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclinput_interface: AclOpenconfigaclaclAclsetsAclentriesInputinterface=None):  # noqa: E501
        """PutAclEntryInputInterface - a model defined in Swagger

        :param openconfig_aclinput_interface: The openconfig_aclinput_interface of this PutAclEntryInputInterface.  # noqa: E501
        :type openconfig_aclinput_interface: AclOpenconfigaclaclAclsetsAclentriesInputinterface
        """
        self.swagger_types = {
            'openconfig_aclinput_interface': AclOpenconfigaclaclAclsetsAclentriesInputinterface
        }

        self.attribute_map = {
            'openconfig_aclinput_interface': 'openconfig-acl:input-interface'
        }

        self._openconfig_aclinput_interface = openconfig_aclinput_interface

    @classmethod
    def from_dict(cls, dikt) -> 'PutAclEntryInputInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The put_acl_entry_input_interface of this PutAclEntryInputInterface.  # noqa: E501
        :rtype: PutAclEntryInputInterface
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclinput_interface(self) -> AclOpenconfigaclaclAclsetsAclentriesInputinterface:
        """Gets the openconfig_aclinput_interface of this PutAclEntryInputInterface.


        :return: The openconfig_aclinput_interface of this PutAclEntryInputInterface.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesInputinterface
        """
        return self._openconfig_aclinput_interface

    @openconfig_aclinput_interface.setter
    def openconfig_aclinput_interface(self, openconfig_aclinput_interface: AclOpenconfigaclaclAclsetsAclentriesInputinterface):
        """Sets the openconfig_aclinput_interface of this PutAclEntryInputInterface.


        :param openconfig_aclinput_interface: The openconfig_aclinput_interface of this PutAclEntryInputInterface.
        :type openconfig_aclinput_interface: AclOpenconfigaclaclAclsetsAclentriesInputinterface
        """

        self._openconfig_aclinput_interface = openconfig_aclinput_interface
