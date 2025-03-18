# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .migration import Migration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleMigration(Migration):
    """
    Oracle Migration resource
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleMigration object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.OracleMigration.database_combination` attribute
        of this class is ``ORACLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OracleMigration.
        :type id: str

        :param description:
            The value to assign to the description property of this OracleMigration.
        :type description: str

        :param database_combination:
            The value to assign to the database_combination property of this OracleMigration.
            Allowed values for this property are: "MYSQL", "ORACLE"
        :type database_combination: str

        :param display_name:
            The value to assign to the display_name property of this OracleMigration.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OracleMigration.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this OracleMigration.
            Allowed values for this property are: "ONLINE", "OFFLINE"
        :type type: str

        :param wait_after:
            The value to assign to the wait_after property of this OracleMigration.
            Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_FETCH_METADATA_SRC", "ODMS_FETCH_METADATA_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIALIZE_REPLICATION_INFRASTRUCTURE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_EXPORT_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"
        :type wait_after: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this OracleMigration.
        :type source_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this OracleMigration.
        :type target_database_connection_id: str

        :param executing_job_id:
            The value to assign to the executing_job_id property of this OracleMigration.
        :type executing_job_id: str

        :param time_created:
            The value to assign to the time_created property of this OracleMigration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OracleMigration.
        :type time_updated: datetime

        :param time_last_migration:
            The value to assign to the time_last_migration property of this OracleMigration.
        :type time_last_migration: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OracleMigration.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OracleMigration.
            Allowed values for this property are: "READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE"
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OracleMigration.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OracleMigration.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OracleMigration.
        :type system_tags: dict(str, dict(str, object))

        :param data_transfer_medium_details:
            The value to assign to the data_transfer_medium_details property of this OracleMigration.
        :type data_transfer_medium_details: oci.database_migration.models.OracleDataTransferMediumDetails

        :param initial_load_settings:
            The value to assign to the initial_load_settings property of this OracleMigration.
        :type initial_load_settings: oci.database_migration.models.OracleInitialLoadSettings

        :param advisor_settings:
            The value to assign to the advisor_settings property of this OracleMigration.
        :type advisor_settings: oci.database_migration.models.OracleAdvisorSettings

        :param hub_details:
            The value to assign to the hub_details property of this OracleMigration.
        :type hub_details: oci.database_migration.models.GoldenGateHubDetails

        :param ggs_details:
            The value to assign to the ggs_details property of this OracleMigration.
        :type ggs_details: oci.database_migration.models.OracleGgsDeploymentDetails

        :param source_container_database_connection_id:
            The value to assign to the source_container_database_connection_id property of this OracleMigration.
        :type source_container_database_connection_id: str

        :param advanced_parameters:
            The value to assign to the advanced_parameters property of this OracleMigration.
        :type advanced_parameters: list[oci.database_migration.models.MigrationParameterDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'database_combination': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'wait_after': 'str',
            'source_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'executing_job_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_migration': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'data_transfer_medium_details': 'OracleDataTransferMediumDetails',
            'initial_load_settings': 'OracleInitialLoadSettings',
            'advisor_settings': 'OracleAdvisorSettings',
            'hub_details': 'GoldenGateHubDetails',
            'ggs_details': 'OracleGgsDeploymentDetails',
            'source_container_database_connection_id': 'str',
            'advanced_parameters': 'list[MigrationParameterDetails]'
        }
        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'database_combination': 'databaseCombination',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'wait_after': 'waitAfter',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'executing_job_id': 'executingJobId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_migration': 'timeLastMigration',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'data_transfer_medium_details': 'dataTransferMediumDetails',
            'initial_load_settings': 'initialLoadSettings',
            'advisor_settings': 'advisorSettings',
            'hub_details': 'hubDetails',
            'ggs_details': 'ggsDetails',
            'source_container_database_connection_id': 'sourceContainerDatabaseConnectionId',
            'advanced_parameters': 'advancedParameters'
        }
        self._id = None
        self._description = None
        self._database_combination = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._wait_after = None
        self._source_database_connection_id = None
        self._target_database_connection_id = None
        self._executing_job_id = None
        self._time_created = None
        self._time_updated = None
        self._time_last_migration = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._data_transfer_medium_details = None
        self._initial_load_settings = None
        self._advisor_settings = None
        self._hub_details = None
        self._ggs_details = None
        self._source_container_database_connection_id = None
        self._advanced_parameters = None
        self._database_combination = 'ORACLE'

    @property
    def data_transfer_medium_details(self):
        """
        Gets the data_transfer_medium_details of this OracleMigration.

        :return: The data_transfer_medium_details of this OracleMigration.
        :rtype: oci.database_migration.models.OracleDataTransferMediumDetails
        """
        return self._data_transfer_medium_details

    @data_transfer_medium_details.setter
    def data_transfer_medium_details(self, data_transfer_medium_details):
        """
        Sets the data_transfer_medium_details of this OracleMigration.

        :param data_transfer_medium_details: The data_transfer_medium_details of this OracleMigration.
        :type: oci.database_migration.models.OracleDataTransferMediumDetails
        """
        self._data_transfer_medium_details = data_transfer_medium_details

    @property
    def initial_load_settings(self):
        """
        Gets the initial_load_settings of this OracleMigration.

        :return: The initial_load_settings of this OracleMigration.
        :rtype: oci.database_migration.models.OracleInitialLoadSettings
        """
        return self._initial_load_settings

    @initial_load_settings.setter
    def initial_load_settings(self, initial_load_settings):
        """
        Sets the initial_load_settings of this OracleMigration.

        :param initial_load_settings: The initial_load_settings of this OracleMigration.
        :type: oci.database_migration.models.OracleInitialLoadSettings
        """
        self._initial_load_settings = initial_load_settings

    @property
    def advisor_settings(self):
        """
        Gets the advisor_settings of this OracleMigration.

        :return: The advisor_settings of this OracleMigration.
        :rtype: oci.database_migration.models.OracleAdvisorSettings
        """
        return self._advisor_settings

    @advisor_settings.setter
    def advisor_settings(self, advisor_settings):
        """
        Sets the advisor_settings of this OracleMigration.

        :param advisor_settings: The advisor_settings of this OracleMigration.
        :type: oci.database_migration.models.OracleAdvisorSettings
        """
        self._advisor_settings = advisor_settings

    @property
    def hub_details(self):
        """
        Gets the hub_details of this OracleMigration.

        :return: The hub_details of this OracleMigration.
        :rtype: oci.database_migration.models.GoldenGateHubDetails
        """
        return self._hub_details

    @hub_details.setter
    def hub_details(self, hub_details):
        """
        Sets the hub_details of this OracleMigration.

        :param hub_details: The hub_details of this OracleMigration.
        :type: oci.database_migration.models.GoldenGateHubDetails
        """
        self._hub_details = hub_details

    @property
    def ggs_details(self):
        """
        Gets the ggs_details of this OracleMigration.

        :return: The ggs_details of this OracleMigration.
        :rtype: oci.database_migration.models.OracleGgsDeploymentDetails
        """
        return self._ggs_details

    @ggs_details.setter
    def ggs_details(self, ggs_details):
        """
        Sets the ggs_details of this OracleMigration.

        :param ggs_details: The ggs_details of this OracleMigration.
        :type: oci.database_migration.models.OracleGgsDeploymentDetails
        """
        self._ggs_details = ggs_details

    @property
    def source_container_database_connection_id(self):
        """
        Gets the source_container_database_connection_id of this OracleMigration.
        The OCID of the resource being referenced.


        :return: The source_container_database_connection_id of this OracleMigration.
        :rtype: str
        """
        return self._source_container_database_connection_id

    @source_container_database_connection_id.setter
    def source_container_database_connection_id(self, source_container_database_connection_id):
        """
        Sets the source_container_database_connection_id of this OracleMigration.
        The OCID of the resource being referenced.


        :param source_container_database_connection_id: The source_container_database_connection_id of this OracleMigration.
        :type: str
        """
        self._source_container_database_connection_id = source_container_database_connection_id

    @property
    def advanced_parameters(self):
        """
        Gets the advanced_parameters of this OracleMigration.
        List of Migration Parameter objects.


        :return: The advanced_parameters of this OracleMigration.
        :rtype: list[oci.database_migration.models.MigrationParameterDetails]
        """
        return self._advanced_parameters

    @advanced_parameters.setter
    def advanced_parameters(self, advanced_parameters):
        """
        Sets the advanced_parameters of this OracleMigration.
        List of Migration Parameter objects.


        :param advanced_parameters: The advanced_parameters of this OracleMigration.
        :type: list[oci.database_migration.models.MigrationParameterDetails]
        """
        self._advanced_parameters = advanced_parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
