# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.egress_acl_set_config_set_name import EgressAclSetConfigSetName  # noqa: F401,E501
from swagger_server import util


class PatchEgressAclSetConfigSetName(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, set_name: str=None):  # noqa: E501
        """PatchEgressAclSetConfigSetName - a model defined in Swagger

        :param set_name: The set_name of this PatchEgressAclSetConfigSetName.  # noqa: E501
        :type set_name: str
        """
        self.swagger_types = {
            'set_name': str
        }

        self.attribute_map = {
            'set_name': 'set-name'
        }

        self._set_name = set_name

    @classmethod
    def from_dict(cls, dikt) -> 'PatchEgressAclSetConfigSetName':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patch_egress_acl_set_config_set_name of this PatchEgressAclSetConfigSetName.  # noqa: E501
        :rtype: PatchEgressAclSetConfigSetName
        """
        return util.deserialize_model(dikt, cls)

    @property
    def set_name(self) -> str:
        """Gets the set_name of this PatchEgressAclSetConfigSetName.


        :return: The set_name of this PatchEgressAclSetConfigSetName.
        :rtype: str
        """
        return self._set_name

    @set_name.setter
    def set_name(self, set_name: str):
        """Sets the set_name of this PatchEgressAclSetConfigSetName.


        :param set_name: The set_name of this PatchEgressAclSetConfigSetName.
        :type set_name: str
        """

        self._set_name = set_name
