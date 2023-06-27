# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceSummary(object):
    """
    Summary of the ManagedInstance.
    """

    #: A constant which can be used with the location property of a ManagedInstanceSummary.
    #: This constant has a value of "ON_PREMISE"
    LOCATION_ON_PREMISE = "ON_PREMISE"

    #: A constant which can be used with the location property of a ManagedInstanceSummary.
    #: This constant has a value of "OCI_COMPUTE"
    LOCATION_OCI_COMPUTE = "OCI_COMPUTE"

    #: A constant which can be used with the location property of a ManagedInstanceSummary.
    #: This constant has a value of "AZURE"
    LOCATION_AZURE = "AZURE"

    #: A constant which can be used with the location property of a ManagedInstanceSummary.
    #: This constant has a value of "EC2"
    LOCATION_EC2 = "EC2"

    #: A constant which can be used with the architecture property of a ManagedInstanceSummary.
    #: This constant has a value of "X86_64"
    ARCHITECTURE_X86_64 = "X86_64"

    #: A constant which can be used with the architecture property of a ManagedInstanceSummary.
    #: This constant has a value of "AARCH64"
    ARCHITECTURE_AARCH64 = "AARCH64"

    #: A constant which can be used with the architecture property of a ManagedInstanceSummary.
    #: This constant has a value of "I686"
    ARCHITECTURE_I686 = "I686"

    #: A constant which can be used with the architecture property of a ManagedInstanceSummary.
    #: This constant has a value of "NOARCH"
    ARCHITECTURE_NOARCH = "NOARCH"

    #: A constant which can be used with the architecture property of a ManagedInstanceSummary.
    #: This constant has a value of "SRC"
    ARCHITECTURE_SRC = "SRC"

    #: A constant which can be used with the os_family property of a ManagedInstanceSummary.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a ManagedInstanceSummary.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a ManagedInstanceSummary.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "NORMAL"
    STATUS_NORMAL = "NORMAL"

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "UNREACHABLE"
    STATUS_UNREACHABLE = "UNREACHABLE"

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "REGISTRATION_ERROR"
    STATUS_REGISTRATION_ERROR = "REGISTRATION_ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedInstanceSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ManagedInstanceSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ManagedInstanceSummary.
        :type description: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this ManagedInstanceSummary.
        :type tenancy_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedInstanceSummary.
        :type compartment_id: str

        :param location:
            The value to assign to the location property of this ManagedInstanceSummary.
            Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type location: str

        :param architecture:
            The value to assign to the architecture property of this ManagedInstanceSummary.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type architecture: str

        :param os_family:
            The value to assign to the os_family property of this ManagedInstanceSummary.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param status:
            The value to assign to the status property of this ManagedInstanceSummary.
            Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param managed_instance_group:
            The value to assign to the managed_instance_group property of this ManagedInstanceSummary.
        :type managed_instance_group: oci.os_management_hub.models.Id

        :param lifecycle_environment:
            The value to assign to the lifecycle_environment property of this ManagedInstanceSummary.
        :type lifecycle_environment: oci.os_management_hub.models.Id

        :param lifecycle_stage:
            The value to assign to the lifecycle_stage property of this ManagedInstanceSummary.
        :type lifecycle_stage: oci.os_management_hub.models.Id

        :param is_reboot_required:
            The value to assign to the is_reboot_required property of this ManagedInstanceSummary.
        :type is_reboot_required: bool

        :param updates_available:
            The value to assign to the updates_available property of this ManagedInstanceSummary.
        :type updates_available: int

        :param is_management_station:
            The value to assign to the is_management_station property of this ManagedInstanceSummary.
        :type is_management_station: bool

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'tenancy_id': 'str',
            'compartment_id': 'str',
            'location': 'str',
            'architecture': 'str',
            'os_family': 'str',
            'status': 'str',
            'managed_instance_group': 'Id',
            'lifecycle_environment': 'Id',
            'lifecycle_stage': 'Id',
            'is_reboot_required': 'bool',
            'updates_available': 'int',
            'is_management_station': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'tenancy_id': 'tenancyId',
            'compartment_id': 'compartmentId',
            'location': 'location',
            'architecture': 'architecture',
            'os_family': 'osFamily',
            'status': 'status',
            'managed_instance_group': 'managedInstanceGroup',
            'lifecycle_environment': 'lifecycleEnvironment',
            'lifecycle_stage': 'lifecycleStage',
            'is_reboot_required': 'isRebootRequired',
            'updates_available': 'updatesAvailable',
            'is_management_station': 'isManagementStation'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._tenancy_id = None
        self._compartment_id = None
        self._location = None
        self._architecture = None
        self._os_family = None
        self._status = None
        self._managed_instance_group = None
        self._lifecycle_environment = None
        self._lifecycle_stage = None
        self._is_reboot_required = None
        self._updates_available = None
        self._is_management_station = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedInstanceSummary.
        The OCID for the managed instance.


        :return: The id of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedInstanceSummary.
        The OCID for the managed instance.


        :param id: The id of this ManagedInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagedInstanceSummary.
        Managed instance identifier.


        :return: The display_name of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedInstanceSummary.
        Managed instance identifier.


        :param display_name: The display_name of this ManagedInstanceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ManagedInstanceSummary.
        Information specified by the user about the managed instance.


        :return: The description of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagedInstanceSummary.
        Information specified by the user about the managed instance.


        :param description: The description of this ManagedInstanceSummary.
        :type: str
        """
        self._description = description

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this ManagedInstanceSummary.
        The OCID for the tenancy this managed instance resides in.


        :return: The tenancy_id of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this ManagedInstanceSummary.
        The OCID for the tenancy this managed instance resides in.


        :param tenancy_id: The tenancy_id of this ManagedInstanceSummary.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedInstanceSummary.
        The OCID for the compartment this managed instance resides in.


        :return: The compartment_id of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedInstanceSummary.
        The OCID for the compartment this managed instance resides in.


        :param compartment_id: The compartment_id of this ManagedInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def location(self):
        """
        Gets the location of this ManagedInstanceSummary.
        Location of the managed instance.

        Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The location of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this ManagedInstanceSummary.
        Location of the managed instance.


        :param location: The location of this ManagedInstanceSummary.
        :type: str
        """
        allowed_values = ["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2"]
        if not value_allowed_none_or_none_sentinel(location, allowed_values):
            location = 'UNKNOWN_ENUM_VALUE'
        self._location = location

    @property
    def architecture(self):
        """
        Gets the architecture of this ManagedInstanceSummary.
        The CPU architecture type of the managed instance.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The architecture of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this ManagedInstanceSummary.
        The CPU architecture type of the managed instance.


        :param architecture: The architecture of this ManagedInstanceSummary.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(architecture, allowed_values):
            architecture = 'UNKNOWN_ENUM_VALUE'
        self._architecture = architecture

    @property
    def os_family(self):
        """
        Gets the os_family of this ManagedInstanceSummary.
        The Operating System type of the managed instance.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this ManagedInstanceSummary.
        The Operating System type of the managed instance.


        :param os_family: The os_family of this ManagedInstanceSummary.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ManagedInstanceSummary.
        status of the managed instance.

        Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ManagedInstanceSummary.
        status of the managed instance.


        :param status: The status of this ManagedInstanceSummary.
        :type: str
        """
        allowed_values = ["NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def managed_instance_group(self):
        """
        Gets the managed_instance_group of this ManagedInstanceSummary.

        :return: The managed_instance_group of this ManagedInstanceSummary.
        :rtype: oci.os_management_hub.models.Id
        """
        return self._managed_instance_group

    @managed_instance_group.setter
    def managed_instance_group(self, managed_instance_group):
        """
        Sets the managed_instance_group of this ManagedInstanceSummary.

        :param managed_instance_group: The managed_instance_group of this ManagedInstanceSummary.
        :type: oci.os_management_hub.models.Id
        """
        self._managed_instance_group = managed_instance_group

    @property
    def lifecycle_environment(self):
        """
        Gets the lifecycle_environment of this ManagedInstanceSummary.

        :return: The lifecycle_environment of this ManagedInstanceSummary.
        :rtype: oci.os_management_hub.models.Id
        """
        return self._lifecycle_environment

    @lifecycle_environment.setter
    def lifecycle_environment(self, lifecycle_environment):
        """
        Sets the lifecycle_environment of this ManagedInstanceSummary.

        :param lifecycle_environment: The lifecycle_environment of this ManagedInstanceSummary.
        :type: oci.os_management_hub.models.Id
        """
        self._lifecycle_environment = lifecycle_environment

    @property
    def lifecycle_stage(self):
        """
        Gets the lifecycle_stage of this ManagedInstanceSummary.

        :return: The lifecycle_stage of this ManagedInstanceSummary.
        :rtype: oci.os_management_hub.models.Id
        """
        return self._lifecycle_stage

    @lifecycle_stage.setter
    def lifecycle_stage(self, lifecycle_stage):
        """
        Sets the lifecycle_stage of this ManagedInstanceSummary.

        :param lifecycle_stage: The lifecycle_stage of this ManagedInstanceSummary.
        :type: oci.os_management_hub.models.Id
        """
        self._lifecycle_stage = lifecycle_stage

    @property
    def is_reboot_required(self):
        """
        Gets the is_reboot_required of this ManagedInstanceSummary.
        Indicates whether a reboot is required to complete installation of updates.


        :return: The is_reboot_required of this ManagedInstanceSummary.
        :rtype: bool
        """
        return self._is_reboot_required

    @is_reboot_required.setter
    def is_reboot_required(self, is_reboot_required):
        """
        Sets the is_reboot_required of this ManagedInstanceSummary.
        Indicates whether a reboot is required to complete installation of updates.


        :param is_reboot_required: The is_reboot_required of this ManagedInstanceSummary.
        :type: bool
        """
        self._is_reboot_required = is_reboot_required

    @property
    def updates_available(self):
        """
        Gets the updates_available of this ManagedInstanceSummary.
        Number of updates available to be installed.


        :return: The updates_available of this ManagedInstanceSummary.
        :rtype: int
        """
        return self._updates_available

    @updates_available.setter
    def updates_available(self, updates_available):
        """
        Sets the updates_available of this ManagedInstanceSummary.
        Number of updates available to be installed.


        :param updates_available: The updates_available of this ManagedInstanceSummary.
        :type: int
        """
        self._updates_available = updates_available

    @property
    def is_management_station(self):
        """
        Gets the is_management_station of this ManagedInstanceSummary.
        Whether this managed instance is acting as an on-premise management station.


        :return: The is_management_station of this ManagedInstanceSummary.
        :rtype: bool
        """
        return self._is_management_station

    @is_management_station.setter
    def is_management_station(self, is_management_station):
        """
        Sets the is_management_station of this ManagedInstanceSummary.
        Whether this managed instance is acting as an on-premise management station.


        :param is_management_station: The is_management_station of this ManagedInstanceSummary.
        :type: bool
        """
        self._is_management_station = is_management_station

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
