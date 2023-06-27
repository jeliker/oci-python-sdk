# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dbm_resource import DbmResource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalExadataStorageConnectorSummary(DbmResource):
    """
    The connector of the Exadata storage server.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalExadataStorageConnectorSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalExadataStorageConnectorSummary.resource_type` attribute
        of this class is ``STORAGE_CONNECTOR_SUMMARY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalExadataStorageConnectorSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalExadataStorageConnectorSummary.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalExadataStorageConnectorSummary.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalExadataStorageConnectorSummary.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalExadataStorageConnectorSummary.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalExadataStorageConnectorSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ExternalExadataStorageConnectorSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalExadataStorageConnectorSummary.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalExadataStorageConnectorSummary.
        :type lifecycle_details: str

        :param additional_details:
            The value to assign to the additional_details property of this ExternalExadataStorageConnectorSummary.
        :type additional_details: dict(str, str)

        :param resource_type:
            The value to assign to the resource_type property of this ExternalExadataStorageConnectorSummary.
            Allowed values for this property are: "INFRASTRUCTURE_SUMMARY", "INFRASTRUCTURE", "STORAGE_SERVER_SUMMARY", "STORAGE_SERVER", "STORAGE_GRID_SUMMARY", "STORAGE_GRID", "STORAGE_CONNECTOR_SUMMARY", "STORAGE_CONNECTOR", "DATABASE_SYSTEM_SUMMARY", "DATABASE_SUMMARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param connection_uri:
            The value to assign to the connection_uri property of this ExternalExadataStorageConnectorSummary.
        :type connection_uri: str

        :param storage_server_id:
            The value to assign to the storage_server_id property of this ExternalExadataStorageConnectorSummary.
        :type storage_server_id: str

        :param agent_id:
            The value to assign to the agent_id property of this ExternalExadataStorageConnectorSummary.
        :type agent_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'additional_details': 'dict(str, str)',
            'resource_type': 'str',
            'connection_uri': 'str',
            'storage_server_id': 'str',
            'agent_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'additional_details': 'additionalDetails',
            'resource_type': 'resourceType',
            'connection_uri': 'connectionUri',
            'storage_server_id': 'storageServerId',
            'agent_id': 'agentId'
        }

        self._id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_details = None
        self._additional_details = None
        self._resource_type = None
        self._connection_uri = None
        self._storage_server_id = None
        self._agent_id = None
        self._resource_type = 'STORAGE_CONNECTOR_SUMMARY'

    @property
    def connection_uri(self):
        """
        Gets the connection_uri of this ExternalExadataStorageConnectorSummary.
        The unique string of the connection. For example, \"https://<storage-server-name>/MS/RESTService/\".


        :return: The connection_uri of this ExternalExadataStorageConnectorSummary.
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """
        Sets the connection_uri of this ExternalExadataStorageConnectorSummary.
        The unique string of the connection. For example, \"https://<storage-server-name>/MS/RESTService/\".


        :param connection_uri: The connection_uri of this ExternalExadataStorageConnectorSummary.
        :type: str
        """
        self._connection_uri = connection_uri

    @property
    def storage_server_id(self):
        """
        Gets the storage_server_id of this ExternalExadataStorageConnectorSummary.
        The `OCID`__ of the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The storage_server_id of this ExternalExadataStorageConnectorSummary.
        :rtype: str
        """
        return self._storage_server_id

    @storage_server_id.setter
    def storage_server_id(self, storage_server_id):
        """
        Sets the storage_server_id of this ExternalExadataStorageConnectorSummary.
        The `OCID`__ of the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param storage_server_id: The storage_server_id of this ExternalExadataStorageConnectorSummary.
        :type: str
        """
        self._storage_server_id = storage_server_id

    @property
    def agent_id(self):
        """
        Gets the agent_id of this ExternalExadataStorageConnectorSummary.
        The `OCID`__ of the agent for the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this ExternalExadataStorageConnectorSummary.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this ExternalExadataStorageConnectorSummary.
        The `OCID`__ of the agent for the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this ExternalExadataStorageConnectorSummary.
        :type: str
        """
        self._agent_id = agent_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
