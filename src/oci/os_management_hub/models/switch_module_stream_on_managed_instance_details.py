# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SwitchModuleStreamOnManagedInstanceDetails(object):
    """
    The details of the module stream to be version switched on a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SwitchModuleStreamOnManagedInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param work_request_details:
            The value to assign to the work_request_details property of this SwitchModuleStreamOnManagedInstanceDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        :param module_name:
            The value to assign to the module_name property of this SwitchModuleStreamOnManagedInstanceDetails.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this SwitchModuleStreamOnManagedInstanceDetails.
        :type stream_name: str

        """
        self.swagger_types = {
            'work_request_details': 'WorkRequestDetails',
            'module_name': 'str',
            'stream_name': 'str'
        }

        self.attribute_map = {
            'work_request_details': 'workRequestDetails',
            'module_name': 'moduleName',
            'stream_name': 'streamName'
        }

        self._work_request_details = None
        self._module_name = None
        self._stream_name = None

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this SwitchModuleStreamOnManagedInstanceDetails.

        :return: The work_request_details of this SwitchModuleStreamOnManagedInstanceDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this SwitchModuleStreamOnManagedInstanceDetails.

        :param work_request_details: The work_request_details of this SwitchModuleStreamOnManagedInstanceDetails.
        :type: oci.os_management_hub.models.WorkRequestDetails
        """
        self._work_request_details = work_request_details

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this SwitchModuleStreamOnManagedInstanceDetails.
        The name of a module.


        :return: The module_name of this SwitchModuleStreamOnManagedInstanceDetails.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this SwitchModuleStreamOnManagedInstanceDetails.
        The name of a module.


        :param module_name: The module_name of this SwitchModuleStreamOnManagedInstanceDetails.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this SwitchModuleStreamOnManagedInstanceDetails.
        The name of a stream of the specified module.


        :return: The stream_name of this SwitchModuleStreamOnManagedInstanceDetails.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this SwitchModuleStreamOnManagedInstanceDetails.
        The name of a stream of the specified module.


        :param stream_name: The stream_name of this SwitchModuleStreamOnManagedInstanceDetails.
        :type: str
        """
        self._stream_name = stream_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
