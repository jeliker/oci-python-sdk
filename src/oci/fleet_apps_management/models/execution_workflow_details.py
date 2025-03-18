# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecutionWorkflowDetails(object):
    """
    Execution Workflow details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExecutionWorkflowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param workflow:
            The value to assign to the workflow property of this ExecutionWorkflowDetails.
        :type workflow: list[oci.fleet_apps_management.models.WorkflowGroup]

        """
        self.swagger_types = {
            'workflow': 'list[WorkflowGroup]'
        }
        self.attribute_map = {
            'workflow': 'workflow'
        }
        self._workflow = None

    @property
    def workflow(self):
        """
        **[Required]** Gets the workflow of this ExecutionWorkflowDetails.
        Execution Workflow for the runbook.


        :return: The workflow of this ExecutionWorkflowDetails.
        :rtype: list[oci.fleet_apps_management.models.WorkflowGroup]
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """
        Sets the workflow of this ExecutionWorkflowDetails.
        Execution Workflow for the runbook.


        :param workflow: The workflow of this ExecutionWorkflowDetails.
        :type: list[oci.fleet_apps_management.models.WorkflowGroup]
        """
        self._workflow = workflow

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
