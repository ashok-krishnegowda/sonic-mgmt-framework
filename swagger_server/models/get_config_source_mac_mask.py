# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetConfigSourceMacMask(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, source_mac_mask: str=None):  # noqa: E501
        """GetConfigSourceMacMask - a model defined in Swagger

        :param source_mac_mask: The source_mac_mask of this GetConfigSourceMacMask.  # noqa: E501
        :type source_mac_mask: str
        """
        self.swagger_types = {
            'source_mac_mask': str
        }

        self.attribute_map = {
            'source_mac_mask': 'source-mac-mask'
        }

        self._source_mac_mask = source_mac_mask

    @classmethod
    def from_dict(cls, dikt) -> 'GetConfigSourceMacMask':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_config_source_mac_mask of this GetConfigSourceMacMask.  # noqa: E501
        :rtype: GetConfigSourceMacMask
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source_mac_mask(self) -> str:
        """Gets the source_mac_mask of this GetConfigSourceMacMask.


        :return: The source_mac_mask of this GetConfigSourceMacMask.
        :rtype: str
        """
        return self._source_mac_mask

    @source_mac_mask.setter
    def source_mac_mask(self, source_mac_mask: str):
        """Sets the source_mac_mask of this GetConfigSourceMacMask.


        :param source_mac_mask: The source_mac_mask of this GetConfigSourceMacMask.
        :type source_mac_mask: str
        """

        self._source_mac_mask = source_mac_mask
