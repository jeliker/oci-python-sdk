# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):
    """
    Describes a work request.
    """

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "INSTALL_PACKAGES"
    OPERATION_TYPE_INSTALL_PACKAGES = "INSTALL_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "REMOVE_PACKAGES"
    OPERATION_TYPE_REMOVE_PACKAGES = "REMOVE_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_PACKAGES"
    OPERATION_TYPE_UPDATE_PACKAGES = "UPDATE_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_ALL_PACKAGES"
    OPERATION_TYPE_UPDATE_ALL_PACKAGES = "UPDATE_ALL_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_SECURITY"
    OPERATION_TYPE_UPDATE_SECURITY = "UPDATE_SECURITY"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_BUGFIX"
    OPERATION_TYPE_UPDATE_BUGFIX = "UPDATE_BUGFIX"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_ENHANCEMENT"
    OPERATION_TYPE_UPDATE_ENHANCEMENT = "UPDATE_ENHANCEMENT"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_OTHER"
    OPERATION_TYPE_UPDATE_OTHER = "UPDATE_OTHER"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_KSPLICE_KERNEL"
    OPERATION_TYPE_UPDATE_KSPLICE_KERNEL = "UPDATE_KSPLICE_KERNEL"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_KSPLICE_USERSPACE"
    OPERATION_TYPE_UPDATE_KSPLICE_USERSPACE = "UPDATE_KSPLICE_USERSPACE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "ENABLE_MODULE_STREAMS"
    OPERATION_TYPE_ENABLE_MODULE_STREAMS = "ENABLE_MODULE_STREAMS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DISABLE_MODULE_STREAMS"
    OPERATION_TYPE_DISABLE_MODULE_STREAMS = "DISABLE_MODULE_STREAMS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "SWITCH_MODULE_STREAM"
    OPERATION_TYPE_SWITCH_MODULE_STREAM = "SWITCH_MODULE_STREAM"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "INSTALL_MODULE_PROFILES"
    OPERATION_TYPE_INSTALL_MODULE_PROFILES = "INSTALL_MODULE_PROFILES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "REMOVE_MODULE_PROFILES"
    OPERATION_TYPE_REMOVE_MODULE_PROFILES = "REMOVE_MODULE_PROFILES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "SET_SOFTWARE_SOURCES"
    OPERATION_TYPE_SET_SOFTWARE_SOURCES = "SET_SOFTWARE_SOURCES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "LIST_PACKAGES"
    OPERATION_TYPE_LIST_PACKAGES = "LIST_PACKAGES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "SET_MANAGEMENT_STATION_CONFIG"
    OPERATION_TYPE_SET_MANAGEMENT_STATION_CONFIG = "SET_MANAGEMENT_STATION_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "SYNC_MANAGEMENT_STATION_MIRROR"
    OPERATION_TYPE_SYNC_MANAGEMENT_STATION_MIRROR = "SYNC_MANAGEMENT_STATION_MIRROR"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_MANAGEMENT_STATION_SOFTWARE"
    OPERATION_TYPE_UPDATE_MANAGEMENT_STATION_SOFTWARE = "UPDATE_MANAGEMENT_STATION_SOFTWARE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE"
    OPERATION_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "MODULE_ACTIONS"
    OPERATION_TYPE_MODULE_ACTIONS = "MODULE_ACTIONS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "LIFECYCLE_PROMOTION"
    OPERATION_TYPE_LIFECYCLE_PROMOTION = "LIFECYCLE_PROMOTION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_SOFTWARE_SOURCE"
    OPERATION_TYPE_CREATE_SOFTWARE_SOURCE = "CREATE_SOFTWARE_SOURCE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_SOFTWARE_SOURCE"
    OPERATION_TYPE_UPDATE_SOFTWARE_SOURCE = "UPDATE_SOFTWARE_SOURCE"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequest.
            Allowed values for this property are: "INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_ALL_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_KERNEL", "UPDATE_KSPLICE_USERSPACE", "ENABLE_MODULE_STREAMS", "DISABLE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "INSTALL_MODULE_PROFILES", "REMOVE_MODULE_PROFILES", "SET_SOFTWARE_SOURCES", "LIST_PACKAGES", "SET_MANAGEMENT_STATION_CONFIG", "SYNC_MANAGEMENT_STATION_MIRROR", "UPDATE_MANAGEMENT_STATION_SOFTWARE", "UPDATE", "MODULE_ACTIONS", "LIFECYCLE_PROMOTION", "CREATE_SOFTWARE_SOURCE", "UPDATE_SOFTWARE_SOURCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param id:
            The value to assign to the id property of this WorkRequest.
        :type id: str

        :param description:
            The value to assign to the description property of this WorkRequest.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this WorkRequest.
        :type display_name: str

        :param message:
            The value to assign to the message property of this WorkRequest.
        :type message: str

        :param parent_id:
            The value to assign to the parent_id property of this WorkRequest.
        :type parent_id: str

        :param children_id:
            The value to assign to the children_id property of this WorkRequest.
        :type children_id: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequest.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this WorkRequest.
        :type resources: list[oci.os_management_hub.models.WorkRequestResource]

        :param package_names:
            The value to assign to the package_names property of this WorkRequest.
        :type package_names: list[str]

        :param module_specs:
            The value to assign to the module_specs property of this WorkRequest.
        :type module_specs: list[oci.os_management_hub.models.ModuleSpecDetails]

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequest.
        :type percent_complete: float

        :param time_created:
            The value to assign to the time_created property of this WorkRequest.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this WorkRequest.
        :type time_updated: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequest.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequest.
        :type time_finished: datetime

        :param initiator_id:
            The value to assign to the initiator_id property of this WorkRequest.
        :type initiator_id: str

        :param management_station:
            The value to assign to the management_station property of this WorkRequest.
        :type management_station: oci.os_management_hub.models.WorkRequestManagementStationDetails

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'message': 'str',
            'parent_id': 'str',
            'children_id': 'list[str]',
            'compartment_id': 'str',
            'resources': 'list[WorkRequestResource]',
            'package_names': 'list[str]',
            'module_specs': 'list[ModuleSpecDetails]',
            'percent_complete': 'float',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'initiator_id': 'str',
            'management_station': 'WorkRequestManagementStationDetails'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'message': 'message',
            'parent_id': 'parentId',
            'children_id': 'childrenId',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'package_names': 'packageNames',
            'module_specs': 'moduleSpecs',
            'percent_complete': 'percentComplete',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'initiator_id': 'initiatorId',
            'management_station': 'managementStation'
        }

        self._operation_type = None
        self._status = None
        self._id = None
        self._description = None
        self._display_name = None
        self._message = None
        self._parent_id = None
        self._children_id = None
        self._compartment_id = None
        self._resources = None
        self._package_names = None
        self._module_specs = None
        self._percent_complete = None
        self._time_created = None
        self._time_updated = None
        self._time_started = None
        self._time_finished = None
        self._initiator_id = None
        self._management_station = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequest.
        Type of the work request.

        Allowed values for this property are: "INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_ALL_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_KERNEL", "UPDATE_KSPLICE_USERSPACE", "ENABLE_MODULE_STREAMS", "DISABLE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "INSTALL_MODULE_PROFILES", "REMOVE_MODULE_PROFILES", "SET_SOFTWARE_SOURCES", "LIST_PACKAGES", "SET_MANAGEMENT_STATION_CONFIG", "SYNC_MANAGEMENT_STATION_MIRROR", "UPDATE_MANAGEMENT_STATION_SOFTWARE", "UPDATE", "MODULE_ACTIONS", "LIFECYCLE_PROMOTION", "CREATE_SOFTWARE_SOURCE", "UPDATE_SOFTWARE_SOURCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequest.
        Type of the work request.


        :param operation_type: The operation_type of this WorkRequest.
        :type: str
        """
        allowed_values = ["INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_ALL_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", "UPDATE_KSPLICE_KERNEL", "UPDATE_KSPLICE_USERSPACE", "ENABLE_MODULE_STREAMS", "DISABLE_MODULE_STREAMS", "SWITCH_MODULE_STREAM", "INSTALL_MODULE_PROFILES", "REMOVE_MODULE_PROFILES", "SET_SOFTWARE_SOURCES", "LIST_PACKAGES", "SET_MANAGEMENT_STATION_CONFIG", "SYNC_MANAGEMENT_STATION_MIRROR", "UPDATE_MANAGEMENT_STATION_SOFTWARE", "UPDATE", "MODULE_ACTIONS", "LIFECYCLE_PROMOTION", "CREATE_SOFTWARE_SOURCE", "UPDATE_SOFTWARE_SOURCE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequest.
        Status of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequest.
        Status of the work request.


        :param status: The status of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequest.
        The OCID of the work request.


        :return: The id of this WorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequest.
        The OCID of the work request.


        :param id: The id of this WorkRequest.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this WorkRequest.
        A short description about the work request.


        :return: The description of this WorkRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkRequest.
        A short description about the work request.


        :param description: The description of this WorkRequest.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this WorkRequest.
        A short display name for the work request.


        :return: The display_name of this WorkRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WorkRequest.
        A short display name for the work request.


        :param display_name: The display_name of this WorkRequest.
        :type: str
        """
        self._display_name = display_name

    @property
    def message(self):
        """
        Gets the message of this WorkRequest.
        A progress or error message, if there is any.


        :return: The message of this WorkRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequest.
        A progress or error message, if there is any.


        :param message: The message of this WorkRequest.
        :type: str
        """
        self._message = message

    @property
    def parent_id(self):
        """
        Gets the parent_id of this WorkRequest.
        The OCID of the parent work request, if there is any.


        :return: The parent_id of this WorkRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this WorkRequest.
        The OCID of the parent work request, if there is any.


        :param parent_id: The parent_id of this WorkRequest.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def children_id(self):
        """
        Gets the children_id of this WorkRequest.
        The list of OCIDs for the child work requests.


        :return: The children_id of this WorkRequest.
        :rtype: list[str]
        """
        return self._children_id

    @children_id.setter
    def children_id(self, children_id):
        """
        Sets the children_id of this WorkRequest.
        The list of OCIDs for the child work requests.


        :param children_id: The children_id of this WorkRequest.
        :type: list[str]
        """
        self._children_id = children_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequest.
        The OCID of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource it affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used.


        :return: The compartment_id of this WorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequest.
        The OCID of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource it affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used.


        :param compartment_id: The compartment_id of this WorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequest.
        The list of OCIDs for the resources affected by the work request.


        :return: The resources of this WorkRequest.
        :rtype: list[oci.os_management_hub.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequest.
        The list of OCIDs for the resources affected by the work request.


        :param resources: The resources of this WorkRequest.
        :type: list[oci.os_management_hub.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def package_names(self):
        """
        Gets the package_names of this WorkRequest.
        A list of package names to be installed/updated/removed.


        :return: The package_names of this WorkRequest.
        :rtype: list[str]
        """
        return self._package_names

    @package_names.setter
    def package_names(self, package_names):
        """
        Sets the package_names of this WorkRequest.
        A list of package names to be installed/updated/removed.


        :param package_names: The package_names of this WorkRequest.
        :type: list[str]
        """
        self._package_names = package_names

    @property
    def module_specs(self):
        """
        Gets the module_specs of this WorkRequest.
        The list of appstream modules being operated on.


        :return: The module_specs of this WorkRequest.
        :rtype: list[oci.os_management_hub.models.ModuleSpecDetails]
        """
        return self._module_specs

    @module_specs.setter
    def module_specs(self, module_specs):
        """
        Sets the module_specs of this WorkRequest.
        The list of appstream modules being operated on.


        :param module_specs: The module_specs of this WorkRequest.
        :type: list[oci.os_management_hub.models.ModuleSpecDetails]
        """
        self._module_specs = module_specs

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequest.
        The percentage complete of the operation tracked by this work request.


        :return: The percent_complete of this WorkRequest.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequest.
        The percentage complete of the operation tracked by this work request.


        :param percent_complete: The percent_complete of this WorkRequest.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this WorkRequest.
        The date and time the work request was created - as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this WorkRequest.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WorkRequest.
        The date and time the work request was created - as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this WorkRequest.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this WorkRequest.
        The date and time the work request was created - as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this WorkRequest.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this WorkRequest.
        The date and time the work request was created - as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this WorkRequest.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequest.
        The date and time the work request was started - as described in
        `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_started of this WorkRequest.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequest.
        The date and time the work request was started - as described in
        `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_started: The time_started of this WorkRequest.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequest.
        The date and time the work request was finished - as described in
        `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The date and time the work request was finished - as described in
        `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_finished: The time_finished of this WorkRequest.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def initiator_id(self):
        """
        Gets the initiator_id of this WorkRequest.
        The OCID of the resource that initiated the work request.


        :return: The initiator_id of this WorkRequest.
        :rtype: str
        """
        return self._initiator_id

    @initiator_id.setter
    def initiator_id(self, initiator_id):
        """
        Sets the initiator_id of this WorkRequest.
        The OCID of the resource that initiated the work request.


        :param initiator_id: The initiator_id of this WorkRequest.
        :type: str
        """
        self._initiator_id = initiator_id

    @property
    def management_station(self):
        """
        Gets the management_station of this WorkRequest.

        :return: The management_station of this WorkRequest.
        :rtype: oci.os_management_hub.models.WorkRequestManagementStationDetails
        """
        return self._management_station

    @management_station.setter
    def management_station(self, management_station):
        """
        Sets the management_station of this WorkRequest.

        :param management_station: The management_station of this WorkRequest.
        :type: oci.os_management_hub.models.WorkRequestManagementStationDetails
        """
        self._management_station = management_station

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
