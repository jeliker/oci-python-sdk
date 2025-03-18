# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateKafkaSchemaRegistryConnectionDetails(UpdateConnectionDetails):
    """
    The information to update Kafka (e.g. Confluent) Schema Registry Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateKafkaSchemaRegistryConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateKafkaSchemaRegistryConnectionDetails.connection_type` attribute
        of this class is ``KAFKA_SCHEMA_REGISTRY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateKafkaSchemaRegistryConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this UpdateKafkaSchemaRegistryConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type does_use_secret_ids: bool

        :param url:
            The value to assign to the url property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type url: str

        :param authentication_type:
            The value to assign to the authentication_type property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type authentication_type: str

        :param username:
            The value to assign to the username property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type password: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type password_secret_id: str

        :param trust_store:
            The value to assign to the trust_store property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type trust_store: str

        :param trust_store_secret_id:
            The value to assign to the trust_store_secret_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type trust_store_secret_id: str

        :param trust_store_password:
            The value to assign to the trust_store_password property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type trust_store_password: str

        :param trust_store_password_secret_id:
            The value to assign to the trust_store_password_secret_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type trust_store_password_secret_id: str

        :param key_store:
            The value to assign to the key_store property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type key_store: str

        :param key_store_secret_id:
            The value to assign to the key_store_secret_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type key_store_secret_id: str

        :param key_store_password:
            The value to assign to the key_store_password property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type key_store_password: str

        :param key_store_password_secret_id:
            The value to assign to the key_store_password_secret_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type key_store_password_secret_id: str

        :param ssl_key_password:
            The value to assign to the ssl_key_password property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type ssl_key_password: str

        :param ssl_key_password_secret_id:
            The value to assign to the ssl_key_password_secret_id property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type ssl_key_password_secret_id: str

        :param private_ip:
            The value to assign to the private_ip property of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type private_ip: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'does_use_secret_ids': 'bool',
            'url': 'str',
            'authentication_type': 'str',
            'username': 'str',
            'password': 'str',
            'password_secret_id': 'str',
            'trust_store': 'str',
            'trust_store_secret_id': 'str',
            'trust_store_password': 'str',
            'trust_store_password_secret_id': 'str',
            'key_store': 'str',
            'key_store_secret_id': 'str',
            'key_store_password': 'str',
            'key_store_password_secret_id': 'str',
            'ssl_key_password': 'str',
            'ssl_key_password_secret_id': 'str',
            'private_ip': 'str'
        }
        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'does_use_secret_ids': 'doesUseSecretIds',
            'url': 'url',
            'authentication_type': 'authenticationType',
            'username': 'username',
            'password': 'password',
            'password_secret_id': 'passwordSecretId',
            'trust_store': 'trustStore',
            'trust_store_secret_id': 'trustStoreSecretId',
            'trust_store_password': 'trustStorePassword',
            'trust_store_password_secret_id': 'trustStorePasswordSecretId',
            'key_store': 'keyStore',
            'key_store_secret_id': 'keyStoreSecretId',
            'key_store_password': 'keyStorePassword',
            'key_store_password_secret_id': 'keyStorePasswordSecretId',
            'ssl_key_password': 'sslKeyPassword',
            'ssl_key_password_secret_id': 'sslKeyPasswordSecretId',
            'private_ip': 'privateIp'
        }
        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._does_use_secret_ids = None
        self._url = None
        self._authentication_type = None
        self._username = None
        self._password = None
        self._password_secret_id = None
        self._trust_store = None
        self._trust_store_secret_id = None
        self._trust_store_password = None
        self._trust_store_password_secret_id = None
        self._key_store = None
        self._key_store_secret_id = None
        self._key_store_password = None
        self._key_store_password_secret_id = None
        self._ssl_key_password = None
        self._ssl_key_password_secret_id = None
        self._private_ip = None
        self._connection_type = 'KAFKA_SCHEMA_REGISTRY'

    @property
    def url(self):
        """
        Gets the url of this UpdateKafkaSchemaRegistryConnectionDetails.
        Kafka Schema Registry URL.
        e.g.: 'https://server1.us.oracle.com:8081'


        :return: The url of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this UpdateKafkaSchemaRegistryConnectionDetails.
        Kafka Schema Registry URL.
        e.g.: 'https://server1.us.oracle.com:8081'


        :param url: The url of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._url = url

    @property
    def authentication_type(self):
        """
        Gets the authentication_type of this UpdateKafkaSchemaRegistryConnectionDetails.
        Used authentication mechanism to access Schema Registry.


        :return: The authentication_type of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this UpdateKafkaSchemaRegistryConnectionDetails.
        Used authentication mechanism to access Schema Registry.


        :param authentication_type: The authentication_type of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._authentication_type = authentication_type

    @property
    def username(self):
        """
        Gets the username of this UpdateKafkaSchemaRegistryConnectionDetails.
        The username to access Schema Registry using basic authentication.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.


        :return: The username of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UpdateKafkaSchemaRegistryConnectionDetails.
        The username to access Schema Registry using basic authentication.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.


        :param username: The username of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this UpdateKafkaSchemaRegistryConnectionDetails.
        The password to access Schema Registry using basic authentication.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.
        Deprecated: This field is deprecated and replaced by \"passwordSecretId\". This field will be removed after February 15 2026.


        :return: The password of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateKafkaSchemaRegistryConnectionDetails.
        The password to access Schema Registry using basic authentication.
        This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.
        Deprecated: This field is deprecated and replaced by \"passwordSecretId\". This field will be removed after February 15 2026.


        :param password: The password of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._password = password

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret where the password is stored.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        If secretId is used plaintext field must not be provided.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret where the password is stored.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        If secretId is used plaintext field must not be provided.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def trust_store(self):
        """
        Gets the trust_store of this UpdateKafkaSchemaRegistryConnectionDetails.
        The base64 encoded content of the TrustStore file.
        Deprecated: This field is deprecated and replaced by \"trustStoreSecretId\". This field will be removed after February 15 2026.


        :return: The trust_store of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._trust_store

    @trust_store.setter
    def trust_store(self, trust_store):
        """
        Sets the trust_store of this UpdateKafkaSchemaRegistryConnectionDetails.
        The base64 encoded content of the TrustStore file.
        Deprecated: This field is deprecated and replaced by \"trustStoreSecretId\". This field will be removed after February 15 2026.


        :param trust_store: The trust_store of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._trust_store = trust_store

    @property
    def trust_store_secret_id(self):
        """
        Gets the trust_store_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret that stores the content of the TrustStore file.
        Note: When provided, 'trustStore' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The trust_store_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._trust_store_secret_id

    @trust_store_secret_id.setter
    def trust_store_secret_id(self, trust_store_secret_id):
        """
        Sets the trust_store_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret that stores the content of the TrustStore file.
        Note: When provided, 'trustStore' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param trust_store_secret_id: The trust_store_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._trust_store_secret_id = trust_store_secret_id

    @property
    def trust_store_password(self):
        """
        Gets the trust_store_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        The TrustStore password.
        Deprecated: This field is deprecated and replaced by \"trustStorePasswordSecretId\". This field will be removed after February 15 2026.


        :return: The trust_store_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._trust_store_password

    @trust_store_password.setter
    def trust_store_password(self, trust_store_password):
        """
        Sets the trust_store_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        The TrustStore password.
        Deprecated: This field is deprecated and replaced by \"trustStorePasswordSecretId\". This field will be removed after February 15 2026.


        :param trust_store_password: The trust_store_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._trust_store_password = trust_store_password

    @property
    def trust_store_password_secret_id(self):
        """
        Gets the trust_store_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret where the kafka Ssl TrustStore password is stored.
        Note: When provided, 'trustStorePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The trust_store_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._trust_store_password_secret_id

    @trust_store_password_secret_id.setter
    def trust_store_password_secret_id(self, trust_store_password_secret_id):
        """
        Sets the trust_store_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret where the kafka Ssl TrustStore password is stored.
        Note: When provided, 'trustStorePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param trust_store_password_secret_id: The trust_store_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._trust_store_password_secret_id = trust_store_password_secret_id

    @property
    def key_store(self):
        """
        Gets the key_store of this UpdateKafkaSchemaRegistryConnectionDetails.
        The base64 encoded content of the KeyStore file.
        Deprecated: This field is deprecated and replaced by \"keyStoreSecretId\". This field will be removed after February 15 2026.


        :return: The key_store of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._key_store

    @key_store.setter
    def key_store(self, key_store):
        """
        Sets the key_store of this UpdateKafkaSchemaRegistryConnectionDetails.
        The base64 encoded content of the KeyStore file.
        Deprecated: This field is deprecated and replaced by \"keyStoreSecretId\". This field will be removed after February 15 2026.


        :param key_store: The key_store of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._key_store = key_store

    @property
    def key_store_secret_id(self):
        """
        Gets the key_store_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret that stores the content of the KeyStore file.
        Note: When provided, 'keyStore' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_store_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._key_store_secret_id

    @key_store_secret_id.setter
    def key_store_secret_id(self, key_store_secret_id):
        """
        Sets the key_store_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret that stores the content of the KeyStore file.
        Note: When provided, 'keyStore' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_store_secret_id: The key_store_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._key_store_secret_id = key_store_secret_id

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        The KeyStore password.
        Deprecated: This field is deprecated and replaced by \"keyStorePasswordSecretId\". This field will be removed after February 15 2026.


        :return: The key_store_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        The KeyStore password.
        Deprecated: This field is deprecated and replaced by \"keyStorePasswordSecretId\". This field will be removed after February 15 2026.


        :param key_store_password: The key_store_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._key_store_password = key_store_password

    @property
    def key_store_password_secret_id(self):
        """
        Gets the key_store_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret where the kafka Ssl KeyStore password is stored.
        Note: When provided, 'keyStorePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_store_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._key_store_password_secret_id

    @key_store_password_secret_id.setter
    def key_store_password_secret_id(self, key_store_password_secret_id):
        """
        Sets the key_store_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret where the kafka Ssl KeyStore password is stored.
        Note: When provided, 'keyStorePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_store_password_secret_id: The key_store_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._key_store_password_secret_id = key_store_password_secret_id

    @property
    def ssl_key_password(self):
        """
        Gets the ssl_key_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        The password for the cert inside the KeyStore.
        In case it differs from the KeyStore password, it should be provided.
        Deprecated: This field is deprecated and replaced by \"sslKeyPasswordSecretId\". This field will be removed after February 15 2026.


        :return: The ssl_key_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._ssl_key_password

    @ssl_key_password.setter
    def ssl_key_password(self, ssl_key_password):
        """
        Sets the ssl_key_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        The password for the cert inside the KeyStore.
        In case it differs from the KeyStore password, it should be provided.
        Deprecated: This field is deprecated and replaced by \"sslKeyPasswordSecretId\". This field will be removed after February 15 2026.


        :param ssl_key_password: The ssl_key_password of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._ssl_key_password = ssl_key_password

    @property
    def ssl_key_password_secret_id(self):
        """
        Gets the ssl_key_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret that stores the password for the cert inside the KeyStore.
        In case it differs from the KeyStore password, it should be provided.
        Note: When provided, 'sslKeyPassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The ssl_key_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._ssl_key_password_secret_id

    @ssl_key_password_secret_id.setter
    def ssl_key_password_secret_id(self, ssl_key_password_secret_id):
        """
        Sets the ssl_key_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        The `OCID`__ of the Secret that stores the password for the cert inside the KeyStore.
        In case it differs from the KeyStore password, it should be provided.
        Note: When provided, 'sslKeyPassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param ssl_key_password_secret_id: The ssl_key_password_secret_id of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._ssl_key_password_secret_id = ssl_key_password_secret_id

    @property
    def private_ip(self):
        """
        Gets the private_ip of this UpdateKafkaSchemaRegistryConnectionDetails.
        Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
        field, or make sure the host name is resolvable in the target VCN.

        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this UpdateKafkaSchemaRegistryConnectionDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this UpdateKafkaSchemaRegistryConnectionDetails.
        Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
        field, or make sure the host name is resolvable in the target VCN.

        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this UpdateKafkaSchemaRegistryConnectionDetails.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
