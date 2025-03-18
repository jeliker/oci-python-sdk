# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200909

from .monitoring_source_namespace_details import MonitoringSourceNamespaceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoringSourceSelectedNamespaceDetails(MonitoringSourceNamespaceDetails):
    """
    The namespaces for the compartment-specific list.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoringSourceSelectedNamespaceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.MonitoringSourceSelectedNamespaceDetails.kind` attribute
        of this class is ``selected`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this MonitoringSourceSelectedNamespaceDetails.
            Allowed values for this property are: "selected"
        :type kind: str

        :param namespaces:
            The value to assign to the namespaces property of this MonitoringSourceSelectedNamespaceDetails.
        :type namespaces: list[oci.sch.models.MonitoringSourceSelectedNamespace]

        """
        self.swagger_types = {
            'kind': 'str',
            'namespaces': 'list[MonitoringSourceSelectedNamespace]'
        }
        self.attribute_map = {
            'kind': 'kind',
            'namespaces': 'namespaces'
        }
        self._kind = None
        self._namespaces = None
        self._kind = 'selected'

    @property
    def namespaces(self):
        """
        **[Required]** Gets the namespaces of this MonitoringSourceSelectedNamespaceDetails.
        The namespaces for the compartment-specific list.


        :return: The namespaces of this MonitoringSourceSelectedNamespaceDetails.
        :rtype: list[oci.sch.models.MonitoringSourceSelectedNamespace]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """
        Sets the namespaces of this MonitoringSourceSelectedNamespaceDetails.
        The namespaces for the compartment-specific list.


        :param namespaces: The namespaces of this MonitoringSourceSelectedNamespaceDetails.
        :type: list[oci.sch.models.MonitoringSourceSelectedNamespace]
        """
        self._namespaces = namespaces

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
