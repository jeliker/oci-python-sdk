# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFindingDetails(object):
    """
    Details to update a finding in a security assessment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFindingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param severity:
            The value to assign to the severity property of this UpdateFindingDetails.
        :type severity: str

        :param justification:
            The value to assign to the justification property of this UpdateFindingDetails.
        :type justification: str

        :param time_valid_until:
            The value to assign to the time_valid_until property of this UpdateFindingDetails.
        :type time_valid_until: datetime

        """
        self.swagger_types = {
            'severity': 'str',
            'justification': 'str',
            'time_valid_until': 'datetime'
        }
        self.attribute_map = {
            'severity': 'severity',
            'justification': 'justification',
            'time_valid_until': 'timeValidUntil'
        }
        self._severity = None
        self._justification = None
        self._time_valid_until = None

    @property
    def severity(self):
        """
        Gets the severity of this UpdateFindingDetails.
        The severity of the finding as defined or changed by the user.


        :return: The severity of this UpdateFindingDetails.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this UpdateFindingDetails.
        The severity of the finding as defined or changed by the user.


        :param severity: The severity of this UpdateFindingDetails.
        :type: str
        """
        self._severity = severity

    @property
    def justification(self):
        """
        Gets the justification of this UpdateFindingDetails.
        User provided reason for accepting or modifying this finding if they choose to do so.


        :return: The justification of this UpdateFindingDetails.
        :rtype: str
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """
        Sets the justification of this UpdateFindingDetails.
        User provided reason for accepting or modifying this finding if they choose to do so.


        :param justification: The justification of this UpdateFindingDetails.
        :type: str
        """
        self._justification = justification

    @property
    def time_valid_until(self):
        """
        Gets the time_valid_until of this UpdateFindingDetails.
        The time until which the change in severity (deferred / modified) got the given finding is valid.


        :return: The time_valid_until of this UpdateFindingDetails.
        :rtype: datetime
        """
        return self._time_valid_until

    @time_valid_until.setter
    def time_valid_until(self, time_valid_until):
        """
        Sets the time_valid_until of this UpdateFindingDetails.
        The time until which the change in severity (deferred / modified) got the given finding is valid.


        :param time_valid_until: The time_valid_until of this UpdateFindingDetails.
        :type: datetime
        """
        self._time_valid_until = time_valid_until

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
