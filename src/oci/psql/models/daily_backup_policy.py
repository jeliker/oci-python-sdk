# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915

from .backup_policy import BackupPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DailyBackupPolicy(BackupPolicy):
    """
    Daily backup policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DailyBackupPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.psql.models.DailyBackupPolicy.kind` attribute
        of this class is ``DAILY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this DailyBackupPolicy.
            Allowed values for this property are: "DAILY", "WEEKLY", "MONTHLY", "NONE"
        :type kind: str

        :param retention_days:
            The value to assign to the retention_days property of this DailyBackupPolicy.
        :type retention_days: int

        :param copy_policy:
            The value to assign to the copy_policy property of this DailyBackupPolicy.
        :type copy_policy: oci.psql.models.BackupCopyPolicy

        :param backup_start:
            The value to assign to the backup_start property of this DailyBackupPolicy.
        :type backup_start: str

        """
        self.swagger_types = {
            'kind': 'str',
            'retention_days': 'int',
            'copy_policy': 'BackupCopyPolicy',
            'backup_start': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'retention_days': 'retentionDays',
            'copy_policy': 'copyPolicy',
            'backup_start': 'backupStart'
        }

        self._kind = None
        self._retention_days = None
        self._copy_policy = None
        self._backup_start = None
        self._kind = 'DAILY'

    @property
    def backup_start(self):
        """
        **[Required]** Gets the backup_start of this DailyBackupPolicy.
        Hour of the day when the backup starts.


        :return: The backup_start of this DailyBackupPolicy.
        :rtype: str
        """
        return self._backup_start

    @backup_start.setter
    def backup_start(self, backup_start):
        """
        Sets the backup_start of this DailyBackupPolicy.
        Hour of the day when the backup starts.


        :param backup_start: The backup_start of this DailyBackupPolicy.
        :type: str
        """
        self._backup_start = backup_start

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
