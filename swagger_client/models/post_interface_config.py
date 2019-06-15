# coding: utf-8

"""
    Sonic NMS

    Network management Open APIs for Broadcom's Sonic.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: mohammed.faraaz@broadcom.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref import AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_interfaces_config import AclOpenconfigaclaclInterfacesConfig  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_interfaces_egressaclsets import AclOpenconfigaclaclInterfacesEgressaclsets  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_interfaces_ingressaclsets import AclOpenconfigaclaclInterfacesIngressaclsets  # noqa: F401,E501
from swagger_client.models.interface_config import InterfaceConfig  # noqa: F401,E501
from swagger_client.models.interface_ingress_acl_sets import InterfaceIngressAclSets  # noqa: F401,E501
from swagger_client.models.interface_interface_ref import InterfaceInterfaceRef  # noqa: F401,E501


class PostInterfaceConfig(InterfaceConfig):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'openconfig_aclinterface_ref': 'AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref',
        'openconfig_aclingress_acl_sets': 'AclOpenconfigaclaclInterfacesIngressaclsets',
        'openconfig_aclegress_acl_sets': 'AclOpenconfigaclaclInterfacesEgressaclsets'
    }

    attribute_map = {
        'openconfig_aclinterface_ref': 'openconfig-acl:interface-ref',
        'openconfig_aclingress_acl_sets': 'openconfig-acl:ingress-acl-sets',
        'openconfig_aclegress_acl_sets': 'openconfig-acl:egress-acl-sets'
    }

    def __init__(self, openconfig_aclinterface_ref=None, openconfig_aclingress_acl_sets=None, openconfig_aclegress_acl_sets=None):  # noqa: E501
        """PostInterfaceConfig - a model defined in Swagger"""  # noqa: E501

        self._openconfig_aclinterface_ref = None
        self._openconfig_aclingress_acl_sets = None
        self._openconfig_aclegress_acl_sets = None
        self.discriminator = None

        if openconfig_aclinterface_ref is not None:
            self.openconfig_aclinterface_ref = openconfig_aclinterface_ref
        if openconfig_aclingress_acl_sets is not None:
            self.openconfig_aclingress_acl_sets = openconfig_aclingress_acl_sets
        if openconfig_aclegress_acl_sets is not None:
            self.openconfig_aclegress_acl_sets = openconfig_aclegress_acl_sets

    @property
    def openconfig_aclinterface_ref(self):
        """Gets the openconfig_aclinterface_ref of this PostInterfaceConfig.  # noqa: E501


        :return: The openconfig_aclinterface_ref of this PostInterfaceConfig.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        """
        return self._openconfig_aclinterface_ref

    @openconfig_aclinterface_ref.setter
    def openconfig_aclinterface_ref(self, openconfig_aclinterface_ref):
        """Sets the openconfig_aclinterface_ref of this PostInterfaceConfig.


        :param openconfig_aclinterface_ref: The openconfig_aclinterface_ref of this PostInterfaceConfig.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        """

        self._openconfig_aclinterface_ref = openconfig_aclinterface_ref

    @property
    def openconfig_aclingress_acl_sets(self):
        """Gets the openconfig_aclingress_acl_sets of this PostInterfaceConfig.  # noqa: E501


        :return: The openconfig_aclingress_acl_sets of this PostInterfaceConfig.  # noqa: E501
        :rtype: AclOpenconfigaclaclInterfacesIngressaclsets
        """
        return self._openconfig_aclingress_acl_sets

    @openconfig_aclingress_acl_sets.setter
    def openconfig_aclingress_acl_sets(self, openconfig_aclingress_acl_sets):
        """Sets the openconfig_aclingress_acl_sets of this PostInterfaceConfig.


        :param openconfig_aclingress_acl_sets: The openconfig_aclingress_acl_sets of this PostInterfaceConfig.  # noqa: E501
        :type: AclOpenconfigaclaclInterfacesIngressaclsets
        """

        self._openconfig_aclingress_acl_sets = openconfig_aclingress_acl_sets

    @property
    def openconfig_aclegress_acl_sets(self):
        """Gets the openconfig_aclegress_acl_sets of this PostInterfaceConfig.  # noqa: E501


        :return: The openconfig_aclegress_acl_sets of this PostInterfaceConfig.  # noqa: E501
        :rtype: AclOpenconfigaclaclInterfacesEgressaclsets
        """
        return self._openconfig_aclegress_acl_sets

    @openconfig_aclegress_acl_sets.setter
    def openconfig_aclegress_acl_sets(self, openconfig_aclegress_acl_sets):
        """Sets the openconfig_aclegress_acl_sets of this PostInterfaceConfig.


        :param openconfig_aclegress_acl_sets: The openconfig_aclegress_acl_sets of this PostInterfaceConfig.  # noqa: E501
        :type: AclOpenconfigaclaclInterfacesEgressaclsets
        """

        self._openconfig_aclegress_acl_sets = openconfig_aclegress_acl_sets

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PostInterfaceConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PostInterfaceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
