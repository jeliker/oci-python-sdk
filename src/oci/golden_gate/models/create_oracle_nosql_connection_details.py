# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOracleNosqlConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Oracle NoSQL Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOracleNosqlConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateOracleNosqlConnectionDetails.connection_type` attribute
        of this class is ``ORACLE_NOSQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateOracleNosqlConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateOracleNosqlConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateOracleNosqlConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOracleNosqlConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOracleNosqlConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOracleNosqlConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param locks:
            The value to assign to the locks property of this CreateOracleNosqlConnectionDetails.
        :type locks: list[oci.golden_gate.models.AddResourceLockDetails]

        :param vault_id:
            The value to assign to the vault_id property of this CreateOracleNosqlConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateOracleNosqlConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateOracleNosqlConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateOracleNosqlConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this CreateOracleNosqlConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this CreateOracleNosqlConnectionDetails.
        :type does_use_secret_ids: bool

        :param technology_type:
            The value to assign to the technology_type property of this CreateOracleNosqlConnectionDetails.
        :type technology_type: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this CreateOracleNosqlConnectionDetails.
        :type tenancy_id: str

        :param region:
            The value to assign to the region property of this CreateOracleNosqlConnectionDetails.
        :type region: str

        :param user_id:
            The value to assign to the user_id property of this CreateOracleNosqlConnectionDetails.
        :type user_id: str

        :param private_key_file:
            The value to assign to the private_key_file property of this CreateOracleNosqlConnectionDetails.
        :type private_key_file: str

        :param private_key_file_secret_id:
            The value to assign to the private_key_file_secret_id property of this CreateOracleNosqlConnectionDetails.
        :type private_key_file_secret_id: str

        :param private_key_passphrase:
            The value to assign to the private_key_passphrase property of this CreateOracleNosqlConnectionDetails.
        :type private_key_passphrase: str

        :param private_key_passphrase_secret_id:
            The value to assign to the private_key_passphrase_secret_id property of this CreateOracleNosqlConnectionDetails.
        :type private_key_passphrase_secret_id: str

        :param public_key_fingerprint:
            The value to assign to the public_key_fingerprint property of this CreateOracleNosqlConnectionDetails.
        :type public_key_fingerprint: str

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
            'tenancy_id': 'str',
            'region': 'str',
            'user_id': 'str',
            'private_key_file': 'str',
            'private_key_file_secret_id': 'str',
            'private_key_passphrase': 'str',
            'private_key_passphrase_secret_id': 'str',
            'public_key_fingerprint': 'str'
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
            'tenancy_id': 'tenancyId',
            'region': 'region',
            'user_id': 'userId',
            'private_key_file': 'privateKeyFile',
            'private_key_file_secret_id': 'privateKeyFileSecretId',
            'private_key_passphrase': 'privateKeyPassphrase',
            'private_key_passphrase_secret_id': 'privateKeyPassphraseSecretId',
            'public_key_fingerprint': 'publicKeyFingerprint'
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
        self._tenancy_id = None
        self._region = None
        self._user_id = None
        self._private_key_file = None
        self._private_key_file_secret_id = None
        self._private_key_passphrase = None
        self._private_key_passphrase_secret_id = None
        self._public_key_fingerprint = None
        self._connection_type = 'ORACLE_NOSQL'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateOracleNosqlConnectionDetails.
        The Oracle NoSQL technology type.


        :return: The technology_type of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateOracleNosqlConnectionDetails.
        The Oracle NoSQL technology type.


        :param technology_type: The technology_type of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this CreateOracleNosqlConnectionDetails.
        The `OCID`__ of the related OCI tenancy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenancy_id of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this CreateOracleNosqlConnectionDetails.
        The `OCID`__ of the related OCI tenancy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenancy_id: The tenancy_id of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def region(self):
        """
        Gets the region of this CreateOracleNosqlConnectionDetails.
        The name of the region. e.g.: us-ashburn-1


        :return: The region of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CreateOracleNosqlConnectionDetails.
        The name of the region. e.g.: us-ashburn-1


        :param region: The region of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._region = region

    @property
    def user_id(self):
        """
        Gets the user_id of this CreateOracleNosqlConnectionDetails.
        The `OCID`__ of the OCI user who will access the Oracle NoSQL database.
        The user must have write access to the table they want to connect to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The user_id of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CreateOracleNosqlConnectionDetails.
        The `OCID`__ of the OCI user who will access the Oracle NoSQL database.
        The user must have write access to the table they want to connect to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param user_id: The user_id of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._user_id = user_id

    @property
    def private_key_file(self):
        """
        Gets the private_key_file of this CreateOracleNosqlConnectionDetails.
        The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :return: The private_key_file of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._private_key_file

    @private_key_file.setter
    def private_key_file(self, private_key_file):
        """
        Sets the private_key_file of this CreateOracleNosqlConnectionDetails.
        The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :param private_key_file: The private_key_file of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._private_key_file = private_key_file

    @property
    def private_key_file_secret_id(self):
        """
        Gets the private_key_file_secret_id of this CreateOracleNosqlConnectionDetails.
        The `OCID`__ of the Secret that stores the content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm
        Note: When provided, 'privateKeyFile' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_key_file_secret_id of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._private_key_file_secret_id

    @private_key_file_secret_id.setter
    def private_key_file_secret_id(self, private_key_file_secret_id):
        """
        Sets the private_key_file_secret_id of this CreateOracleNosqlConnectionDetails.
        The `OCID`__ of the Secret that stores the content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm
        Note: When provided, 'privateKeyFile' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_key_file_secret_id: The private_key_file_secret_id of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._private_key_file_secret_id = private_key_file_secret_id

    @property
    def private_key_passphrase(self):
        """
        Gets the private_key_passphrase of this CreateOracleNosqlConnectionDetails.
        The passphrase of the private key.


        :return: The private_key_passphrase of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._private_key_passphrase

    @private_key_passphrase.setter
    def private_key_passphrase(self, private_key_passphrase):
        """
        Sets the private_key_passphrase of this CreateOracleNosqlConnectionDetails.
        The passphrase of the private key.


        :param private_key_passphrase: The private_key_passphrase of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._private_key_passphrase = private_key_passphrase

    @property
    def private_key_passphrase_secret_id(self):
        """
        Gets the private_key_passphrase_secret_id of this CreateOracleNosqlConnectionDetails.
        The `OCID`__ of the Secret that stores the passphrase of the private key.
        Note: When provided, 'privateKeyPassphrase' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_key_passphrase_secret_id of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._private_key_passphrase_secret_id

    @private_key_passphrase_secret_id.setter
    def private_key_passphrase_secret_id(self, private_key_passphrase_secret_id):
        """
        Sets the private_key_passphrase_secret_id of this CreateOracleNosqlConnectionDetails.
        The `OCID`__ of the Secret that stores the passphrase of the private key.
        Note: When provided, 'privateKeyPassphrase' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_key_passphrase_secret_id: The private_key_passphrase_secret_id of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._private_key_passphrase_secret_id = private_key_passphrase_secret_id

    @property
    def public_key_fingerprint(self):
        """
        **[Required]** Gets the public_key_fingerprint of this CreateOracleNosqlConnectionDetails.
        The fingerprint of the API Key of the user specified by the userId.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :return: The public_key_fingerprint of this CreateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._public_key_fingerprint

    @public_key_fingerprint.setter
    def public_key_fingerprint(self, public_key_fingerprint):
        """
        Sets the public_key_fingerprint of this CreateOracleNosqlConnectionDetails.
        The fingerprint of the API Key of the user specified by the userId.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :param public_key_fingerprint: The public_key_fingerprint of this CreateOracleNosqlConnectionDetails.
        :type: str
        """
        self._public_key_fingerprint = public_key_fingerprint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
