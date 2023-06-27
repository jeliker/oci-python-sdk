# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateWorkRequestDetails(object):
    """
    Detail information for updating a work request.
    """

    #: A constant which can be used with the status property of a UpdateWorkRequestDetails.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a UpdateWorkRequestDetails.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a UpdateWorkRequestDetails.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a UpdateWorkRequestDetails.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a UpdateWorkRequestDetails.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a UpdateWorkRequestDetails.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateWorkRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateWorkRequestDetails.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"
        :type status: str

        :param percent_complete:
            The value to assign to the percent_complete property of this UpdateWorkRequestDetails.
        :type percent_complete: float

        :param time_finished:
            The value to assign to the time_finished property of this UpdateWorkRequestDetails.
        :type time_finished: datetime

        :param description:
            The value to assign to the description property of this UpdateWorkRequestDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateWorkRequestDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'status': 'str',
            'percent_complete': 'float',
            'time_finished': 'datetime',
            'description': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'percent_complete': 'percentComplete',
            'time_finished': 'timeFinished',
            'description': 'description',
            'display_name': 'displayName'
        }

        self._status = None
        self._percent_complete = None
        self._time_finished = None
        self._description = None
        self._display_name = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpdateWorkRequestDetails.
        status of current work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"


        :return: The status of this UpdateWorkRequestDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateWorkRequestDetails.
        status of current work request.


        :param status: The status of this UpdateWorkRequestDetails.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this UpdateWorkRequestDetails.
        The percentage complete of the operation tracked by this work request.


        :return: The percent_complete of this UpdateWorkRequestDetails.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this UpdateWorkRequestDetails.
        The percentage complete of the operation tracked by this work request.


        :param percent_complete: The percent_complete of this UpdateWorkRequestDetails.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_finished(self):
        """
        Gets the time_finished of this UpdateWorkRequestDetails.
        The date and time the object was finished, as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_finished of this UpdateWorkRequestDetails.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this UpdateWorkRequestDetails.
        The date and time the object was finished, as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_finished: The time_finished of this UpdateWorkRequestDetails.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def description(self):
        """
        Gets the description of this UpdateWorkRequestDetails.
        A short description about the work request.


        :return: The description of this UpdateWorkRequestDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateWorkRequestDetails.
        A short description about the work request.


        :param description: The description of this UpdateWorkRequestDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateWorkRequestDetails.
        A short display for about the work request.


        :return: The display_name of this UpdateWorkRequestDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateWorkRequestDetails.
        A short display for about the work request.


        :param display_name: The display_name of this UpdateWorkRequestDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
