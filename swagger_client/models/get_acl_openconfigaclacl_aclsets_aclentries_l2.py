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

from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_l2_config import AclOpenconfigaclaclAclsetsAclentriesL2Config  # noqa: F401,E501


class GetAclOpenconfigaclaclAclsetsAclentriesL2(object):
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
        'config': 'AclOpenconfigaclaclAclsetsAclentriesL2Config',
        'state': 'AclOpenconfigaclaclAclsetsAclentriesL2Config'
    }

    attribute_map = {
        'config': 'config',
        'state': 'state'
    }

    def __init__(self, config=None, state=None):  # noqa: E501
        """GetAclOpenconfigaclaclAclsetsAclentriesL2 - a model defined in Swagger"""  # noqa: E501

        self._config = None
        self._state = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if state is not None:
            self.state = state

    @property
    def config(self):
        """Gets the config of this GetAclOpenconfigaclaclAclsetsAclentriesL2.  # noqa: E501


        :return: The config of this GetAclOpenconfigaclaclAclsetsAclentriesL2.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesL2Config
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this GetAclOpenconfigaclaclAclsetsAclentriesL2.


        :param config: The config of this GetAclOpenconfigaclaclAclsetsAclentriesL2.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesL2Config
        """

        self._config = config

    @property
    def state(self):
        """Gets the state of this GetAclOpenconfigaclaclAclsetsAclentriesL2.  # noqa: E501


        :return: The state of this GetAclOpenconfigaclaclAclsetsAclentriesL2.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesL2Config
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetAclOpenconfigaclaclAclsetsAclentriesL2.


        :param state: The state of this GetAclOpenconfigaclaclAclsetsAclentriesL2.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesL2Config
        """

        self._state = state

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
        if issubclass(GetAclOpenconfigaclaclAclsetsAclentriesL2, dict):
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
        if not isinstance(other, GetAclOpenconfigaclaclAclsetsAclentriesL2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
