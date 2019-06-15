# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ConfigDestinationFlowLabel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, destination_flow_label: int=None):  # noqa: E501
        """ConfigDestinationFlowLabel - a model defined in Swagger

        :param destination_flow_label: The destination_flow_label of this ConfigDestinationFlowLabel.  # noqa: E501
        :type destination_flow_label: int
        """
        self.swagger_types = {
            'destination_flow_label': int
        }

        self.attribute_map = {
            'destination_flow_label': 'destination-flow-label'
        }

        self._destination_flow_label = destination_flow_label

    @classmethod
    def from_dict(cls, dikt) -> 'ConfigDestinationFlowLabel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The config_destination_flow_label of this ConfigDestinationFlowLabel.  # noqa: E501
        :rtype: ConfigDestinationFlowLabel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destination_flow_label(self) -> int:
        """Gets the destination_flow_label of this ConfigDestinationFlowLabel.


        :return: The destination_flow_label of this ConfigDestinationFlowLabel.
        :rtype: int
        """
        return self._destination_flow_label

    @destination_flow_label.setter
    def destination_flow_label(self, destination_flow_label: int):
        """Sets the destination_flow_label of this ConfigDestinationFlowLabel.


        :param destination_flow_label: The destination_flow_label of this ConfigDestinationFlowLabel.
        :type destination_flow_label: int
        """

        self._destination_flow_label = destination_flow_label
