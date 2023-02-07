# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .configuration_item_allowed_value_details import ConfigurationItemAllowedValueDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationItemLimitAllowedValueDetails(ConfigurationItemAllowedValueDetails):
    """
    Allowed value details of configuration item for LIMIT type. Value has to be between minValue and maxValue.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationItemLimitAllowedValueDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.ConfigurationItemLimitAllowedValueDetails.allowed_value_type` attribute
        of this class is ``LIMIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allowed_value_type:
            The value to assign to the allowed_value_type property of this ConfigurationItemLimitAllowedValueDetails.
            Allowed values for this property are: "LIMIT", "PICK", "FREE_TEXT"
        :type allowed_value_type: str

        :param min_value:
            The value to assign to the min_value property of this ConfigurationItemLimitAllowedValueDetails.
        :type min_value: str

        :param max_value:
            The value to assign to the max_value property of this ConfigurationItemLimitAllowedValueDetails.
        :type max_value: str

        """
        self.swagger_types = {
            'allowed_value_type': 'str',
            'min_value': 'str',
            'max_value': 'str'
        }

        self.attribute_map = {
            'allowed_value_type': 'allowedValueType',
            'min_value': 'minValue',
            'max_value': 'maxValue'
        }

        self._allowed_value_type = None
        self._min_value = None
        self._max_value = None
        self._allowed_value_type = 'LIMIT'

    @property
    def min_value(self):
        """
        Gets the min_value of this ConfigurationItemLimitAllowedValueDetails.
        Minimum value limit for the configuration item.


        :return: The min_value of this ConfigurationItemLimitAllowedValueDetails.
        :rtype: str
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """
        Sets the min_value of this ConfigurationItemLimitAllowedValueDetails.
        Minimum value limit for the configuration item.


        :param min_value: The min_value of this ConfigurationItemLimitAllowedValueDetails.
        :type: str
        """
        self._min_value = min_value

    @property
    def max_value(self):
        """
        Gets the max_value of this ConfigurationItemLimitAllowedValueDetails.
        Maximum value limit for the configuration item.


        :return: The max_value of this ConfigurationItemLimitAllowedValueDetails.
        :rtype: str
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """
        Sets the max_value of this ConfigurationItemLimitAllowedValueDetails.
        Maximum value limit for the configuration item.


        :param max_value: The max_value of this ConfigurationItemLimitAllowedValueDetails.
        :type: str
        """
        self._max_value = max_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
