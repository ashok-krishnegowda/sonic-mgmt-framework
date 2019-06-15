# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.config_tcp_flags import ConfigTcpFlags  # noqa: F401,E501
from swagger_server import util


class PutConfigTcpFlags(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, tcp_flags: str=None):  # noqa: E501
        """PutConfigTcpFlags - a model defined in Swagger

        :param tcp_flags: The tcp_flags of this PutConfigTcpFlags.  # noqa: E501
        :type tcp_flags: str
        """
        self.swagger_types = {
            'tcp_flags': str
        }

        self.attribute_map = {
            'tcp_flags': 'tcp-flags'
        }

        self._tcp_flags = tcp_flags

    @classmethod
    def from_dict(cls, dikt) -> 'PutConfigTcpFlags':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The put_config_tcp_flags of this PutConfigTcpFlags.  # noqa: E501
        :rtype: PutConfigTcpFlags
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tcp_flags(self) -> str:
        """Gets the tcp_flags of this PutConfigTcpFlags.


        :return: The tcp_flags of this PutConfigTcpFlags.
        :rtype: str
        """
        return self._tcp_flags

    @tcp_flags.setter
    def tcp_flags(self, tcp_flags: str):
        """Sets the tcp_flags of this PutConfigTcpFlags.


        :param tcp_flags: The tcp_flags of this PutConfigTcpFlags.
        :type tcp_flags: str
        """

        self._tcp_flags = tcp_flags
