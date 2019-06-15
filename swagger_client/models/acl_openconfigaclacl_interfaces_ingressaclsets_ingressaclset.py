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

from swagger_client.models.acl_openconfigaclacl_interfaces_ingressaclsets_config import AclOpenconfigaclaclInterfacesIngressaclsetsConfig  # noqa: F401,E501


class AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset(object):
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
        'set_name': 'str',
        'type': 'str',
        'config': 'AclOpenconfigaclaclInterfacesIngressaclsetsConfig'
    }

    attribute_map = {
        'set_name': 'set-name',
        'type': 'type',
        'config': 'config'
    }

    def __init__(self, set_name=None, type=None, config=None):  # noqa: E501
        """AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset - a model defined in Swagger"""  # noqa: E501

        self._set_name = None
        self._type = None
        self._config = None
        self.discriminator = None

        self.set_name = set_name
        self.type = type
        if config is not None:
            self.config = config

    @property
    def set_name(self):
        """Gets the set_name of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501


        :return: The set_name of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501
        :rtype: str
        """
        return self._set_name

    @set_name.setter
    def set_name(self, set_name):
        """Sets the set_name of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.


        :param set_name: The set_name of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501
        :type: str
        """
        if set_name is None:
            raise ValueError("Invalid value for `set_name`, must not be `None`")  # noqa: E501

        self._set_name = set_name

    @property
    def type(self):
        """Gets the type of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501


        :return: The type of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.


        :param type: The type of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def config(self):
        """Gets the config of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501


        :return: The config of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501
        :rtype: AclOpenconfigaclaclInterfacesIngressaclsetsConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.


        :param config: The config of this AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset.  # noqa: E501
        :type: AclOpenconfigaclaclInterfacesIngressaclsetsConfig
        """

        self._config = config

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
        if issubclass(AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset, dict):
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
        if not isinstance(other, AclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
