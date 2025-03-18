# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetErrorAggregation(object):
    """
    Aggregation of FleetErrors
    """

    #: A constant which can be used with the reason property of a FleetErrorAggregation.
    #: This constant has a value of "NO_MANAGED_INSTANCES"
    REASON_NO_MANAGED_INSTANCES = "NO_MANAGED_INSTANCES"

    #: A constant which can be used with the reason property of a FleetErrorAggregation.
    #: This constant has a value of "INVENTORY_LOG"
    REASON_INVENTORY_LOG = "INVENTORY_LOG"

    def __init__(self, **kwargs):
        """
        Initializes a new FleetErrorAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reason:
            The value to assign to the reason property of this FleetErrorAggregation.
            Allowed values for this property are: "NO_MANAGED_INSTANCES", "INVENTORY_LOG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reason: str

        :param count:
            The value to assign to the count property of this FleetErrorAggregation.
        :type count: int

        """
        self.swagger_types = {
            'reason': 'str',
            'count': 'int'
        }
        self.attribute_map = {
            'reason': 'reason',
            'count': 'count'
        }
        self._reason = None
        self._count = None

    @property
    def reason(self):
        """
        **[Required]** Gets the reason of this FleetErrorAggregation.
        Enum that uniquely identifies the fleet error.

        Allowed values for this property are: "NO_MANAGED_INSTANCES", "INVENTORY_LOG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reason of this FleetErrorAggregation.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this FleetErrorAggregation.
        Enum that uniquely identifies the fleet error.


        :param reason: The reason of this FleetErrorAggregation.
        :type: str
        """
        allowed_values = ["NO_MANAGED_INSTANCES", "INVENTORY_LOG"]
        if not value_allowed_none_or_none_sentinel(reason, allowed_values):
            reason = 'UNKNOWN_ENUM_VALUE'
        self._reason = reason

    @property
    def count(self):
        """
        **[Required]** Gets the count of this FleetErrorAggregation.
        Number of FleetErrors encountered for the specific reason.


        :return: The count of this FleetErrorAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this FleetErrorAggregation.
        Number of FleetErrors encountered for the specific reason.


        :param count: The count of this FleetErrorAggregation.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
