# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentsConfiguration(object):
    """
    Input documents configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentsConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config:
            The value to assign to the config property of this DocumentsConfiguration.
        :type config: dict(str, str)

        """
        self.swagger_types = {
            'config': 'dict(str, str)'
        }
        self.attribute_map = {
            'config': 'config'
        }
        self._config = None

    @property
    def config(self):
        """
        Gets the config of this DocumentsConfiguration.
        meta data about documents
         For CSV valid JSON format is {\"CSV\" :{inputColumn: \"reviewDetails\", rowId: \"reviewId\", copyColumnsToOutput: [\"reviewId\" \"userId\"] , delimiter: \",\"}
        Note: In future if new file types added we will update here in documentation about input file meta data


        :return: The config of this DocumentsConfiguration.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this DocumentsConfiguration.
        meta data about documents
         For CSV valid JSON format is {\"CSV\" :{inputColumn: \"reviewDetails\", rowId: \"reviewId\", copyColumnsToOutput: [\"reviewId\" \"userId\"] , delimiter: \",\"}
        Note: In future if new file types added we will update here in documentation about input file meta data


        :param config: The config of this DocumentsConfiguration.
        :type: dict(str, str)
        """
        self._config = config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
