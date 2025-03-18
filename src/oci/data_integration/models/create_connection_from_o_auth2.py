# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionFromOAuth2(CreateConnectionDetails):
    """
    The details to create a OAuth2 connection
    """

    #: A constant which can be used with the grant_type property of a CreateConnectionFromOAuth2.
    #: This constant has a value of "CLIENT_CREDENTIALS"
    GRANT_TYPE_CLIENT_CREDENTIALS = "CLIENT_CREDENTIALS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionFromOAuth2 object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateConnectionFromOAuth2.model_type` attribute
        of this class is ``OAUTH2_CONNECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateConnectionFromOAuth2.
            Allowed values for this property are: "ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION", "MYSQL_CONNECTION", "GENERIC_JDBC_CONNECTION", "BICC_CONNECTION", "AMAZON_S3_CONNECTION", "BIP_CONNECTION", "LAKE_CONNECTION", "ORACLE_PEOPLESOFT_CONNECTION", "ORACLE_EBS_CONNECTION", "ORACLE_SIEBEL_CONNECTION", "HDFS_CONNECTION", "MYSQL_HEATWAVE_CONNECTION", "REST_NO_AUTH_CONNECTION", "REST_BASIC_AUTH_CONNECTION", "OAUTH2_CONNECTION"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateConnectionFromOAuth2.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateConnectionFromOAuth2.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateConnectionFromOAuth2.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateConnectionFromOAuth2.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateConnectionFromOAuth2.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateConnectionFromOAuth2.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateConnectionFromOAuth2.
        :type identifier: str

        :param connection_properties:
            The value to assign to the connection_properties property of this CreateConnectionFromOAuth2.
        :type connection_properties: list[oci.data_integration.models.ConnectionProperty]

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateConnectionFromOAuth2.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param access_token_url:
            The value to assign to the access_token_url property of this CreateConnectionFromOAuth2.
        :type access_token_url: str

        :param client_id:
            The value to assign to the client_id property of this CreateConnectionFromOAuth2.
        :type client_id: str

        :param client_secret:
            The value to assign to the client_secret property of this CreateConnectionFromOAuth2.
        :type client_secret: oci.data_integration.models.SensitiveAttribute

        :param scope:
            The value to assign to the scope property of this CreateConnectionFromOAuth2.
        :type scope: str

        :param grant_type:
            The value to assign to the grant_type property of this CreateConnectionFromOAuth2.
            Allowed values for this property are: "CLIENT_CREDENTIALS"
        :type grant_type: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'connection_properties': 'list[ConnectionProperty]',
            'registry_metadata': 'RegistryMetadata',
            'access_token_url': 'str',
            'client_id': 'str',
            'client_secret': 'SensitiveAttribute',
            'scope': 'str',
            'grant_type': 'str'
        }
        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'connection_properties': 'connectionProperties',
            'registry_metadata': 'registryMetadata',
            'access_token_url': 'accessTokenUrl',
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'scope': 'scope',
            'grant_type': 'grantType'
        }
        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._connection_properties = None
        self._registry_metadata = None
        self._access_token_url = None
        self._client_id = None
        self._client_secret = None
        self._scope = None
        self._grant_type = None
        self._model_type = 'OAUTH2_CONNECTION'

    @property
    def access_token_url(self):
        """
        **[Required]** Gets the access_token_url of this CreateConnectionFromOAuth2.
        Specifies the endpoint used to exchange authentication credentials for access tokens


        :return: The access_token_url of this CreateConnectionFromOAuth2.
        :rtype: str
        """
        return self._access_token_url

    @access_token_url.setter
    def access_token_url(self, access_token_url):
        """
        Sets the access_token_url of this CreateConnectionFromOAuth2.
        Specifies the endpoint used to exchange authentication credentials for access tokens


        :param access_token_url: The access_token_url of this CreateConnectionFromOAuth2.
        :type: str
        """
        self._access_token_url = access_token_url

    @property
    def client_id(self):
        """
        Gets the client_id of this CreateConnectionFromOAuth2.
        Specifies the client ID key for specific application


        :return: The client_id of this CreateConnectionFromOAuth2.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CreateConnectionFromOAuth2.
        Specifies the client ID key for specific application


        :param client_id: The client_id of this CreateConnectionFromOAuth2.
        :type: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        """
        Gets the client_secret of this CreateConnectionFromOAuth2.

        :return: The client_secret of this CreateConnectionFromOAuth2.
        :rtype: oci.data_integration.models.SensitiveAttribute
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this CreateConnectionFromOAuth2.

        :param client_secret: The client_secret of this CreateConnectionFromOAuth2.
        :type: oci.data_integration.models.SensitiveAttribute
        """
        self._client_secret = client_secret

    @property
    def scope(self):
        """
        Gets the scope of this CreateConnectionFromOAuth2.
        Specifies the OAuth scopes that limit the permissions granted by an access token.


        :return: The scope of this CreateConnectionFromOAuth2.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this CreateConnectionFromOAuth2.
        Specifies the OAuth scopes that limit the permissions granted by an access token.


        :param scope: The scope of this CreateConnectionFromOAuth2.
        :type: str
        """
        self._scope = scope

    @property
    def grant_type(self):
        """
        Gets the grant_type of this CreateConnectionFromOAuth2.
        Specifies the OAuth2 grant mechanism. Example CLIENT_CREDENTIALS, Implicit Flow etc.

        Allowed values for this property are: "CLIENT_CREDENTIALS"


        :return: The grant_type of this CreateConnectionFromOAuth2.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """
        Sets the grant_type of this CreateConnectionFromOAuth2.
        Specifies the OAuth2 grant mechanism. Example CLIENT_CREDENTIALS, Implicit Flow etc.


        :param grant_type: The grant_type of this CreateConnectionFromOAuth2.
        :type: str
        """
        allowed_values = ["CLIENT_CREDENTIALS"]
        if not value_allowed_none_or_none_sentinel(grant_type, allowed_values):
            raise ValueError(
                f"Invalid value for `grant_type`, must be None or one of {allowed_values}"
            )
        self._grant_type = grant_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
