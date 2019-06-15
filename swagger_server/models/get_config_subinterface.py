# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetConfigSubinterface(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, subinterface: int=None):  # noqa: E501
        """GetConfigSubinterface - a model defined in Swagger

        :param subinterface: The subinterface of this GetConfigSubinterface.  # noqa: E501
        :type subinterface: int
        """
        self.swagger_types = {
            'subinterface': int
        }

        self.attribute_map = {
            'subinterface': 'subinterface'
        }

        self._subinterface = subinterface

    @classmethod
    def from_dict(cls, dikt) -> 'GetConfigSubinterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_config_subinterface of this GetConfigSubinterface.  # noqa: E501
        :rtype: GetConfigSubinterface
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subinterface(self) -> int:
        """Gets the subinterface of this GetConfigSubinterface.


        :return: The subinterface of this GetConfigSubinterface.
        :rtype: int
        """
        return self._subinterface

    @subinterface.setter
    def subinterface(self, subinterface: int):
        """Sets the subinterface of this GetConfigSubinterface.


        :param subinterface: The subinterface of this GetConfigSubinterface.
        :type subinterface: int
        """

        self._subinterface = subinterface
