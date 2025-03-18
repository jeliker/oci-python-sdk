# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaintenanceWindow(object):
    """
    Maintenance Window object. It contains all the information of the Maintenance window.
    Used in the Create and Get operations.
    """

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindow.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindow.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindow.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindow.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindow.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceWindow.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_details property of a MaintenanceWindow.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_DETAILS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_details property of a MaintenanceWindow.
    #: This constant has a value of "SCHEDULED"
    LIFECYCLE_DETAILS_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the lifecycle_details property of a MaintenanceWindow.
    #: This constant has a value of "COMPLETED"
    LIFECYCLE_DETAILS_COMPLETED = "COMPLETED"

    def __init__(self, **kwargs):
        """
        Initializes a new MaintenanceWindow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MaintenanceWindow.
        :type id: str

        :param name:
            The value to assign to the name property of this MaintenanceWindow.
        :type name: str

        :param description:
            The value to assign to the description property of this MaintenanceWindow.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MaintenanceWindow.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this MaintenanceWindow.
        :type resources: list[oci.stack_monitoring.models.CreateMaintenanceWindowResourceDetails]

        :param resources_details:
            The value to assign to the resources_details property of this MaintenanceWindow.
        :type resources_details: list[oci.stack_monitoring.models.MonitoredResourceDetails]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MaintenanceWindow.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MaintenanceWindow.
            Allowed values for this property are: "IN_PROGRESS", "SCHEDULED", "COMPLETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param schedule:
            The value to assign to the schedule property of this MaintenanceWindow.
        :type schedule: oci.stack_monitoring.models.MaintenanceWindowSchedule

        :param time_created:
            The value to assign to the time_created property of this MaintenanceWindow.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MaintenanceWindow.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'resources': 'list[CreateMaintenanceWindowResourceDetails]',
            'resources_details': 'list[MonitoredResourceDetails]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'schedule': 'MaintenanceWindowSchedule',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'resources_details': 'resourcesDetails',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'schedule': 'schedule',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }
        self._id = None
        self._name = None
        self._description = None
        self._compartment_id = None
        self._resources = None
        self._resources_details = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._schedule = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MaintenanceWindow.
        The `OCID`__ of maintenance window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MaintenanceWindow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaintenanceWindow.
        The `OCID`__ of maintenance window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MaintenanceWindow.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MaintenanceWindow.
        Maintenance Window name.


        :return: The name of this MaintenanceWindow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MaintenanceWindow.
        Maintenance Window name.


        :param name: The name of this MaintenanceWindow.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this MaintenanceWindow.
        Maintenance Window description.


        :return: The description of this MaintenanceWindow.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MaintenanceWindow.
        Maintenance Window description.


        :param description: The description of this MaintenanceWindow.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MaintenanceWindow.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MaintenanceWindow.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MaintenanceWindow.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MaintenanceWindow.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        Gets the resources of this MaintenanceWindow.
        List of resource Ids which are part of the Maintenance Window


        :return: The resources of this MaintenanceWindow.
        :rtype: list[oci.stack_monitoring.models.CreateMaintenanceWindowResourceDetails]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this MaintenanceWindow.
        List of resource Ids which are part of the Maintenance Window


        :param resources: The resources of this MaintenanceWindow.
        :type: list[oci.stack_monitoring.models.CreateMaintenanceWindowResourceDetails]
        """
        self._resources = resources

    @property
    def resources_details(self):
        """
        Gets the resources_details of this MaintenanceWindow.
        List of resource details that are part of the Maintenance Window.


        :return: The resources_details of this MaintenanceWindow.
        :rtype: list[oci.stack_monitoring.models.MonitoredResourceDetails]
        """
        return self._resources_details

    @resources_details.setter
    def resources_details(self, resources_details):
        """
        Sets the resources_details of this MaintenanceWindow.
        List of resource details that are part of the Maintenance Window.


        :param resources_details: The resources_details of this MaintenanceWindow.
        :type: list[oci.stack_monitoring.models.MonitoredResourceDetails]
        """
        self._resources_details = resources_details

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MaintenanceWindow.
        Lifecycle state of the monitored resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MaintenanceWindow.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MaintenanceWindow.
        Lifecycle state of the monitored resource.


        :param lifecycle_state: The lifecycle_state of this MaintenanceWindow.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MaintenanceWindow.
        Lifecycle Details of the Maintenance Window.

        Allowed values for this property are: "IN_PROGRESS", "SCHEDULED", "COMPLETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this MaintenanceWindow.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MaintenanceWindow.
        Lifecycle Details of the Maintenance Window.


        :param lifecycle_details: The lifecycle_details of this MaintenanceWindow.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "SCHEDULED", "COMPLETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def schedule(self):
        """
        Gets the schedule of this MaintenanceWindow.

        :return: The schedule of this MaintenanceWindow.
        :rtype: oci.stack_monitoring.models.MaintenanceWindowSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this MaintenanceWindow.

        :param schedule: The schedule of this MaintenanceWindow.
        :type: oci.stack_monitoring.models.MaintenanceWindowSchedule
        """
        self._schedule = schedule

    @property
    def time_created(self):
        """
        Gets the time_created of this MaintenanceWindow.
        The time the the maintenance window was created. An RFC3339 formatted datetime string


        :return: The time_created of this MaintenanceWindow.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MaintenanceWindow.
        The time the the maintenance window was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this MaintenanceWindow.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MaintenanceWindow.
        The time the the mainteance window was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this MaintenanceWindow.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MaintenanceWindow.
        The time the the mainteance window was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this MaintenanceWindow.
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
