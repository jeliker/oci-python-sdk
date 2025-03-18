# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataGuardGroupMember(object):
    """
    The member of a Data Guard group. Represents either a PRIMARY or a STANDBY Data Guard instance.
    """

    #: A constant which can be used with the role property of a DataGuardGroupMember.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a DataGuardGroupMember.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a DataGuardGroupMember.
    #: This constant has a value of "DISABLED_STANDBY"
    ROLE_DISABLED_STANDBY = "DISABLED_STANDBY"

    #: A constant which can be used with the transport_type property of a DataGuardGroupMember.
    #: This constant has a value of "SYNC"
    TRANSPORT_TYPE_SYNC = "SYNC"

    #: A constant which can be used with the transport_type property of a DataGuardGroupMember.
    #: This constant has a value of "ASYNC"
    TRANSPORT_TYPE_ASYNC = "ASYNC"

    #: A constant which can be used with the transport_type property of a DataGuardGroupMember.
    #: This constant has a value of "FASTSYNC"
    TRANSPORT_TYPE_FASTSYNC = "FASTSYNC"

    def __init__(self, **kwargs):
        """
        Initializes a new DataGuardGroupMember object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_system_id:
            The value to assign to the db_system_id property of this DataGuardGroupMember.
        :type db_system_id: str

        :param database_id:
            The value to assign to the database_id property of this DataGuardGroupMember.
        :type database_id: str

        :param role:
            The value to assign to the role property of this DataGuardGroupMember.
            Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param apply_lag:
            The value to assign to the apply_lag property of this DataGuardGroupMember.
        :type apply_lag: str

        :param apply_rate:
            The value to assign to the apply_rate property of this DataGuardGroupMember.
        :type apply_rate: str

        :param transport_lag:
            The value to assign to the transport_lag property of this DataGuardGroupMember.
        :type transport_lag: str

        :param transport_lag_refresh:
            The value to assign to the transport_lag_refresh property of this DataGuardGroupMember.
        :type transport_lag_refresh: str

        :param transport_type:
            The value to assign to the transport_type property of this DataGuardGroupMember.
            Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type transport_type: str

        :param is_active_data_guard_enabled:
            The value to assign to the is_active_data_guard_enabled property of this DataGuardGroupMember.
        :type is_active_data_guard_enabled: bool

        """
        self.swagger_types = {
            'db_system_id': 'str',
            'database_id': 'str',
            'role': 'str',
            'apply_lag': 'str',
            'apply_rate': 'str',
            'transport_lag': 'str',
            'transport_lag_refresh': 'str',
            'transport_type': 'str',
            'is_active_data_guard_enabled': 'bool'
        }
        self.attribute_map = {
            'db_system_id': 'dbSystemId',
            'database_id': 'databaseId',
            'role': 'role',
            'apply_lag': 'applyLag',
            'apply_rate': 'applyRate',
            'transport_lag': 'transportLag',
            'transport_lag_refresh': 'transportLagRefresh',
            'transport_type': 'transportType',
            'is_active_data_guard_enabled': 'isActiveDataGuardEnabled'
        }
        self._db_system_id = None
        self._database_id = None
        self._role = None
        self._apply_lag = None
        self._apply_rate = None
        self._transport_lag = None
        self._transport_lag_refresh = None
        self._transport_type = None
        self._is_active_data_guard_enabled = None

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this DataGuardGroupMember.
        The `OCID`__ of the DB system, Cloud VM cluster or VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this DataGuardGroupMember.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this DataGuardGroupMember.
        The `OCID`__ of the DB system, Cloud VM cluster or VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this DataGuardGroupMember.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this DataGuardGroupMember.
        The `OCID`__ of the Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this DataGuardGroupMember.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this DataGuardGroupMember.
        The `OCID`__ of the Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this DataGuardGroupMember.
        :type: str
        """
        self._database_id = database_id

    @property
    def role(self):
        """
        **[Required]** Gets the role of this DataGuardGroupMember.
        The role of the reporting database in this Data Guard association.

        Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this DataGuardGroupMember.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this DataGuardGroupMember.
        The role of the reporting database in this Data Guard association.


        :param role: The role of this DataGuardGroupMember.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "DISABLED_STANDBY"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def apply_lag(self):
        """
        Gets the apply_lag of this DataGuardGroupMember.
        The lag time between updates to the primary database and application of the redo data on the standby database,
        as computed by the reporting database.

        Example: `1 second`


        :return: The apply_lag of this DataGuardGroupMember.
        :rtype: str
        """
        return self._apply_lag

    @apply_lag.setter
    def apply_lag(self, apply_lag):
        """
        Sets the apply_lag of this DataGuardGroupMember.
        The lag time between updates to the primary database and application of the redo data on the standby database,
        as computed by the reporting database.

        Example: `1 second`


        :param apply_lag: The apply_lag of this DataGuardGroupMember.
        :type: str
        """
        self._apply_lag = apply_lag

    @property
    def apply_rate(self):
        """
        Gets the apply_rate of this DataGuardGroupMember.
        The rate at which redo logs are synced between the associated databases.

        Example: `102.96 MByte/s`


        :return: The apply_rate of this DataGuardGroupMember.
        :rtype: str
        """
        return self._apply_rate

    @apply_rate.setter
    def apply_rate(self, apply_rate):
        """
        Sets the apply_rate of this DataGuardGroupMember.
        The rate at which redo logs are synced between the associated databases.

        Example: `102.96 MByte/s`


        :param apply_rate: The apply_rate of this DataGuardGroupMember.
        :type: str
        """
        self._apply_rate = apply_rate

    @property
    def transport_lag(self):
        """
        Gets the transport_lag of this DataGuardGroupMember.
        The rate at which redo logs are transported between the associated databases.

        Example: `1 second`


        :return: The transport_lag of this DataGuardGroupMember.
        :rtype: str
        """
        return self._transport_lag

    @transport_lag.setter
    def transport_lag(self, transport_lag):
        """
        Sets the transport_lag of this DataGuardGroupMember.
        The rate at which redo logs are transported between the associated databases.

        Example: `1 second`


        :param transport_lag: The transport_lag of this DataGuardGroupMember.
        :type: str
        """
        self._transport_lag = transport_lag

    @property
    def transport_lag_refresh(self):
        """
        Gets the transport_lag_refresh of this DataGuardGroupMember.
        The date and time when last redo transport has been done.


        :return: The transport_lag_refresh of this DataGuardGroupMember.
        :rtype: str
        """
        return self._transport_lag_refresh

    @transport_lag_refresh.setter
    def transport_lag_refresh(self, transport_lag_refresh):
        """
        Sets the transport_lag_refresh of this DataGuardGroupMember.
        The date and time when last redo transport has been done.


        :param transport_lag_refresh: The transport_lag_refresh of this DataGuardGroupMember.
        :type: str
        """
        self._transport_lag_refresh = transport_lag_refresh

    @property
    def transport_type(self):
        """
        Gets the transport_type of this DataGuardGroupMember.
        The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

        * MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
        * MAXIMUM_PERFORMANCE - ASYNC
        * MAXIMUM_PROTECTION - SYNC

        For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only transport type currently supported by the Database service is ASYNC.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400

        Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The transport_type of this DataGuardGroupMember.
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """
        Sets the transport_type of this DataGuardGroupMember.
        The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

        * MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
        * MAXIMUM_PERFORMANCE - ASYNC
        * MAXIMUM_PROTECTION - SYNC

        For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only transport type currently supported by the Database service is ASYNC.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400


        :param transport_type: The transport_type of this DataGuardGroupMember.
        :type: str
        """
        allowed_values = ["SYNC", "ASYNC", "FASTSYNC"]
        if not value_allowed_none_or_none_sentinel(transport_type, allowed_values):
            transport_type = 'UNKNOWN_ENUM_VALUE'
        self._transport_type = transport_type

    @property
    def is_active_data_guard_enabled(self):
        """
        Gets the is_active_data_guard_enabled of this DataGuardGroupMember.
        True if active Data Guard is enabled.


        :return: The is_active_data_guard_enabled of this DataGuardGroupMember.
        :rtype: bool
        """
        return self._is_active_data_guard_enabled

    @is_active_data_guard_enabled.setter
    def is_active_data_guard_enabled(self, is_active_data_guard_enabled):
        """
        Sets the is_active_data_guard_enabled of this DataGuardGroupMember.
        True if active Data Guard is enabled.


        :param is_active_data_guard_enabled: The is_active_data_guard_enabled of this DataGuardGroupMember.
        :type: bool
        """
        self._is_active_data_guard_enabled = is_active_data_guard_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
