# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupNodeDetails(object):
    """
    The information about the nodes to backup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupNodeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level_type_details:
            The value to assign to the level_type_details property of this BackupNodeDetails.
        :type level_type_details: oci.bds.models.LevelTypeDetails

        :param backup_type:
            The value to assign to the backup_type property of this BackupNodeDetails.
        :type backup_type: str

        """
        self.swagger_types = {
            'level_type_details': 'LevelTypeDetails',
            'backup_type': 'str'
        }
        self.attribute_map = {
            'level_type_details': 'levelTypeDetails',
            'backup_type': 'backupType'
        }
        self._level_type_details = None
        self._backup_type = None

    @property
    def level_type_details(self):
        """
        **[Required]** Gets the level_type_details of this BackupNodeDetails.

        :return: The level_type_details of this BackupNodeDetails.
        :rtype: oci.bds.models.LevelTypeDetails
        """
        return self._level_type_details

    @level_type_details.setter
    def level_type_details(self, level_type_details):
        """
        Sets the level_type_details of this BackupNodeDetails.

        :param level_type_details: The level_type_details of this BackupNodeDetails.
        :type: oci.bds.models.LevelTypeDetails
        """
        self._level_type_details = level_type_details

    @property
    def backup_type(self):
        """
        Gets the backup_type of this BackupNodeDetails.
        Incremental backup type includes only the changes since the last backup. Full backup type includes all changes since the volume was created.


        :return: The backup_type of this BackupNodeDetails.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this BackupNodeDetails.
        Incremental backup type includes only the changes since the last backup. Full backup type includes all changes since the volume was created.


        :param backup_type: The backup_type of this BackupNodeDetails.
        :type: str
        """
        self._backup_type = backup_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
