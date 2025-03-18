# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineSchemaSummary(object):
    """
    List of source and target schemas of a pipeline's assigned connection.
    1. If there is no explicit mapping defined for the pipeline then only matched source and target schema names will be returned.
    2. If there are explicit mappings defined for the pipeline then along with the mapped source and target schema names, the matched source and target schema names also will be returned.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineSchemaSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_schema_name:
            The value to assign to the source_schema_name property of this PipelineSchemaSummary.
        :type source_schema_name: str

        :param target_schema_name:
            The value to assign to the target_schema_name property of this PipelineSchemaSummary.
        :type target_schema_name: str

        """
        self.swagger_types = {
            'source_schema_name': 'str',
            'target_schema_name': 'str'
        }
        self.attribute_map = {
            'source_schema_name': 'sourceSchemaName',
            'target_schema_name': 'targetSchemaName'
        }
        self._source_schema_name = None
        self._target_schema_name = None

    @property
    def source_schema_name(self):
        """
        **[Required]** Gets the source_schema_name of this PipelineSchemaSummary.
        The schema name from the database connection.


        :return: The source_schema_name of this PipelineSchemaSummary.
        :rtype: str
        """
        return self._source_schema_name

    @source_schema_name.setter
    def source_schema_name(self, source_schema_name):
        """
        Sets the source_schema_name of this PipelineSchemaSummary.
        The schema name from the database connection.


        :param source_schema_name: The source_schema_name of this PipelineSchemaSummary.
        :type: str
        """
        self._source_schema_name = source_schema_name

    @property
    def target_schema_name(self):
        """
        **[Required]** Gets the target_schema_name of this PipelineSchemaSummary.
        The schema name from the database connection.


        :return: The target_schema_name of this PipelineSchemaSummary.
        :rtype: str
        """
        return self._target_schema_name

    @target_schema_name.setter
    def target_schema_name(self, target_schema_name):
        """
        Sets the target_schema_name of this PipelineSchemaSummary.
        The schema name from the database connection.


        :param target_schema_name: The target_schema_name of this PipelineSchemaSummary.
        :type: str
        """
        self._target_schema_name = target_schema_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
