# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleSummary(object):
    """
    This is the summary information about a schedule.
    """

    #: A constant which can be used with the action property of a ScheduleSummary.
    #: This constant has a value of "START_RESOURCE"
    ACTION_START_RESOURCE = "START_RESOURCE"

    #: A constant which can be used with the action property of a ScheduleSummary.
    #: This constant has a value of "STOP_RESOURCE"
    ACTION_STOP_RESOURCE = "STOP_RESOURCE"

    #: A constant which can be used with the recurrence_type property of a ScheduleSummary.
    #: This constant has a value of "CRON"
    RECURRENCE_TYPE_CRON = "CRON"

    #: A constant which can be used with the recurrence_type property of a ScheduleSummary.
    #: This constant has a value of "ICAL"
    RECURRENCE_TYPE_ICAL = "ICAL"

    #: A constant which can be used with the last_run_status property of a ScheduleSummary.
    #: This constant has a value of "ACCEPTED"
    LAST_RUN_STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the last_run_status property of a ScheduleSummary.
    #: This constant has a value of "IN_PROGRESS"
    LAST_RUN_STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the last_run_status property of a ScheduleSummary.
    #: This constant has a value of "WAITING"
    LAST_RUN_STATUS_WAITING = "WAITING"

    #: A constant which can be used with the last_run_status property of a ScheduleSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LAST_RUN_STATUS_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the last_run_status property of a ScheduleSummary.
    #: This constant has a value of "FAILED"
    LAST_RUN_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the last_run_status property of a ScheduleSummary.
    #: This constant has a value of "SUCCEEDED"
    LAST_RUN_STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the last_run_status property of a ScheduleSummary.
    #: This constant has a value of "CANCELING"
    LAST_RUN_STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the last_run_status property of a ScheduleSummary.
    #: This constant has a value of "CANCELED"
    LAST_RUN_STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduleSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ScheduleSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduleSummary.
        :type display_name: str

        :param action:
            The value to assign to the action property of this ScheduleSummary.
            Allowed values for this property are: "START_RESOURCE", "STOP_RESOURCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param description:
            The value to assign to the description property of this ScheduleSummary.
        :type description: str

        :param recurrence_details:
            The value to assign to the recurrence_details property of this ScheduleSummary.
        :type recurrence_details: str

        :param recurrence_type:
            The value to assign to the recurrence_type property of this ScheduleSummary.
            Allowed values for this property are: "CRON", "ICAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type recurrence_type: str

        :param resource_filters:
            The value to assign to the resource_filters property of this ScheduleSummary.
        :type resource_filters: list[oci.resource_scheduler.models.ResourceFilter]

        :param resources:
            The value to assign to the resources property of this ScheduleSummary.
        :type resources: list[oci.resource_scheduler.models.Resource]

        :param time_starts:
            The value to assign to the time_starts property of this ScheduleSummary.
        :type time_starts: datetime

        :param time_ends:
            The value to assign to the time_ends property of this ScheduleSummary.
        :type time_ends: datetime

        :param time_created:
            The value to assign to the time_created property of this ScheduleSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ScheduleSummary.
        :type time_updated: datetime

        :param time_last_run:
            The value to assign to the time_last_run property of this ScheduleSummary.
        :type time_last_run: datetime

        :param time_next_run:
            The value to assign to the time_next_run property of this ScheduleSummary.
        :type time_next_run: datetime

        :param last_run_status:
            The value to assign to the last_run_status property of this ScheduleSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "NEEDS_ATTENTION", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_run_status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduleSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduleSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduleSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ScheduleSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'action': 'str',
            'description': 'str',
            'recurrence_details': 'str',
            'recurrence_type': 'str',
            'resource_filters': 'list[ResourceFilter]',
            'resources': 'list[Resource]',
            'time_starts': 'datetime',
            'time_ends': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_run': 'datetime',
            'time_next_run': 'datetime',
            'last_run_status': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'action': 'action',
            'description': 'description',
            'recurrence_details': 'recurrenceDetails',
            'recurrence_type': 'recurrenceType',
            'resource_filters': 'resourceFilters',
            'resources': 'resources',
            'time_starts': 'timeStarts',
            'time_ends': 'timeEnds',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_run': 'timeLastRun',
            'time_next_run': 'timeNextRun',
            'last_run_status': 'lastRunStatus',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._action = None
        self._description = None
        self._recurrence_details = None
        self._recurrence_type = None
        self._resource_filters = None
        self._resources = None
        self._time_starts = None
        self._time_ends = None
        self._time_created = None
        self._time_updated = None
        self._time_last_run = None
        self._time_next_run = None
        self._last_run_status = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduleSummary.
        The `OCID`__ of the schedule

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ScheduleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduleSummary.
        The `OCID`__ of the schedule

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ScheduleSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ScheduleSummary.
        The `OCID`__ of the compartment in which the schedule is created

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ScheduleSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScheduleSummary.
        The `OCID`__ of the compartment in which the schedule is created

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ScheduleSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScheduleSummary.
        This is a user-friendly name for the schedule. It does not have to be unique, and it's changeable.


        :return: The display_name of this ScheduleSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduleSummary.
        This is a user-friendly name for the schedule. It does not have to be unique, and it's changeable.


        :param display_name: The display_name of this ScheduleSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ScheduleSummary.
        This is the action that will be executed by the schedule.

        Allowed values for this property are: "START_RESOURCE", "STOP_RESOURCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this ScheduleSummary.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ScheduleSummary.
        This is the action that will be executed by the schedule.


        :param action: The action of this ScheduleSummary.
        :type: str
        """
        allowed_values = ["START_RESOURCE", "STOP_RESOURCE"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def description(self):
        """
        Gets the description of this ScheduleSummary.
        This is the description of the schedule.


        :return: The description of this ScheduleSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScheduleSummary.
        This is the description of the schedule.


        :param description: The description of this ScheduleSummary.
        :type: str
        """
        self._description = description

    @property
    def recurrence_details(self):
        """
        **[Required]** Gets the recurrence_details of this ScheduleSummary.
        This is the frequency of recurrence of a schedule. The frequency field can either conform to RFC-5545 formatting
        or UNIX cron formatting for recurrences, based on the value specified by the recurrenceType field.


        :return: The recurrence_details of this ScheduleSummary.
        :rtype: str
        """
        return self._recurrence_details

    @recurrence_details.setter
    def recurrence_details(self, recurrence_details):
        """
        Sets the recurrence_details of this ScheduleSummary.
        This is the frequency of recurrence of a schedule. The frequency field can either conform to RFC-5545 formatting
        or UNIX cron formatting for recurrences, based on the value specified by the recurrenceType field.


        :param recurrence_details: The recurrence_details of this ScheduleSummary.
        :type: str
        """
        self._recurrence_details = recurrence_details

    @property
    def recurrence_type(self):
        """
        **[Required]** Gets the recurrence_type of this ScheduleSummary.
        Type of recurrence of a schedule

        Allowed values for this property are: "CRON", "ICAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The recurrence_type of this ScheduleSummary.
        :rtype: str
        """
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, recurrence_type):
        """
        Sets the recurrence_type of this ScheduleSummary.
        Type of recurrence of a schedule


        :param recurrence_type: The recurrence_type of this ScheduleSummary.
        :type: str
        """
        allowed_values = ["CRON", "ICAL"]
        if not value_allowed_none_or_none_sentinel(recurrence_type, allowed_values):
            recurrence_type = 'UNKNOWN_ENUM_VALUE'
        self._recurrence_type = recurrence_type

    @property
    def resource_filters(self):
        """
        Gets the resource_filters of this ScheduleSummary.
        This is a list of resources filters.  The schedule will be applied to resources matching all of them.


        :return: The resource_filters of this ScheduleSummary.
        :rtype: list[oci.resource_scheduler.models.ResourceFilter]
        """
        return self._resource_filters

    @resource_filters.setter
    def resource_filters(self, resource_filters):
        """
        Sets the resource_filters of this ScheduleSummary.
        This is a list of resources filters.  The schedule will be applied to resources matching all of them.


        :param resource_filters: The resource_filters of this ScheduleSummary.
        :type: list[oci.resource_scheduler.models.ResourceFilter]
        """
        self._resource_filters = resource_filters

    @property
    def resources(self):
        """
        Gets the resources of this ScheduleSummary.
        This is the list of resources to which the scheduled operation is applied.


        :return: The resources of this ScheduleSummary.
        :rtype: list[oci.resource_scheduler.models.Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this ScheduleSummary.
        This is the list of resources to which the scheduled operation is applied.


        :param resources: The resources of this ScheduleSummary.
        :type: list[oci.resource_scheduler.models.Resource]
        """
        self._resources = resources

    @property
    def time_starts(self):
        """
        Gets the time_starts of this ScheduleSummary.
        This is the date and time the schedule starts, in the format defined by `RFC 3339`__

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_starts of this ScheduleSummary.
        :rtype: datetime
        """
        return self._time_starts

    @time_starts.setter
    def time_starts(self, time_starts):
        """
        Sets the time_starts of this ScheduleSummary.
        This is the date and time the schedule starts, in the format defined by `RFC 3339`__

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_starts: The time_starts of this ScheduleSummary.
        :type: datetime
        """
        self._time_starts = time_starts

    @property
    def time_ends(self):
        """
        Gets the time_ends of this ScheduleSummary.
        This is the date and time the schedule ends, in the format defined by `RFC 3339`__

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_ends of this ScheduleSummary.
        :rtype: datetime
        """
        return self._time_ends

    @time_ends.setter
    def time_ends(self, time_ends):
        """
        Sets the time_ends of this ScheduleSummary.
        This is the date and time the schedule ends, in the format defined by `RFC 3339`__

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_ends: The time_ends of this ScheduleSummary.
        :type: datetime
        """
        self._time_ends = time_ends

    @property
    def time_created(self):
        """
        Gets the time_created of this ScheduleSummary.
        This is the date and time the schedule was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ScheduleSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ScheduleSummary.
        This is the date and time the schedule was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ScheduleSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ScheduleSummary.
        This is the date and time the schedule was updated, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ScheduleSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ScheduleSummary.
        This is the date and time the schedule was updated, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ScheduleSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_run(self):
        """
        Gets the time_last_run of this ScheduleSummary.
        This is the date and time the schedule runs last time, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_run of this ScheduleSummary.
        :rtype: datetime
        """
        return self._time_last_run

    @time_last_run.setter
    def time_last_run(self, time_last_run):
        """
        Sets the time_last_run of this ScheduleSummary.
        This is the date and time the schedule runs last time, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_run: The time_last_run of this ScheduleSummary.
        :type: datetime
        """
        self._time_last_run = time_last_run

    @property
    def time_next_run(self):
        """
        Gets the time_next_run of this ScheduleSummary.
        This is the date and time the schedule run the next time, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_next_run of this ScheduleSummary.
        :rtype: datetime
        """
        return self._time_next_run

    @time_next_run.setter
    def time_next_run(self, time_next_run):
        """
        Sets the time_next_run of this ScheduleSummary.
        This is the date and time the schedule run the next time, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_next_run: The time_next_run of this ScheduleSummary.
        :type: datetime
        """
        self._time_next_run = time_next_run

    @property
    def last_run_status(self):
        """
        Gets the last_run_status of this ScheduleSummary.
        This is the status of the last work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "NEEDS_ATTENTION", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_run_status of this ScheduleSummary.
        :rtype: str
        """
        return self._last_run_status

    @last_run_status.setter
    def last_run_status(self, last_run_status):
        """
        Sets the last_run_status of this ScheduleSummary.
        This is the status of the last work request.


        :param last_run_status: The last_run_status of this ScheduleSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "WAITING", "NEEDS_ATTENTION", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(last_run_status, allowed_values):
            last_run_status = 'UNKNOWN_ENUM_VALUE'
        self._last_run_status = last_run_status

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ScheduleSummary.
        This is the current state of the schedule.


        :return: The lifecycle_state of this ScheduleSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduleSummary.
        This is the current state of the schedule.


        :param lifecycle_state: The lifecycle_state of this ScheduleSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScheduleSummary.
        These are free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ScheduleSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduleSummary.
        These are free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ScheduleSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScheduleSummary.
        These are defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ScheduleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduleSummary.
        These are defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ScheduleSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ScheduleSummary.
        These are system tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ScheduleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ScheduleSummary.
        These are system tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ScheduleSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
