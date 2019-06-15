# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ipv6_config_hop_limit import Ipv6ConfigHopLimit  # noqa: F401,E501
from swagger_server import util


class PutIpv6ConfigHopLimit(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, hop_limit: int=None):  # noqa: E501
        """PutIpv6ConfigHopLimit - a model defined in Swagger

        :param hop_limit: The hop_limit of this PutIpv6ConfigHopLimit.  # noqa: E501
        :type hop_limit: int
        """
        self.swagger_types = {
            'hop_limit': int
        }

        self.attribute_map = {
            'hop_limit': 'hop-limit'
        }

        self._hop_limit = hop_limit

    @classmethod
    def from_dict(cls, dikt) -> 'PutIpv6ConfigHopLimit':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The put_ipv6_config_hop_limit of this PutIpv6ConfigHopLimit.  # noqa: E501
        :rtype: PutIpv6ConfigHopLimit
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hop_limit(self) -> int:
        """Gets the hop_limit of this PutIpv6ConfigHopLimit.


        :return: The hop_limit of this PutIpv6ConfigHopLimit.
        :rtype: int
        """
        return self._hop_limit

    @hop_limit.setter
    def hop_limit(self, hop_limit: int):
        """Sets the hop_limit of this PutIpv6ConfigHopLimit.


        :param hop_limit: The hop_limit of this PutIpv6ConfigHopLimit.
        :type hop_limit: int
        """

        self._hop_limit = hop_limit
