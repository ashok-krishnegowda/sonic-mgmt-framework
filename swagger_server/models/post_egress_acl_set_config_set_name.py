# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.egress_acl_set_config_set_name import EgressAclSetConfigSetName  # noqa: F401,E501
from swagger_server import util


class PostEgressAclSetConfigSetName(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, set_name: str=None, type: str=None):  # noqa: E501
        """PostEgressAclSetConfigSetName - a model defined in Swagger

        :param set_name: The set_name of this PostEgressAclSetConfigSetName.  # noqa: E501
        :type set_name: str
        :param type: The type of this PostEgressAclSetConfigSetName.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'set_name': str,
            'type': str
        }

        self.attribute_map = {
            'set_name': 'set-name',
            'type': 'type'
        }

        self._set_name = set_name
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'PostEgressAclSetConfigSetName':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The post_egress_acl_set_config_set_name of this PostEgressAclSetConfigSetName.  # noqa: E501
        :rtype: PostEgressAclSetConfigSetName
        """
        return util.deserialize_model(dikt, cls)

    @property
    def set_name(self) -> str:
        """Gets the set_name of this PostEgressAclSetConfigSetName.


        :return: The set_name of this PostEgressAclSetConfigSetName.
        :rtype: str
        """
        return self._set_name

    @set_name.setter
    def set_name(self, set_name: str):
        """Sets the set_name of this PostEgressAclSetConfigSetName.


        :param set_name: The set_name of this PostEgressAclSetConfigSetName.
        :type set_name: str
        """

        self._set_name = set_name

    @property
    def type(self) -> str:
        """Gets the type of this PostEgressAclSetConfigSetName.


        :return: The type of this PostEgressAclSetConfigSetName.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this PostEgressAclSetConfigSetName.


        :param type: The type of this PostEgressAclSetConfigSetName.
        :type type: str
        """

        self._type = type
