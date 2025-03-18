# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OutputVariableDetails(object):
    """
    The details of the output variable that will be used for mapping.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OutputVariableDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_name:
            The value to assign to the step_name property of this OutputVariableDetails.
        :type step_name: str

        :param output_variable_name:
            The value to assign to the output_variable_name property of this OutputVariableDetails.
        :type output_variable_name: str

        """
        self.swagger_types = {
            'step_name': 'str',
            'output_variable_name': 'str'
        }
        self.attribute_map = {
            'step_name': 'stepName',
            'output_variable_name': 'outputVariableName'
        }
        self._step_name = None
        self._output_variable_name = None

    @property
    def step_name(self):
        """
        **[Required]** Gets the step_name of this OutputVariableDetails.
        The name of the task step the output variable belongs to.


        :return: The step_name of this OutputVariableDetails.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this OutputVariableDetails.
        The name of the task step the output variable belongs to.


        :param step_name: The step_name of this OutputVariableDetails.
        :type: str
        """
        self._step_name = step_name

    @property
    def output_variable_name(self):
        """
        **[Required]** Gets the output_variable_name of this OutputVariableDetails.
        The name of the output variable whose value has to be mapped.


        :return: The output_variable_name of this OutputVariableDetails.
        :rtype: str
        """
        return self._output_variable_name

    @output_variable_name.setter
    def output_variable_name(self, output_variable_name):
        """
        Sets the output_variable_name of this OutputVariableDetails.
        The name of the output variable whose value has to be mapped.


        :param output_variable_name: The output_variable_name of this OutputVariableDetails.
        :type: str
        """
        self._output_variable_name = output_variable_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
