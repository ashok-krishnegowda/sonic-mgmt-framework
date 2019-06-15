# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.config_destination_port import ConfigDestinationPort  # noqa: F401,E501
from swagger_server import util


class PutConfigDestinationPort(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, destination_port: str=None):  # noqa: E501
        """PutConfigDestinationPort - a model defined in Swagger

        :param destination_port: The destination_port of this PutConfigDestinationPort.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'PutConfigDestinationPort':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The put_config_destination_port of this PutConfigDestinationPort.  # noqa: E501
        :rtype: PutConfigDestinationPort
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destination_port(self) -> str:
        """Gets the destination_port of this PutConfigDestinationPort.


        :return: The destination_port of this PutConfigDestinationPort.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port: str):
        """Sets the destination_port of this PutConfigDestinationPort.


        :param destination_port: The destination_port of this PutConfigDestinationPort.
        :type destination_port: str
        """

        self._destination_port = destination_port
