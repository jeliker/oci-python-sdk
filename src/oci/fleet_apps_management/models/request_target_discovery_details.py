# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestTargetDiscoveryDetails(object):
    """
    Request to initiate target discovery.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestTargetDiscoveryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_applicable_to_all_resources:
            The value to assign to the is_applicable_to_all_resources property of this RequestTargetDiscoveryDetails.
        :type is_applicable_to_all_resources: bool

        :param resource_ids:
            The value to assign to the resource_ids property of this RequestTargetDiscoveryDetails.
        :type resource_ids: list[str]

        """
        self.swagger_types = {
            'is_applicable_to_all_resources': 'bool',
            'resource_ids': 'list[str]'
        }
        self.attribute_map = {
            'is_applicable_to_all_resources': 'isApplicableToAllResources',
            'resource_ids': 'resourceIds'
        }
        self._is_applicable_to_all_resources = None
        self._resource_ids = None

    @property
    def is_applicable_to_all_resources(self):
        """
        Gets the is_applicable_to_all_resources of this RequestTargetDiscoveryDetails.
        A boolean flag that decides if all resources within the fleet should be part of discovery.


        :return: The is_applicable_to_all_resources of this RequestTargetDiscoveryDetails.
        :rtype: bool
        """
        return self._is_applicable_to_all_resources

    @is_applicable_to_all_resources.setter
    def is_applicable_to_all_resources(self, is_applicable_to_all_resources):
        """
        Sets the is_applicable_to_all_resources of this RequestTargetDiscoveryDetails.
        A boolean flag that decides if all resources within the fleet should be part of discovery.


        :param is_applicable_to_all_resources: The is_applicable_to_all_resources of this RequestTargetDiscoveryDetails.
        :type: bool
        """
        self._is_applicable_to_all_resources = is_applicable_to_all_resources

    @property
    def resource_ids(self):
        """
        Gets the resource_ids of this RequestTargetDiscoveryDetails.
        Resource OCIDS to be included for discovery.


        :return: The resource_ids of this RequestTargetDiscoveryDetails.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """
        Sets the resource_ids of this RequestTargetDiscoveryDetails.
        Resource OCIDS to be included for discovery.


        :param resource_ids: The resource_ids of this RequestTargetDiscoveryDetails.
        :type: list[str]
        """
        self._resource_ids = resource_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
