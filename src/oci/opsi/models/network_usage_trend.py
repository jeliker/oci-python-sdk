# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkUsageTrend(object):
    """
    Usage data samples.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkUsageTrend object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param end_timestamp:
            The value to assign to the end_timestamp property of this NetworkUsageTrend.
        :type end_timestamp: datetime

        :param all_network_read_in_mbps:
            The value to assign to the all_network_read_in_mbps property of this NetworkUsageTrend.
        :type all_network_read_in_mbps: float

        :param all_network_write_in_mbps:
            The value to assign to the all_network_write_in_mbps property of this NetworkUsageTrend.
        :type all_network_write_in_mbps: float

        :param all_network_io_in_mbps:
            The value to assign to the all_network_io_in_mbps property of this NetworkUsageTrend.
        :type all_network_io_in_mbps: float

        """
        self.swagger_types = {
            'end_timestamp': 'datetime',
            'all_network_read_in_mbps': 'float',
            'all_network_write_in_mbps': 'float',
            'all_network_io_in_mbps': 'float'
        }
        self.attribute_map = {
            'end_timestamp': 'endTimestamp',
            'all_network_read_in_mbps': 'allNetworkReadInMbps',
            'all_network_write_in_mbps': 'allNetworkWriteInMbps',
            'all_network_io_in_mbps': 'allNetworkIoInMbps'
        }
        self._end_timestamp = None
        self._all_network_read_in_mbps = None
        self._all_network_write_in_mbps = None
        self._all_network_io_in_mbps = None

    @property
    def end_timestamp(self):
        """
        **[Required]** Gets the end_timestamp of this NetworkUsageTrend.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :return: The end_timestamp of this NetworkUsageTrend.
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this NetworkUsageTrend.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :param end_timestamp: The end_timestamp of this NetworkUsageTrend.
        :type: datetime
        """
        self._end_timestamp = end_timestamp

    @property
    def all_network_read_in_mbps(self):
        """
        **[Required]** Gets the all_network_read_in_mbps of this NetworkUsageTrend.
        Network read in Mbps.


        :return: The all_network_read_in_mbps of this NetworkUsageTrend.
        :rtype: float
        """
        return self._all_network_read_in_mbps

    @all_network_read_in_mbps.setter
    def all_network_read_in_mbps(self, all_network_read_in_mbps):
        """
        Sets the all_network_read_in_mbps of this NetworkUsageTrend.
        Network read in Mbps.


        :param all_network_read_in_mbps: The all_network_read_in_mbps of this NetworkUsageTrend.
        :type: float
        """
        self._all_network_read_in_mbps = all_network_read_in_mbps

    @property
    def all_network_write_in_mbps(self):
        """
        **[Required]** Gets the all_network_write_in_mbps of this NetworkUsageTrend.
        Network write in Mbps.


        :return: The all_network_write_in_mbps of this NetworkUsageTrend.
        :rtype: float
        """
        return self._all_network_write_in_mbps

    @all_network_write_in_mbps.setter
    def all_network_write_in_mbps(self, all_network_write_in_mbps):
        """
        Sets the all_network_write_in_mbps of this NetworkUsageTrend.
        Network write in Mbps.


        :param all_network_write_in_mbps: The all_network_write_in_mbps of this NetworkUsageTrend.
        :type: float
        """
        self._all_network_write_in_mbps = all_network_write_in_mbps

    @property
    def all_network_io_in_mbps(self):
        """
        **[Required]** Gets the all_network_io_in_mbps of this NetworkUsageTrend.
        Network input/output in Mbps.


        :return: The all_network_io_in_mbps of this NetworkUsageTrend.
        :rtype: float
        """
        return self._all_network_io_in_mbps

    @all_network_io_in_mbps.setter
    def all_network_io_in_mbps(self, all_network_io_in_mbps):
        """
        Sets the all_network_io_in_mbps of this NetworkUsageTrend.
        Network input/output in Mbps.


        :param all_network_io_in_mbps: The all_network_io_in_mbps of this NetworkUsageTrend.
        :type: float
        """
        self._all_network_io_in_mbps = all_network_io_in_mbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
