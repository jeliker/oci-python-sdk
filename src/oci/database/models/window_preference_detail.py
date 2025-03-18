# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WindowPreferenceDetail(object):
    """
    The Single Scheduling Window details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WindowPreferenceDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param months:
            The value to assign to the months property of this WindowPreferenceDetail.
        :type months: list[oci.database.models.Month]

        :param weeks_of_month:
            The value to assign to the weeks_of_month property of this WindowPreferenceDetail.
        :type weeks_of_month: list[int]

        :param days_of_week:
            The value to assign to the days_of_week property of this WindowPreferenceDetail.
        :type days_of_week: list[oci.database.models.DayOfWeek]

        :param start_time:
            The value to assign to the start_time property of this WindowPreferenceDetail.
        :type start_time: str

        :param duration:
            The value to assign to the duration property of this WindowPreferenceDetail.
        :type duration: int

        :param is_enforced_duration:
            The value to assign to the is_enforced_duration property of this WindowPreferenceDetail.
        :type is_enforced_duration: bool

        """
        self.swagger_types = {
            'months': 'list[Month]',
            'weeks_of_month': 'list[int]',
            'days_of_week': 'list[DayOfWeek]',
            'start_time': 'str',
            'duration': 'int',
            'is_enforced_duration': 'bool'
        }
        self.attribute_map = {
            'months': 'months',
            'weeks_of_month': 'weeksOfMonth',
            'days_of_week': 'daysOfWeek',
            'start_time': 'startTime',
            'duration': 'duration',
            'is_enforced_duration': 'isEnforcedDuration'
        }
        self._months = None
        self._weeks_of_month = None
        self._days_of_week = None
        self._start_time = None
        self._duration = None
        self._is_enforced_duration = None

    @property
    def months(self):
        """
        Gets the months of this WindowPreferenceDetail.
        Months during the year when scheduled window should be performed.


        :return: The months of this WindowPreferenceDetail.
        :rtype: list[oci.database.models.Month]
        """
        return self._months

    @months.setter
    def months(self, months):
        """
        Sets the months of this WindowPreferenceDetail.
        Months during the year when scheduled window should be performed.


        :param months: The months of this WindowPreferenceDetail.
        :type: list[oci.database.models.Month]
        """
        self._months = months

    @property
    def weeks_of_month(self):
        """
        **[Required]** Gets the weeks_of_month of this WindowPreferenceDetail.
        Weeks during the month when scheduled window should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
        For example, to allow scheduling window during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2. Scheduling window cannot be scheduled for the fifth week of months that contain more than 28 days.
        Note that this parameter works in conjunction with the  daysOfWeek and startTime parameters to allow you to specify specific days of the week and hours that scheduled window will be performed.


        :return: The weeks_of_month of this WindowPreferenceDetail.
        :rtype: list[int]
        """
        return self._weeks_of_month

    @weeks_of_month.setter
    def weeks_of_month(self, weeks_of_month):
        """
        Sets the weeks_of_month of this WindowPreferenceDetail.
        Weeks during the month when scheduled window should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
        For example, to allow scheduling window during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2. Scheduling window cannot be scheduled for the fifth week of months that contain more than 28 days.
        Note that this parameter works in conjunction with the  daysOfWeek and startTime parameters to allow you to specify specific days of the week and hours that scheduled window will be performed.


        :param weeks_of_month: The weeks_of_month of this WindowPreferenceDetail.
        :type: list[int]
        """
        self._weeks_of_month = weeks_of_month

    @property
    def days_of_week(self):
        """
        **[Required]** Gets the days_of_week of this WindowPreferenceDetail.
        Days during the week when scheduling window should be performed.


        :return: The days_of_week of this WindowPreferenceDetail.
        :rtype: list[oci.database.models.DayOfWeek]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        """
        Sets the days_of_week of this WindowPreferenceDetail.
        Days during the week when scheduling window should be performed.


        :param days_of_week: The days_of_week of this WindowPreferenceDetail.
        :type: list[oci.database.models.DayOfWeek]
        """
        self._days_of_week = days_of_week

    @property
    def start_time(self):
        """
        **[Required]** Gets the start_time of this WindowPreferenceDetail.
        The scheduling window start time. The value must use the ISO-8601 format \"hh:mm\".


        :return: The start_time of this WindowPreferenceDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this WindowPreferenceDetail.
        The scheduling window start time. The value must use the ISO-8601 format \"hh:mm\".


        :param start_time: The start_time of this WindowPreferenceDetail.
        :type: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        """
        **[Required]** Gets the duration of this WindowPreferenceDetail.
        Duration window allows user to set a duration they plan to allocate for Scheduling window. The duration is in minutes.


        :return: The duration of this WindowPreferenceDetail.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this WindowPreferenceDetail.
        Duration window allows user to set a duration they plan to allocate for Scheduling window. The duration is in minutes.


        :param duration: The duration of this WindowPreferenceDetail.
        :type: int
        """
        self._duration = duration

    @property
    def is_enforced_duration(self):
        """
        **[Required]** Gets the is_enforced_duration of this WindowPreferenceDetail.
        Indicates if duration the user plans to allocate for scheduling window is strictly enforced. The default value is `FALSE`.


        :return: The is_enforced_duration of this WindowPreferenceDetail.
        :rtype: bool
        """
        return self._is_enforced_duration

    @is_enforced_duration.setter
    def is_enforced_duration(self, is_enforced_duration):
        """
        Sets the is_enforced_duration of this WindowPreferenceDetail.
        Indicates if duration the user plans to allocate for scheduling window is strictly enforced. The default value is `FALSE`.


        :param is_enforced_duration: The is_enforced_duration of this WindowPreferenceDetail.
        :type: bool
        """
        self._is_enforced_duration = is_enforced_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
