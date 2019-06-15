# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetAclOpenconfigaclaclState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, counter_capability: str=None):  # noqa: E501
        """GetAclOpenconfigaclaclState - a model defined in Swagger

        :param counter_capability: The counter_capability of this GetAclOpenconfigaclaclState.  # noqa: E501
        :type counter_capability: str
        """
        self.swagger_types = {
            'counter_capability': str
        }

        self.attribute_map = {
            'counter_capability': 'counter-capability'
        }

        self._counter_capability = counter_capability

    @classmethod
    def from_dict(cls, dikt) -> 'GetAclOpenconfigaclaclState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_acl_openconfigaclacl_state of this GetAclOpenconfigaclaclState.  # noqa: E501
        :rtype: GetAclOpenconfigaclaclState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def counter_capability(self) -> str:
        """Gets the counter_capability of this GetAclOpenconfigaclaclState.


        :return: The counter_capability of this GetAclOpenconfigaclaclState.
        :rtype: str
        """
        return self._counter_capability

    @counter_capability.setter
    def counter_capability(self, counter_capability: str):
        """Sets the counter_capability of this GetAclOpenconfigaclaclState.


        :param counter_capability: The counter_capability of this GetAclOpenconfigaclaclState.
        :type counter_capability: str
        """

        self._counter_capability = counter_capability
