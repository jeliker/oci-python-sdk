# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachSoftwareSourcesToManagedInstanceGroupDetails(object):
    """
    Provides the information used to attach software sources to a managed instance group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachSoftwareSourcesToManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_sources:
            The value to assign to the software_sources property of this AttachSoftwareSourcesToManagedInstanceGroupDetails.
        :type software_sources: list[str]

        :param work_request_details:
            The value to assign to the work_request_details property of this AttachSoftwareSourcesToManagedInstanceGroupDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'software_sources': 'list[str]',
            'work_request_details': 'WorkRequestDetails'
        }
        self.attribute_map = {
            'software_sources': 'softwareSources',
            'work_request_details': 'workRequestDetails'
        }
        self._software_sources = None
        self._work_request_details = None

    @property
    def software_sources(self):
        """
        **[Required]** Gets the software_sources of this AttachSoftwareSourcesToManagedInstanceGroupDetails.
        List of software source `OCIDs`__ to attach to the group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The software_sources of this AttachSoftwareSourcesToManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this AttachSoftwareSourcesToManagedInstanceGroupDetails.
        List of software source `OCIDs`__ to attach to the group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param software_sources: The software_sources of this AttachSoftwareSourcesToManagedInstanceGroupDetails.
        :type: list[str]
        """
        self._software_sources = software_sources

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this AttachSoftwareSourcesToManagedInstanceGroupDetails.

        :return: The work_request_details of this AttachSoftwareSourcesToManagedInstanceGroupDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this AttachSoftwareSourcesToManagedInstanceGroupDetails.

        :param work_request_details: The work_request_details of this AttachSoftwareSourcesToManagedInstanceGroupDetails.
        :type: oci.os_management_hub.models.WorkRequestDetails
        """
        self._work_request_details = work_request_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
