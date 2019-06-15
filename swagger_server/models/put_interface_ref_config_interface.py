# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.interface_ref_config_interface import InterfaceRefConfigInterface  # noqa: F401,E501
from swagger_server import util


class PutInterfaceRefConfigInterface(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, interface: str=None):  # noqa: E501
        """PutInterfaceRefConfigInterface - a model defined in Swagger

        :param interface: The interface of this PutInterfaceRefConfigInterface.  # noqa: E501
        :type interface: str
        """
        self.swagger_types = {
            'interface': str
        }

        self.attribute_map = {
            'interface': 'interface'
        }

        self._interface = interface

    @classmethod
    def from_dict(cls, dikt) -> 'PutInterfaceRefConfigInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The put_interface_ref_config_interface of this PutInterfaceRefConfigInterface.  # noqa: E501
        :rtype: PutInterfaceRefConfigInterface
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interface(self) -> str:
        """Gets the interface of this PutInterfaceRefConfigInterface.


        :return: The interface of this PutInterfaceRefConfigInterface.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface: str):
        """Sets the interface of this PutInterfaceRefConfigInterface.


        :param interface: The interface of this PutInterfaceRefConfigInterface.
        :type interface: str
        """

        self._interface = interface
