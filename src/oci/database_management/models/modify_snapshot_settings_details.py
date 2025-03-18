# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModifySnapshotSettingsDetails(object):
    """
    Details to modify the AWR snapshot settings for a database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModifySnapshotSettingsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param retention:
            The value to assign to the retention property of this ModifySnapshotSettingsDetails.
        :type retention: int

        :param interval:
            The value to assign to the interval property of this ModifySnapshotSettingsDetails.
        :type interval: int

        """
        self.swagger_types = {
            'retention': 'int',
            'interval': 'int'
        }
        self.attribute_map = {
            'retention': 'retention',
            'interval': 'interval'
        }
        self._retention = None
        self._interval = None

    @property
    def retention(self):
        """
        Gets the retention of this ModifySnapshotSettingsDetails.
        The retention time in minutes. Acceptable values are 0, 1440 to 52596000 (inclusive), and null.


        :return: The retention of this ModifySnapshotSettingsDetails.
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """
        Sets the retention of this ModifySnapshotSettingsDetails.
        The retention time in minutes. Acceptable values are 0, 1440 to 52596000 (inclusive), and null.


        :param retention: The retention of this ModifySnapshotSettingsDetails.
        :type: int
        """
        self._retention = retention

    @property
    def interval(self):
        """
        Gets the interval of this ModifySnapshotSettingsDetails.
        The interval time in minutes. Acceptable values are 0, 10 to 527040 (inclusive), and null.


        :return: The interval of this ModifySnapshotSettingsDetails.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this ModifySnapshotSettingsDetails.
        The interval time in minutes. Acceptable values are 0, 10 to 527040 (inclusive), and null.


        :param interval: The interval of this ModifySnapshotSettingsDetails.
        :type: int
        """
        self._interval = interval

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
