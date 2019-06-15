# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetStateSourceMac(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, source_mac: str=None):  # noqa: E501
        """GetStateSourceMac - a model defined in Swagger

        :param source_mac: The source_mac of this GetStateSourceMac.  # noqa: E501
        :type source_mac: str
        """
        self.swagger_types = {
            'source_mac': str
        }

        self.attribute_map = {
            'source_mac': 'source-mac'
        }

        self._source_mac = source_mac

    @classmethod
    def from_dict(cls, dikt) -> 'GetStateSourceMac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_state_source_mac of this GetStateSourceMac.  # noqa: E501
        :rtype: GetStateSourceMac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source_mac(self) -> str:
        """Gets the source_mac of this GetStateSourceMac.


        :return: The source_mac of this GetStateSourceMac.
        :rtype: str
        """
        return self._source_mac

    @source_mac.setter
    def source_mac(self, source_mac: str):
        """Sets the source_mac of this GetStateSourceMac.


        :param source_mac: The source_mac of this GetStateSourceMac.
        :type source_mac: str
        """

        self._source_mac = source_mac
