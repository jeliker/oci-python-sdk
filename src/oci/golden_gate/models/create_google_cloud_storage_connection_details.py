# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGoogleCloudStorageConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Google Cloud Storage Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGoogleCloudStorageConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateGoogleCloudStorageConnectionDetails.connection_type` attribute
        of this class is ``GOOGLE_CLOUD_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateGoogleCloudStorageConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateGoogleCloudStorageConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateGoogleCloudStorageConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateGoogleCloudStorageConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateGoogleCloudStorageConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateGoogleCloudStorageConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param locks:
            The value to assign to the locks property of this CreateGoogleCloudStorageConnectionDetails.
        :type locks: list[oci.golden_gate.models.AddResourceLockDetails]

        :param vault_id:
            The value to assign to the vault_id property of this CreateGoogleCloudStorageConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateGoogleCloudStorageConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateGoogleCloudStorageConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateGoogleCloudStorageConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this CreateGoogleCloudStorageConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this CreateGoogleCloudStorageConnectionDetails.
        :type does_use_secret_ids: bool

        :param technology_type:
            The value to assign to the technology_type property of this CreateGoogleCloudStorageConnectionDetails.
        :type technology_type: str

        :param service_account_key_file:
            The value to assign to the service_account_key_file property of this CreateGoogleCloudStorageConnectionDetails.
        :type service_account_key_file: str

        :param service_account_key_file_secret_id:
            The value to assign to the service_account_key_file_secret_id property of this CreateGoogleCloudStorageConnectionDetails.
        :type service_account_key_file_secret_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'locks': 'list[AddResourceLockDetails]',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'does_use_secret_ids': 'bool',
            'technology_type': 'str',
            'service_account_key_file': 'str',
            'service_account_key_file_secret_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'locks': 'locks',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'does_use_secret_ids': 'doesUseSecretIds',
            'technology_type': 'technologyType',
            'service_account_key_file': 'serviceAccountKeyFile',
            'service_account_key_file_secret_id': 'serviceAccountKeyFileSecretId'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._locks = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._does_use_secret_ids = None
        self._technology_type = None
        self._service_account_key_file = None
        self._service_account_key_file_secret_id = None
        self._connection_type = 'GOOGLE_CLOUD_STORAGE'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateGoogleCloudStorageConnectionDetails.
        The Google Cloud Storage technology type.


        :return: The technology_type of this CreateGoogleCloudStorageConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateGoogleCloudStorageConnectionDetails.
        The Google Cloud Storage technology type.


        :param technology_type: The technology_type of this CreateGoogleCloudStorageConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def service_account_key_file(self):
        """
        Gets the service_account_key_file of this CreateGoogleCloudStorageConnectionDetails.
        The base64 encoded content of the service account key file containing
        the credentials required to use Google Cloud Storage.


        :return: The service_account_key_file of this CreateGoogleCloudStorageConnectionDetails.
        :rtype: str
        """
        return self._service_account_key_file

    @service_account_key_file.setter
    def service_account_key_file(self, service_account_key_file):
        """
        Sets the service_account_key_file of this CreateGoogleCloudStorageConnectionDetails.
        The base64 encoded content of the service account key file containing
        the credentials required to use Google Cloud Storage.


        :param service_account_key_file: The service_account_key_file of this CreateGoogleCloudStorageConnectionDetails.
        :type: str
        """
        self._service_account_key_file = service_account_key_file

    @property
    def service_account_key_file_secret_id(self):
        """
        Gets the service_account_key_file_secret_id of this CreateGoogleCloudStorageConnectionDetails.
        The `OCID`__ of the Secret where the content of the service account key file is stored,
        which containing the credentials required to use Google Cloud Storage.
        Note: When provided, 'serviceAccountKeyFile' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The service_account_key_file_secret_id of this CreateGoogleCloudStorageConnectionDetails.
        :rtype: str
        """
        return self._service_account_key_file_secret_id

    @service_account_key_file_secret_id.setter
    def service_account_key_file_secret_id(self, service_account_key_file_secret_id):
        """
        Sets the service_account_key_file_secret_id of this CreateGoogleCloudStorageConnectionDetails.
        The `OCID`__ of the Secret where the content of the service account key file is stored,
        which containing the credentials required to use Google Cloud Storage.
        Note: When provided, 'serviceAccountKeyFile' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param service_account_key_file_secret_id: The service_account_key_file_secret_id of this CreateGoogleCloudStorageConnectionDetails.
        :type: str
        """
        self._service_account_key_file_secret_id = service_account_key_file_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
