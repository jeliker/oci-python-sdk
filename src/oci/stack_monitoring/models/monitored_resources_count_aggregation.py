# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourcesCountAggregation(object):
    """
    The count of resources for specified dimension.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourcesCountAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimensions:
            The value to assign to the dimensions property of this MonitoredResourcesCountAggregation.
        :type dimensions: dict(str, str)

        :param count:
            The value to assign to the count property of this MonitoredResourcesCountAggregation.
        :type count: int

        """
        self.swagger_types = {
            'dimensions': 'dict(str, str)',
            'count': 'int'
        }
        self.attribute_map = {
            'dimensions': 'dimensions',
            'count': 'count'
        }
        self._dimensions = None
        self._count = None

    @property
    def dimensions(self):
        """
        **[Required]** Gets the dimensions of this MonitoredResourcesCountAggregation.
        Qualifiers provided in a metric definition.
        Available dimensions vary based on groupBy parameter.
        Each dimension takes the form of a key-value pair.

        Example: `\"resourceType\": \"oci_autonomous_database\"`


        :return: The dimensions of this MonitoredResourcesCountAggregation.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this MonitoredResourcesCountAggregation.
        Qualifiers provided in a metric definition.
        Available dimensions vary based on groupBy parameter.
        Each dimension takes the form of a key-value pair.

        Example: `\"resourceType\": \"oci_autonomous_database\"`


        :param dimensions: The dimensions of this MonitoredResourcesCountAggregation.
        :type: dict(str, str)
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """
        **[Required]** Gets the count of this MonitoredResourcesCountAggregation.
        the value of this metric


        :return: The count of this MonitoredResourcesCountAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this MonitoredResourcesCountAggregation.
        the value of this metric


        :param count: The count of this MonitoredResourcesCountAggregation.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
