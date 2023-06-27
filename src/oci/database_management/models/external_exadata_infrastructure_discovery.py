# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .entity_discovered import EntityDiscovered
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalExadataInfrastructureDiscovery(EntityDiscovered):
    """
    The result of the Exadata infrastructure discovery.
    """

    #: A constant which can be used with the license_model property of a ExternalExadataInfrastructureDiscovery.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a ExternalExadataInfrastructureDiscovery.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscovery.
    #: This constant has a value of "FULL"
    RACK_SIZE_FULL = "FULL"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscovery.
    #: This constant has a value of "HALF"
    RACK_SIZE_HALF = "HALF"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscovery.
    #: This constant has a value of "QUARTER"
    RACK_SIZE_QUARTER = "QUARTER"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscovery.
    #: This constant has a value of "EIGHTH"
    RACK_SIZE_EIGHTH = "EIGHTH"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscovery.
    #: This constant has a value of "UNKNOWN"
    RACK_SIZE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalExadataInfrastructureDiscovery object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalExadataInfrastructureDiscovery.entity_type` attribute
        of this class is ``INFRASTRUCTURE_DISCOVER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalExadataInfrastructureDiscovery.
        :type id: str

        :param agent_id:
            The value to assign to the agent_id property of this ExternalExadataInfrastructureDiscovery.
        :type agent_id: str

        :param connector_id:
            The value to assign to the connector_id property of this ExternalExadataInfrastructureDiscovery.
        :type connector_id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalExadataInfrastructureDiscovery.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalExadataInfrastructureDiscovery.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalExadataInfrastructureDiscovery.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalExadataInfrastructureDiscovery.
        :type status: str

        :param discover_status:
            The value to assign to the discover_status property of this ExternalExadataInfrastructureDiscovery.
            Allowed values for this property are: "PREV_DISCOVERED", "NEW_DISCOVERED", "NOT_FOUND", "DISCOVERING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type discover_status: str

        :param discover_error_code:
            The value to assign to the discover_error_code property of this ExternalExadataInfrastructureDiscovery.
        :type discover_error_code: str

        :param discover_error_msg:
            The value to assign to the discover_error_msg property of this ExternalExadataInfrastructureDiscovery.
        :type discover_error_msg: str

        :param entity_type:
            The value to assign to the entity_type property of this ExternalExadataInfrastructureDiscovery.
            Allowed values for this property are: "STORAGE_SERVER_DISCOVER_SUMMARY", "STORAGE_GRID_DISCOVER_SUMMARY", "DATABASE_SYSTEM_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param discovery_key:
            The value to assign to the discovery_key property of this ExternalExadataInfrastructureDiscovery.
        :type discovery_key: str

        :param license_model:
            The value to assign to the license_model property of this ExternalExadataInfrastructureDiscovery.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalExadataInfrastructureDiscovery.
        :type compartment_id: str

        :param rack_size:
            The value to assign to the rack_size property of this ExternalExadataInfrastructureDiscovery.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rack_size: str

        :param grid_home_path:
            The value to assign to the grid_home_path property of this ExternalExadataInfrastructureDiscovery.
        :type grid_home_path: str

        :param db_systems:
            The value to assign to the db_systems property of this ExternalExadataInfrastructureDiscovery.
        :type db_systems: list[oci.database_management.models.ExternalDatabaseSystemDiscoverySummary]

        :param storage_grid:
            The value to assign to the storage_grid property of this ExternalExadataInfrastructureDiscovery.
        :type storage_grid: oci.database_management.models.ExternalStorageGridDiscoverySummary

        :param storage_servers:
            The value to assign to the storage_servers property of this ExternalExadataInfrastructureDiscovery.
        :type storage_servers: list[oci.database_management.models.ExternalStorageServerDiscoverySummary]

        """
        self.swagger_types = {
            'id': 'str',
            'agent_id': 'str',
            'connector_id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'discover_status': 'str',
            'discover_error_code': 'str',
            'discover_error_msg': 'str',
            'entity_type': 'str',
            'discovery_key': 'str',
            'license_model': 'str',
            'compartment_id': 'str',
            'rack_size': 'str',
            'grid_home_path': 'str',
            'db_systems': 'list[ExternalDatabaseSystemDiscoverySummary]',
            'storage_grid': 'ExternalStorageGridDiscoverySummary',
            'storage_servers': 'list[ExternalStorageServerDiscoverySummary]'
        }

        self.attribute_map = {
            'id': 'id',
            'agent_id': 'agentId',
            'connector_id': 'connectorId',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'discover_status': 'discoverStatus',
            'discover_error_code': 'discoverErrorCode',
            'discover_error_msg': 'discoverErrorMsg',
            'entity_type': 'entityType',
            'discovery_key': 'discoveryKey',
            'license_model': 'licenseModel',
            'compartment_id': 'compartmentId',
            'rack_size': 'rackSize',
            'grid_home_path': 'gridHomePath',
            'db_systems': 'dbSystems',
            'storage_grid': 'storageGrid',
            'storage_servers': 'storageServers'
        }

        self._id = None
        self._agent_id = None
        self._connector_id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._discover_status = None
        self._discover_error_code = None
        self._discover_error_msg = None
        self._entity_type = None
        self._discovery_key = None
        self._license_model = None
        self._compartment_id = None
        self._rack_size = None
        self._grid_home_path = None
        self._db_systems = None
        self._storage_grid = None
        self._storage_servers = None
        self._entity_type = 'INFRASTRUCTURE_DISCOVER'

    @property
    def discovery_key(self):
        """
        **[Required]** Gets the discovery_key of this ExternalExadataInfrastructureDiscovery.
        The unique key of the discovery request.


        :return: The discovery_key of this ExternalExadataInfrastructureDiscovery.
        :rtype: str
        """
        return self._discovery_key

    @discovery_key.setter
    def discovery_key(self, discovery_key):
        """
        Sets the discovery_key of this ExternalExadataInfrastructureDiscovery.
        The unique key of the discovery request.


        :param discovery_key: The discovery_key of this ExternalExadataInfrastructureDiscovery.
        :type: str
        """
        self._discovery_key = discovery_key

    @property
    def license_model(self):
        """
        Gets the license_model of this ExternalExadataInfrastructureDiscovery.
        The Oracle license model that applies to the database management resources.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this ExternalExadataInfrastructureDiscovery.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this ExternalExadataInfrastructureDiscovery.
        The Oracle license model that applies to the database management resources.


        :param license_model: The license_model of this ExternalExadataInfrastructureDiscovery.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ExternalExadataInfrastructureDiscovery.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalExadataInfrastructureDiscovery.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalExadataInfrastructureDiscovery.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalExadataInfrastructureDiscovery.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def rack_size(self):
        """
        Gets the rack_size of this ExternalExadataInfrastructureDiscovery.
        The size of the Exadata infrastructure.

        Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rack_size of this ExternalExadataInfrastructureDiscovery.
        :rtype: str
        """
        return self._rack_size

    @rack_size.setter
    def rack_size(self, rack_size):
        """
        Sets the rack_size of this ExternalExadataInfrastructureDiscovery.
        The size of the Exadata infrastructure.


        :param rack_size: The rack_size of this ExternalExadataInfrastructureDiscovery.
        :type: str
        """
        allowed_values = ["FULL", "HALF", "QUARTER", "EIGHTH", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(rack_size, allowed_values):
            rack_size = 'UNKNOWN_ENUM_VALUE'
        self._rack_size = rack_size

    @property
    def grid_home_path(self):
        """
        Gets the grid_home_path of this ExternalExadataInfrastructureDiscovery.
        The Oracle home path of the Exadata infrastructure.


        :return: The grid_home_path of this ExternalExadataInfrastructureDiscovery.
        :rtype: str
        """
        return self._grid_home_path

    @grid_home_path.setter
    def grid_home_path(self, grid_home_path):
        """
        Sets the grid_home_path of this ExternalExadataInfrastructureDiscovery.
        The Oracle home path of the Exadata infrastructure.


        :param grid_home_path: The grid_home_path of this ExternalExadataInfrastructureDiscovery.
        :type: str
        """
        self._grid_home_path = grid_home_path

    @property
    def db_systems(self):
        """
        Gets the db_systems of this ExternalExadataInfrastructureDiscovery.
        The list of DB systems in the Exadata infrastructure.


        :return: The db_systems of this ExternalExadataInfrastructureDiscovery.
        :rtype: list[oci.database_management.models.ExternalDatabaseSystemDiscoverySummary]
        """
        return self._db_systems

    @db_systems.setter
    def db_systems(self, db_systems):
        """
        Sets the db_systems of this ExternalExadataInfrastructureDiscovery.
        The list of DB systems in the Exadata infrastructure.


        :param db_systems: The db_systems of this ExternalExadataInfrastructureDiscovery.
        :type: list[oci.database_management.models.ExternalDatabaseSystemDiscoverySummary]
        """
        self._db_systems = db_systems

    @property
    def storage_grid(self):
        """
        Gets the storage_grid of this ExternalExadataInfrastructureDiscovery.

        :return: The storage_grid of this ExternalExadataInfrastructureDiscovery.
        :rtype: oci.database_management.models.ExternalStorageGridDiscoverySummary
        """
        return self._storage_grid

    @storage_grid.setter
    def storage_grid(self, storage_grid):
        """
        Sets the storage_grid of this ExternalExadataInfrastructureDiscovery.

        :param storage_grid: The storage_grid of this ExternalExadataInfrastructureDiscovery.
        :type: oci.database_management.models.ExternalStorageGridDiscoverySummary
        """
        self._storage_grid = storage_grid

    @property
    def storage_servers(self):
        """
        Gets the storage_servers of this ExternalExadataInfrastructureDiscovery.
        The list of storage servers in the Exadata infrastructure.


        :return: The storage_servers of this ExternalExadataInfrastructureDiscovery.
        :rtype: list[oci.database_management.models.ExternalStorageServerDiscoverySummary]
        """
        return self._storage_servers

    @storage_servers.setter
    def storage_servers(self, storage_servers):
        """
        Sets the storage_servers of this ExternalExadataInfrastructureDiscovery.
        The list of storage servers in the Exadata infrastructure.


        :param storage_servers: The storage_servers of this ExternalExadataInfrastructureDiscovery.
        :type: list[oci.database_management.models.ExternalStorageServerDiscoverySummary]
        """
        self._storage_servers = storage_servers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
