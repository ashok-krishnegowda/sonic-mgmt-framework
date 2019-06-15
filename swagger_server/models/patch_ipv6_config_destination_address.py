# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ipv6_config_destination_address import Ipv6ConfigDestinationAddress  # noqa: F401,E501
from swagger_server import util


class PatchIpv6ConfigDestinationAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, destination_address: str=None):  # noqa: E501
        """PatchIpv6ConfigDestinationAddress - a model defined in Swagger

        :param destination_address: The destination_address of this PatchIpv6ConfigDestinationAddress.  # noqa: E501
        :type destination_address: str
        """
        self.swagger_types = {
            'destination_address': str
        }

        self.attribute_map = {
            'destination_address': 'destination-address'
        }

        self._destination_address = destination_address

    @classmethod
    def from_dict(cls, dikt) -> 'PatchIpv6ConfigDestinationAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patch_ipv6_config_destination_address of this PatchIpv6ConfigDestinationAddress.  # noqa: E501
        :rtype: PatchIpv6ConfigDestinationAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destination_address(self) -> str:
        """Gets the destination_address of this PatchIpv6ConfigDestinationAddress.


        :return: The destination_address of this PatchIpv6ConfigDestinationAddress.
        :rtype: str
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address: str):
        """Sets the destination_address of this PatchIpv6ConfigDestinationAddress.


        :param destination_address: The destination_address of this PatchIpv6ConfigDestinationAddress.
        :type destination_address: str
        """

        self._destination_address = destination_address
