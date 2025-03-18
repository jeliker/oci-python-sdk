# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200202

from .data_source import DataSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrometheusEmitterDataSource(DataSource):
    """
    A Prometheus data source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrometheusEmitterDataSource object with values from keyword arguments. The default value of the :py:attr:`~oci.management_agent.models.PrometheusEmitterDataSource.type` attribute
        of this class is ``PROMETHEUS_EMITTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this PrometheusEmitterDataSource.
        :type key: str

        :param type:
            The value to assign to the type property of this PrometheusEmitterDataSource.
            Allowed values for this property are: "KUBERNETES_CLUSTER", "PROMETHEUS_EMITTER"
        :type type: str

        :param name:
            The value to assign to the name property of this PrometheusEmitterDataSource.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PrometheusEmitterDataSource.
        :type compartment_id: str

        :param state:
            The value to assign to the state property of this PrometheusEmitterDataSource.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"
        :type state: str

        :param time_created:
            The value to assign to the time_created property of this PrometheusEmitterDataSource.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PrometheusEmitterDataSource.
        :type time_updated: datetime

        :param url:
            The value to assign to the url property of this PrometheusEmitterDataSource.
        :type url: str

        :param namespace:
            The value to assign to the namespace property of this PrometheusEmitterDataSource.
        :type namespace: str

        :param allow_metrics:
            The value to assign to the allow_metrics property of this PrometheusEmitterDataSource.
        :type allow_metrics: str

        :param proxy_url:
            The value to assign to the proxy_url property of this PrometheusEmitterDataSource.
        :type proxy_url: str

        :param connection_timeout:
            The value to assign to the connection_timeout property of this PrometheusEmitterDataSource.
        :type connection_timeout: int

        :param read_timeout:
            The value to assign to the read_timeout property of this PrometheusEmitterDataSource.
        :type read_timeout: int

        :param read_data_limit:
            The value to assign to the read_data_limit property of this PrometheusEmitterDataSource.
        :type read_data_limit: int

        :param schedule_mins:
            The value to assign to the schedule_mins property of this PrometheusEmitterDataSource.
        :type schedule_mins: int

        :param resource_group:
            The value to assign to the resource_group property of this PrometheusEmitterDataSource.
        :type resource_group: str

        :param metric_dimensions:
            The value to assign to the metric_dimensions property of this PrometheusEmitterDataSource.
        :type metric_dimensions: list[oci.management_agent.models.MetricDimension]

        """
        self.swagger_types = {
            'key': 'str',
            'type': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'url': 'str',
            'namespace': 'str',
            'allow_metrics': 'str',
            'proxy_url': 'str',
            'connection_timeout': 'int',
            'read_timeout': 'int',
            'read_data_limit': 'int',
            'schedule_mins': 'int',
            'resource_group': 'str',
            'metric_dimensions': 'list[MetricDimension]'
        }
        self.attribute_map = {
            'key': 'key',
            'type': 'type',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'state': 'state',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'url': 'url',
            'namespace': 'namespace',
            'allow_metrics': 'allowMetrics',
            'proxy_url': 'proxyUrl',
            'connection_timeout': 'connectionTimeout',
            'read_timeout': 'readTimeout',
            'read_data_limit': 'readDataLimit',
            'schedule_mins': 'scheduleMins',
            'resource_group': 'resourceGroup',
            'metric_dimensions': 'metricDimensions'
        }
        self._key = None
        self._type = None
        self._name = None
        self._compartment_id = None
        self._state = None
        self._time_created = None
        self._time_updated = None
        self._url = None
        self._namespace = None
        self._allow_metrics = None
        self._proxy_url = None
        self._connection_timeout = None
        self._read_timeout = None
        self._read_data_limit = None
        self._schedule_mins = None
        self._resource_group = None
        self._metric_dimensions = None
        self._type = 'PROMETHEUS_EMITTER'

    @property
    def url(self):
        """
        **[Required]** Gets the url of this PrometheusEmitterDataSource.
        The url through which the Prometheus Exporter publishes its metrics. (http only)


        :return: The url of this PrometheusEmitterDataSource.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PrometheusEmitterDataSource.
        The url through which the Prometheus Exporter publishes its metrics. (http only)


        :param url: The url of this PrometheusEmitterDataSource.
        :type: str
        """
        self._url = url

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this PrometheusEmitterDataSource.
        The OCI monitoring namespace to which scraped metrics should be uploaded.


        :return: The namespace of this PrometheusEmitterDataSource.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this PrometheusEmitterDataSource.
        The OCI monitoring namespace to which scraped metrics should be uploaded.


        :param namespace: The namespace of this PrometheusEmitterDataSource.
        :type: str
        """
        self._namespace = namespace

    @property
    def allow_metrics(self):
        """
        Gets the allow_metrics of this PrometheusEmitterDataSource.
        Comma separated metric name list. The complete set of desired scraped metrics. Use this property to limit the set of metrics uploaded if required.


        :return: The allow_metrics of this PrometheusEmitterDataSource.
        :rtype: str
        """
        return self._allow_metrics

    @allow_metrics.setter
    def allow_metrics(self, allow_metrics):
        """
        Sets the allow_metrics of this PrometheusEmitterDataSource.
        Comma separated metric name list. The complete set of desired scraped metrics. Use this property to limit the set of metrics uploaded if required.


        :param allow_metrics: The allow_metrics of this PrometheusEmitterDataSource.
        :type: str
        """
        self._allow_metrics = allow_metrics

    @property
    def proxy_url(self):
        """
        Gets the proxy_url of this PrometheusEmitterDataSource.
        The url of the network proxy that provides access to the Prometheus Exporter's endpoint (url required property).


        :return: The proxy_url of this PrometheusEmitterDataSource.
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """
        Sets the proxy_url of this PrometheusEmitterDataSource.
        The url of the network proxy that provides access to the Prometheus Exporter's endpoint (url required property).


        :param proxy_url: The proxy_url of this PrometheusEmitterDataSource.
        :type: str
        """
        self._proxy_url = proxy_url

    @property
    def connection_timeout(self):
        """
        Gets the connection_timeout of this PrometheusEmitterDataSource.
        Number in milliseconds. The timeout for connecting to the Prometheus Exporter's endpoint.


        :return: The connection_timeout of this PrometheusEmitterDataSource.
        :rtype: int
        """
        return self._connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, connection_timeout):
        """
        Sets the connection_timeout of this PrometheusEmitterDataSource.
        Number in milliseconds. The timeout for connecting to the Prometheus Exporter's endpoint.


        :param connection_timeout: The connection_timeout of this PrometheusEmitterDataSource.
        :type: int
        """
        self._connection_timeout = connection_timeout

    @property
    def read_timeout(self):
        """
        Gets the read_timeout of this PrometheusEmitterDataSource.
        Number in milliseconds. The timeout for reading the response from the Prometheus Exporter's endpoint.


        :return: The read_timeout of this PrometheusEmitterDataSource.
        :rtype: int
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """
        Sets the read_timeout of this PrometheusEmitterDataSource.
        Number in milliseconds. The timeout for reading the response from the Prometheus Exporter's endpoint.


        :param read_timeout: The read_timeout of this PrometheusEmitterDataSource.
        :type: int
        """
        self._read_timeout = read_timeout

    @property
    def read_data_limit(self):
        """
        Gets the read_data_limit of this PrometheusEmitterDataSource.
        Number in kilobytes. The limit on the data being sent, not to exceed the agent's fixed limit of 400 (KB).


        :return: The read_data_limit of this PrometheusEmitterDataSource.
        :rtype: int
        """
        return self._read_data_limit

    @read_data_limit.setter
    def read_data_limit(self, read_data_limit):
        """
        Sets the read_data_limit of this PrometheusEmitterDataSource.
        Number in kilobytes. The limit on the data being sent, not to exceed the agent's fixed limit of 400 (KB).


        :param read_data_limit: The read_data_limit of this PrometheusEmitterDataSource.
        :type: int
        """
        self._read_data_limit = read_data_limit

    @property
    def schedule_mins(self):
        """
        Gets the schedule_mins of this PrometheusEmitterDataSource.
        Number in minutes. The scraping occurs at the specified interval.


        :return: The schedule_mins of this PrometheusEmitterDataSource.
        :rtype: int
        """
        return self._schedule_mins

    @schedule_mins.setter
    def schedule_mins(self, schedule_mins):
        """
        Sets the schedule_mins of this PrometheusEmitterDataSource.
        Number in minutes. The scraping occurs at the specified interval.


        :param schedule_mins: The schedule_mins of this PrometheusEmitterDataSource.
        :type: int
        """
        self._schedule_mins = schedule_mins

    @property
    def resource_group(self):
        """
        Gets the resource_group of this PrometheusEmitterDataSource.
        OCI monitoring resource group to assign the metric to.


        :return: The resource_group of this PrometheusEmitterDataSource.
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """
        Sets the resource_group of this PrometheusEmitterDataSource.
        OCI monitoring resource group to assign the metric to.


        :param resource_group: The resource_group of this PrometheusEmitterDataSource.
        :type: str
        """
        self._resource_group = resource_group

    @property
    def metric_dimensions(self):
        """
        Gets the metric_dimensions of this PrometheusEmitterDataSource.
        The names of other user-supplied properties expressed as fixed values to be used as dimensions for every uploaded datapoint.


        :return: The metric_dimensions of this PrometheusEmitterDataSource.
        :rtype: list[oci.management_agent.models.MetricDimension]
        """
        return self._metric_dimensions

    @metric_dimensions.setter
    def metric_dimensions(self, metric_dimensions):
        """
        Sets the metric_dimensions of this PrometheusEmitterDataSource.
        The names of other user-supplied properties expressed as fixed values to be used as dimensions for every uploaded datapoint.


        :param metric_dimensions: The metric_dimensions of this PrometheusEmitterDataSource.
        :type: list[oci.management_agent.models.MetricDimension]
        """
        self._metric_dimensions = metric_dimensions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
