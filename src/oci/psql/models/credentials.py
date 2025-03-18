# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Credentials(object):
    """
    Initial database system credentials that the database system will be provisioned with.
    The password details are not visible on any subsequent operation, such as GET /dbSystems/{dbSystemId}.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Credentials object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param username:
            The value to assign to the username property of this Credentials.
        :type username: str

        :param password_details:
            The value to assign to the password_details property of this Credentials.
        :type password_details: oci.psql.models.PasswordDetails

        """
        self.swagger_types = {
            'username': 'str',
            'password_details': 'PasswordDetails'
        }
        self.attribute_map = {
            'username': 'username',
            'password_details': 'passwordDetails'
        }
        self._username = None
        self._password_details = None

    @property
    def username(self):
        """
        **[Required]** Gets the username of this Credentials.
        The database system administrator username.


        :return: The username of this Credentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this Credentials.
        The database system administrator username.


        :param username: The username of this Credentials.
        :type: str
        """
        self._username = username

    @property
    def password_details(self):
        """
        **[Required]** Gets the password_details of this Credentials.

        :return: The password_details of this Credentials.
        :rtype: oci.psql.models.PasswordDetails
        """
        return self._password_details

    @password_details.setter
    def password_details(self, password_details):
        """
        Sets the password_details of this Credentials.

        :param password_details: The password_details of this Credentials.
        :type: oci.psql.models.PasswordDetails
        """
        self._password_details = password_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
