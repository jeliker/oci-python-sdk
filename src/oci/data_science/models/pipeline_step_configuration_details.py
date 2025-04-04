# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineStepConfigurationDetails(object):
    """
    The configuration details of a step.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineStepConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param maximum_runtime_in_minutes:
            The value to assign to the maximum_runtime_in_minutes property of this PipelineStepConfigurationDetails.
        :type maximum_runtime_in_minutes: int

        :param environment_variables:
            The value to assign to the environment_variables property of this PipelineStepConfigurationDetails.
        :type environment_variables: dict(str, str)

        :param command_line_arguments:
            The value to assign to the command_line_arguments property of this PipelineStepConfigurationDetails.
        :type command_line_arguments: str

        """
        self.swagger_types = {
            'maximum_runtime_in_minutes': 'int',
            'environment_variables': 'dict(str, str)',
            'command_line_arguments': 'str'
        }
        self.attribute_map = {
            'maximum_runtime_in_minutes': 'maximumRuntimeInMinutes',
            'environment_variables': 'environmentVariables',
            'command_line_arguments': 'commandLineArguments'
        }
        self._maximum_runtime_in_minutes = None
        self._environment_variables = None
        self._command_line_arguments = None

    @property
    def maximum_runtime_in_minutes(self):
        """
        Gets the maximum_runtime_in_minutes of this PipelineStepConfigurationDetails.
        A time bound for the execution of the step.


        :return: The maximum_runtime_in_minutes of this PipelineStepConfigurationDetails.
        :rtype: int
        """
        return self._maximum_runtime_in_minutes

    @maximum_runtime_in_minutes.setter
    def maximum_runtime_in_minutes(self, maximum_runtime_in_minutes):
        """
        Sets the maximum_runtime_in_minutes of this PipelineStepConfigurationDetails.
        A time bound for the execution of the step.


        :param maximum_runtime_in_minutes: The maximum_runtime_in_minutes of this PipelineStepConfigurationDetails.
        :type: int
        """
        self._maximum_runtime_in_minutes = maximum_runtime_in_minutes

    @property
    def environment_variables(self):
        """
        Gets the environment_variables of this PipelineStepConfigurationDetails.
        Environment variables to set for step.


        :return: The environment_variables of this PipelineStepConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        """
        Sets the environment_variables of this PipelineStepConfigurationDetails.
        Environment variables to set for step.


        :param environment_variables: The environment_variables of this PipelineStepConfigurationDetails.
        :type: dict(str, str)
        """
        self._environment_variables = environment_variables

    @property
    def command_line_arguments(self):
        """
        Gets the command_line_arguments of this PipelineStepConfigurationDetails.
        The command line arguments to set for step.


        :return: The command_line_arguments of this PipelineStepConfigurationDetails.
        :rtype: str
        """
        return self._command_line_arguments

    @command_line_arguments.setter
    def command_line_arguments(self, command_line_arguments):
        """
        Sets the command_line_arguments of this PipelineStepConfigurationDetails.
        The command line arguments to set for step.


        :param command_line_arguments: The command_line_arguments of this PipelineStepConfigurationDetails.
        :type: str
        """
        self._command_line_arguments = command_line_arguments

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
