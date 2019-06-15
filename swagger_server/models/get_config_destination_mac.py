# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetConfigDestinationMac(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, destination_mac: str=None):  # noqa: E501
        """GetConfigDestinationMac - a model defined in Swagger

        :param destination_mac: The destination_mac of this GetConfigDestinationMac.  # noqa: E501
        :type destination_mac: str
        """
        self.swagger_types = {
            'destination_mac': str
        }

        self.attribute_map = {
            'destination_mac': 'destination-mac'
        }

        self._destination_mac = destination_mac

    @classmethod
    def from_dict(cls, dikt) -> 'GetConfigDestinationMac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_config_destination_mac of this GetConfigDestinationMac.  # noqa: E501
        :rtype: GetConfigDestinationMac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destination_mac(self) -> str:
        """Gets the destination_mac of this GetConfigDestinationMac.


        :return: The destination_mac of this GetConfigDestinationMac.
        :rtype: str
        """
        return self._destination_mac

    @destination_mac.setter
    def destination_mac(self, destination_mac: str):
        """Sets the destination_mac of this GetConfigDestinationMac.


        :param destination_mac: The destination_mac of this GetConfigDestinationMac.
        :type destination_mac: str
        """

        self._destination_mac = destination_mac
