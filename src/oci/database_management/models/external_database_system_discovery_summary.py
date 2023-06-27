# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .entity_discovered import EntityDiscovered
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDatabaseSystemDiscoverySummary(EntityDiscovered):
    """
    The summary of the DB system discovery.
    """

    #: A constant which can be used with the license_model property of a ExternalDatabaseSystemDiscoverySummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a ExternalDatabaseSystemDiscoverySummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDatabaseSystemDiscoverySummary object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalDatabaseSystemDiscoverySummary.entity_type` attribute
        of this class is ``DATABASE_SYSTEM_DISCOVER_SUMMARY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalDatabaseSystemDiscoverySummary.
        :type id: str

        :param agent_id:
            The value to assign to the agent_id property of this ExternalDatabaseSystemDiscoverySummary.
        :type agent_id: str

        :param connector_id:
            The value to assign to the connector_id property of this ExternalDatabaseSystemDiscoverySummary.
        :type connector_id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalDatabaseSystemDiscoverySummary.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalDatabaseSystemDiscoverySummary.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalDatabaseSystemDiscoverySummary.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalDatabaseSystemDiscoverySummary.
        :type status: str

        :param discover_status:
            The value to assign to the discover_status property of this ExternalDatabaseSystemDiscoverySummary.
            Allowed values for this property are: "PREV_DISCOVERED", "NEW_DISCOVERED", "NOT_FOUND", "DISCOVERING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type discover_status: str

        :param discover_error_code:
            The value to assign to the discover_error_code property of this ExternalDatabaseSystemDiscoverySummary.
        :type discover_error_code: str

        :param discover_error_msg:
            The value to assign to the discover_error_msg property of this ExternalDatabaseSystemDiscoverySummary.
        :type discover_error_msg: str

        :param entity_type:
            The value to assign to the entity_type property of this ExternalDatabaseSystemDiscoverySummary.
            Allowed values for this property are: "STORAGE_SERVER_DISCOVER_SUMMARY", "STORAGE_GRID_DISCOVER_SUMMARY", "DATABASE_SYSTEM_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param oracle_home:
            The value to assign to the oracle_home property of this ExternalDatabaseSystemDiscoverySummary.
        :type oracle_home: str

        :param asm_connector_name:
            The value to assign to the asm_connector_name property of this ExternalDatabaseSystemDiscoverySummary.
        :type asm_connector_name: str

        :param license_model:
            The value to assign to the license_model property of this ExternalDatabaseSystemDiscoverySummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalDatabaseSystemDiscoverySummary.
        :type compartment_id: str

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
            'oracle_home': 'str',
            'asm_connector_name': 'str',
            'license_model': 'str',
            'compartment_id': 'str'
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
            'oracle_home': 'oracleHome',
            'asm_connector_name': 'asmConnectorName',
            'license_model': 'licenseModel',
            'compartment_id': 'compartmentId'
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
        self._oracle_home = None
        self._asm_connector_name = None
        self._license_model = None
        self._compartment_id = None
        self._entity_type = 'DATABASE_SYSTEM_DISCOVER_SUMMARY'

    @property
    def oracle_home(self):
        """
        Gets the oracle_home of this ExternalDatabaseSystemDiscoverySummary.
        The Oracle home path.


        :return: The oracle_home of this ExternalDatabaseSystemDiscoverySummary.
        :rtype: str
        """
        return self._oracle_home

    @oracle_home.setter
    def oracle_home(self, oracle_home):
        """
        Sets the oracle_home of this ExternalDatabaseSystemDiscoverySummary.
        The Oracle home path.


        :param oracle_home: The oracle_home of this ExternalDatabaseSystemDiscoverySummary.
        :type: str
        """
        self._oracle_home = oracle_home

    @property
    def asm_connector_name(self):
        """
        Gets the asm_connector_name of this ExternalDatabaseSystemDiscoverySummary.
        The display name of the ASM connector.


        :return: The asm_connector_name of this ExternalDatabaseSystemDiscoverySummary.
        :rtype: str
        """
        return self._asm_connector_name

    @asm_connector_name.setter
    def asm_connector_name(self, asm_connector_name):
        """
        Sets the asm_connector_name of this ExternalDatabaseSystemDiscoverySummary.
        The display name of the ASM connector.


        :param asm_connector_name: The asm_connector_name of this ExternalDatabaseSystemDiscoverySummary.
        :type: str
        """
        self._asm_connector_name = asm_connector_name

    @property
    def license_model(self):
        """
        Gets the license_model of this ExternalDatabaseSystemDiscoverySummary.
        The Oracle license model that applies to the database management resources.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this ExternalDatabaseSystemDiscoverySummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this ExternalDatabaseSystemDiscoverySummary.
        The Oracle license model that applies to the database management resources.


        :param license_model: The license_model of this ExternalDatabaseSystemDiscoverySummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ExternalDatabaseSystemDiscoverySummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalDatabaseSystemDiscoverySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalDatabaseSystemDiscoverySummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalDatabaseSystemDiscoverySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
