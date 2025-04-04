# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .host_resource_statistics import HostResourceStatistics
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostNetworkStatistics(HostResourceStatistics):
    """
    Contains network statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostNetworkStatistics object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostNetworkStatistics.resource_name` attribute
        of this class is ``HOST_NETWORK_STATISTICS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param usage:
            The value to assign to the usage property of this HostNetworkStatistics.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this HostNetworkStatistics.
        :type capacity: float

        :param utilization_percent:
            The value to assign to the utilization_percent property of this HostNetworkStatistics.
        :type utilization_percent: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this HostNetworkStatistics.
        :type usage_change_percent: float

        :param resource_name:
            The value to assign to the resource_name property of this HostNetworkStatistics.
            Allowed values for this property are: "HOST_CPU_STATISTICS", "HOST_MEMORY_STATISTICS", "HOST_STORAGE_STATISTICS", "HOST_NETWORK_STATISTICS", "HOST_IO_STATISTICS"
        :type resource_name: str

        :param network_read_in_mbs:
            The value to assign to the network_read_in_mbs property of this HostNetworkStatistics.
        :type network_read_in_mbs: float

        :param network_write_in_mbs:
            The value to assign to the network_write_in_mbs property of this HostNetworkStatistics.
        :type network_write_in_mbs: float

        """
        self.swagger_types = {
            'usage': 'float',
            'capacity': 'float',
            'utilization_percent': 'float',
            'usage_change_percent': 'float',
            'resource_name': 'str',
            'network_read_in_mbs': 'float',
            'network_write_in_mbs': 'float'
        }
        self.attribute_map = {
            'usage': 'usage',
            'capacity': 'capacity',
            'utilization_percent': 'utilizationPercent',
            'usage_change_percent': 'usageChangePercent',
            'resource_name': 'resourceName',
            'network_read_in_mbs': 'networkReadInMBs',
            'network_write_in_mbs': 'networkWriteInMBs'
        }
        self._usage = None
        self._capacity = None
        self._utilization_percent = None
        self._usage_change_percent = None
        self._resource_name = None
        self._network_read_in_mbs = None
        self._network_write_in_mbs = None
        self._resource_name = 'HOST_NETWORK_STATISTICS'

    @property
    def network_read_in_mbs(self):
        """
        Gets the network_read_in_mbs of this HostNetworkStatistics.

        :return: The network_read_in_mbs of this HostNetworkStatistics.
        :rtype: float
        """
        return self._network_read_in_mbs

    @network_read_in_mbs.setter
    def network_read_in_mbs(self, network_read_in_mbs):
        """
        Sets the network_read_in_mbs of this HostNetworkStatistics.

        :param network_read_in_mbs: The network_read_in_mbs of this HostNetworkStatistics.
        :type: float
        """
        self._network_read_in_mbs = network_read_in_mbs

    @property
    def network_write_in_mbs(self):
        """
        Gets the network_write_in_mbs of this HostNetworkStatistics.

        :return: The network_write_in_mbs of this HostNetworkStatistics.
        :rtype: float
        """
        return self._network_write_in_mbs

    @network_write_in_mbs.setter
    def network_write_in_mbs(self, network_write_in_mbs):
        """
        Sets the network_write_in_mbs of this HostNetworkStatistics.

        :param network_write_in_mbs: The network_write_in_mbs of this HostNetworkStatistics.
        :type: float
        """
        self._network_write_in_mbs = network_write_in_mbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
