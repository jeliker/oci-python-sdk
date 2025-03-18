# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCustomPropertyDetails(object):
    """
    Properties used in custom atrribute update operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCustomPropertyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateCustomPropertyDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateCustomPropertyDetails.
        :type description: str

        :param is_sortable:
            The value to assign to the is_sortable property of this UpdateCustomPropertyDetails.
        :type is_sortable: bool

        :param is_filterable:
            The value to assign to the is_filterable property of this UpdateCustomPropertyDetails.
        :type is_filterable: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this UpdateCustomPropertyDetails.
        :type is_multi_valued: bool

        :param is_hidden:
            The value to assign to the is_hidden property of this UpdateCustomPropertyDetails.
        :type is_hidden: bool

        :param is_editable:
            The value to assign to the is_editable property of this UpdateCustomPropertyDetails.
        :type is_editable: bool

        :param is_shown_in_list:
            The value to assign to the is_shown_in_list property of this UpdateCustomPropertyDetails.
        :type is_shown_in_list: bool

        :param is_hidden_in_search:
            The value to assign to the is_hidden_in_search property of this UpdateCustomPropertyDetails.
        :type is_hidden_in_search: bool

        :param is_event_enabled:
            The value to assign to the is_event_enabled property of this UpdateCustomPropertyDetails.
        :type is_event_enabled: bool

        :param allowed_values:
            The value to assign to the allowed_values property of this UpdateCustomPropertyDetails.
        :type allowed_values: list[str]

        :param properties:
            The value to assign to the properties property of this UpdateCustomPropertyDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'is_sortable': 'bool',
            'is_filterable': 'bool',
            'is_multi_valued': 'bool',
            'is_hidden': 'bool',
            'is_editable': 'bool',
            'is_shown_in_list': 'bool',
            'is_hidden_in_search': 'bool',
            'is_event_enabled': 'bool',
            'allowed_values': 'list[str]',
            'properties': 'dict(str, dict(str, str))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'is_sortable': 'isSortable',
            'is_filterable': 'isFilterable',
            'is_multi_valued': 'isMultiValued',
            'is_hidden': 'isHidden',
            'is_editable': 'isEditable',
            'is_shown_in_list': 'isShownInList',
            'is_hidden_in_search': 'isHiddenInSearch',
            'is_event_enabled': 'isEventEnabled',
            'allowed_values': 'allowedValues',
            'properties': 'properties'
        }
        self._display_name = None
        self._description = None
        self._is_sortable = None
        self._is_filterable = None
        self._is_multi_valued = None
        self._is_hidden = None
        self._is_editable = None
        self._is_shown_in_list = None
        self._is_hidden_in_search = None
        self._is_event_enabled = None
        self._allowed_values = None
        self._properties = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCustomPropertyDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateCustomPropertyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCustomPropertyDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateCustomPropertyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateCustomPropertyDetails.
        Detailed description of the data asset.


        :return: The description of this UpdateCustomPropertyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCustomPropertyDetails.
        Detailed description of the data asset.


        :param description: The description of this UpdateCustomPropertyDetails.
        :type: str
        """
        self._description = description

    @property
    def is_sortable(self):
        """
        Gets the is_sortable of this UpdateCustomPropertyDetails.
        If this field allows to sort from UI


        :return: The is_sortable of this UpdateCustomPropertyDetails.
        :rtype: bool
        """
        return self._is_sortable

    @is_sortable.setter
    def is_sortable(self, is_sortable):
        """
        Sets the is_sortable of this UpdateCustomPropertyDetails.
        If this field allows to sort from UI


        :param is_sortable: The is_sortable of this UpdateCustomPropertyDetails.
        :type: bool
        """
        self._is_sortable = is_sortable

    @property
    def is_filterable(self):
        """
        Gets the is_filterable of this UpdateCustomPropertyDetails.
        If this field allows to filter or create facets from UI


        :return: The is_filterable of this UpdateCustomPropertyDetails.
        :rtype: bool
        """
        return self._is_filterable

    @is_filterable.setter
    def is_filterable(self, is_filterable):
        """
        Sets the is_filterable of this UpdateCustomPropertyDetails.
        If this field allows to filter or create facets from UI


        :param is_filterable: The is_filterable of this UpdateCustomPropertyDetails.
        :type: bool
        """
        self._is_filterable = is_filterable

    @property
    def is_multi_valued(self):
        """
        Gets the is_multi_valued of this UpdateCustomPropertyDetails.
        If this field allows multiple values to be set


        :return: The is_multi_valued of this UpdateCustomPropertyDetails.
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """
        Sets the is_multi_valued of this UpdateCustomPropertyDetails.
        If this field allows multiple values to be set


        :param is_multi_valued: The is_multi_valued of this UpdateCustomPropertyDetails.
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this UpdateCustomPropertyDetails.
        If this field is a hidden field


        :return: The is_hidden of this UpdateCustomPropertyDetails.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this UpdateCustomPropertyDetails.
        If this field is a hidden field


        :param is_hidden: The is_hidden of this UpdateCustomPropertyDetails.
        :type: bool
        """
        self._is_hidden = is_hidden

    @property
    def is_editable(self):
        """
        Gets the is_editable of this UpdateCustomPropertyDetails.
        If this field is a editable field


        :return: The is_editable of this UpdateCustomPropertyDetails.
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """
        Sets the is_editable of this UpdateCustomPropertyDetails.
        If this field is a editable field


        :param is_editable: The is_editable of this UpdateCustomPropertyDetails.
        :type: bool
        """
        self._is_editable = is_editable

    @property
    def is_shown_in_list(self):
        """
        Gets the is_shown_in_list of this UpdateCustomPropertyDetails.
        If this field is displayed in a list view of applicable objects.


        :return: The is_shown_in_list of this UpdateCustomPropertyDetails.
        :rtype: bool
        """
        return self._is_shown_in_list

    @is_shown_in_list.setter
    def is_shown_in_list(self, is_shown_in_list):
        """
        Sets the is_shown_in_list of this UpdateCustomPropertyDetails.
        If this field is displayed in a list view of applicable objects.


        :param is_shown_in_list: The is_shown_in_list of this UpdateCustomPropertyDetails.
        :type: bool
        """
        self._is_shown_in_list = is_shown_in_list

    @property
    def is_hidden_in_search(self):
        """
        Gets the is_hidden_in_search of this UpdateCustomPropertyDetails.
        If this field is allowed to pop in search results


        :return: The is_hidden_in_search of this UpdateCustomPropertyDetails.
        :rtype: bool
        """
        return self._is_hidden_in_search

    @is_hidden_in_search.setter
    def is_hidden_in_search(self, is_hidden_in_search):
        """
        Sets the is_hidden_in_search of this UpdateCustomPropertyDetails.
        If this field is allowed to pop in search results


        :param is_hidden_in_search: The is_hidden_in_search of this UpdateCustomPropertyDetails.
        :type: bool
        """
        self._is_hidden_in_search = is_hidden_in_search

    @property
    def is_event_enabled(self):
        """
        Gets the is_event_enabled of this UpdateCustomPropertyDetails.
        If an OCI Event will be emitted when the custom property is modified.


        :return: The is_event_enabled of this UpdateCustomPropertyDetails.
        :rtype: bool
        """
        return self._is_event_enabled

    @is_event_enabled.setter
    def is_event_enabled(self, is_event_enabled):
        """
        Sets the is_event_enabled of this UpdateCustomPropertyDetails.
        If an OCI Event will be emitted when the custom property is modified.


        :param is_event_enabled: The is_event_enabled of this UpdateCustomPropertyDetails.
        :type: bool
        """
        self._is_event_enabled = is_event_enabled

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this UpdateCustomPropertyDetails.
        Allowed values for the custom property if any


        :return: The allowed_values of this UpdateCustomPropertyDetails.
        :rtype: list[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this UpdateCustomPropertyDetails.
        Allowed values for the custom property if any


        :param allowed_values: The allowed_values of this UpdateCustomPropertyDetails.
        :type: list[str]
        """
        self._allowed_values = allowed_values

    @property
    def properties(self):
        """
        Gets the properties of this UpdateCustomPropertyDetails.
        A map of maps that contains the properties which are specific to the asset type. Each data asset type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data assets have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :return: The properties of this UpdateCustomPropertyDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateCustomPropertyDetails.
        A map of maps that contains the properties which are specific to the asset type. Each data asset type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data assets have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :param properties: The properties of this UpdateCustomPropertyDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
