# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .tool_choice import ToolChoice
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ToolChoiceFunction(ToolChoice):
    """
    The tool choice for a function.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ToolChoiceFunction object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_inference.models.ToolChoiceFunction.type` attribute
        of this class is ``FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ToolChoiceFunction.
            Allowed values for this property are: "NONE", "AUTO", "REQUIRED", "FUNCTION"
        :type type: str

        :param name:
            The value to assign to the name property of this ToolChoiceFunction.
        :type name: str

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'name': 'name'
        }
        self._type = None
        self._name = None
        self._type = 'FUNCTION'

    @property
    def name(self):
        """
        Gets the name of this ToolChoiceFunction.
        The function name.


        :return: The name of this ToolChoiceFunction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ToolChoiceFunction.
        The function name.


        :param name: The name of this ToolChoiceFunction.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
