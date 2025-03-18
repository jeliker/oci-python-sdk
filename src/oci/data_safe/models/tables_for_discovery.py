# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TablesForDiscovery(object):
    """
    This contains the schema name along with one or more optional table names.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TablesForDiscovery object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schema_name:
            The value to assign to the schema_name property of this TablesForDiscovery.
        :type schema_name: str

        :param table_names:
            The value to assign to the table_names property of this TablesForDiscovery.
        :type table_names: list[str]

        """
        self.swagger_types = {
            'schema_name': 'str',
            'table_names': 'list[str]'
        }
        self.attribute_map = {
            'schema_name': 'schemaName',
            'table_names': 'tableNames'
        }
        self._schema_name = None
        self._table_names = None

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this TablesForDiscovery.
        This contains the name of the schema.


        :return: The schema_name of this TablesForDiscovery.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this TablesForDiscovery.
        This contains the name of the schema.


        :param schema_name: The schema_name of this TablesForDiscovery.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def table_names(self):
        """
        Gets the table_names of this TablesForDiscovery.
        This contains an optional list of the table names.


        :return: The table_names of this TablesForDiscovery.
        :rtype: list[str]
        """
        return self._table_names

    @table_names.setter
    def table_names(self, table_names):
        """
        Sets the table_names of this TablesForDiscovery.
        This contains an optional list of the table names.


        :param table_names: The table_names of this TablesForDiscovery.
        :type: list[str]
        """
        self._table_names = table_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
