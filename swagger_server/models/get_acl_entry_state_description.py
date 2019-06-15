# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetAclEntryStateDescription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, description: str=None):  # noqa: E501
        """GetAclEntryStateDescription - a model defined in Swagger

        :param description: The description of this GetAclEntryStateDescription.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'description': str
        }

        self.attribute_map = {
            'description': 'description'
        }

        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'GetAclEntryStateDescription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_acl_entry_state_description of this GetAclEntryStateDescription.  # noqa: E501
        :rtype: GetAclEntryStateDescription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> str:
        """Gets the description of this GetAclEntryStateDescription.


        :return: The description of this GetAclEntryStateDescription.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this GetAclEntryStateDescription.


        :param description: The description of this GetAclEntryStateDescription.
        :type description: str
        """

        self._description = description
