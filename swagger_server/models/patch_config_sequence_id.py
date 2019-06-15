# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.config_sequence_id import ConfigSequenceId  # noqa: F401,E501
from swagger_server import util


class PatchConfigSequenceId(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sequence_id: int=None):  # noqa: E501
        """PatchConfigSequenceId - a model defined in Swagger

        :param sequence_id: The sequence_id of this PatchConfigSequenceId.  # noqa: E501
        :type sequence_id: int
        """
        self.swagger_types = {
            'sequence_id': int
        }

        self.attribute_map = {
            'sequence_id': 'sequence-id'
        }

        self._sequence_id = sequence_id

    @classmethod
    def from_dict(cls, dikt) -> 'PatchConfigSequenceId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patch_config_sequence_id of this PatchConfigSequenceId.  # noqa: E501
        :rtype: PatchConfigSequenceId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sequence_id(self) -> int:
        """Gets the sequence_id of this PatchConfigSequenceId.


        :return: The sequence_id of this PatchConfigSequenceId.
        :rtype: int
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id: int):
        """Sets the sequence_id of this PatchConfigSequenceId.


        :param sequence_id: The sequence_id of this PatchConfigSequenceId.
        :type sequence_id: int
        """

        self._sequence_id = sequence_id
