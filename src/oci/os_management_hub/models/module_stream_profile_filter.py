# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStreamProfileFilter(object):
    """
    Used to select module stream/profiles from VendorSoftwareSources to create/update CustomSoftwareSources.
    """

    #: A constant which can be used with the filter_type property of a ModuleStreamProfileFilter.
    #: This constant has a value of "INCLUDE"
    FILTER_TYPE_INCLUDE = "INCLUDE"

    #: A constant which can be used with the filter_type property of a ModuleStreamProfileFilter.
    #: This constant has a value of "EXCLUDE"
    FILTER_TYPE_EXCLUDE = "EXCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStreamProfileFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStreamProfileFilter.
        :type module_name: str

        :param profile_name:
            The value to assign to the profile_name property of this ModuleStreamProfileFilter.
        :type profile_name: str

        :param stream_name:
            The value to assign to the stream_name property of this ModuleStreamProfileFilter.
        :type stream_name: str

        :param filter_type:
            The value to assign to the filter_type property of this ModuleStreamProfileFilter.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type filter_type: str

        """
        self.swagger_types = {
            'module_name': 'str',
            'profile_name': 'str',
            'stream_name': 'str',
            'filter_type': 'str'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'profile_name': 'profileName',
            'stream_name': 'streamName',
            'filter_type': 'filterType'
        }

        self._module_name = None
        self._profile_name = None
        self._stream_name = None
        self._filter_type = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStreamProfileFilter.
        Module name.


        :return: The module_name of this ModuleStreamProfileFilter.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStreamProfileFilter.
        Module name.


        :param module_name: The module_name of this ModuleStreamProfileFilter.
        :type: str
        """
        self._module_name = module_name

    @property
    def profile_name(self):
        """
        Gets the profile_name of this ModuleStreamProfileFilter.
        Profile name.


        :return: The profile_name of this ModuleStreamProfileFilter.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """
        Sets the profile_name of this ModuleStreamProfileFilter.
        Profile name.


        :param profile_name: The profile_name of this ModuleStreamProfileFilter.
        :type: str
        """
        self._profile_name = profile_name

    @property
    def stream_name(self):
        """
        Gets the stream_name of this ModuleStreamProfileFilter.
        Stream name.


        :return: The stream_name of this ModuleStreamProfileFilter.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ModuleStreamProfileFilter.
        Stream name.


        :param stream_name: The stream_name of this ModuleStreamProfileFilter.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def filter_type(self):
        """
        **[Required]** Gets the filter_type of this ModuleStreamProfileFilter.
        The type of the filter, which can be of two types - INCLUDE or EXCLUDE.

        Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The filter_type of this ModuleStreamProfileFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this ModuleStreamProfileFilter.
        The type of the filter, which can be of two types - INCLUDE or EXCLUDE.


        :param filter_type: The filter_type of this ModuleStreamProfileFilter.
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]
        if not value_allowed_none_or_none_sentinel(filter_type, allowed_values):
            filter_type = 'UNKNOWN_ENUM_VALUE'
        self._filter_type = filter_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
