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


class GetStateDestinationFlowLabel(object):
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
        'destination_flow_label': 'int'
    }

    attribute_map = {
        'destination_flow_label': 'destination-flow-label'
    }

    def __init__(self, destination_flow_label=None):  # noqa: E501
        """GetStateDestinationFlowLabel - a model defined in Swagger"""  # noqa: E501

        self._destination_flow_label = None
        self.discriminator = None

        if destination_flow_label is not None:
            self.destination_flow_label = destination_flow_label

    @property
    def destination_flow_label(self):
        """Gets the destination_flow_label of this GetStateDestinationFlowLabel.  # noqa: E501


        :return: The destination_flow_label of this GetStateDestinationFlowLabel.  # noqa: E501
        :rtype: int
        """
        return self._destination_flow_label

    @destination_flow_label.setter
    def destination_flow_label(self, destination_flow_label):
        """Sets the destination_flow_label of this GetStateDestinationFlowLabel.


        :param destination_flow_label: The destination_flow_label of this GetStateDestinationFlowLabel.  # noqa: E501
        :type: int
        """

        self._destination_flow_label = destination_flow_label

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
        if issubclass(GetStateDestinationFlowLabel, dict):
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
        if not isinstance(other, GetStateDestinationFlowLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
