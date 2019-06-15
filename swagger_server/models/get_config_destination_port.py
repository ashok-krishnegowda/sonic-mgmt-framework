# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetConfigDestinationPort(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, destination_port: str=None):  # noqa: E501
        """GetConfigDestinationPort - a model defined in Swagger

        :param destination_port: The destination_port of this GetConfigDestinationPort.  # noqa: E501
        :type destination_port: str
        """
        self.swagger_types = {
            'destination_port': str
        }

        self.attribute_map = {
            'destination_port': 'destination-port'
        }

        self._destination_port = destination_port

    @classmethod
    def from_dict(cls, dikt) -> 'GetConfigDestinationPort':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_config_destination_port of this GetConfigDestinationPort.  # noqa: E501
        :rtype: GetConfigDestinationPort
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destination_port(self) -> str:
        """Gets the destination_port of this GetConfigDestinationPort.


        :return: The destination_port of this GetConfigDestinationPort.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port: str):
        """Sets the destination_port of this GetConfigDestinationPort.


        :param destination_port: The destination_port of this GetConfigDestinationPort.
        :type destination_port: str
        """

        self._destination_port = destination_port
