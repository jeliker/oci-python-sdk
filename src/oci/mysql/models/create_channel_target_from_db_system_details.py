# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_channel_target_details import CreateChannelTargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateChannelTargetFromDbSystemDetails(CreateChannelTargetDetails):
    """
    Parameters detailing how to provision the target endpoint that is a DB System.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateChannelTargetFromDbSystemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.CreateChannelTargetFromDbSystemDetails.target_type` attribute
        of this class is ``DBSYSTEM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this CreateChannelTargetFromDbSystemDetails.
        :type target_type: str

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateChannelTargetFromDbSystemDetails.
        :type db_system_id: str

        :param channel_name:
            The value to assign to the channel_name property of this CreateChannelTargetFromDbSystemDetails.
        :type channel_name: str

        :param applier_username:
            The value to assign to the applier_username property of this CreateChannelTargetFromDbSystemDetails.
        :type applier_username: str

        :param filters:
            The value to assign to the filters property of this CreateChannelTargetFromDbSystemDetails.
        :type filters: list[oci.mysql.models.ChannelFilter]

        :param tables_without_primary_key_handling:
            The value to assign to the tables_without_primary_key_handling property of this CreateChannelTargetFromDbSystemDetails.
        :type tables_without_primary_key_handling: str

        :param delay_in_seconds:
            The value to assign to the delay_in_seconds property of this CreateChannelTargetFromDbSystemDetails.
        :type delay_in_seconds: int

        """
        self.swagger_types = {
            'target_type': 'str',
            'db_system_id': 'str',
            'channel_name': 'str',
            'applier_username': 'str',
            'filters': 'list[ChannelFilter]',
            'tables_without_primary_key_handling': 'str',
            'delay_in_seconds': 'int'
        }

        self.attribute_map = {
            'target_type': 'targetType',
            'db_system_id': 'dbSystemId',
            'channel_name': 'channelName',
            'applier_username': 'applierUsername',
            'filters': 'filters',
            'tables_without_primary_key_handling': 'tablesWithoutPrimaryKeyHandling',
            'delay_in_seconds': 'delayInSeconds'
        }

        self._target_type = None
        self._db_system_id = None
        self._channel_name = None
        self._applier_username = None
        self._filters = None
        self._tables_without_primary_key_handling = None
        self._delay_in_seconds = None
        self._target_type = 'DBSYSTEM'

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this CreateChannelTargetFromDbSystemDetails.
        The OCID of the target DB System.


        :return: The db_system_id of this CreateChannelTargetFromDbSystemDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this CreateChannelTargetFromDbSystemDetails.
        The OCID of the target DB System.


        :param db_system_id: The db_system_id of this CreateChannelTargetFromDbSystemDetails.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def channel_name(self):
        """
        Gets the channel_name of this CreateChannelTargetFromDbSystemDetails.
        The case-insensitive name that identifies the replication channel. Channel names
        must follow the rules defined for `MySQL identifiers`__.
        The names of non-Deleted Channels must be unique for each DB System.

        __ https://dev.mysql.com/doc/refman/8.0/en/identifiers.html


        :return: The channel_name of this CreateChannelTargetFromDbSystemDetails.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """
        Sets the channel_name of this CreateChannelTargetFromDbSystemDetails.
        The case-insensitive name that identifies the replication channel. Channel names
        must follow the rules defined for `MySQL identifiers`__.
        The names of non-Deleted Channels must be unique for each DB System.

        __ https://dev.mysql.com/doc/refman/8.0/en/identifiers.html


        :param channel_name: The channel_name of this CreateChannelTargetFromDbSystemDetails.
        :type: str
        """
        self._channel_name = channel_name

    @property
    def applier_username(self):
        """
        Gets the applier_username of this CreateChannelTargetFromDbSystemDetails.
        The username for the replication applier of the target MySQL DB System.


        :return: The applier_username of this CreateChannelTargetFromDbSystemDetails.
        :rtype: str
        """
        return self._applier_username

    @applier_username.setter
    def applier_username(self, applier_username):
        """
        Sets the applier_username of this CreateChannelTargetFromDbSystemDetails.
        The username for the replication applier of the target MySQL DB System.


        :param applier_username: The applier_username of this CreateChannelTargetFromDbSystemDetails.
        :type: str
        """
        self._applier_username = applier_username

    @property
    def filters(self):
        """
        Gets the filters of this CreateChannelTargetFromDbSystemDetails.
        Replication filter rules to be applied at the DB System Channel target.


        :return: The filters of this CreateChannelTargetFromDbSystemDetails.
        :rtype: list[oci.mysql.models.ChannelFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this CreateChannelTargetFromDbSystemDetails.
        Replication filter rules to be applied at the DB System Channel target.


        :param filters: The filters of this CreateChannelTargetFromDbSystemDetails.
        :type: list[oci.mysql.models.ChannelFilter]
        """
        self._filters = filters

    @property
    def tables_without_primary_key_handling(self):
        """
        Gets the tables_without_primary_key_handling of this CreateChannelTargetFromDbSystemDetails.
        Specifies how a replication channel handles the creation and alteration of tables
        that do not have a primary key. The default value is set to ALLOW.


        :return: The tables_without_primary_key_handling of this CreateChannelTargetFromDbSystemDetails.
        :rtype: str
        """
        return self._tables_without_primary_key_handling

    @tables_without_primary_key_handling.setter
    def tables_without_primary_key_handling(self, tables_without_primary_key_handling):
        """
        Sets the tables_without_primary_key_handling of this CreateChannelTargetFromDbSystemDetails.
        Specifies how a replication channel handles the creation and alteration of tables
        that do not have a primary key. The default value is set to ALLOW.


        :param tables_without_primary_key_handling: The tables_without_primary_key_handling of this CreateChannelTargetFromDbSystemDetails.
        :type: str
        """
        self._tables_without_primary_key_handling = tables_without_primary_key_handling

    @property
    def delay_in_seconds(self):
        """
        Gets the delay_in_seconds of this CreateChannelTargetFromDbSystemDetails.
        Specifies the amount of time, in seconds, that the channel waits before
        applying a transaction received from the source.


        :return: The delay_in_seconds of this CreateChannelTargetFromDbSystemDetails.
        :rtype: int
        """
        return self._delay_in_seconds

    @delay_in_seconds.setter
    def delay_in_seconds(self, delay_in_seconds):
        """
        Sets the delay_in_seconds of this CreateChannelTargetFromDbSystemDetails.
        Specifies the amount of time, in seconds, that the channel waits before
        applying a transaction received from the source.


        :param delay_in_seconds: The delay_in_seconds of this CreateChannelTargetFromDbSystemDetails.
        :type: int
        """
        self._delay_in_seconds = delay_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
