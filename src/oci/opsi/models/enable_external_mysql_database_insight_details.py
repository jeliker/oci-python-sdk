# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .enable_database_insight_details import EnableDatabaseInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableExternalMysqlDatabaseInsightDetails(EnableDatabaseInsightDetails):
    """
    The information about database to be analyzed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableExternalMysqlDatabaseInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EnableExternalMysqlDatabaseInsightDetails.entity_source` attribute
        of this class is ``EXTERNAL_MYSQL_DATABASE_SYSTEM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EnableExternalMysqlDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE", "MDS_MYSQL_DATABASE_SYSTEM", "EXTERNAL_MYSQL_DATABASE_SYSTEM", "MACS_MANAGED_CLOUD_DATABASE"
        :type entity_source: str

        :param database_connector_id:
            The value to assign to the database_connector_id property of this EnableExternalMysqlDatabaseInsightDetails.
        :type database_connector_id: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'database_connector_id': 'str'
        }
        self.attribute_map = {
            'entity_source': 'entitySource',
            'database_connector_id': 'databaseConnectorId'
        }
        self._entity_source = None
        self._database_connector_id = None
        self._entity_source = 'EXTERNAL_MYSQL_DATABASE_SYSTEM'

    @property
    def database_connector_id(self):
        """
        **[Required]** Gets the database_connector_id of this EnableExternalMysqlDatabaseInsightDetails.
        The DBM owned database connector `OCID`__ mapping to the database credentials and connection details.

        __ https://docs.cloud.oracle.com/iaas/database-management/doc/view-connector-details.html


        :return: The database_connector_id of this EnableExternalMysqlDatabaseInsightDetails.
        :rtype: str
        """
        return self._database_connector_id

    @database_connector_id.setter
    def database_connector_id(self, database_connector_id):
        """
        Sets the database_connector_id of this EnableExternalMysqlDatabaseInsightDetails.
        The DBM owned database connector `OCID`__ mapping to the database credentials and connection details.

        __ https://docs.cloud.oracle.com/iaas/database-management/doc/view-connector-details.html


        :param database_connector_id: The database_connector_id of this EnableExternalMysqlDatabaseInsightDetails.
        :type: str
        """
        self._database_connector_id = database_connector_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
