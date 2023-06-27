# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DropSqlPlanBaselinesDetails(object):
    """
    The details required to drop SQL plan baselines.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DropSqlPlanBaselinesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_handle:
            The value to assign to the sql_handle property of this DropSqlPlanBaselinesDetails.
        :type sql_handle: str

        :param plan_name:
            The value to assign to the plan_name property of this DropSqlPlanBaselinesDetails.
        :type plan_name: str

        :param credentials:
            The value to assign to the credentials property of this DropSqlPlanBaselinesDetails.
        :type credentials: oci.database_management.models.ManagedDatabaseCredential

        """
        self.swagger_types = {
            'sql_handle': 'str',
            'plan_name': 'str',
            'credentials': 'ManagedDatabaseCredential'
        }

        self.attribute_map = {
            'sql_handle': 'sqlHandle',
            'plan_name': 'planName',
            'credentials': 'credentials'
        }

        self._sql_handle = None
        self._plan_name = None
        self._credentials = None

    @property
    def sql_handle(self):
        """
        Gets the sql_handle of this DropSqlPlanBaselinesDetails.
        The SQL statement handle. It identifies plans associated with a SQL statement
        that are to be dropped. If `null` then `planName` must be specified.


        :return: The sql_handle of this DropSqlPlanBaselinesDetails.
        :rtype: str
        """
        return self._sql_handle

    @sql_handle.setter
    def sql_handle(self, sql_handle):
        """
        Sets the sql_handle of this DropSqlPlanBaselinesDetails.
        The SQL statement handle. It identifies plans associated with a SQL statement
        that are to be dropped. If `null` then `planName` must be specified.


        :param sql_handle: The sql_handle of this DropSqlPlanBaselinesDetails.
        :type: str
        """
        self._sql_handle = sql_handle

    @property
    def plan_name(self):
        """
        Gets the plan_name of this DropSqlPlanBaselinesDetails.
        The plan name. It identifies a specific plan. If `null' then all plans
        associated with the SQL statement identified by `sqlHandle' are dropped.


        :return: The plan_name of this DropSqlPlanBaselinesDetails.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """
        Sets the plan_name of this DropSqlPlanBaselinesDetails.
        The plan name. It identifies a specific plan. If `null' then all plans
        associated with the SQL statement identified by `sqlHandle' are dropped.


        :param plan_name: The plan_name of this DropSqlPlanBaselinesDetails.
        :type: str
        """
        self._plan_name = plan_name

    @property
    def credentials(self):
        """
        **[Required]** Gets the credentials of this DropSqlPlanBaselinesDetails.

        :return: The credentials of this DropSqlPlanBaselinesDetails.
        :rtype: oci.database_management.models.ManagedDatabaseCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this DropSqlPlanBaselinesDetails.

        :param credentials: The credentials of this DropSqlPlanBaselinesDetails.
        :type: oci.database_management.models.ManagedDatabaseCredential
        """
        self._credentials = credentials

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
