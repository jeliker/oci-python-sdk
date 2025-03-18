# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceFilters(object):
    """
    Information to filter the actual target resources in an operation.
    e.g: While querying a DATABASE_INSIGHTS_DATA_OBJECT using /opsiDataObjects/actions/queryData API,
    if resourceFilters is set with valid value for definedTagEquals field, only data of the database insights
    resources for which the specified freeform tags exist will be considered for the actual query scope.
    """

    #: A constant which can be used with the resource_status property of a ResourceFilters.
    #: This constant has a value of "DISABLED"
    RESOURCE_STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the resource_status property of a ResourceFilters.
    #: This constant has a value of "ENABLED"
    RESOURCE_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the resource_status property of a ResourceFilters.
    #: This constant has a value of "TERMINATED"
    RESOURCE_STATUS_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceFilters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tag_equals:
            The value to assign to the defined_tag_equals property of this ResourceFilters.
        :type defined_tag_equals: list[str]

        :param freeform_tag_equals:
            The value to assign to the freeform_tag_equals property of this ResourceFilters.
        :type freeform_tag_equals: list[str]

        :param defined_tag_exists:
            The value to assign to the defined_tag_exists property of this ResourceFilters.
        :type defined_tag_exists: list[str]

        :param freeform_tag_exists:
            The value to assign to the freeform_tag_exists property of this ResourceFilters.
        :type freeform_tag_exists: list[str]

        :param compartment_id_in_subtree:
            The value to assign to the compartment_id_in_subtree property of this ResourceFilters.
        :type compartment_id_in_subtree: bool

        :param resource_status:
            The value to assign to the resource_status property of this ResourceFilters.
            Allowed values for items in this list are: "DISABLED", "ENABLED", "TERMINATED"
        :type resource_status: list[str]

        """
        self.swagger_types = {
            'defined_tag_equals': 'list[str]',
            'freeform_tag_equals': 'list[str]',
            'defined_tag_exists': 'list[str]',
            'freeform_tag_exists': 'list[str]',
            'compartment_id_in_subtree': 'bool',
            'resource_status': 'list[str]'
        }
        self.attribute_map = {
            'defined_tag_equals': 'definedTagEquals',
            'freeform_tag_equals': 'freeformTagEquals',
            'defined_tag_exists': 'definedTagExists',
            'freeform_tag_exists': 'freeformTagExists',
            'compartment_id_in_subtree': 'compartmentIdInSubtree',
            'resource_status': 'resourceStatus'
        }
        self._defined_tag_equals = None
        self._freeform_tag_equals = None
        self._defined_tag_exists = None
        self._freeform_tag_exists = None
        self._compartment_id_in_subtree = None
        self._resource_status = None

    @property
    def defined_tag_equals(self):
        """
        Gets the defined_tag_equals of this ResourceFilters.
        A list of tag filters to apply.  Only resources with a defined tag matching the value will be considered.
        Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
        Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
        Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".


        :return: The defined_tag_equals of this ResourceFilters.
        :rtype: list[str]
        """
        return self._defined_tag_equals

    @defined_tag_equals.setter
    def defined_tag_equals(self, defined_tag_equals):
        """
        Sets the defined_tag_equals of this ResourceFilters.
        A list of tag filters to apply.  Only resources with a defined tag matching the value will be considered.
        Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
        Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
        Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".


        :param defined_tag_equals: The defined_tag_equals of this ResourceFilters.
        :type: list[str]
        """
        self._defined_tag_equals = defined_tag_equals

    @property
    def freeform_tag_equals(self):
        """
        Gets the freeform_tag_equals of this ResourceFilters.
        A list of tag filters to apply.  Only resources with a freeform tag matching the value will be considered.
        The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
        Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".


        :return: The freeform_tag_equals of this ResourceFilters.
        :rtype: list[str]
        """
        return self._freeform_tag_equals

    @freeform_tag_equals.setter
    def freeform_tag_equals(self, freeform_tag_equals):
        """
        Sets the freeform_tag_equals of this ResourceFilters.
        A list of tag filters to apply.  Only resources with a freeform tag matching the value will be considered.
        The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
        Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".


        :param freeform_tag_equals: The freeform_tag_equals of this ResourceFilters.
        :type: list[str]
        """
        self._freeform_tag_equals = freeform_tag_equals

    @property
    def defined_tag_exists(self):
        """
        Gets the defined_tag_exists of this ResourceFilters.
        A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be considered.
        Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
        or \"{namespace}.true\".  All inputs are case-insensitive.
        Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
        Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
        Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".


        :return: The defined_tag_exists of this ResourceFilters.
        :rtype: list[str]
        """
        return self._defined_tag_exists

    @defined_tag_exists.setter
    def defined_tag_exists(self, defined_tag_exists):
        """
        Sets the defined_tag_exists of this ResourceFilters.
        A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be considered.
        Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
        or \"{namespace}.true\".  All inputs are case-insensitive.
        Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
        Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
        Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".


        :param defined_tag_exists: The defined_tag_exists of this ResourceFilters.
        :type: list[str]
        """
        self._defined_tag_exists = defined_tag_exists

    @property
    def freeform_tag_exists(self):
        """
        Gets the freeform_tag_exists of this ResourceFilters.
        A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist will be considered.
        The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
        Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
        Multiple values for different tag names are interpreted as \"AND\".


        :return: The freeform_tag_exists of this ResourceFilters.
        :rtype: list[str]
        """
        return self._freeform_tag_exists

    @freeform_tag_exists.setter
    def freeform_tag_exists(self, freeform_tag_exists):
        """
        Sets the freeform_tag_exists of this ResourceFilters.
        A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist will be considered.
        The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
        Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
        Multiple values for different tag names are interpreted as \"AND\".


        :param freeform_tag_exists: The freeform_tag_exists of this ResourceFilters.
        :type: list[str]
        """
        self._freeform_tag_exists = freeform_tag_exists

    @property
    def compartment_id_in_subtree(self):
        """
        Gets the compartment_id_in_subtree of this ResourceFilters.
        A flag to consider all resources within a given compartment and all sub-compartments.


        :return: The compartment_id_in_subtree of this ResourceFilters.
        :rtype: bool
        """
        return self._compartment_id_in_subtree

    @compartment_id_in_subtree.setter
    def compartment_id_in_subtree(self, compartment_id_in_subtree):
        """
        Sets the compartment_id_in_subtree of this ResourceFilters.
        A flag to consider all resources within a given compartment and all sub-compartments.


        :param compartment_id_in_subtree: The compartment_id_in_subtree of this ResourceFilters.
        :type: bool
        """
        self._compartment_id_in_subtree = compartment_id_in_subtree

    @property
    def resource_status(self):
        """
        Gets the resource_status of this ResourceFilters.
        Filter resources by status, multiple options could be chosen to show authorized resources even if those are disabled or deleted.

        Allowed values for items in this list are: "DISABLED", "ENABLED", "TERMINATED"


        :return: The resource_status of this ResourceFilters.
        :rtype: list[str]
        """
        return self._resource_status

    @resource_status.setter
    def resource_status(self, resource_status):
        """
        Sets the resource_status of this ResourceFilters.
        Filter resources by status, multiple options could be chosen to show authorized resources even if those are disabled or deleted.


        :param resource_status: The resource_status of this ResourceFilters.
        :type: list[str]
        """
        allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]

        if resource_status and resource_status is not NONE_SENTINEL:
            for value in resource_status:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        f"Invalid value for `resource_status`, must be None or one of {allowed_values}"
                    )
        self._resource_status = resource_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
