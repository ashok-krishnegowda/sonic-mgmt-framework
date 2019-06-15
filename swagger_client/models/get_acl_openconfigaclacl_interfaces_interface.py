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

from swagger_client.models.acl_openconfigaclacl_interfaces_config import AclOpenconfigaclaclInterfacesConfig  # noqa: F401,E501
from swagger_client.models.get_acl_openconfigaclacl_aclsets_aclentries_inputinterface_interfaceref import GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref  # noqa: F401,E501
from swagger_client.models.get_acl_openconfigaclacl_interfaces_egressaclsets import GetAclOpenconfigaclaclInterfacesEgressaclsets  # noqa: F401,E501
from swagger_client.models.get_acl_openconfigaclacl_interfaces_ingressaclsets import GetAclOpenconfigaclaclInterfacesIngressaclsets  # noqa: F401,E501


class GetAclOpenconfigaclaclInterfacesInterface(object):
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
        'id': 'str',
        'config': 'AclOpenconfigaclaclInterfacesConfig',
        'state': 'AclOpenconfigaclaclInterfacesConfig',
        'interface_ref': 'GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref',
        'ingress_acl_sets': 'GetAclOpenconfigaclaclInterfacesIngressaclsets',
        'egress_acl_sets': 'GetAclOpenconfigaclaclInterfacesEgressaclsets'
    }

    attribute_map = {
        'id': 'id',
        'config': 'config',
        'state': 'state',
        'interface_ref': 'interface-ref',
        'ingress_acl_sets': 'ingress-acl-sets',
        'egress_acl_sets': 'egress-acl-sets'
    }

    def __init__(self, id=None, config=None, state=None, interface_ref=None, ingress_acl_sets=None, egress_acl_sets=None):  # noqa: E501
        """GetAclOpenconfigaclaclInterfacesInterface - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._config = None
        self._state = None
        self._interface_ref = None
        self._ingress_acl_sets = None
        self._egress_acl_sets = None
        self.discriminator = None

        self.id = id
        if config is not None:
            self.config = config
        if state is not None:
            self.state = state
        if interface_ref is not None:
            self.interface_ref = interface_ref
        if ingress_acl_sets is not None:
            self.ingress_acl_sets = ingress_acl_sets
        if egress_acl_sets is not None:
            self.egress_acl_sets = egress_acl_sets

    @property
    def id(self):
        """Gets the id of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501


        :return: The id of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAclOpenconfigaclaclInterfacesInterface.


        :param id: The id of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def config(self):
        """Gets the config of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501


        :return: The config of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :rtype: AclOpenconfigaclaclInterfacesConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this GetAclOpenconfigaclaclInterfacesInterface.


        :param config: The config of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :type: AclOpenconfigaclaclInterfacesConfig
        """

        self._config = config

    @property
    def state(self):
        """Gets the state of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501


        :return: The state of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :rtype: AclOpenconfigaclaclInterfacesConfig
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetAclOpenconfigaclaclInterfacesInterface.


        :param state: The state of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :type: AclOpenconfigaclaclInterfacesConfig
        """

        self._state = state

    @property
    def interface_ref(self):
        """Gets the interface_ref of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501


        :return: The interface_ref of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :rtype: GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        """
        return self._interface_ref

    @interface_ref.setter
    def interface_ref(self, interface_ref):
        """Sets the interface_ref of this GetAclOpenconfigaclaclInterfacesInterface.


        :param interface_ref: The interface_ref of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :type: GetAclOpenconfigaclaclAclsetsAclentriesInputinterfaceInterfaceref
        """

        self._interface_ref = interface_ref

    @property
    def ingress_acl_sets(self):
        """Gets the ingress_acl_sets of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501


        :return: The ingress_acl_sets of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :rtype: GetAclOpenconfigaclaclInterfacesIngressaclsets
        """
        return self._ingress_acl_sets

    @ingress_acl_sets.setter
    def ingress_acl_sets(self, ingress_acl_sets):
        """Sets the ingress_acl_sets of this GetAclOpenconfigaclaclInterfacesInterface.


        :param ingress_acl_sets: The ingress_acl_sets of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :type: GetAclOpenconfigaclaclInterfacesIngressaclsets
        """

        self._ingress_acl_sets = ingress_acl_sets

    @property
    def egress_acl_sets(self):
        """Gets the egress_acl_sets of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501


        :return: The egress_acl_sets of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :rtype: GetAclOpenconfigaclaclInterfacesEgressaclsets
        """
        return self._egress_acl_sets

    @egress_acl_sets.setter
    def egress_acl_sets(self, egress_acl_sets):
        """Sets the egress_acl_sets of this GetAclOpenconfigaclaclInterfacesInterface.


        :param egress_acl_sets: The egress_acl_sets of this GetAclOpenconfigaclaclInterfacesInterface.  # noqa: E501
        :type: GetAclOpenconfigaclaclInterfacesEgressaclsets
        """

        self._egress_acl_sets = egress_acl_sets

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
        if issubclass(GetAclOpenconfigaclaclInterfacesInterface, dict):
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
        if not isinstance(other, GetAclOpenconfigaclaclInterfacesInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
