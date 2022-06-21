# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttentionLogSummary(object):
    """
    The details for one attention log entry.
    """

    #: A constant which can be used with the message_urgency property of a AttentionLogSummary.
    #: This constant has a value of "IMMEDIATE"
    MESSAGE_URGENCY_IMMEDIATE = "IMMEDIATE"

    #: A constant which can be used with the message_urgency property of a AttentionLogSummary.
    #: This constant has a value of "SOON"
    MESSAGE_URGENCY_SOON = "SOON"

    #: A constant which can be used with the message_urgency property of a AttentionLogSummary.
    #: This constant has a value of "DEFERRABLE"
    MESSAGE_URGENCY_DEFERRABLE = "DEFERRABLE"

    #: A constant which can be used with the message_urgency property of a AttentionLogSummary.
    #: This constant has a value of "INFO"
    MESSAGE_URGENCY_INFO = "INFO"

    #: A constant which can be used with the message_type property of a AttentionLogSummary.
    #: This constant has a value of "UNKNOWN"
    MESSAGE_TYPE_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the message_type property of a AttentionLogSummary.
    #: This constant has a value of "INCIDENT_ERROR"
    MESSAGE_TYPE_INCIDENT_ERROR = "INCIDENT_ERROR"

    #: A constant which can be used with the message_type property of a AttentionLogSummary.
    #: This constant has a value of "ERROR"
    MESSAGE_TYPE_ERROR = "ERROR"

    #: A constant which can be used with the message_type property of a AttentionLogSummary.
    #: This constant has a value of "WARNING"
    MESSAGE_TYPE_WARNING = "WARNING"

    #: A constant which can be used with the message_type property of a AttentionLogSummary.
    #: This constant has a value of "NOTIFICATION"
    MESSAGE_TYPE_NOTIFICATION = "NOTIFICATION"

    #: A constant which can be used with the message_type property of a AttentionLogSummary.
    #: This constant has a value of "TRACE"
    MESSAGE_TYPE_TRACE = "TRACE"

    def __init__(self, **kwargs):
        """
        Initializes a new AttentionLogSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message_urgency:
            The value to assign to the message_urgency property of this AttentionLogSummary.
            Allowed values for this property are: "IMMEDIATE", "SOON", "DEFERRABLE", "INFO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type message_urgency: str

        :param message_type:
            The value to assign to the message_type property of this AttentionLogSummary.
            Allowed values for this property are: "UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type message_type: str

        :param message_content:
            The value to assign to the message_content property of this AttentionLogSummary.
        :type message_content: str

        :param timestamp:
            The value to assign to the timestamp property of this AttentionLogSummary.
        :type timestamp: datetime

        :param scope:
            The value to assign to the scope property of this AttentionLogSummary.
        :type scope: str

        :param target_user:
            The value to assign to the target_user property of this AttentionLogSummary.
        :type target_user: str

        :param cause:
            The value to assign to the cause property of this AttentionLogSummary.
        :type cause: str

        :param action:
            The value to assign to the action property of this AttentionLogSummary.
        :type action: str

        :param supplemental_detail:
            The value to assign to the supplemental_detail property of this AttentionLogSummary.
        :type supplemental_detail: str

        :param file_location:
            The value to assign to the file_location property of this AttentionLogSummary.
        :type file_location: str

        """
        self.swagger_types = {
            'message_urgency': 'str',
            'message_type': 'str',
            'message_content': 'str',
            'timestamp': 'datetime',
            'scope': 'str',
            'target_user': 'str',
            'cause': 'str',
            'action': 'str',
            'supplemental_detail': 'str',
            'file_location': 'str'
        }

        self.attribute_map = {
            'message_urgency': 'messageUrgency',
            'message_type': 'messageType',
            'message_content': 'messageContent',
            'timestamp': 'timestamp',
            'scope': 'scope',
            'target_user': 'targetUser',
            'cause': 'cause',
            'action': 'action',
            'supplemental_detail': 'supplementalDetail',
            'file_location': 'fileLocation'
        }

        self._message_urgency = None
        self._message_type = None
        self._message_content = None
        self._timestamp = None
        self._scope = None
        self._target_user = None
        self._cause = None
        self._action = None
        self._supplemental_detail = None
        self._file_location = None

    @property
    def message_urgency(self):
        """
        **[Required]** Gets the message_urgency of this AttentionLogSummary.
        The urgency of the attention log.

        Allowed values for this property are: "IMMEDIATE", "SOON", "DEFERRABLE", "INFO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The message_urgency of this AttentionLogSummary.
        :rtype: str
        """
        return self._message_urgency

    @message_urgency.setter
    def message_urgency(self, message_urgency):
        """
        Sets the message_urgency of this AttentionLogSummary.
        The urgency of the attention log.


        :param message_urgency: The message_urgency of this AttentionLogSummary.
        :type: str
        """
        allowed_values = ["IMMEDIATE", "SOON", "DEFERRABLE", "INFO"]
        if not value_allowed_none_or_none_sentinel(message_urgency, allowed_values):
            message_urgency = 'UNKNOWN_ENUM_VALUE'
        self._message_urgency = message_urgency

    @property
    def message_type(self):
        """
        **[Required]** Gets the message_type of this AttentionLogSummary.
        The type of attention log message.

        Allowed values for this property are: "UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The message_type of this AttentionLogSummary.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """
        Sets the message_type of this AttentionLogSummary.
        The type of attention log message.


        :param message_type: The message_type of this AttentionLogSummary.
        :type: str
        """
        allowed_values = ["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE"]
        if not value_allowed_none_or_none_sentinel(message_type, allowed_values):
            message_type = 'UNKNOWN_ENUM_VALUE'
        self._message_type = message_type

    @property
    def message_content(self):
        """
        Gets the message_content of this AttentionLogSummary.
        The contents of the attention log message.


        :return: The message_content of this AttentionLogSummary.
        :rtype: str
        """
        return self._message_content

    @message_content.setter
    def message_content(self, message_content):
        """
        Sets the message_content of this AttentionLogSummary.
        The contents of the attention log message.


        :param message_content: The message_content of this AttentionLogSummary.
        :type: str
        """
        self._message_content = message_content

    @property
    def timestamp(self):
        """
        Gets the timestamp of this AttentionLogSummary.
        The date and time the attention log was created.


        :return: The timestamp of this AttentionLogSummary.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this AttentionLogSummary.
        The date and time the attention log was created.


        :param timestamp: The timestamp of this AttentionLogSummary.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def scope(self):
        """
        Gets the scope of this AttentionLogSummary.
        The database scope for the attention log.


        :return: The scope of this AttentionLogSummary.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this AttentionLogSummary.
        The database scope for the attention log.


        :param scope: The scope of this AttentionLogSummary.
        :type: str
        """
        self._scope = scope

    @property
    def target_user(self):
        """
        Gets the target_user of this AttentionLogSummary.
        The user who must act on the attention log message.


        :return: The target_user of this AttentionLogSummary.
        :rtype: str
        """
        return self._target_user

    @target_user.setter
    def target_user(self, target_user):
        """
        Sets the target_user of this AttentionLogSummary.
        The user who must act on the attention log message.


        :param target_user: The target_user of this AttentionLogSummary.
        :type: str
        """
        self._target_user = target_user

    @property
    def cause(self):
        """
        Gets the cause of this AttentionLogSummary.
        The cause of the attention log.


        :return: The cause of this AttentionLogSummary.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """
        Sets the cause of this AttentionLogSummary.
        The cause of the attention log.


        :param cause: The cause of this AttentionLogSummary.
        :type: str
        """
        self._cause = cause

    @property
    def action(self):
        """
        Gets the action of this AttentionLogSummary.
        The recommended action to handle the attention log.


        :return: The action of this AttentionLogSummary.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AttentionLogSummary.
        The recommended action to handle the attention log.


        :param action: The action of this AttentionLogSummary.
        :type: str
        """
        self._action = action

    @property
    def supplemental_detail(self):
        """
        Gets the supplemental_detail of this AttentionLogSummary.
        The supplemental details of the attention log.


        :return: The supplemental_detail of this AttentionLogSummary.
        :rtype: str
        """
        return self._supplemental_detail

    @supplemental_detail.setter
    def supplemental_detail(self, supplemental_detail):
        """
        Sets the supplemental_detail of this AttentionLogSummary.
        The supplemental details of the attention log.


        :param supplemental_detail: The supplemental_detail of this AttentionLogSummary.
        :type: str
        """
        self._supplemental_detail = supplemental_detail

    @property
    def file_location(self):
        """
        Gets the file_location of this AttentionLogSummary.
        The attention log file location.


        :return: The file_location of this AttentionLogSummary.
        :rtype: str
        """
        return self._file_location

    @file_location.setter
    def file_location(self, file_location):
        """
        Sets the file_location of this AttentionLogSummary.
        The attention log file location.


        :param file_location: The file_location of this AttentionLogSummary.
        :type: str
        """
        self._file_location = file_location

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
