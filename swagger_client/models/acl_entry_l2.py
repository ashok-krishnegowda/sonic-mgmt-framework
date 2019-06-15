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

from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_l2 import AclOpenconfigaclaclAclsetsAclentriesL2  # noqa: F401,E501


class AclEntryL2(object):
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
        'openconfig_acll2': 'AclOpenconfigaclaclAclsetsAclentriesL2'
    }

    attribute_map = {
        'openconfig_acll2': 'openconfig-acl:l2'
    }

    def __init__(self, openconfig_acll2=None):  # noqa: E501
        """AclEntryL2 - a model defined in Swagger"""  # noqa: E501

        self._openconfig_acll2 = None
        self.discriminator = None

        if openconfig_acll2 is not None:
            self.openconfig_acll2 = openconfig_acll2

    @property
    def openconfig_acll2(self):
        """Gets the openconfig_acll2 of this AclEntryL2.  # noqa: E501


        :return: The openconfig_acll2 of this AclEntryL2.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesL2
        """
        return self._openconfig_acll2

    @openconfig_acll2.setter
    def openconfig_acll2(self, openconfig_acll2):
        """Sets the openconfig_acll2 of this AclEntryL2.


        :param openconfig_acll2: The openconfig_acll2 of this AclEntryL2.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesL2
        """

        self._openconfig_acll2 = openconfig_acll2

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
        if issubclass(AclEntryL2, dict):
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
        if not isinstance(other, AclEntryL2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
