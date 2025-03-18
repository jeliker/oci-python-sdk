# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildRunSnapshotSummary(object):
    """
    Summary of a single build run snapshot. Contains information including pipelineId, commitId.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BuildRunSnapshotSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this BuildRunSnapshotSummary.
        :type build_pipeline_id: str

        :param commit_id:
            The value to assign to the commit_id property of this BuildRunSnapshotSummary.
        :type commit_id: str

        :param build_run_id:
            The value to assign to the build_run_id property of this BuildRunSnapshotSummary.
        :type build_run_id: str

        :param display_name:
            The value to assign to the display_name property of this BuildRunSnapshotSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BuildRunSnapshotSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this BuildRunSnapshotSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this BuildRunSnapshotSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BuildRunSnapshotSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'build_pipeline_id': 'str',
            'commit_id': 'str',
            'build_run_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'build_pipeline_id': 'buildPipelineId',
            'commit_id': 'commitId',
            'build_run_id': 'buildRunId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }
        self._build_pipeline_id = None
        self._commit_id = None
        self._build_run_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None

    @property
    def build_pipeline_id(self):
        """
        **[Required]** Gets the build_pipeline_id of this BuildRunSnapshotSummary.
        The OCID of the build pipeline where the build was triggered.


        :return: The build_pipeline_id of this BuildRunSnapshotSummary.
        :rtype: str
        """
        return self._build_pipeline_id

    @build_pipeline_id.setter
    def build_pipeline_id(self, build_pipeline_id):
        """
        Sets the build_pipeline_id of this BuildRunSnapshotSummary.
        The OCID of the build pipeline where the build was triggered.


        :param build_pipeline_id: The build_pipeline_id of this BuildRunSnapshotSummary.
        :type: str
        """
        self._build_pipeline_id = build_pipeline_id

    @property
    def commit_id(self):
        """
        **[Required]** Gets the commit_id of this BuildRunSnapshotSummary.
        The commit id which the build was triggered from.


        :return: The commit_id of this BuildRunSnapshotSummary.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this BuildRunSnapshotSummary.
        The commit id which the build was triggered from.


        :param commit_id: The commit_id of this BuildRunSnapshotSummary.
        :type: str
        """
        self._commit_id = commit_id

    @property
    def build_run_id(self):
        """
        **[Required]** Gets the build_run_id of this BuildRunSnapshotSummary.
        The OCID of the build run.


        :return: The build_run_id of this BuildRunSnapshotSummary.
        :rtype: str
        """
        return self._build_run_id

    @build_run_id.setter
    def build_run_id(self, build_run_id):
        """
        Sets the build_run_id of this BuildRunSnapshotSummary.
        The OCID of the build run.


        :param build_run_id: The build_run_id of this BuildRunSnapshotSummary.
        :type: str
        """
        self._build_run_id = build_run_id

    @property
    def display_name(self):
        """
        Gets the display_name of this BuildRunSnapshotSummary.
        The display name of the build run.


        :return: The display_name of this BuildRunSnapshotSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BuildRunSnapshotSummary.
        The display name of the build run.


        :param display_name: The display_name of this BuildRunSnapshotSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BuildRunSnapshotSummary.
        The current status of the build run.


        :return: The lifecycle_state of this BuildRunSnapshotSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BuildRunSnapshotSummary.
        The current status of the build run.


        :param lifecycle_state: The lifecycle_state of this BuildRunSnapshotSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this BuildRunSnapshotSummary.
        A message describing the current state in more detail.


        :return: The lifecycle_details of this BuildRunSnapshotSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this BuildRunSnapshotSummary.
        A message describing the current state in more detail.


        :param lifecycle_details: The lifecycle_details of this BuildRunSnapshotSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        Gets the time_created of this BuildRunSnapshotSummary.
        The time the build run was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this BuildRunSnapshotSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BuildRunSnapshotSummary.
        The time the build run was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this BuildRunSnapshotSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BuildRunSnapshotSummary.
        The time the build run was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this BuildRunSnapshotSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BuildRunSnapshotSummary.
        The time the build run was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this BuildRunSnapshotSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
