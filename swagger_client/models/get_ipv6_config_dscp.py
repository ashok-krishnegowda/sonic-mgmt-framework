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


class GetIpv6ConfigDscp(object):
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
        'dscp': 'int'
    }

    attribute_map = {
        'dscp': 'dscp'
    }

    def __init__(self, dscp=None):  # noqa: E501
        """GetIpv6ConfigDscp - a model defined in Swagger"""  # noqa: E501

        self._dscp = None
        self.discriminator = None

        if dscp is not None:
            self.dscp = dscp

    @property
    def dscp(self):
        """Gets the dscp of this GetIpv6ConfigDscp.  # noqa: E501


        :return: The dscp of this GetIpv6ConfigDscp.  # noqa: E501
        :rtype: int
        """
        return self._dscp

    @dscp.setter
    def dscp(self, dscp):
        """Sets the dscp of this GetIpv6ConfigDscp.


        :param dscp: The dscp of this GetIpv6ConfigDscp.  # noqa: E501
        :type: int
        """

        self._dscp = dscp

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
        if issubclass(GetIpv6ConfigDscp, dict):
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
        if not isinstance(other, GetIpv6ConfigDscp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
