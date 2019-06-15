# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetIpv6ConfigProtocol(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, protocol: str=None):  # noqa: E501
        """GetIpv6ConfigProtocol - a model defined in Swagger

        :param protocol: The protocol of this GetIpv6ConfigProtocol.  # noqa: E501
        :type protocol: str
        """
        self.swagger_types = {
            'protocol': str
        }

        self.attribute_map = {
            'protocol': 'protocol'
        }

        self._protocol = protocol

    @classmethod
    def from_dict(cls, dikt) -> 'GetIpv6ConfigProtocol':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_ipv6_config_protocol of this GetIpv6ConfigProtocol.  # noqa: E501
        :rtype: GetIpv6ConfigProtocol
        """
        return util.deserialize_model(dikt, cls)

    @property
    def protocol(self) -> str:
        """Gets the protocol of this GetIpv6ConfigProtocol.


        :return: The protocol of this GetIpv6ConfigProtocol.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol: str):
        """Sets the protocol of this GetIpv6ConfigProtocol.


        :param protocol: The protocol of this GetIpv6ConfigProtocol.
        :type protocol: str
        """

        self._protocol = protocol
