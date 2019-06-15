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

from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_actions import AclOpenconfigaclaclAclsetsAclentriesActions  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_config import AclOpenconfigaclaclAclsetsAclentriesConfig  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_inputinterface import AclOpenconfigaclaclAclsetsAclentriesInputinterface  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_ipv4 import AclOpenconfigaclaclAclsetsAclentriesIpv4  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_ipv6 import AclOpenconfigaclaclAclsetsAclentriesIpv6  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_l2 import AclOpenconfigaclaclAclsetsAclentriesL2  # noqa: F401,E501
from swagger_client.models.acl_openconfigaclacl_aclsets_aclentries_transport import AclOpenconfigaclaclAclsetsAclentriesTransport  # noqa: F401,E501


class AclSetAclEntriesAclEntryOpenconfigaclaclentry(object):
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
        'config': 'AclOpenconfigaclaclAclsetsAclentriesConfig',
        'l2': 'AclOpenconfigaclaclAclsetsAclentriesL2',
        'ipv4': 'AclOpenconfigaclaclAclsetsAclentriesIpv4',
        'ipv6': 'AclOpenconfigaclaclAclsetsAclentriesIpv6',
        'transport': 'AclOpenconfigaclaclAclsetsAclentriesTransport',
        'input_interface': 'AclOpenconfigaclaclAclsetsAclentriesInputinterface',
        'actions': 'AclOpenconfigaclaclAclsetsAclentriesActions'
    }

    attribute_map = {
        'config': 'config',
        'l2': 'l2',
        'ipv4': 'ipv4',
        'ipv6': 'ipv6',
        'transport': 'transport',
        'input_interface': 'input-interface',
        'actions': 'actions'
    }

    def __init__(self, config=None, l2=None, ipv4=None, ipv6=None, transport=None, input_interface=None, actions=None):  # noqa: E501
        """AclSetAclEntriesAclEntryOpenconfigaclaclentry - a model defined in Swagger"""  # noqa: E501

        self._config = None
        self._l2 = None
        self._ipv4 = None
        self._ipv6 = None
        self._transport = None
        self._input_interface = None
        self._actions = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if l2 is not None:
            self.l2 = l2
        if ipv4 is not None:
            self.ipv4 = ipv4
        if ipv6 is not None:
            self.ipv6 = ipv6
        if transport is not None:
            self.transport = transport
        if input_interface is not None:
            self.input_interface = input_interface
        if actions is not None:
            self.actions = actions

    @property
    def config(self):
        """Gets the config of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501


        :return: The config of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.


        :param config: The config of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesConfig
        """

        self._config = config

    @property
    def l2(self):
        """Gets the l2 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501


        :return: The l2 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesL2
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.


        :param l2: The l2 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesL2
        """

        self._l2 = l2

    @property
    def ipv4(self):
        """Gets the ipv4 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501


        :return: The ipv4 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesIpv4
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.


        :param ipv4: The ipv4 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesIpv4
        """

        self._ipv4 = ipv4

    @property
    def ipv6(self):
        """Gets the ipv6 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501


        :return: The ipv6 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesIpv6
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.


        :param ipv6: The ipv6 of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesIpv6
        """

        self._ipv6 = ipv6

    @property
    def transport(self):
        """Gets the transport of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501


        :return: The transport of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesTransport
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.


        :param transport: The transport of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesTransport
        """

        self._transport = transport

    @property
    def input_interface(self):
        """Gets the input_interface of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501


        :return: The input_interface of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesInputinterface
        """
        return self._input_interface

    @input_interface.setter
    def input_interface(self, input_interface):
        """Sets the input_interface of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.


        :param input_interface: The input_interface of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesInputinterface
        """

        self._input_interface = input_interface

    @property
    def actions(self):
        """Gets the actions of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501


        :return: The actions of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :rtype: AclOpenconfigaclaclAclsetsAclentriesActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.


        :param actions: The actions of this AclSetAclEntriesAclEntryOpenconfigaclaclentry.  # noqa: E501
        :type: AclOpenconfigaclaclAclsetsAclentriesActions
        """

        self._actions = actions

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
        if issubclass(AclSetAclEntriesAclEntryOpenconfigaclaclentry, dict):
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
        if not isinstance(other, AclSetAclEntriesAclEntryOpenconfigaclaclentry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
