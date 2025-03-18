# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeExadataInsightResourceForecastTrendAggregation(object):
    """
    Usage and Forecast results from the selected time period.
    """

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "CPU"
    EXADATA_RESOURCE_METRIC_CPU = "CPU"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "STORAGE"
    EXADATA_RESOURCE_METRIC_STORAGE = "STORAGE"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "IO"
    EXADATA_RESOURCE_METRIC_IO = "IO"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "MEMORY"
    EXADATA_RESOURCE_METRIC_MEMORY = "MEMORY"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "IOPS"
    EXADATA_RESOURCE_METRIC_IOPS = "IOPS"

    #: A constant which can be used with the exadata_resource_metric property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "THROUGHPUT"
    EXADATA_RESOURCE_METRIC_THROUGHPUT = "THROUGHPUT"

    #: A constant which can be used with the exadata_resource_type property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "DATABASE"
    EXADATA_RESOURCE_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the exadata_resource_type property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "HOST"
    EXADATA_RESOURCE_TYPE_HOST = "HOST"

    #: A constant which can be used with the exadata_resource_type property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "STORAGE_SERVER"
    EXADATA_RESOURCE_TYPE_STORAGE_SERVER = "STORAGE_SERVER"

    #: A constant which can be used with the exadata_resource_type property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "DISKGROUP"
    EXADATA_RESOURCE_TYPE_DISKGROUP = "DISKGROUP"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "CORES"
    USAGE_UNIT_CORES = "CORES"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "GB"
    USAGE_UNIT_GB = "GB"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "MBPS"
    USAGE_UNIT_MBPS = "MBPS"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "IOPS"
    USAGE_UNIT_IOPS = "IOPS"

    #: A constant which can be used with the usage_unit property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "PERCENT"
    USAGE_UNIT_PERCENT = "PERCENT"

    #: A constant which can be used with the pattern property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "LINEAR"
    PATTERN_LINEAR = "LINEAR"

    #: A constant which can be used with the pattern property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "MONTHLY_SEASONS"
    PATTERN_MONTHLY_SEASONS = "MONTHLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "MONTHLY_AND_YEARLY_SEASONS"
    PATTERN_MONTHLY_AND_YEARLY_SEASONS = "MONTHLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "WEEKLY_SEASONS"
    PATTERN_WEEKLY_SEASONS = "WEEKLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "WEEKLY_AND_MONTHLY_SEASONS"
    PATTERN_WEEKLY_AND_MONTHLY_SEASONS = "WEEKLY_AND_MONTHLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "WEEKLY_MONTHLY_AND_YEARLY_SEASONS"
    PATTERN_WEEKLY_MONTHLY_AND_YEARLY_SEASONS = "WEEKLY_MONTHLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "WEEKLY_AND_YEARLY_SEASONS"
    PATTERN_WEEKLY_AND_YEARLY_SEASONS = "WEEKLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a SummarizeExadataInsightResourceForecastTrendAggregation.
    #: This constant has a value of "YEARLY_SEASONS"
    PATTERN_YEARLY_SEASONS = "YEARLY_SEASONS"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeExadataInsightResourceForecastTrendAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type time_interval_end: datetime

        :param exadata_resource_metric:
            The value to assign to the exadata_resource_metric property of this SummarizeExadataInsightResourceForecastTrendAggregation.
            Allowed values for this property are: "CPU", "STORAGE", "IO", "MEMORY", "IOPS", "THROUGHPUT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_resource_metric: str

        :param exadata_resource_type:
            The value to assign to the exadata_resource_type property of this SummarizeExadataInsightResourceForecastTrendAggregation.
            Allowed values for this property are: "DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_resource_type: str

        :param usage_unit:
            The value to assign to the usage_unit property of this SummarizeExadataInsightResourceForecastTrendAggregation.
            Allowed values for this property are: "CORES", "GB", "MBPS", "IOPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type usage_unit: str

        :param selected_forecast_algorithm:
            The value to assign to the selected_forecast_algorithm property of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type selected_forecast_algorithm: str

        :param pattern:
            The value to assign to the pattern property of this SummarizeExadataInsightResourceForecastTrendAggregation.
            Allowed values for this property are: "LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pattern: str

        :param days_to_reach_capacity:
            The value to assign to the days_to_reach_capacity property of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type days_to_reach_capacity: int

        :param historical_data:
            The value to assign to the historical_data property of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type historical_data: list[oci.opsi.models.HistoricalDataItem]

        :param projected_data:
            The value to assign to the projected_data property of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type projected_data: list[oci.opsi.models.ProjectedDataItem]

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'exadata_resource_metric': 'str',
            'exadata_resource_type': 'str',
            'usage_unit': 'str',
            'selected_forecast_algorithm': 'str',
            'pattern': 'str',
            'days_to_reach_capacity': 'int',
            'historical_data': 'list[HistoricalDataItem]',
            'projected_data': 'list[ProjectedDataItem]'
        }
        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'exadata_resource_metric': 'exadataResourceMetric',
            'exadata_resource_type': 'exadataResourceType',
            'usage_unit': 'usageUnit',
            'selected_forecast_algorithm': 'selectedForecastAlgorithm',
            'pattern': 'pattern',
            'days_to_reach_capacity': 'daysToReachCapacity',
            'historical_data': 'historicalData',
            'projected_data': 'projectedData'
        }
        self._time_interval_start = None
        self._time_interval_end = None
        self._exadata_resource_metric = None
        self._exadata_resource_type = None
        self._usage_unit = None
        self._selected_forecast_algorithm = None
        self._pattern = None
        self._days_to_reach_capacity = None
        self._historical_data = None
        self._projected_data = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SummarizeExadataInsightResourceForecastTrendAggregation.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SummarizeExadataInsightResourceForecastTrendAggregation.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SummarizeExadataInsightResourceForecastTrendAggregation.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SummarizeExadataInsightResourceForecastTrendAggregation.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def exadata_resource_metric(self):
        """
        **[Required]** Gets the exadata_resource_metric of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Defines the type of exadata resource metric (example: CPU, STORAGE)

        Allowed values for this property are: "CPU", "STORAGE", "IO", "MEMORY", "IOPS", "THROUGHPUT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_resource_metric of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: str
        """
        return self._exadata_resource_metric

    @exadata_resource_metric.setter
    def exadata_resource_metric(self, exadata_resource_metric):
        """
        Sets the exadata_resource_metric of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Defines the type of exadata resource metric (example: CPU, STORAGE)


        :param exadata_resource_metric: The exadata_resource_metric of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: str
        """
        allowed_values = ["CPU", "STORAGE", "IO", "MEMORY", "IOPS", "THROUGHPUT"]
        if not value_allowed_none_or_none_sentinel(exadata_resource_metric, allowed_values):
            exadata_resource_metric = 'UNKNOWN_ENUM_VALUE'
        self._exadata_resource_metric = exadata_resource_metric

    @property
    def exadata_resource_type(self):
        """
        **[Required]** Gets the exadata_resource_type of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Defines the resource type for an exadata  (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

        Allowed values for this property are: "DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_resource_type of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: str
        """
        return self._exadata_resource_type

    @exadata_resource_type.setter
    def exadata_resource_type(self, exadata_resource_type):
        """
        Sets the exadata_resource_type of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Defines the resource type for an exadata  (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)


        :param exadata_resource_type: The exadata_resource_type of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: str
        """
        allowed_values = ["DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP"]
        if not value_allowed_none_or_none_sentinel(exadata_resource_type, allowed_values):
            exadata_resource_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_resource_type = exadata_resource_type

    @property
    def usage_unit(self):
        """
        **[Required]** Gets the usage_unit of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Displays usage unit ( CORES, GB , PERCENT, MBPS)

        Allowed values for this property are: "CORES", "GB", "MBPS", "IOPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The usage_unit of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: str
        """
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        """
        Sets the usage_unit of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Displays usage unit ( CORES, GB , PERCENT, MBPS)


        :param usage_unit: The usage_unit of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: str
        """
        allowed_values = ["CORES", "GB", "MBPS", "IOPS", "PERCENT"]
        if not value_allowed_none_or_none_sentinel(usage_unit, allowed_values):
            usage_unit = 'UNKNOWN_ENUM_VALUE'
        self._usage_unit = usage_unit

    @property
    def selected_forecast_algorithm(self):
        """
        Gets the selected_forecast_algorithm of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Auto-ML algorithm leveraged for the forecast. Only applicable for Auto-ML forecast.


        :return: The selected_forecast_algorithm of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: str
        """
        return self._selected_forecast_algorithm

    @selected_forecast_algorithm.setter
    def selected_forecast_algorithm(self, selected_forecast_algorithm):
        """
        Sets the selected_forecast_algorithm of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Auto-ML algorithm leveraged for the forecast. Only applicable for Auto-ML forecast.


        :param selected_forecast_algorithm: The selected_forecast_algorithm of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: str
        """
        self._selected_forecast_algorithm = selected_forecast_algorithm

    @property
    def pattern(self):
        """
        **[Required]** Gets the pattern of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Time series patterns used in the forecasting.

        Allowed values for this property are: "LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pattern of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Time series patterns used in the forecasting.


        :param pattern: The pattern of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: str
        """
        allowed_values = ["LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS"]
        if not value_allowed_none_or_none_sentinel(pattern, allowed_values):
            pattern = 'UNKNOWN_ENUM_VALUE'
        self._pattern = pattern

    @property
    def days_to_reach_capacity(self):
        """
        **[Required]** Gets the days_to_reach_capacity of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Days to reach capacity for a storage server


        :return: The days_to_reach_capacity of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: int
        """
        return self._days_to_reach_capacity

    @days_to_reach_capacity.setter
    def days_to_reach_capacity(self, days_to_reach_capacity):
        """
        Sets the days_to_reach_capacity of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Days to reach capacity for a storage server


        :param days_to_reach_capacity: The days_to_reach_capacity of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: int
        """
        self._days_to_reach_capacity = days_to_reach_capacity

    @property
    def historical_data(self):
        """
        **[Required]** Gets the historical_data of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Time series data used for the forecast analysis.


        :return: The historical_data of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: list[oci.opsi.models.HistoricalDataItem]
        """
        return self._historical_data

    @historical_data.setter
    def historical_data(self, historical_data):
        """
        Sets the historical_data of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Time series data used for the forecast analysis.


        :param historical_data: The historical_data of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: list[oci.opsi.models.HistoricalDataItem]
        """
        self._historical_data = historical_data

    @property
    def projected_data(self):
        """
        **[Required]** Gets the projected_data of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Time series data result of the forecasting analysis.


        :return: The projected_data of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :rtype: list[oci.opsi.models.ProjectedDataItem]
        """
        return self._projected_data

    @projected_data.setter
    def projected_data(self, projected_data):
        """
        Sets the projected_data of this SummarizeExadataInsightResourceForecastTrendAggregation.
        Time series data result of the forecasting analysis.


        :param projected_data: The projected_data of this SummarizeExadataInsightResourceForecastTrendAggregation.
        :type: list[oci.opsi.models.ProjectedDataItem]
        """
        self._projected_data = projected_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
