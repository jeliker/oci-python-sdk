# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .database_configuration_metric_group import DatabaseConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostAllocation(DatabaseConfigurationMetricGroup):
    """
    Resource Allocation metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostAllocation object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostAllocation.metric_name` attribute
        of this class is ``HOST_RESOURCE_ALLOCATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostAllocation.
            Allowed values for this property are: "DB_EXTERNAL_PROPERTIES", "DB_EXTERNAL_INSTANCE", "DB_OS_CONFIG_INSTANCE", "DB_PARAMETERS", "DB_CONNECTION_STATUS", "HOST_RESOURCE_ALLOCATION", "ASM_ENTITY", "EXADATA_CELL_CONFIG"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostAllocation.
        :type time_collected: datetime

        :param resource_name:
            The value to assign to the resource_name property of this HostAllocation.
        :type resource_name: str

        :param resource_value:
            The value to assign to the resource_value property of this HostAllocation.
        :type resource_value: int

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'resource_name': 'str',
            'resource_value': 'int'
        }
        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'resource_name': 'resourceName',
            'resource_value': 'resourceValue'
        }
        self._metric_name = None
        self._time_collected = None
        self._resource_name = None
        self._resource_value = None
        self._metric_name = 'HOST_RESOURCE_ALLOCATION'

    @property
    def resource_name(self):
        """
        Gets the resource_name of this HostAllocation.
        Name of the host resource


        :return: The resource_name of this HostAllocation.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this HostAllocation.
        Name of the host resource


        :param resource_name: The resource_name of this HostAllocation.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_value(self):
        """
        Gets the resource_value of this HostAllocation.
        Value of the host resource


        :return: The resource_value of this HostAllocation.
        :rtype: int
        """
        return self._resource_value

    @resource_value.setter
    def resource_value(self, resource_value):
        """
        Sets the resource_value of this HostAllocation.
        Value of the host resource


        :param resource_value: The resource_value of this HostAllocation.
        :type: int
        """
        self._resource_value = resource_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
