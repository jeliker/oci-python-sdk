# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201005

from .database_tools_connection import DatabaseToolsConnection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsConnectionGenericJdbc(DatabaseToolsConnection):
    """
    Database Tools connection of a Generic JDBC database system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsConnectionGenericJdbc object with values from keyword arguments. The default value of the :py:attr:`~oci.database_tools.models.DatabaseToolsConnectionGenericJdbc.type` attribute
        of this class is ``GENERIC_JDBC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DatabaseToolsConnectionGenericJdbc.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DatabaseToolsConnectionGenericJdbc.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseToolsConnectionGenericJdbc.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseToolsConnectionGenericJdbc.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "INACTIVE"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseToolsConnectionGenericJdbc.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this DatabaseToolsConnectionGenericJdbc.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatabaseToolsConnectionGenericJdbc.
        :type time_updated: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseToolsConnectionGenericJdbc.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseToolsConnectionGenericJdbc.
        :type freeform_tags: dict(str, str)

        :param system_tags:
            The value to assign to the system_tags property of this DatabaseToolsConnectionGenericJdbc.
        :type system_tags: dict(str, dict(str, object))

        :param locks:
            The value to assign to the locks property of this DatabaseToolsConnectionGenericJdbc.
        :type locks: list[oci.database_tools.models.ResourceLock]

        :param type:
            The value to assign to the type property of this DatabaseToolsConnectionGenericJdbc.
            Allowed values for this property are: "ORACLE_DATABASE", "MYSQL", "POSTGRESQL", "GENERIC_JDBC"
        :type type: str

        :param runtime_support:
            The value to assign to the runtime_support property of this DatabaseToolsConnectionGenericJdbc.
            Allowed values for this property are: "SUPPORTED", "UNSUPPORTED"
        :type runtime_support: str

        :param url:
            The value to assign to the url property of this DatabaseToolsConnectionGenericJdbc.
        :type url: str

        :param user_name:
            The value to assign to the user_name property of this DatabaseToolsConnectionGenericJdbc.
        :type user_name: str

        :param user_password:
            The value to assign to the user_password property of this DatabaseToolsConnectionGenericJdbc.
        :type user_password: oci.database_tools.models.DatabaseToolsUserPassword

        :param advanced_properties:
            The value to assign to the advanced_properties property of this DatabaseToolsConnectionGenericJdbc.
        :type advanced_properties: dict(str, str)

        :param key_stores:
            The value to assign to the key_stores property of this DatabaseToolsConnectionGenericJdbc.
        :type key_stores: list[oci.database_tools.models.DatabaseToolsKeyStoreGenericJdbc]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'system_tags': 'dict(str, dict(str, object))',
            'locks': 'list[ResourceLock]',
            'type': 'str',
            'runtime_support': 'str',
            'url': 'str',
            'user_name': 'str',
            'user_password': 'DatabaseToolsUserPassword',
            'advanced_properties': 'dict(str, str)',
            'key_stores': 'list[DatabaseToolsKeyStoreGenericJdbc]'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'system_tags': 'systemTags',
            'locks': 'locks',
            'type': 'type',
            'runtime_support': 'runtimeSupport',
            'url': 'url',
            'user_name': 'userName',
            'user_password': 'userPassword',
            'advanced_properties': 'advancedProperties',
            'key_stores': 'keyStores'
        }
        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._defined_tags = None
        self._freeform_tags = None
        self._system_tags = None
        self._locks = None
        self._type = None
        self._runtime_support = None
        self._url = None
        self._user_name = None
        self._user_password = None
        self._advanced_properties = None
        self._key_stores = None
        self._type = 'GENERIC_JDBC'

    @property
    def url(self):
        """
        **[Required]** Gets the url of this DatabaseToolsConnectionGenericJdbc.
        The JDBC URL used to connect to the Generic JDBC database system.


        :return: The url of this DatabaseToolsConnectionGenericJdbc.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DatabaseToolsConnectionGenericJdbc.
        The JDBC URL used to connect to the Generic JDBC database system.


        :param url: The url of this DatabaseToolsConnectionGenericJdbc.
        :type: str
        """
        self._url = url

    @property
    def user_name(self):
        """
        Gets the user_name of this DatabaseToolsConnectionGenericJdbc.
        The user name.


        :return: The user_name of this DatabaseToolsConnectionGenericJdbc.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DatabaseToolsConnectionGenericJdbc.
        The user name.


        :param user_name: The user_name of this DatabaseToolsConnectionGenericJdbc.
        :type: str
        """
        self._user_name = user_name

    @property
    def user_password(self):
        """
        Gets the user_password of this DatabaseToolsConnectionGenericJdbc.

        :return: The user_password of this DatabaseToolsConnectionGenericJdbc.
        :rtype: oci.database_tools.models.DatabaseToolsUserPassword
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """
        Sets the user_password of this DatabaseToolsConnectionGenericJdbc.

        :param user_password: The user_password of this DatabaseToolsConnectionGenericJdbc.
        :type: oci.database_tools.models.DatabaseToolsUserPassword
        """
        self._user_password = user_password

    @property
    def advanced_properties(self):
        """
        Gets the advanced_properties of this DatabaseToolsConnectionGenericJdbc.
        The advanced connection properties key-value pair.


        :return: The advanced_properties of this DatabaseToolsConnectionGenericJdbc.
        :rtype: dict(str, str)
        """
        return self._advanced_properties

    @advanced_properties.setter
    def advanced_properties(self, advanced_properties):
        """
        Sets the advanced_properties of this DatabaseToolsConnectionGenericJdbc.
        The advanced connection properties key-value pair.


        :param advanced_properties: The advanced_properties of this DatabaseToolsConnectionGenericJdbc.
        :type: dict(str, str)
        """
        self._advanced_properties = advanced_properties

    @property
    def key_stores(self):
        """
        Gets the key_stores of this DatabaseToolsConnectionGenericJdbc.
        The CA certificate to verify the server's certificate and
        the client private key and associated certificate required for client authentication.


        :return: The key_stores of this DatabaseToolsConnectionGenericJdbc.
        :rtype: list[oci.database_tools.models.DatabaseToolsKeyStoreGenericJdbc]
        """
        return self._key_stores

    @key_stores.setter
    def key_stores(self, key_stores):
        """
        Sets the key_stores of this DatabaseToolsConnectionGenericJdbc.
        The CA certificate to verify the server's certificate and
        the client private key and associated certificate required for client authentication.


        :param key_stores: The key_stores of this DatabaseToolsConnectionGenericJdbc.
        :type: list[oci.database_tools.models.DatabaseToolsKeyStoreGenericJdbc]
        """
        self._key_stores = key_stores

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
