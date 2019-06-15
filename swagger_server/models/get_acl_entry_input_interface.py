# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_acl_openconfigaclacl_aclsets_aclentries_inputinterface import GetAclOpenconfigaclaclAclsetsAclentriesInputinterface  # noqa: F401,E501
from swagger_server import util


class GetAclEntryInputInterface(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclinput_interface: GetAclOpenconfigaclaclAclsetsAclentriesInputinterface=None):  # noqa: E501
        """GetAclEntryInputInterface - a model defined in Swagger

        :param openconfig_aclinput_interface: The openconfig_aclinput_interface of this GetAclEntryInputInterface.  # noqa: E501
        :type openconfig_aclinput_interface: GetAclOpenconfigaclaclAclsetsAclentriesInputinterface
        """
        self.swagger_types = {
            'openconfig_aclinput_interface': GetAclOpenconfigaclaclAclsetsAclentriesInputinterface
        }

        self.attribute_map = {
            'openconfig_aclinput_interface': 'openconfig-acl:input-interface'
        }

        self._openconfig_aclinput_interface = openconfig_aclinput_interface

    @classmethod
    def from_dict(cls, dikt) -> 'GetAclEntryInputInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_acl_entry_input_interface of this GetAclEntryInputInterface.  # noqa: E501
        :rtype: GetAclEntryInputInterface
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclinput_interface(self) -> GetAclOpenconfigaclaclAclsetsAclentriesInputinterface:
        """Gets the openconfig_aclinput_interface of this GetAclEntryInputInterface.


        :return: The openconfig_aclinput_interface of this GetAclEntryInputInterface.
        :rtype: GetAclOpenconfigaclaclAclsetsAclentriesInputinterface
        """
        return self._openconfig_aclinput_interface

    @openconfig_aclinput_interface.setter
    def openconfig_aclinput_interface(self, openconfig_aclinput_interface: GetAclOpenconfigaclaclAclsetsAclentriesInputinterface):
        """Sets the openconfig_aclinput_interface of this GetAclEntryInputInterface.


        :param openconfig_aclinput_interface: The openconfig_aclinput_interface of this GetAclEntryInputInterface.
        :type openconfig_aclinput_interface: GetAclOpenconfigaclaclAclsetsAclentriesInputinterface
        """

        self._openconfig_aclinput_interface = openconfig_aclinput_interface
