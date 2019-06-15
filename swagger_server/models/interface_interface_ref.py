# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref import AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref  # noqa: F401,E501
from swagger_server import util


class InterfaceInterfaceRef(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, openconfig_aclinterface_ref: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref=None):  # noqa: E501
        """InterfaceInterfaceRef - a model defined in Swagger

        :param openconfig_aclinterface_ref: The openconfig_aclinterface_ref of this InterfaceInterfaceRef.  # noqa: E501
        :type openconfig_aclinterface_ref: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        """
        self.swagger_types = {
            'openconfig_aclinterface_ref': AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        }

        self.attribute_map = {
            'openconfig_aclinterface_ref': 'openconfig-acl:interface-ref'
        }

        self._openconfig_aclinterface_ref = openconfig_aclinterface_ref

    @classmethod
    def from_dict(cls, dikt) -> 'InterfaceInterfaceRef':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The interface_interface_ref of this InterfaceInterfaceRef.  # noqa: E501
        :rtype: InterfaceInterfaceRef
        """
        return util.deserialize_model(dikt, cls)

    @property
    def openconfig_aclinterface_ref(self) -> AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref:
        """Gets the openconfig_aclinterface_ref of this InterfaceInterfaceRef.


        :return: The openconfig_aclinterface_ref of this InterfaceInterfaceRef.
        :rtype: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        """
        return self._openconfig_aclinterface_ref

    @openconfig_aclinterface_ref.setter
    def openconfig_aclinterface_ref(self, openconfig_aclinterface_ref: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref):
        """Sets the openconfig_aclinterface_ref of this InterfaceInterfaceRef.


        :param openconfig_aclinterface_ref: The openconfig_aclinterface_ref of this InterfaceInterfaceRef.
        :type openconfig_aclinterface_ref: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        """

        self._openconfig_aclinterface_ref = openconfig_aclinterface_ref
