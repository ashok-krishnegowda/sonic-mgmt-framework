# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.config_log_action import ConfigLogAction  # noqa: F401,E501
from swagger_server import util


class PatchConfigLogAction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, log_action: str=None):  # noqa: E501
        """PatchConfigLogAction - a model defined in Swagger

        :param log_action: The log_action of this PatchConfigLogAction.  # noqa: E501
        :type log_action: str
        """
        self.swagger_types = {
            'log_action': str
        }

        self.attribute_map = {
            'log_action': 'log-action'
        }

        self._log_action = log_action

    @classmethod
    def from_dict(cls, dikt) -> 'PatchConfigLogAction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patch_config_log_action of this PatchConfigLogAction.  # noqa: E501
        :rtype: PatchConfigLogAction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def log_action(self) -> str:
        """Gets the log_action of this PatchConfigLogAction.


        :return: The log_action of this PatchConfigLogAction.
        :rtype: str
        """
        return self._log_action

    @log_action.setter
    def log_action(self, log_action: str):
        """Sets the log_action of this PatchConfigLogAction.


        :param log_action: The log_action of this PatchConfigLogAction.
        :type log_action: str
        """

        self._log_action = log_action
