# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DependentParser(object):
    """
    A parser used by another parser.
    """

    #: A constant which can be used with the parser_type property of a DependentParser.
    #: This constant has a value of "XML"
    PARSER_TYPE_XML = "XML"

    #: A constant which can be used with the parser_type property of a DependentParser.
    #: This constant has a value of "JSON"
    PARSER_TYPE_JSON = "JSON"

    #: A constant which can be used with the parser_type property of a DependentParser.
    #: This constant has a value of "REGEX"
    PARSER_TYPE_REGEX = "REGEX"

    #: A constant which can be used with the parser_type property of a DependentParser.
    #: This constant has a value of "ODL"
    PARSER_TYPE_ODL = "ODL"

    #: A constant which can be used with the parser_type property of a DependentParser.
    #: This constant has a value of "DELIMITED"
    PARSER_TYPE_DELIMITED = "DELIMITED"

    def __init__(self, **kwargs):
        """
        Initializes a new DependentParser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parser_name:
            The value to assign to the parser_name property of this DependentParser.
        :type parser_name: str

        :param parser_display_name:
            The value to assign to the parser_display_name property of this DependentParser.
        :type parser_display_name: str

        :param parser_id:
            The value to assign to the parser_id property of this DependentParser.
        :type parser_id: int

        :param is_system:
            The value to assign to the is_system property of this DependentParser.
        :type is_system: bool

        :param parser_type:
            The value to assign to the parser_type property of this DependentParser.
            Allowed values for this property are: "XML", "JSON", "REGEX", "ODL", "DELIMITED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type parser_type: str

        :param dependencies:
            The value to assign to the dependencies property of this DependentParser.
        :type dependencies: list[oci.log_analytics.models.Dependency]

        """
        self.swagger_types = {
            'parser_name': 'str',
            'parser_display_name': 'str',
            'parser_id': 'int',
            'is_system': 'bool',
            'parser_type': 'str',
            'dependencies': 'list[Dependency]'
        }

        self.attribute_map = {
            'parser_name': 'parserName',
            'parser_display_name': 'parserDisplayName',
            'parser_id': 'parserId',
            'is_system': 'isSystem',
            'parser_type': 'parserType',
            'dependencies': 'dependencies'
        }

        self._parser_name = None
        self._parser_display_name = None
        self._parser_id = None
        self._is_system = None
        self._parser_type = None
        self._dependencies = None

    @property
    def parser_name(self):
        """
        Gets the parser_name of this DependentParser.
        The parser name.


        :return: The parser_name of this DependentParser.
        :rtype: str
        """
        return self._parser_name

    @parser_name.setter
    def parser_name(self, parser_name):
        """
        Sets the parser_name of this DependentParser.
        The parser name.


        :param parser_name: The parser_name of this DependentParser.
        :type: str
        """
        self._parser_name = parser_name

    @property
    def parser_display_name(self):
        """
        Gets the parser_display_name of this DependentParser.
        The parser display name.


        :return: The parser_display_name of this DependentParser.
        :rtype: str
        """
        return self._parser_display_name

    @parser_display_name.setter
    def parser_display_name(self, parser_display_name):
        """
        Sets the parser_display_name of this DependentParser.
        The parser display name.


        :param parser_display_name: The parser_display_name of this DependentParser.
        :type: str
        """
        self._parser_display_name = parser_display_name

    @property
    def parser_id(self):
        """
        Gets the parser_id of this DependentParser.
        The parser unique identifier.


        :return: The parser_id of this DependentParser.
        :rtype: int
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        """
        Sets the parser_id of this DependentParser.
        The parser unique identifier.


        :param parser_id: The parser_id of this DependentParser.
        :type: int
        """
        self._parser_id = parser_id

    @property
    def is_system(self):
        """
        Gets the is_system of this DependentParser.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this DependentParser.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this DependentParser.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this DependentParser.
        :type: bool
        """
        self._is_system = is_system

    @property
    def parser_type(self):
        """
        Gets the parser_type of this DependentParser.
        The parser type

        Allowed values for this property are: "XML", "JSON", "REGEX", "ODL", "DELIMITED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The parser_type of this DependentParser.
        :rtype: str
        """
        return self._parser_type

    @parser_type.setter
    def parser_type(self, parser_type):
        """
        Sets the parser_type of this DependentParser.
        The parser type


        :param parser_type: The parser_type of this DependentParser.
        :type: str
        """
        allowed_values = ["XML", "JSON", "REGEX", "ODL", "DELIMITED"]
        if not value_allowed_none_or_none_sentinel(parser_type, allowed_values):
            parser_type = 'UNKNOWN_ENUM_VALUE'
        self._parser_type = parser_type

    @property
    def dependencies(self):
        """
        Gets the dependencies of this DependentParser.
        The list of dependencies of the parser.


        :return: The dependencies of this DependentParser.
        :rtype: list[oci.log_analytics.models.Dependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this DependentParser.
        The list of dependencies of the parser.


        :param dependencies: The dependencies of this DependentParser.
        :type: list[oci.log_analytics.models.Dependency]
        """
        self._dependencies = dependencies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other