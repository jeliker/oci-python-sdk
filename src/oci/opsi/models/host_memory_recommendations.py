# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .host_insight_host_recommendations import HostInsightHostRecommendations
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostMemoryRecommendations(HostInsightHostRecommendations):
    """
    Contains memory recommendation.
    """

    #: A constant which can be used with the unused_instance property of a HostMemoryRecommendations.
    #: This constant has a value of "IN_USE"
    UNUSED_INSTANCE_IN_USE = "IN_USE"

    #: A constant which can be used with the unused_instance property of a HostMemoryRecommendations.
    #: This constant has a value of "NOT_IN_USE"
    UNUSED_INSTANCE_NOT_IN_USE = "NOT_IN_USE"

    #: A constant which can be used with the unused_instance property of a HostMemoryRecommendations.
    #: This constant has a value of "IS_NOT_DETERMINED"
    UNUSED_INSTANCE_IS_NOT_DETERMINED = "IS_NOT_DETERMINED"

    def __init__(self, **kwargs):
        """
        Initializes a new HostMemoryRecommendations object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostMemoryRecommendations.metric_recommendation_name` attribute
        of this class is ``HOST_MEMORY_RECOMMENDATIONS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_recommendation_name:
            The value to assign to the metric_recommendation_name property of this HostMemoryRecommendations.
            Allowed values for this property are: "HOST_CPU_RECOMMENDATIONS", "HOST_MEMORY_RECOMMENDATIONS", "HOST_NETWORK_RECOMMENDATIONS", "HOST_STORAGE_RECOMMENDATIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metric_recommendation_name: str

        :param unused_instance:
            The value to assign to the unused_instance property of this HostMemoryRecommendations.
            Allowed values for this property are: "IN_USE", "NOT_IN_USE", "IS_NOT_DETERMINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unused_instance: str

        :param is_abandoned_instance:
            The value to assign to the is_abandoned_instance property of this HostMemoryRecommendations.
        :type is_abandoned_instance: bool

        :param memory_optimization:
            The value to assign to the memory_optimization property of this HostMemoryRecommendations.
        :type memory_optimization: str

        """
        self.swagger_types = {
            'metric_recommendation_name': 'str',
            'unused_instance': 'str',
            'is_abandoned_instance': 'bool',
            'memory_optimization': 'str'
        }
        self.attribute_map = {
            'metric_recommendation_name': 'metricRecommendationName',
            'unused_instance': 'unusedInstance',
            'is_abandoned_instance': 'isAbandonedInstance',
            'memory_optimization': 'memoryOptimization'
        }
        self._metric_recommendation_name = None
        self._unused_instance = None
        self._is_abandoned_instance = None
        self._memory_optimization = None
        self._metric_recommendation_name = 'HOST_MEMORY_RECOMMENDATIONS'

    @property
    def unused_instance(self):
        """
        Gets the unused_instance of this HostMemoryRecommendations.
        Identify unused instances based on cpu, memory and network metrics.

        Allowed values for this property are: "IN_USE", "NOT_IN_USE", "IS_NOT_DETERMINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unused_instance of this HostMemoryRecommendations.
        :rtype: str
        """
        return self._unused_instance

    @unused_instance.setter
    def unused_instance(self, unused_instance):
        """
        Sets the unused_instance of this HostMemoryRecommendations.
        Identify unused instances based on cpu, memory and network metrics.


        :param unused_instance: The unused_instance of this HostMemoryRecommendations.
        :type: str
        """
        allowed_values = ["IN_USE", "NOT_IN_USE", "IS_NOT_DETERMINED"]
        if not value_allowed_none_or_none_sentinel(unused_instance, allowed_values):
            unused_instance = 'UNKNOWN_ENUM_VALUE'
        self._unused_instance = unused_instance

    @property
    def is_abandoned_instance(self):
        """
        Gets the is_abandoned_instance of this HostMemoryRecommendations.
        Identify if an instance is abandoned.


        :return: The is_abandoned_instance of this HostMemoryRecommendations.
        :rtype: bool
        """
        return self._is_abandoned_instance

    @is_abandoned_instance.setter
    def is_abandoned_instance(self, is_abandoned_instance):
        """
        Sets the is_abandoned_instance of this HostMemoryRecommendations.
        Identify if an instance is abandoned.


        :param is_abandoned_instance: The is_abandoned_instance of this HostMemoryRecommendations.
        :type: bool
        """
        self._is_abandoned_instance = is_abandoned_instance

    @property
    def memory_optimization(self):
        """
        Gets the memory_optimization of this HostMemoryRecommendations.
        Show if OPSI recommends to change memory capacity based on Memory utilization and current shape.


        :return: The memory_optimization of this HostMemoryRecommendations.
        :rtype: str
        """
        return self._memory_optimization

    @memory_optimization.setter
    def memory_optimization(self, memory_optimization):
        """
        Sets the memory_optimization of this HostMemoryRecommendations.
        Show if OPSI recommends to change memory capacity based on Memory utilization and current shape.


        :param memory_optimization: The memory_optimization of this HostMemoryRecommendations.
        :type: str
        """
        self._memory_optimization = memory_optimization

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
