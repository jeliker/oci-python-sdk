# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledJobOperation(object):
    """
    Defines an operation in a scheduled job.
    """

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "INSTALL_PACKAGES"
    OPERATION_TYPE_INSTALL_PACKAGES = "INSTALL_PACKAGES"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "UPDATE_PACKAGES"
    OPERATION_TYPE_UPDATE_PACKAGES = "UPDATE_PACKAGES"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "REMOVE_PACKAGES"
    OPERATION_TYPE_REMOVE_PACKAGES = "REMOVE_PACKAGES"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "UPDATE_ALL"
    OPERATION_TYPE_UPDATE_ALL = "UPDATE_ALL"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "UPDATE_SECURITY"
    OPERATION_TYPE_UPDATE_SECURITY = "UPDATE_SECURITY"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "UPDATE_BUGFIX"
    OPERATION_TYPE_UPDATE_BUGFIX = "UPDATE_BUGFIX"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "UPDATE_ENHANCEMENT"
    OPERATION_TYPE_UPDATE_ENHANCEMENT = "UPDATE_ENHANCEMENT"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "UPDATE_OTHER"
    OPERATION_TYPE_UPDATE_OTHER = "UPDATE_OTHER"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "UPDATE_KSPLICE_USERSPACE"
    OPERATION_TYPE_UPDATE_KSPLICE_USERSPACE = "UPDATE_KSPLICE_USERSPACE"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "UPDATE_KSPLICE_KERNEL"
    OPERATION_TYPE_UPDATE_KSPLICE_KERNEL = "UPDATE_KSPLICE_KERNEL"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "MANAGE_MODULE_STREAMS"
    OPERATION_TYPE_MANAGE_MODULE_STREAMS = "MANAGE_MODULE_STREAMS"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "SWITCH_MODULE_STREAM"
    OPERATION_TYPE_SWITCH_MODULE_STREAM = "SWITCH_MODULE_STREAM"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "ATTACH_SOFTWARE_SOURCES"
    OPERATION_TYPE_ATTACH_SOFTWARE_SOURCES = "ATTACH_SOFTWARE_SOURCES"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "DETACH_SOFTWARE_SOURCES"
    OPERATION_TYPE_DETACH_SOFTWARE_SOURCES = "DETACH_SOFTWARE_SOURCES"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "SYNC_MANAGEMENT_STATION_MIRROR"
    OPERATION_TYPE_SYNC_MANAGEMENT_STATION_MIRROR = "SYNC_MANAGEMENT_STATION_MIRROR"

    #: A constant which can be used with the operation_type property of a ScheduledJobOperation.
    #: This constant has a value of "PROMOTE_LIFECYCLE"
    OPERATION_TYPE_PROMOTE_LIFECYCLE = "PROMOTE_LIFECYCLE"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledJobOperation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this ScheduledJobOperation.
            Allowed values for this property are: "INSTALL_PACKAGES", "UPDATE_PACKAGES", "REMOVE_PACKAGES", "UPDATE_ALL", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_USERSPACE", "UPDATE_KSPLICE_KERNEL", "MANAGE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "ATTACH_SOFTWARE_SOURCES", "DETACH_SOFTWARE_SOURCES", "SYNC_MANAGEMENT_STATION_MIRROR", "PROMOTE_LIFECYCLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param package_names:
            The value to assign to the package_names property of this ScheduledJobOperation.
        :type package_names: list[str]

        :param manage_module_streams_details:
            The value to assign to the manage_module_streams_details property of this ScheduledJobOperation.
        :type manage_module_streams_details: oci.os_management_hub.models.ManageModuleStreamsInScheduledJobDetails

        :param switch_module_streams_details:
            The value to assign to the switch_module_streams_details property of this ScheduledJobOperation.
        :type switch_module_streams_details: oci.os_management_hub.models.ModuleStreamDetails

        :param software_source_ids:
            The value to assign to the software_source_ids property of this ScheduledJobOperation.
        :type software_source_ids: list[str]

        """
        self.swagger_types = {
            'operation_type': 'str',
            'package_names': 'list[str]',
            'manage_module_streams_details': 'ManageModuleStreamsInScheduledJobDetails',
            'switch_module_streams_details': 'ModuleStreamDetails',
            'software_source_ids': 'list[str]'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'package_names': 'packageNames',
            'manage_module_streams_details': 'manageModuleStreamsDetails',
            'switch_module_streams_details': 'switchModuleStreamsDetails',
            'software_source_ids': 'softwareSourceIds'
        }

        self._operation_type = None
        self._package_names = None
        self._manage_module_streams_details = None
        self._switch_module_streams_details = None
        self._software_source_ids = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this ScheduledJobOperation.
        The type of operation this scheduled job performs.

        Allowed values for this property are: "INSTALL_PACKAGES", "UPDATE_PACKAGES", "REMOVE_PACKAGES", "UPDATE_ALL", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_USERSPACE", "UPDATE_KSPLICE_KERNEL", "MANAGE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "ATTACH_SOFTWARE_SOURCES", "DETACH_SOFTWARE_SOURCES", "SYNC_MANAGEMENT_STATION_MIRROR", "PROMOTE_LIFECYCLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this ScheduledJobOperation.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this ScheduledJobOperation.
        The type of operation this scheduled job performs.


        :param operation_type: The operation_type of this ScheduledJobOperation.
        :type: str
        """
        allowed_values = ["INSTALL_PACKAGES", "UPDATE_PACKAGES", "REMOVE_PACKAGES", "UPDATE_ALL", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_USERSPACE", "UPDATE_KSPLICE_KERNEL", "MANAGE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "ATTACH_SOFTWARE_SOURCES", "DETACH_SOFTWARE_SOURCES", "SYNC_MANAGEMENT_STATION_MIRROR", "PROMOTE_LIFECYCLE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def package_names(self):
        """
        Gets the package_names of this ScheduledJobOperation.
        The names of the target packages (only if operation type is INSTALL_PACKAGES/UPDATE_PACKAGES/REMOVE_PACKAGES).


        :return: The package_names of this ScheduledJobOperation.
        :rtype: list[str]
        """
        return self._package_names

    @package_names.setter
    def package_names(self, package_names):
        """
        Sets the package_names of this ScheduledJobOperation.
        The names of the target packages (only if operation type is INSTALL_PACKAGES/UPDATE_PACKAGES/REMOVE_PACKAGES).


        :param package_names: The package_names of this ScheduledJobOperation.
        :type: list[str]
        """
        self._package_names = package_names

    @property
    def manage_module_streams_details(self):
        """
        Gets the manage_module_streams_details of this ScheduledJobOperation.

        :return: The manage_module_streams_details of this ScheduledJobOperation.
        :rtype: oci.os_management_hub.models.ManageModuleStreamsInScheduledJobDetails
        """
        return self._manage_module_streams_details

    @manage_module_streams_details.setter
    def manage_module_streams_details(self, manage_module_streams_details):
        """
        Sets the manage_module_streams_details of this ScheduledJobOperation.

        :param manage_module_streams_details: The manage_module_streams_details of this ScheduledJobOperation.
        :type: oci.os_management_hub.models.ManageModuleStreamsInScheduledJobDetails
        """
        self._manage_module_streams_details = manage_module_streams_details

    @property
    def switch_module_streams_details(self):
        """
        Gets the switch_module_streams_details of this ScheduledJobOperation.

        :return: The switch_module_streams_details of this ScheduledJobOperation.
        :rtype: oci.os_management_hub.models.ModuleStreamDetails
        """
        return self._switch_module_streams_details

    @switch_module_streams_details.setter
    def switch_module_streams_details(self, switch_module_streams_details):
        """
        Sets the switch_module_streams_details of this ScheduledJobOperation.

        :param switch_module_streams_details: The switch_module_streams_details of this ScheduledJobOperation.
        :type: oci.os_management_hub.models.ModuleStreamDetails
        """
        self._switch_module_streams_details = switch_module_streams_details

    @property
    def software_source_ids(self):
        """
        Gets the software_source_ids of this ScheduledJobOperation.
        The OCIDs for the software sources (only if operation type is ATTACH_SOFTWARE_SOURCES/DETACH_SOFTWARE_SOURCES).


        :return: The software_source_ids of this ScheduledJobOperation.
        :rtype: list[str]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this ScheduledJobOperation.
        The OCIDs for the software sources (only if operation type is ATTACH_SOFTWARE_SOURCES/DETACH_SOFTWARE_SOURCES).


        :param software_source_ids: The software_source_ids of this ScheduledJobOperation.
        :type: list[str]
        """
        self._software_source_ids = software_source_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
