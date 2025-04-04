# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentLoggingFilter(object):
    """
    Logging filter object.
    """

    #: A constant which can be used with the filter_type property of a UnifiedAgentLoggingFilter.
    #: This constant has a value of "PARSER_FILTER"
    FILTER_TYPE_PARSER_FILTER = "PARSER_FILTER"

    #: A constant which can be used with the filter_type property of a UnifiedAgentLoggingFilter.
    #: This constant has a value of "GREP_FILTER"
    FILTER_TYPE_GREP_FILTER = "GREP_FILTER"

    #: A constant which can be used with the filter_type property of a UnifiedAgentLoggingFilter.
    #: This constant has a value of "RECORD_TRANSFORMER_FILTER"
    FILTER_TYPE_RECORD_TRANSFORMER_FILTER = "RECORD_TRANSFORMER_FILTER"

    #: A constant which can be used with the filter_type property of a UnifiedAgentLoggingFilter.
    #: This constant has a value of "CUSTOM_FILTER"
    FILTER_TYPE_CUSTOM_FILTER = "CUSTOM_FILTER"

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentLoggingFilter object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.logging.models.UnifiedAgentCustomFilter`
        * :class:`~oci.logging.models.UnifiedAgentParserFilter`
        * :class:`~oci.logging.models.UnifiedAgentLoggingGrepFilter`
        * :class:`~oci.logging.models.UnifiedAgentLoggingRecordTransformerFilter`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UnifiedAgentLoggingFilter.
        :type name: str

        :param filter_type:
            The value to assign to the filter_type property of this UnifiedAgentLoggingFilter.
            Allowed values for this property are: "PARSER_FILTER", "GREP_FILTER", "RECORD_TRANSFORMER_FILTER", "CUSTOM_FILTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type filter_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'filter_type': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'filter_type': 'filterType'
        }
        self._name = None
        self._filter_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['filterType']

        if type == 'CUSTOM_FILTER':
            return 'UnifiedAgentCustomFilter'

        if type == 'PARSER_FILTER':
            return 'UnifiedAgentParserFilter'

        if type == 'GREP_FILTER':
            return 'UnifiedAgentLoggingGrepFilter'

        if type == 'RECORD_TRANSFORMER_FILTER':
            return 'UnifiedAgentLoggingRecordTransformerFilter'
        else:
            return 'UnifiedAgentLoggingFilter'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this UnifiedAgentLoggingFilter.
        Unique name for the filter.


        :return: The name of this UnifiedAgentLoggingFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UnifiedAgentLoggingFilter.
        Unique name for the filter.


        :param name: The name of this UnifiedAgentLoggingFilter.
        :type: str
        """
        self._name = name

    @property
    def filter_type(self):
        """
        **[Required]** Gets the filter_type of this UnifiedAgentLoggingFilter.
        Unified schema logging filter type.

        Allowed values for this property are: "PARSER_FILTER", "GREP_FILTER", "RECORD_TRANSFORMER_FILTER", "CUSTOM_FILTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The filter_type of this UnifiedAgentLoggingFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this UnifiedAgentLoggingFilter.
        Unified schema logging filter type.


        :param filter_type: The filter_type of this UnifiedAgentLoggingFilter.
        :type: str
        """
        allowed_values = ["PARSER_FILTER", "GREP_FILTER", "RECORD_TRANSFORMER_FILTER", "CUSTOM_FILTER"]
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
