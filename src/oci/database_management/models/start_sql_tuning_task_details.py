# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StartSqlTuningTaskDetails(object):
    """
    The request to start a SQL tuning task.
    """

    #: A constant which can be used with the scope property of a StartSqlTuningTaskDetails.
    #: This constant has a value of "LIMITED"
    SCOPE_LIMITED = "LIMITED"

    #: A constant which can be used with the scope property of a StartSqlTuningTaskDetails.
    #: This constant has a value of "COMPREHENSIVE"
    SCOPE_COMPREHENSIVE = "COMPREHENSIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new StartSqlTuningTaskDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param task_name:
            The value to assign to the task_name property of this StartSqlTuningTaskDetails.
        :type task_name: str

        :param task_description:
            The value to assign to the task_description property of this StartSqlTuningTaskDetails.
        :type task_description: str

        :param credential_details:
            The value to assign to the credential_details property of this StartSqlTuningTaskDetails.
        :type credential_details: oci.database_management.models.SqlTuningTaskCredentialDetails

        :param total_time_limit_in_minutes:
            The value to assign to the total_time_limit_in_minutes property of this StartSqlTuningTaskDetails.
        :type total_time_limit_in_minutes: int

        :param scope:
            The value to assign to the scope property of this StartSqlTuningTaskDetails.
            Allowed values for this property are: "LIMITED", "COMPREHENSIVE"
        :type scope: str

        :param statement_time_limit_in_minutes:
            The value to assign to the statement_time_limit_in_minutes property of this StartSqlTuningTaskDetails.
        :type statement_time_limit_in_minutes: int

        :param sql_details:
            The value to assign to the sql_details property of this StartSqlTuningTaskDetails.
        :type sql_details: list[oci.database_management.models.SqlTuningTaskSqlDetail]

        :param time_started:
            The value to assign to the time_started property of this StartSqlTuningTaskDetails.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this StartSqlTuningTaskDetails.
        :type time_ended: datetime

        """
        self.swagger_types = {
            'task_name': 'str',
            'task_description': 'str',
            'credential_details': 'SqlTuningTaskCredentialDetails',
            'total_time_limit_in_minutes': 'int',
            'scope': 'str',
            'statement_time_limit_in_minutes': 'int',
            'sql_details': 'list[SqlTuningTaskSqlDetail]',
            'time_started': 'datetime',
            'time_ended': 'datetime'
        }

        self.attribute_map = {
            'task_name': 'taskName',
            'task_description': 'taskDescription',
            'credential_details': 'credentialDetails',
            'total_time_limit_in_minutes': 'totalTimeLimitInMinutes',
            'scope': 'scope',
            'statement_time_limit_in_minutes': 'statementTimeLimitInMinutes',
            'sql_details': 'sqlDetails',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded'
        }

        self._task_name = None
        self._task_description = None
        self._credential_details = None
        self._total_time_limit_in_minutes = None
        self._scope = None
        self._statement_time_limit_in_minutes = None
        self._sql_details = None
        self._time_started = None
        self._time_ended = None

    @property
    def task_name(self):
        """
        **[Required]** Gets the task_name of this StartSqlTuningTaskDetails.
        The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.


        :return: The task_name of this StartSqlTuningTaskDetails.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """
        Sets the task_name of this StartSqlTuningTaskDetails.
        The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.


        :param task_name: The task_name of this StartSqlTuningTaskDetails.
        :type: str
        """
        self._task_name = task_name

    @property
    def task_description(self):
        """
        Gets the task_description of this StartSqlTuningTaskDetails.
        The description of the SQL tuning task.


        :return: The task_description of this StartSqlTuningTaskDetails.
        :rtype: str
        """
        return self._task_description

    @task_description.setter
    def task_description(self, task_description):
        """
        Sets the task_description of this StartSqlTuningTaskDetails.
        The description of the SQL tuning task.


        :param task_description: The task_description of this StartSqlTuningTaskDetails.
        :type: str
        """
        self._task_description = task_description

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this StartSqlTuningTaskDetails.

        :return: The credential_details of this StartSqlTuningTaskDetails.
        :rtype: oci.database_management.models.SqlTuningTaskCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this StartSqlTuningTaskDetails.

        :param credential_details: The credential_details of this StartSqlTuningTaskDetails.
        :type: oci.database_management.models.SqlTuningTaskCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def total_time_limit_in_minutes(self):
        """
        **[Required]** Gets the total_time_limit_in_minutes of this StartSqlTuningTaskDetails.
        The time limit for running the SQL tuning task.


        :return: The total_time_limit_in_minutes of this StartSqlTuningTaskDetails.
        :rtype: int
        """
        return self._total_time_limit_in_minutes

    @total_time_limit_in_minutes.setter
    def total_time_limit_in_minutes(self, total_time_limit_in_minutes):
        """
        Sets the total_time_limit_in_minutes of this StartSqlTuningTaskDetails.
        The time limit for running the SQL tuning task.


        :param total_time_limit_in_minutes: The total_time_limit_in_minutes of this StartSqlTuningTaskDetails.
        :type: int
        """
        self._total_time_limit_in_minutes = total_time_limit_in_minutes

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this StartSqlTuningTaskDetails.
        The scope for the SQL tuning task. For LIMITED scope, the SQL profile recommendation
        is excluded, so the task is executed faster. For COMPREHENSIVE scope, the SQL profile recommendation
        is included.

        Allowed values for this property are: "LIMITED", "COMPREHENSIVE"


        :return: The scope of this StartSqlTuningTaskDetails.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this StartSqlTuningTaskDetails.
        The scope for the SQL tuning task. For LIMITED scope, the SQL profile recommendation
        is excluded, so the task is executed faster. For COMPREHENSIVE scope, the SQL profile recommendation
        is included.


        :param scope: The scope of this StartSqlTuningTaskDetails.
        :type: str
        """
        allowed_values = ["LIMITED", "COMPREHENSIVE"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            raise ValueError(
                "Invalid value for `scope`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._scope = scope

    @property
    def statement_time_limit_in_minutes(self):
        """
        Gets the statement_time_limit_in_minutes of this StartSqlTuningTaskDetails.
        The time limit per SQL statement (in minutes). This is for a task with the COMPREHENSIVE scope.
        The time limit per SQL statement should not be more than the total time limit.


        :return: The statement_time_limit_in_minutes of this StartSqlTuningTaskDetails.
        :rtype: int
        """
        return self._statement_time_limit_in_minutes

    @statement_time_limit_in_minutes.setter
    def statement_time_limit_in_minutes(self, statement_time_limit_in_minutes):
        """
        Sets the statement_time_limit_in_minutes of this StartSqlTuningTaskDetails.
        The time limit per SQL statement (in minutes). This is for a task with the COMPREHENSIVE scope.
        The time limit per SQL statement should not be more than the total time limit.


        :param statement_time_limit_in_minutes: The statement_time_limit_in_minutes of this StartSqlTuningTaskDetails.
        :type: int
        """
        self._statement_time_limit_in_minutes = statement_time_limit_in_minutes

    @property
    def sql_details(self):
        """
        **[Required]** Gets the sql_details of this StartSqlTuningTaskDetails.
        The array of the details of SQL statement on which tuning is performed.


        :return: The sql_details of this StartSqlTuningTaskDetails.
        :rtype: list[oci.database_management.models.SqlTuningTaskSqlDetail]
        """
        return self._sql_details

    @sql_details.setter
    def sql_details(self, sql_details):
        """
        Sets the sql_details of this StartSqlTuningTaskDetails.
        The array of the details of SQL statement on which tuning is performed.


        :param sql_details: The sql_details of this StartSqlTuningTaskDetails.
        :type: list[oci.database_management.models.SqlTuningTaskSqlDetail]
        """
        self._sql_details = sql_details

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this StartSqlTuningTaskDetails.
        The start time of the period in which SQL statements are running.


        :return: The time_started of this StartSqlTuningTaskDetails.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this StartSqlTuningTaskDetails.
        The start time of the period in which SQL statements are running.


        :param time_started: The time_started of this StartSqlTuningTaskDetails.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        **[Required]** Gets the time_ended of this StartSqlTuningTaskDetails.
        The end time of the period in which SQL statements are running.


        :return: The time_ended of this StartSqlTuningTaskDetails.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this StartSqlTuningTaskDetails.
        The end time of the period in which SQL statements are running.


        :param time_ended: The time_ended of this StartSqlTuningTaskDetails.
        :type: datetime
        """
        self._time_ended = time_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other