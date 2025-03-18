# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopSchedule(object):
    """
    Provides the schedule information for a desktop.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopSchedule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cron_expression:
            The value to assign to the cron_expression property of this DesktopSchedule.
        :type cron_expression: str

        :param timezone:
            The value to assign to the timezone property of this DesktopSchedule.
        :type timezone: str

        """
        self.swagger_types = {
            'cron_expression': 'str',
            'timezone': 'str'
        }
        self.attribute_map = {
            'cron_expression': 'cronExpression',
            'timezone': 'timezone'
        }
        self._cron_expression = None
        self._timezone = None

    @property
    def cron_expression(self):
        """
        **[Required]** Gets the cron_expression of this DesktopSchedule.
        A cron expression describing the desktop's schedule.


        :return: The cron_expression of this DesktopSchedule.
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """
        Sets the cron_expression of this DesktopSchedule.
        A cron expression describing the desktop's schedule.


        :param cron_expression: The cron_expression of this DesktopSchedule.
        :type: str
        """
        self._cron_expression = cron_expression

    @property
    def timezone(self):
        """
        **[Required]** Gets the timezone of this DesktopSchedule.
        The timezone of the desktop's schedule.


        :return: The timezone of this DesktopSchedule.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this DesktopSchedule.
        The timezone of the desktop's schedule.


        :param timezone: The timezone of this DesktopSchedule.
        :type: str
        """
        self._timezone = timezone

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
