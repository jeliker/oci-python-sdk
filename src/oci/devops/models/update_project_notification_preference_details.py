# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateProjectNotificationPreferenceDetails(object):
    """
    Information to update notification preference settings on project resource
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateProjectNotificationPreferenceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param notification_preference:
            The value to assign to the notification_preference property of this UpdateProjectNotificationPreferenceDetails.
        :type notification_preference: str

        """
        self.swagger_types = {
            'notification_preference': 'str'
        }
        self.attribute_map = {
            'notification_preference': 'notificationPreference'
        }
        self._notification_preference = None

    @property
    def notification_preference(self):
        """
        **[Required]** Gets the notification_preference of this UpdateProjectNotificationPreferenceDetails.
        The override value of project notification preference.


        :return: The notification_preference of this UpdateProjectNotificationPreferenceDetails.
        :rtype: str
        """
        return self._notification_preference

    @notification_preference.setter
    def notification_preference(self, notification_preference):
        """
        Sets the notification_preference of this UpdateProjectNotificationPreferenceDetails.
        The override value of project notification preference.


        :param notification_preference: The notification_preference of this UpdateProjectNotificationPreferenceDetails.
        :type: str
        """
        self._notification_preference = notification_preference

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
