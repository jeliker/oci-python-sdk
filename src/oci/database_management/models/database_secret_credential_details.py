# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .database_credential_details import DatabaseCredentialDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseSecretCredentialDetails(DatabaseCredentialDetails):
    """
    User provides a secret OCID, which will be used to retrieve the password to connect to the database.
    """

    #: A constant which can be used with the role property of a DatabaseSecretCredentialDetails.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a DatabaseSecretCredentialDetails.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    #: A constant which can be used with the role property of a DatabaseSecretCredentialDetails.
    #: This constant has a value of "SYSDG"
    ROLE_SYSDG = "SYSDG"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseSecretCredentialDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DatabaseSecretCredentialDetails.credential_type` attribute
        of this class is ``SECRET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this DatabaseSecretCredentialDetails.
            Allowed values for this property are: "SECRET", "PASSWORD", "NAMED_CREDENTIAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this DatabaseSecretCredentialDetails.
        :type password_secret_id: str

        :param username:
            The value to assign to the username property of this DatabaseSecretCredentialDetails.
        :type username: str

        :param role:
            The value to assign to the role property of this DatabaseSecretCredentialDetails.
            Allowed values for this property are: "NORMAL", "SYSDBA", "SYSDG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'password_secret_id': 'str',
            'username': 'str',
            'role': 'str'
        }
        self.attribute_map = {
            'credential_type': 'credentialType',
            'password_secret_id': 'passwordSecretId',
            'username': 'username',
            'role': 'role'
        }
        self._credential_type = None
        self._password_secret_id = None
        self._username = None
        self._role = None
        self._credential_type = 'SECRET'

    @property
    def password_secret_id(self):
        """
        **[Required]** Gets the password_secret_id of this DatabaseSecretCredentialDetails.
        The `OCID`__ of the Secret
        where the database password is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this DatabaseSecretCredentialDetails.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this DatabaseSecretCredentialDetails.
        The `OCID`__ of the Secret
        where the database password is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this DatabaseSecretCredentialDetails.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def username(self):
        """
        Gets the username of this DatabaseSecretCredentialDetails.
        The user to connect to the database.


        :return: The username of this DatabaseSecretCredentialDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DatabaseSecretCredentialDetails.
        The user to connect to the database.


        :param username: The username of this DatabaseSecretCredentialDetails.
        :type: str
        """
        self._username = username

    @property
    def role(self):
        """
        Gets the role of this DatabaseSecretCredentialDetails.
        The role of the database user.

        Allowed values for this property are: "NORMAL", "SYSDBA", "SYSDG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this DatabaseSecretCredentialDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this DatabaseSecretCredentialDetails.
        The role of the database user.


        :param role: The role of this DatabaseSecretCredentialDetails.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA", "SYSDG"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
