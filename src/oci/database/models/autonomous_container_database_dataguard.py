# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousContainerDatabaseDataguard(object):
    """
    The properties that define Autonomous Container Databases Dataguard.
    """

    #: A constant which can be used with the role property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "DISABLED_STANDBY"
    ROLE_DISABLED_STANDBY = "DISABLED_STANDBY"

    #: A constant which can be used with the role property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "BACKUP_COPY"
    ROLE_BACKUP_COPY = "BACKUP_COPY"

    #: A constant which can be used with the role property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "SNAPSHOT_STANDBY"
    ROLE_SNAPSHOT_STANDBY = "SNAPSHOT_STANDBY"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "ROLE_CHANGE_IN_PROGRESS"
    LIFECYCLE_STATE_ROLE_CHANGE_IN_PROGRESS = "ROLE_CHANGE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the protection_mode property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "MAXIMUM_AVAILABILITY"
    PROTECTION_MODE_MAXIMUM_AVAILABILITY = "MAXIMUM_AVAILABILITY"

    #: A constant which can be used with the protection_mode property of a AutonomousContainerDatabaseDataguard.
    #: This constant has a value of "MAXIMUM_PERFORMANCE"
    PROTECTION_MODE_MAXIMUM_PERFORMANCE = "MAXIMUM_PERFORMANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousContainerDatabaseDataguard object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this AutonomousContainerDatabaseDataguard.
        :type autonomous_container_database_id: str

        :param role:
            The value to assign to the role property of this AutonomousContainerDatabaseDataguard.
            Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", "BACKUP_COPY", "SNAPSHOT_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousContainerDatabaseDataguard.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousContainerDatabaseDataguard.
        :type lifecycle_details: str

        :param protection_mode:
            The value to assign to the protection_mode property of this AutonomousContainerDatabaseDataguard.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protection_mode: str

        :param fast_start_fail_over_lag_limit_in_seconds:
            The value to assign to the fast_start_fail_over_lag_limit_in_seconds property of this AutonomousContainerDatabaseDataguard.
        :type fast_start_fail_over_lag_limit_in_seconds: int

        :param apply_lag:
            The value to assign to the apply_lag property of this AutonomousContainerDatabaseDataguard.
        :type apply_lag: str

        :param apply_rate:
            The value to assign to the apply_rate property of this AutonomousContainerDatabaseDataguard.
        :type apply_rate: str

        :param is_automatic_failover_enabled:
            The value to assign to the is_automatic_failover_enabled property of this AutonomousContainerDatabaseDataguard.
        :type is_automatic_failover_enabled: bool

        :param transport_lag:
            The value to assign to the transport_lag property of this AutonomousContainerDatabaseDataguard.
        :type transport_lag: str

        :param time_last_synced:
            The value to assign to the time_last_synced property of this AutonomousContainerDatabaseDataguard.
        :type time_last_synced: datetime

        :param time_created:
            The value to assign to the time_created property of this AutonomousContainerDatabaseDataguard.
        :type time_created: datetime

        :param time_last_role_changed:
            The value to assign to the time_last_role_changed property of this AutonomousContainerDatabaseDataguard.
        :type time_last_role_changed: datetime

        :param availability_domain:
            The value to assign to the availability_domain property of this AutonomousContainerDatabaseDataguard.
        :type availability_domain: str

        :param time_lag_refreshed_on:
            The value to assign to the time_lag_refreshed_on property of this AutonomousContainerDatabaseDataguard.
        :type time_lag_refreshed_on: datetime

        :param redo_transport_mode:
            The value to assign to the redo_transport_mode property of this AutonomousContainerDatabaseDataguard.
        :type redo_transport_mode: str

        :param automatic_failover_target:
            The value to assign to the automatic_failover_target property of this AutonomousContainerDatabaseDataguard.
        :type automatic_failover_target: str

        """
        self.swagger_types = {
            'autonomous_container_database_id': 'str',
            'role': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'protection_mode': 'str',
            'fast_start_fail_over_lag_limit_in_seconds': 'int',
            'apply_lag': 'str',
            'apply_rate': 'str',
            'is_automatic_failover_enabled': 'bool',
            'transport_lag': 'str',
            'time_last_synced': 'datetime',
            'time_created': 'datetime',
            'time_last_role_changed': 'datetime',
            'availability_domain': 'str',
            'time_lag_refreshed_on': 'datetime',
            'redo_transport_mode': 'str',
            'automatic_failover_target': 'str'
        }

        self.attribute_map = {
            'autonomous_container_database_id': 'autonomousContainerDatabaseId',
            'role': 'role',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'protection_mode': 'protectionMode',
            'fast_start_fail_over_lag_limit_in_seconds': 'fastStartFailOverLagLimitInSeconds',
            'apply_lag': 'applyLag',
            'apply_rate': 'applyRate',
            'is_automatic_failover_enabled': 'isAutomaticFailoverEnabled',
            'transport_lag': 'transportLag',
            'time_last_synced': 'timeLastSynced',
            'time_created': 'timeCreated',
            'time_last_role_changed': 'timeLastRoleChanged',
            'availability_domain': 'availabilityDomain',
            'time_lag_refreshed_on': 'timeLagRefreshedOn',
            'redo_transport_mode': 'redoTransportMode',
            'automatic_failover_target': 'automaticFailoverTarget'
        }

        self._autonomous_container_database_id = None
        self._role = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._protection_mode = None
        self._fast_start_fail_over_lag_limit_in_seconds = None
        self._apply_lag = None
        self._apply_rate = None
        self._is_automatic_failover_enabled = None
        self._transport_lag = None
        self._time_last_synced = None
        self._time_created = None
        self._time_last_role_changed = None
        self._availability_domain = None
        self._time_lag_refreshed_on = None
        self._redo_transport_mode = None
        self._automatic_failover_target = None

    @property
    def autonomous_container_database_id(self):
        """
        **[Required]** Gets the autonomous_container_database_id of this AutonomousContainerDatabaseDataguard.
        The `OCID`__ of the Autonomous Container Database that has a relationship with the peer Autonomous Container Database. Used only by Autonomous Database on Dedicated Exadata Infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_container_database_id of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._autonomous_container_database_id

    @autonomous_container_database_id.setter
    def autonomous_container_database_id(self, autonomous_container_database_id):
        """
        Sets the autonomous_container_database_id of this AutonomousContainerDatabaseDataguard.
        The `OCID`__ of the Autonomous Container Database that has a relationship with the peer Autonomous Container Database. Used only by Autonomous Database on Dedicated Exadata Infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_container_database_id: The autonomous_container_database_id of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        self._autonomous_container_database_id = autonomous_container_database_id

    @property
    def role(self):
        """
        **[Required]** Gets the role of this AutonomousContainerDatabaseDataguard.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

        Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", "BACKUP_COPY", "SNAPSHOT_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this AutonomousContainerDatabaseDataguard.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.


        :param role: The role of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "DISABLED_STANDBY", "BACKUP_COPY", "SNAPSHOT_STANDBY"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousContainerDatabaseDataguard.
        The current state of Autonomous Data Guard.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousContainerDatabaseDataguard.
        The current state of Autonomous Data Guard.


        :param lifecycle_state: The lifecycle_state of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousContainerDatabaseDataguard.
        Additional information about the current lifecycleState, if available.


        :return: The lifecycle_details of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousContainerDatabaseDataguard.
        Additional information about the current lifecycleState, if available.


        :param lifecycle_details: The lifecycle_details of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this AutonomousContainerDatabaseDataguard.
        The protection mode of this Autonomous Data Guard association. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000

        Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protection_mode of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this AutonomousContainerDatabaseDataguard.
        The protection mode of this Autonomous Data Guard association. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000


        :param protection_mode: The protection_mode of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        allowed_values = ["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            protection_mode = 'UNKNOWN_ENUM_VALUE'
        self._protection_mode = protection_mode

    @property
    def fast_start_fail_over_lag_limit_in_seconds(self):
        """
        Gets the fast_start_fail_over_lag_limit_in_seconds of this AutonomousContainerDatabaseDataguard.
        The lag time for my preference based on data loss tolerance in seconds.


        :return: The fast_start_fail_over_lag_limit_in_seconds of this AutonomousContainerDatabaseDataguard.
        :rtype: int
        """
        return self._fast_start_fail_over_lag_limit_in_seconds

    @fast_start_fail_over_lag_limit_in_seconds.setter
    def fast_start_fail_over_lag_limit_in_seconds(self, fast_start_fail_over_lag_limit_in_seconds):
        """
        Sets the fast_start_fail_over_lag_limit_in_seconds of this AutonomousContainerDatabaseDataguard.
        The lag time for my preference based on data loss tolerance in seconds.


        :param fast_start_fail_over_lag_limit_in_seconds: The fast_start_fail_over_lag_limit_in_seconds of this AutonomousContainerDatabaseDataguard.
        :type: int
        """
        self._fast_start_fail_over_lag_limit_in_seconds = fast_start_fail_over_lag_limit_in_seconds

    @property
    def apply_lag(self):
        """
        Gets the apply_lag of this AutonomousContainerDatabaseDataguard.
        The lag time between updates to the primary Autonomous Container Database and application of the redo data on the standby Autonomous Container Database,
        as computed by the reporting database.
        Example: `9 seconds`


        :return: The apply_lag of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._apply_lag

    @apply_lag.setter
    def apply_lag(self, apply_lag):
        """
        Sets the apply_lag of this AutonomousContainerDatabaseDataguard.
        The lag time between updates to the primary Autonomous Container Database and application of the redo data on the standby Autonomous Container Database,
        as computed by the reporting database.
        Example: `9 seconds`


        :param apply_lag: The apply_lag of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        self._apply_lag = apply_lag

    @property
    def apply_rate(self):
        """
        Gets the apply_rate of this AutonomousContainerDatabaseDataguard.
        The rate at which redo logs are synchronized between the associated Autonomous Container Databases.
        Example: `180 Mb per second`


        :return: The apply_rate of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._apply_rate

    @apply_rate.setter
    def apply_rate(self, apply_rate):
        """
        Sets the apply_rate of this AutonomousContainerDatabaseDataguard.
        The rate at which redo logs are synchronized between the associated Autonomous Container Databases.
        Example: `180 Mb per second`


        :param apply_rate: The apply_rate of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        self._apply_rate = apply_rate

    @property
    def is_automatic_failover_enabled(self):
        """
        Gets the is_automatic_failover_enabled of this AutonomousContainerDatabaseDataguard.
        Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association


        :return: The is_automatic_failover_enabled of this AutonomousContainerDatabaseDataguard.
        :rtype: bool
        """
        return self._is_automatic_failover_enabled

    @is_automatic_failover_enabled.setter
    def is_automatic_failover_enabled(self, is_automatic_failover_enabled):
        """
        Sets the is_automatic_failover_enabled of this AutonomousContainerDatabaseDataguard.
        Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association


        :param is_automatic_failover_enabled: The is_automatic_failover_enabled of this AutonomousContainerDatabaseDataguard.
        :type: bool
        """
        self._is_automatic_failover_enabled = is_automatic_failover_enabled

    @property
    def transport_lag(self):
        """
        Gets the transport_lag of this AutonomousContainerDatabaseDataguard.
        The approximate number of seconds of redo data not yet available on the standby Autonomous Container Database,
        as computed by the reporting database.
        Example: `7 seconds`


        :return: The transport_lag of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._transport_lag

    @transport_lag.setter
    def transport_lag(self, transport_lag):
        """
        Sets the transport_lag of this AutonomousContainerDatabaseDataguard.
        The approximate number of seconds of redo data not yet available on the standby Autonomous Container Database,
        as computed by the reporting database.
        Example: `7 seconds`


        :param transport_lag: The transport_lag of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        self._transport_lag = transport_lag

    @property
    def time_last_synced(self):
        """
        Gets the time_last_synced of this AutonomousContainerDatabaseDataguard.
        The date and time of the last update to the apply lag, apply rate, and transport lag values.


        :return: The time_last_synced of this AutonomousContainerDatabaseDataguard.
        :rtype: datetime
        """
        return self._time_last_synced

    @time_last_synced.setter
    def time_last_synced(self, time_last_synced):
        """
        Sets the time_last_synced of this AutonomousContainerDatabaseDataguard.
        The date and time of the last update to the apply lag, apply rate, and transport lag values.


        :param time_last_synced: The time_last_synced of this AutonomousContainerDatabaseDataguard.
        :type: datetime
        """
        self._time_last_synced = time_last_synced

    @property
    def time_created(self):
        """
        Gets the time_created of this AutonomousContainerDatabaseDataguard.
        The date and time the Autonomous DataGuard association was created.


        :return: The time_created of this AutonomousContainerDatabaseDataguard.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutonomousContainerDatabaseDataguard.
        The date and time the Autonomous DataGuard association was created.


        :param time_created: The time_created of this AutonomousContainerDatabaseDataguard.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_role_changed(self):
        """
        Gets the time_last_role_changed of this AutonomousContainerDatabaseDataguard.
        The date and time when the last role change action happened.


        :return: The time_last_role_changed of this AutonomousContainerDatabaseDataguard.
        :rtype: datetime
        """
        return self._time_last_role_changed

    @time_last_role_changed.setter
    def time_last_role_changed(self, time_last_role_changed):
        """
        Sets the time_last_role_changed of this AutonomousContainerDatabaseDataguard.
        The date and time when the last role change action happened.


        :param time_last_role_changed: The time_last_role_changed of this AutonomousContainerDatabaseDataguard.
        :type: datetime
        """
        self._time_last_role_changed = time_last_role_changed

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this AutonomousContainerDatabaseDataguard.
        The domain of the Autonomous Container Database


        :return: The availability_domain of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this AutonomousContainerDatabaseDataguard.
        The domain of the Autonomous Container Database


        :param availability_domain: The availability_domain of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def time_lag_refreshed_on(self):
        """
        Gets the time_lag_refreshed_on of this AutonomousContainerDatabaseDataguard.
        Timestamp when the lags were last calculated for a standby.


        :return: The time_lag_refreshed_on of this AutonomousContainerDatabaseDataguard.
        :rtype: datetime
        """
        return self._time_lag_refreshed_on

    @time_lag_refreshed_on.setter
    def time_lag_refreshed_on(self, time_lag_refreshed_on):
        """
        Sets the time_lag_refreshed_on of this AutonomousContainerDatabaseDataguard.
        Timestamp when the lags were last calculated for a standby.


        :param time_lag_refreshed_on: The time_lag_refreshed_on of this AutonomousContainerDatabaseDataguard.
        :type: datetime
        """
        self._time_lag_refreshed_on = time_lag_refreshed_on

    @property
    def redo_transport_mode(self):
        """
        Gets the redo_transport_mode of this AutonomousContainerDatabaseDataguard.
        Automatically selected by backend based on the protection mode.


        :return: The redo_transport_mode of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._redo_transport_mode

    @redo_transport_mode.setter
    def redo_transport_mode(self, redo_transport_mode):
        """
        Sets the redo_transport_mode of this AutonomousContainerDatabaseDataguard.
        Automatically selected by backend based on the protection mode.


        :param redo_transport_mode: The redo_transport_mode of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        self._redo_transport_mode = redo_transport_mode

    @property
    def automatic_failover_target(self):
        """
        Gets the automatic_failover_target of this AutonomousContainerDatabaseDataguard.
        Automatically selected by backend when observer is enabled.


        :return: The automatic_failover_target of this AutonomousContainerDatabaseDataguard.
        :rtype: str
        """
        return self._automatic_failover_target

    @automatic_failover_target.setter
    def automatic_failover_target(self, automatic_failover_target):
        """
        Sets the automatic_failover_target of this AutonomousContainerDatabaseDataguard.
        Automatically selected by backend when observer is enabled.


        :param automatic_failover_target: The automatic_failover_target of this AutonomousContainerDatabaseDataguard.
        :type: str
        """
        self._automatic_failover_target = automatic_failover_target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
