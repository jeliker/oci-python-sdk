# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .create_deploy_stage_details import CreateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWaitDeployStageDetails(CreateDeployStageDetails):
    """
    Specifies the Wait stage. User can specify a criteria for wait time or give an absolute duration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWaitDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateWaitDeployStageDetails.deploy_stage_type` attribute
        of this class is ``WAIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateWaitDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateWaitDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this CreateWaitDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateWaitDeployStageDetails.
        :type deploy_pipeline_id: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this CreateWaitDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateWaitDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateWaitDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param wait_criteria:
            The value to assign to the wait_criteria property of this CreateWaitDeployStageDetails.
        :type wait_criteria: oci.devops.models.WaitCriteria

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_pipeline_id': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'wait_criteria': 'WaitCriteria'
        }
        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_pipeline_id': 'deployPipelineId',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'wait_criteria': 'waitCriteria'
        }
        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_pipeline_id = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._wait_criteria = None
        self._deploy_stage_type = 'WAIT'

    @property
    def wait_criteria(self):
        """
        **[Required]** Gets the wait_criteria of this CreateWaitDeployStageDetails.

        :return: The wait_criteria of this CreateWaitDeployStageDetails.
        :rtype: oci.devops.models.WaitCriteria
        """
        return self._wait_criteria

    @wait_criteria.setter
    def wait_criteria(self, wait_criteria):
        """
        Sets the wait_criteria of this CreateWaitDeployStageDetails.

        :param wait_criteria: The wait_criteria of this CreateWaitDeployStageDetails.
        :type: oci.devops.models.WaitCriteria
        """
        self._wait_criteria = wait_criteria

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
