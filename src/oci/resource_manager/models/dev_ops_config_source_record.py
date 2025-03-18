# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180917

from .config_source_record import ConfigSourceRecord
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DevOpsConfigSourceRecord(ConfigSourceRecord):
    """
    Metadata about the `DevOps`__ configuration source.

    __ https://docs.cloud.oracle.com/iaas/Content/devops/using/home.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DevOpsConfigSourceRecord object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.DevOpsConfigSourceRecord.config_source_record_type` attribute
        of this class is ``DEVOPS_CONFIG_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_record_type:
            The value to assign to the config_source_record_type property of this DevOpsConfigSourceRecord.
            Allowed values for this property are: "BITBUCKET_CLOUD_CONFIG_SOURCE", "BITBUCKET_SERVER_CONFIG_SOURCE", "COMPARTMENT_CONFIG_SOURCE", "DEVOPS_CONFIG_SOURCE", "GIT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE", "ZIP_UPLOAD"
        :type config_source_record_type: str

        :param project_id:
            The value to assign to the project_id property of this DevOpsConfigSourceRecord.
        :type project_id: str

        :param repository_id:
            The value to assign to the repository_id property of this DevOpsConfigSourceRecord.
        :type repository_id: str

        :param branch_name:
            The value to assign to the branch_name property of this DevOpsConfigSourceRecord.
        :type branch_name: str

        :param commit_id:
            The value to assign to the commit_id property of this DevOpsConfigSourceRecord.
        :type commit_id: str

        """
        self.swagger_types = {
            'config_source_record_type': 'str',
            'project_id': 'str',
            'repository_id': 'str',
            'branch_name': 'str',
            'commit_id': 'str'
        }
        self.attribute_map = {
            'config_source_record_type': 'configSourceRecordType',
            'project_id': 'projectId',
            'repository_id': 'repositoryId',
            'branch_name': 'branchName',
            'commit_id': 'commitId'
        }
        self._config_source_record_type = None
        self._project_id = None
        self._repository_id = None
        self._branch_name = None
        self._commit_id = None
        self._config_source_record_type = 'DEVOPS_CONFIG_SOURCE'

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this DevOpsConfigSourceRecord.
        The `OCID`__ of the :class:`Project`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this DevOpsConfigSourceRecord.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this DevOpsConfigSourceRecord.
        The `OCID`__ of the :class:`Project`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this DevOpsConfigSourceRecord.
        :type: str
        """
        self._project_id = project_id

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this DevOpsConfigSourceRecord.
        The `OCID`__ of the :class:`Repository`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The repository_id of this DevOpsConfigSourceRecord.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this DevOpsConfigSourceRecord.
        The `OCID`__ of the :class:`Repository`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param repository_id: The repository_id of this DevOpsConfigSourceRecord.
        :type: str
        """
        self._repository_id = repository_id

    @property
    def branch_name(self):
        """
        **[Required]** Gets the branch_name of this DevOpsConfigSourceRecord.
        The name of the branch that contains the Terraform configuration.


        :return: The branch_name of this DevOpsConfigSourceRecord.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """
        Sets the branch_name of this DevOpsConfigSourceRecord.
        The name of the branch that contains the Terraform configuration.


        :param branch_name: The branch_name of this DevOpsConfigSourceRecord.
        :type: str
        """
        self._branch_name = branch_name

    @property
    def commit_id(self):
        """
        Gets the commit_id of this DevOpsConfigSourceRecord.
        The unique identifier (SHA-1 hash) of the individual change to the DevOps repository.


        :return: The commit_id of this DevOpsConfigSourceRecord.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this DevOpsConfigSourceRecord.
        The unique identifier (SHA-1 hash) of the individual change to the DevOps repository.


        :param commit_id: The commit_id of this DevOpsConfigSourceRecord.
        :type: str
        """
        self._commit_id = commit_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
