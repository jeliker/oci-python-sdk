# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StageSummary(object):
    """
    stage summary of a remediation run. A stage is one step of a remediation run.
    """

    #: A constant which can be used with the type property of a StageSummary.
    #: This constant has a value of "DETECT"
    TYPE_DETECT = "DETECT"

    #: A constant which can be used with the type property of a StageSummary.
    #: This constant has a value of "RECOMMEND"
    TYPE_RECOMMEND = "RECOMMEND"

    #: A constant which can be used with the type property of a StageSummary.
    #: This constant has a value of "VERIFY"
    TYPE_VERIFY = "VERIFY"

    #: A constant which can be used with the type property of a StageSummary.
    #: This constant has a value of "APPLY"
    TYPE_APPLY = "APPLY"

    def __init__(self, **kwargs):
        """
        Initializes a new StageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_created:
            The value to assign to the time_created property of this StageSummary.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this StageSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this StageSummary.
        :type time_finished: datetime

        :param type:
            The value to assign to the type property of this StageSummary.
            Allowed values for this property are: "DETECT", "RECOMMEND", "VERIFY", "APPLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param summary:
            The value to assign to the summary property of this StageSummary.
        :type summary: str

        """
        self.swagger_types = {
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'type': 'str',
            'summary': 'str'
        }
        self.attribute_map = {
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'type': 'type',
            'summary': 'summary'
        }
        self._time_created = None
        self._time_started = None
        self._time_finished = None
        self._type = None
        self._summary = None

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this StageSummary.
        The creation date and time of the stage (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this StageSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this StageSummary.
        The creation date and time of the stage (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this StageSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_started(self):
        """
        Gets the time_started of this StageSummary.
        The date and time of the start of the stage (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_started of this StageSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this StageSummary.
        The date and time of the start of the stage (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_started: The time_started of this StageSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this StageSummary.
        The date and time of the finish of the stage (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_finished of this StageSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this StageSummary.
        The date and time of the finish of the stage (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_finished: The time_finished of this StageSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def type(self):
        """
        **[Required]** Gets the type of this StageSummary.
        The type of stage.

        Allowed values for this property are: "DETECT", "RECOMMEND", "VERIFY", "APPLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this StageSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StageSummary.
        The type of stage.


        :param type: The type of this StageSummary.
        :type: str
        """
        allowed_values = ["DETECT", "RECOMMEND", "VERIFY", "APPLY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def summary(self):
        """
        Gets the summary of this StageSummary.
        Information about the current step within the given stage.


        :return: The summary of this StageSummary.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this StageSummary.
        Information about the current step within the given stage.


        :param summary: The summary of this StageSummary.
        :type: str
        """
        self._summary = summary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
