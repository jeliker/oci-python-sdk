# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentMonitoringDestination(object):
    """
    Kubernetes destination object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentMonitoringDestination object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UnifiedAgentMonitoringDestination.
        :type compartment_id: str

        :param metrics_namespace:
            The value to assign to the metrics_namespace property of this UnifiedAgentMonitoringDestination.
        :type metrics_namespace: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'metrics_namespace': 'str'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'metrics_namespace': 'metricsNamespace'
        }
        self._compartment_id = None
        self._metrics_namespace = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this UnifiedAgentMonitoringDestination.
        The OCID of the compartment that the resource belongs to.


        :return: The compartment_id of this UnifiedAgentMonitoringDestination.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UnifiedAgentMonitoringDestination.
        The OCID of the compartment that the resource belongs to.


        :param compartment_id: The compartment_id of this UnifiedAgentMonitoringDestination.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def metrics_namespace(self):
        """
        **[Required]** Gets the metrics_namespace of this UnifiedAgentMonitoringDestination.
        Namespace to which metrics will be emitted.


        :return: The metrics_namespace of this UnifiedAgentMonitoringDestination.
        :rtype: str
        """
        return self._metrics_namespace

    @metrics_namespace.setter
    def metrics_namespace(self, metrics_namespace):
        """
        Sets the metrics_namespace of this UnifiedAgentMonitoringDestination.
        Namespace to which metrics will be emitted.


        :param metrics_namespace: The metrics_namespace of this UnifiedAgentMonitoringDestination.
        :type: str
        """
        self._metrics_namespace = metrics_namespace

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
