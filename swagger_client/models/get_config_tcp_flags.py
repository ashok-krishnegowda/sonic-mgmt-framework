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


class GetConfigTcpFlags(object):
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
        'tcp_flags': 'str'
    }

    attribute_map = {
        'tcp_flags': 'tcp-flags'
    }

    def __init__(self, tcp_flags=None):  # noqa: E501
        """GetConfigTcpFlags - a model defined in Swagger"""  # noqa: E501

        self._tcp_flags = None
        self.discriminator = None

        if tcp_flags is not None:
            self.tcp_flags = tcp_flags

    @property
    def tcp_flags(self):
        """Gets the tcp_flags of this GetConfigTcpFlags.  # noqa: E501


        :return: The tcp_flags of this GetConfigTcpFlags.  # noqa: E501
        :rtype: str
        """
        return self._tcp_flags

    @tcp_flags.setter
    def tcp_flags(self, tcp_flags):
        """Sets the tcp_flags of this GetConfigTcpFlags.


        :param tcp_flags: The tcp_flags of this GetConfigTcpFlags.  # noqa: E501
        :type: str
        """

        self._tcp_flags = tcp_flags

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
        if issubclass(GetConfigTcpFlags, dict):
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
        if not isinstance(other, GetConfigTcpFlags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
