# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningSetAdminActionStatus(object):
    """
    The status of a Sql tuning set admin action.
    """

    #: A constant which can be used with the status property of a SqlTuningSetAdminActionStatus.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a SqlTuningSetAdminActionStatus.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningSetAdminActionStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this SqlTuningSetAdminActionStatus.
            Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param success_message:
            The value to assign to the success_message property of this SqlTuningSetAdminActionStatus.
        :type success_message: str

        :param error_code:
            The value to assign to the error_code property of this SqlTuningSetAdminActionStatus.
        :type error_code: int

        :param error_message:
            The value to assign to the error_message property of this SqlTuningSetAdminActionStatus.
        :type error_message: str

        :param show_sql_only:
            The value to assign to the show_sql_only property of this SqlTuningSetAdminActionStatus.
        :type show_sql_only: int

        :param sql_statement:
            The value to assign to the sql_statement property of this SqlTuningSetAdminActionStatus.
        :type sql_statement: str

        """
        self.swagger_types = {
            'status': 'str',
            'success_message': 'str',
            'error_code': 'int',
            'error_message': 'str',
            'show_sql_only': 'int',
            'sql_statement': 'str'
        }
        self.attribute_map = {
            'status': 'status',
            'success_message': 'successMessage',
            'error_code': 'errorCode',
            'error_message': 'errorMessage',
            'show_sql_only': 'showSqlOnly',
            'sql_statement': 'sqlStatement'
        }
        self._status = None
        self._success_message = None
        self._error_code = None
        self._error_message = None
        self._show_sql_only = None
        self._sql_statement = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this SqlTuningSetAdminActionStatus.
        The status of a Sql tuning set admin action.

        Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SqlTuningSetAdminActionStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SqlTuningSetAdminActionStatus.
        The status of a Sql tuning set admin action.


        :param status: The status of this SqlTuningSetAdminActionStatus.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def success_message(self):
        """
        Gets the success_message of this SqlTuningSetAdminActionStatus.
        The success message of the Sql tuning set admin action. The success message is \"null\" if the admin action is non successful.


        :return: The success_message of this SqlTuningSetAdminActionStatus.
        :rtype: str
        """
        return self._success_message

    @success_message.setter
    def success_message(self, success_message):
        """
        Sets the success_message of this SqlTuningSetAdminActionStatus.
        The success message of the Sql tuning set admin action. The success message is \"null\" if the admin action is non successful.


        :param success_message: The success_message of this SqlTuningSetAdminActionStatus.
        :type: str
        """
        self._success_message = success_message

    @property
    def error_code(self):
        """
        Gets the error_code of this SqlTuningSetAdminActionStatus.
        The error code that denotes failure if the Sql tuning set admin action is not successful. The error code is \"null\" if the admin action is successful.


        :return: The error_code of this SqlTuningSetAdminActionStatus.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this SqlTuningSetAdminActionStatus.
        The error code that denotes failure if the Sql tuning set admin action is not successful. The error code is \"null\" if the admin action is successful.


        :param error_code: The error_code of this SqlTuningSetAdminActionStatus.
        :type: int
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this SqlTuningSetAdminActionStatus.
        The error message that indicates the reason for failure if the Sql tuning set admin action is not successful. The error message is \"null\" if the admin action is successful.


        :return: The error_message of this SqlTuningSetAdminActionStatus.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this SqlTuningSetAdminActionStatus.
        The error message that indicates the reason for failure if the Sql tuning set admin action is not successful. The error message is \"null\" if the admin action is successful.


        :param error_message: The error_message of this SqlTuningSetAdminActionStatus.
        :type: str
        """
        self._error_message = error_message

    @property
    def show_sql_only(self):
        """
        Gets the show_sql_only of this SqlTuningSetAdminActionStatus.
        Flag to indicate whether to create the Sql tuning set or just display the plsql used for the selected user action.


        :return: The show_sql_only of this SqlTuningSetAdminActionStatus.
        :rtype: int
        """
        return self._show_sql_only

    @show_sql_only.setter
    def show_sql_only(self, show_sql_only):
        """
        Sets the show_sql_only of this SqlTuningSetAdminActionStatus.
        Flag to indicate whether to create the Sql tuning set or just display the plsql used for the selected user action.


        :param show_sql_only: The show_sql_only of this SqlTuningSetAdminActionStatus.
        :type: int
        """
        self._show_sql_only = show_sql_only

    @property
    def sql_statement(self):
        """
        Gets the sql_statement of this SqlTuningSetAdminActionStatus.
        When showSqlOnly is set to 1, this attribute displays the plsql generated for the selected user action.
        When showSqlOnly is set to 0, this attribute will not be returned.


        :return: The sql_statement of this SqlTuningSetAdminActionStatus.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        """
        Sets the sql_statement of this SqlTuningSetAdminActionStatus.
        When showSqlOnly is set to 1, this attribute displays the plsql generated for the selected user action.
        When showSqlOnly is set to 0, this attribute will not be returned.


        :param sql_statement: The sql_statement of this SqlTuningSetAdminActionStatus.
        :type: str
        """
        self._sql_statement = sql_statement

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
