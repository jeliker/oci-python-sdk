# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanBaselineConfiguration(object):
    """
    The configuration details of SQL plan baselines. The details include:

    - whether automatic initial plan capture is enabled or disabled
    - whether use of SQL plan baselines is enabled or disabled
    - whether Automatic SPM Evolve Advisor task is enabled or disabled
    - whether high-frequency Automatic SPM Evolve Advisor task is enabled or disabled
    - filters for the automatic initial plan capture
    - parameters for the Automatic SPM Evolve Advisor task
    - plan retention and allocated space for the plan baselines
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanBaselineConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_automatic_initial_plan_capture_enabled:
            The value to assign to the is_automatic_initial_plan_capture_enabled property of this SqlPlanBaselineConfiguration.
        :type is_automatic_initial_plan_capture_enabled: bool

        :param is_sql_plan_baselines_usage_enabled:
            The value to assign to the is_sql_plan_baselines_usage_enabled property of this SqlPlanBaselineConfiguration.
        :type is_sql_plan_baselines_usage_enabled: bool

        :param is_auto_spm_evolve_task_enabled:
            The value to assign to the is_auto_spm_evolve_task_enabled property of this SqlPlanBaselineConfiguration.
        :type is_auto_spm_evolve_task_enabled: bool

        :param is_high_frequency_auto_spm_evolve_task_enabled:
            The value to assign to the is_high_frequency_auto_spm_evolve_task_enabled property of this SqlPlanBaselineConfiguration.
        :type is_high_frequency_auto_spm_evolve_task_enabled: bool

        :param plan_retention_weeks:
            The value to assign to the plan_retention_weeks property of this SqlPlanBaselineConfiguration.
        :type plan_retention_weeks: int

        :param space_budget_percent:
            The value to assign to the space_budget_percent property of this SqlPlanBaselineConfiguration.
        :type space_budget_percent: float

        :param space_budget_mb:
            The value to assign to the space_budget_mb property of this SqlPlanBaselineConfiguration.
        :type space_budget_mb: float

        :param space_used_mb:
            The value to assign to the space_used_mb property of this SqlPlanBaselineConfiguration.
        :type space_used_mb: float

        :param auto_capture_filters:
            The value to assign to the auto_capture_filters property of this SqlPlanBaselineConfiguration.
        :type auto_capture_filters: list[oci.database_management.models.AutomaticCaptureFilter]

        :param auto_spm_evolve_task_parameters:
            The value to assign to the auto_spm_evolve_task_parameters property of this SqlPlanBaselineConfiguration.
        :type auto_spm_evolve_task_parameters: oci.database_management.models.SpmEvolveTaskParameters

        """
        self.swagger_types = {
            'is_automatic_initial_plan_capture_enabled': 'bool',
            'is_sql_plan_baselines_usage_enabled': 'bool',
            'is_auto_spm_evolve_task_enabled': 'bool',
            'is_high_frequency_auto_spm_evolve_task_enabled': 'bool',
            'plan_retention_weeks': 'int',
            'space_budget_percent': 'float',
            'space_budget_mb': 'float',
            'space_used_mb': 'float',
            'auto_capture_filters': 'list[AutomaticCaptureFilter]',
            'auto_spm_evolve_task_parameters': 'SpmEvolveTaskParameters'
        }

        self.attribute_map = {
            'is_automatic_initial_plan_capture_enabled': 'isAutomaticInitialPlanCaptureEnabled',
            'is_sql_plan_baselines_usage_enabled': 'isSqlPlanBaselinesUsageEnabled',
            'is_auto_spm_evolve_task_enabled': 'isAutoSpmEvolveTaskEnabled',
            'is_high_frequency_auto_spm_evolve_task_enabled': 'isHighFrequencyAutoSpmEvolveTaskEnabled',
            'plan_retention_weeks': 'planRetentionWeeks',
            'space_budget_percent': 'spaceBudgetPercent',
            'space_budget_mb': 'spaceBudgetMB',
            'space_used_mb': 'spaceUsedMB',
            'auto_capture_filters': 'autoCaptureFilters',
            'auto_spm_evolve_task_parameters': 'autoSpmEvolveTaskParameters'
        }

        self._is_automatic_initial_plan_capture_enabled = None
        self._is_sql_plan_baselines_usage_enabled = None
        self._is_auto_spm_evolve_task_enabled = None
        self._is_high_frequency_auto_spm_evolve_task_enabled = None
        self._plan_retention_weeks = None
        self._space_budget_percent = None
        self._space_budget_mb = None
        self._space_used_mb = None
        self._auto_capture_filters = None
        self._auto_spm_evolve_task_parameters = None

    @property
    def is_automatic_initial_plan_capture_enabled(self):
        """
        **[Required]** Gets the is_automatic_initial_plan_capture_enabled of this SqlPlanBaselineConfiguration.
        Indicates whether the automatic capture of SQL plan baselines is enabled (`true`) or not (`false`).


        :return: The is_automatic_initial_plan_capture_enabled of this SqlPlanBaselineConfiguration.
        :rtype: bool
        """
        return self._is_automatic_initial_plan_capture_enabled

    @is_automatic_initial_plan_capture_enabled.setter
    def is_automatic_initial_plan_capture_enabled(self, is_automatic_initial_plan_capture_enabled):
        """
        Sets the is_automatic_initial_plan_capture_enabled of this SqlPlanBaselineConfiguration.
        Indicates whether the automatic capture of SQL plan baselines is enabled (`true`) or not (`false`).


        :param is_automatic_initial_plan_capture_enabled: The is_automatic_initial_plan_capture_enabled of this SqlPlanBaselineConfiguration.
        :type: bool
        """
        self._is_automatic_initial_plan_capture_enabled = is_automatic_initial_plan_capture_enabled

    @property
    def is_sql_plan_baselines_usage_enabled(self):
        """
        **[Required]** Gets the is_sql_plan_baselines_usage_enabled of this SqlPlanBaselineConfiguration.
        Indicates whether the database uses SQL plan baselines (`true`) or not (`false`).


        :return: The is_sql_plan_baselines_usage_enabled of this SqlPlanBaselineConfiguration.
        :rtype: bool
        """
        return self._is_sql_plan_baselines_usage_enabled

    @is_sql_plan_baselines_usage_enabled.setter
    def is_sql_plan_baselines_usage_enabled(self, is_sql_plan_baselines_usage_enabled):
        """
        Sets the is_sql_plan_baselines_usage_enabled of this SqlPlanBaselineConfiguration.
        Indicates whether the database uses SQL plan baselines (`true`) or not (`false`).


        :param is_sql_plan_baselines_usage_enabled: The is_sql_plan_baselines_usage_enabled of this SqlPlanBaselineConfiguration.
        :type: bool
        """
        self._is_sql_plan_baselines_usage_enabled = is_sql_plan_baselines_usage_enabled

    @property
    def is_auto_spm_evolve_task_enabled(self):
        """
        **[Required]** Gets the is_auto_spm_evolve_task_enabled of this SqlPlanBaselineConfiguration.
        Indicates whether the Automatic SPM Evolve Advisor task is enabled (`true`) or not (`false`).


        :return: The is_auto_spm_evolve_task_enabled of this SqlPlanBaselineConfiguration.
        :rtype: bool
        """
        return self._is_auto_spm_evolve_task_enabled

    @is_auto_spm_evolve_task_enabled.setter
    def is_auto_spm_evolve_task_enabled(self, is_auto_spm_evolve_task_enabled):
        """
        Sets the is_auto_spm_evolve_task_enabled of this SqlPlanBaselineConfiguration.
        Indicates whether the Automatic SPM Evolve Advisor task is enabled (`true`) or not (`false`).


        :param is_auto_spm_evolve_task_enabled: The is_auto_spm_evolve_task_enabled of this SqlPlanBaselineConfiguration.
        :type: bool
        """
        self._is_auto_spm_evolve_task_enabled = is_auto_spm_evolve_task_enabled

    @property
    def is_high_frequency_auto_spm_evolve_task_enabled(self):
        """
        **[Required]** Gets the is_high_frequency_auto_spm_evolve_task_enabled of this SqlPlanBaselineConfiguration.
        Indicates whether the high frequency Automatic SPM Evolve Advisor task is enabled (`true`) or not (`false`).


        :return: The is_high_frequency_auto_spm_evolve_task_enabled of this SqlPlanBaselineConfiguration.
        :rtype: bool
        """
        return self._is_high_frequency_auto_spm_evolve_task_enabled

    @is_high_frequency_auto_spm_evolve_task_enabled.setter
    def is_high_frequency_auto_spm_evolve_task_enabled(self, is_high_frequency_auto_spm_evolve_task_enabled):
        """
        Sets the is_high_frequency_auto_spm_evolve_task_enabled of this SqlPlanBaselineConfiguration.
        Indicates whether the high frequency Automatic SPM Evolve Advisor task is enabled (`true`) or not (`false`).


        :param is_high_frequency_auto_spm_evolve_task_enabled: The is_high_frequency_auto_spm_evolve_task_enabled of this SqlPlanBaselineConfiguration.
        :type: bool
        """
        self._is_high_frequency_auto_spm_evolve_task_enabled = is_high_frequency_auto_spm_evolve_task_enabled

    @property
    def plan_retention_weeks(self):
        """
        **[Required]** Gets the plan_retention_weeks of this SqlPlanBaselineConfiguration.
        The number of weeks to retain unused plans before they are purged.


        :return: The plan_retention_weeks of this SqlPlanBaselineConfiguration.
        :rtype: int
        """
        return self._plan_retention_weeks

    @plan_retention_weeks.setter
    def plan_retention_weeks(self, plan_retention_weeks):
        """
        Sets the plan_retention_weeks of this SqlPlanBaselineConfiguration.
        The number of weeks to retain unused plans before they are purged.


        :param plan_retention_weeks: The plan_retention_weeks of this SqlPlanBaselineConfiguration.
        :type: int
        """
        self._plan_retention_weeks = plan_retention_weeks

    @property
    def space_budget_percent(self):
        """
        **[Required]** Gets the space_budget_percent of this SqlPlanBaselineConfiguration.
        The maximum percent of `SYSAUX` space that can be used for SQL Management Base.


        :return: The space_budget_percent of this SqlPlanBaselineConfiguration.
        :rtype: float
        """
        return self._space_budget_percent

    @space_budget_percent.setter
    def space_budget_percent(self, space_budget_percent):
        """
        Sets the space_budget_percent of this SqlPlanBaselineConfiguration.
        The maximum percent of `SYSAUX` space that can be used for SQL Management Base.


        :param space_budget_percent: The space_budget_percent of this SqlPlanBaselineConfiguration.
        :type: float
        """
        self._space_budget_percent = space_budget_percent

    @property
    def space_budget_mb(self):
        """
        Gets the space_budget_mb of this SqlPlanBaselineConfiguration.
        The maximum `SYSAUX` space that can be used for SQL Management Base in MB.


        :return: The space_budget_mb of this SqlPlanBaselineConfiguration.
        :rtype: float
        """
        return self._space_budget_mb

    @space_budget_mb.setter
    def space_budget_mb(self, space_budget_mb):
        """
        Sets the space_budget_mb of this SqlPlanBaselineConfiguration.
        The maximum `SYSAUX` space that can be used for SQL Management Base in MB.


        :param space_budget_mb: The space_budget_mb of this SqlPlanBaselineConfiguration.
        :type: float
        """
        self._space_budget_mb = space_budget_mb

    @property
    def space_used_mb(self):
        """
        Gets the space_used_mb of this SqlPlanBaselineConfiguration.
        The space used by SQL Management Base in MB.


        :return: The space_used_mb of this SqlPlanBaselineConfiguration.
        :rtype: float
        """
        return self._space_used_mb

    @space_used_mb.setter
    def space_used_mb(self, space_used_mb):
        """
        Sets the space_used_mb of this SqlPlanBaselineConfiguration.
        The space used by SQL Management Base in MB.


        :param space_used_mb: The space_used_mb of this SqlPlanBaselineConfiguration.
        :type: float
        """
        self._space_used_mb = space_used_mb

    @property
    def auto_capture_filters(self):
        """
        Gets the auto_capture_filters of this SqlPlanBaselineConfiguration.
        The capture filters used in automatic initial plan capture.


        :return: The auto_capture_filters of this SqlPlanBaselineConfiguration.
        :rtype: list[oci.database_management.models.AutomaticCaptureFilter]
        """
        return self._auto_capture_filters

    @auto_capture_filters.setter
    def auto_capture_filters(self, auto_capture_filters):
        """
        Sets the auto_capture_filters of this SqlPlanBaselineConfiguration.
        The capture filters used in automatic initial plan capture.


        :param auto_capture_filters: The auto_capture_filters of this SqlPlanBaselineConfiguration.
        :type: list[oci.database_management.models.AutomaticCaptureFilter]
        """
        self._auto_capture_filters = auto_capture_filters

    @property
    def auto_spm_evolve_task_parameters(self):
        """
        Gets the auto_spm_evolve_task_parameters of this SqlPlanBaselineConfiguration.

        :return: The auto_spm_evolve_task_parameters of this SqlPlanBaselineConfiguration.
        :rtype: oci.database_management.models.SpmEvolveTaskParameters
        """
        return self._auto_spm_evolve_task_parameters

    @auto_spm_evolve_task_parameters.setter
    def auto_spm_evolve_task_parameters(self, auto_spm_evolve_task_parameters):
        """
        Sets the auto_spm_evolve_task_parameters of this SqlPlanBaselineConfiguration.

        :param auto_spm_evolve_task_parameters: The auto_spm_evolve_task_parameters of this SqlPlanBaselineConfiguration.
        :type: oci.database_management.models.SpmEvolveTaskParameters
        """
        self._auto_spm_evolve_task_parameters = auto_spm_evolve_task_parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
