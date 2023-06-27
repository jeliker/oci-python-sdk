# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeSqlPlanBaselinesAttributesDetails(object):
    """
    The details required to change SQL plan baseline attributes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeSqlPlanBaselinesAttributesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_handle:
            The value to assign to the sql_handle property of this ChangeSqlPlanBaselinesAttributesDetails.
        :type sql_handle: str

        :param plan_name:
            The value to assign to the plan_name property of this ChangeSqlPlanBaselinesAttributesDetails.
        :type plan_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this ChangeSqlPlanBaselinesAttributesDetails.
        :type is_enabled: bool

        :param is_fixed:
            The value to assign to the is_fixed property of this ChangeSqlPlanBaselinesAttributesDetails.
        :type is_fixed: bool

        :param is_auto_purged:
            The value to assign to the is_auto_purged property of this ChangeSqlPlanBaselinesAttributesDetails.
        :type is_auto_purged: bool

        :param credentials:
            The value to assign to the credentials property of this ChangeSqlPlanBaselinesAttributesDetails.
        :type credentials: oci.database_management.models.ManagedDatabaseCredential

        """
        self.swagger_types = {
            'sql_handle': 'str',
            'plan_name': 'str',
            'is_enabled': 'bool',
            'is_fixed': 'bool',
            'is_auto_purged': 'bool',
            'credentials': 'ManagedDatabaseCredential'
        }

        self.attribute_map = {
            'sql_handle': 'sqlHandle',
            'plan_name': 'planName',
            'is_enabled': 'isEnabled',
            'is_fixed': 'isFixed',
            'is_auto_purged': 'isAutoPurged',
            'credentials': 'credentials'
        }

        self._sql_handle = None
        self._plan_name = None
        self._is_enabled = None
        self._is_fixed = None
        self._is_auto_purged = None
        self._credentials = None

    @property
    def sql_handle(self):
        """
        Gets the sql_handle of this ChangeSqlPlanBaselinesAttributesDetails.
        The SQL statement handle. It identifies plans associated with a SQL statement
        for attribute changes. If `null` then `planName` must be specified.


        :return: The sql_handle of this ChangeSqlPlanBaselinesAttributesDetails.
        :rtype: str
        """
        return self._sql_handle

    @sql_handle.setter
    def sql_handle(self, sql_handle):
        """
        Sets the sql_handle of this ChangeSqlPlanBaselinesAttributesDetails.
        The SQL statement handle. It identifies plans associated with a SQL statement
        for attribute changes. If `null` then `planName` must be specified.


        :param sql_handle: The sql_handle of this ChangeSqlPlanBaselinesAttributesDetails.
        :type: str
        """
        self._sql_handle = sql_handle

    @property
    def plan_name(self):
        """
        Gets the plan_name of this ChangeSqlPlanBaselinesAttributesDetails.
        Then plan name. It identifies a specific plan. If `null' then all plans associated
        with a SQL statement identified by `sqlHandle' are considered for attribute changes.


        :return: The plan_name of this ChangeSqlPlanBaselinesAttributesDetails.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """
        Sets the plan_name of this ChangeSqlPlanBaselinesAttributesDetails.
        Then plan name. It identifies a specific plan. If `null' then all plans associated
        with a SQL statement identified by `sqlHandle' are considered for attribute changes.


        :param plan_name: The plan_name of this ChangeSqlPlanBaselinesAttributesDetails.
        :type: str
        """
        self._plan_name = plan_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this ChangeSqlPlanBaselinesAttributesDetails.
        Indicates whether the plan is available for use by the optimizer.


        :return: The is_enabled of this ChangeSqlPlanBaselinesAttributesDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ChangeSqlPlanBaselinesAttributesDetails.
        Indicates whether the plan is available for use by the optimizer.


        :param is_enabled: The is_enabled of this ChangeSqlPlanBaselinesAttributesDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_fixed(self):
        """
        Gets the is_fixed of this ChangeSqlPlanBaselinesAttributesDetails.
        Indicates whether the plan baseline is fixed. A fixed plan takes precedence over a non-fixed plan.


        :return: The is_fixed of this ChangeSqlPlanBaselinesAttributesDetails.
        :rtype: bool
        """
        return self._is_fixed

    @is_fixed.setter
    def is_fixed(self, is_fixed):
        """
        Sets the is_fixed of this ChangeSqlPlanBaselinesAttributesDetails.
        Indicates whether the plan baseline is fixed. A fixed plan takes precedence over a non-fixed plan.


        :param is_fixed: The is_fixed of this ChangeSqlPlanBaselinesAttributesDetails.
        :type: bool
        """
        self._is_fixed = is_fixed

    @property
    def is_auto_purged(self):
        """
        Gets the is_auto_purged of this ChangeSqlPlanBaselinesAttributesDetails.
        Indicates whether the plan is purged if it is not used for a time period.


        :return: The is_auto_purged of this ChangeSqlPlanBaselinesAttributesDetails.
        :rtype: bool
        """
        return self._is_auto_purged

    @is_auto_purged.setter
    def is_auto_purged(self, is_auto_purged):
        """
        Sets the is_auto_purged of this ChangeSqlPlanBaselinesAttributesDetails.
        Indicates whether the plan is purged if it is not used for a time period.


        :param is_auto_purged: The is_auto_purged of this ChangeSqlPlanBaselinesAttributesDetails.
        :type: bool
        """
        self._is_auto_purged = is_auto_purged

    @property
    def credentials(self):
        """
        **[Required]** Gets the credentials of this ChangeSqlPlanBaselinesAttributesDetails.

        :return: The credentials of this ChangeSqlPlanBaselinesAttributesDetails.
        :rtype: oci.database_management.models.ManagedDatabaseCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ChangeSqlPlanBaselinesAttributesDetails.

        :param credentials: The credentials of this ChangeSqlPlanBaselinesAttributesDetails.
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
