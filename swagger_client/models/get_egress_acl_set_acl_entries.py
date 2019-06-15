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

from swagger_client.models.get_acl_openconfigaclacl_interfaces_ingressaclsets_aclentries import GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentries  # noqa: F401,E501


class GetEgressAclSetAclEntries(object):
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
        'openconfig_aclacl_entries': 'GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentries'
    }

    attribute_map = {
        'openconfig_aclacl_entries': 'openconfig-acl:acl-entries'
    }

    def __init__(self, openconfig_aclacl_entries=None):  # noqa: E501
        """GetEgressAclSetAclEntries - a model defined in Swagger"""  # noqa: E501

        self._openconfig_aclacl_entries = None
        self.discriminator = None

        if openconfig_aclacl_entries is not None:
            self.openconfig_aclacl_entries = openconfig_aclacl_entries

    @property
    def openconfig_aclacl_entries(self):
        """Gets the openconfig_aclacl_entries of this GetEgressAclSetAclEntries.  # noqa: E501


        :return: The openconfig_aclacl_entries of this GetEgressAclSetAclEntries.  # noqa: E501
        :rtype: GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentries
        """
        return self._openconfig_aclacl_entries

    @openconfig_aclacl_entries.setter
    def openconfig_aclacl_entries(self, openconfig_aclacl_entries):
        """Sets the openconfig_aclacl_entries of this GetEgressAclSetAclEntries.


        :param openconfig_aclacl_entries: The openconfig_aclacl_entries of this GetEgressAclSetAclEntries.  # noqa: E501
        :type: GetAclOpenconfigaclaclInterfacesIngressaclsetsAclentries
        """

        self._openconfig_aclacl_entries = openconfig_aclacl_entries

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
        if issubclass(GetEgressAclSetAclEntries, dict):
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
        if not isinstance(other, GetEgressAclSetAclEntries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
