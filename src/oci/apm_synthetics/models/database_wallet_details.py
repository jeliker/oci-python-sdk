# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseWalletDetails(object):
    """
    Details for database wallet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseWalletDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_wallet:
            The value to assign to the database_wallet property of this DatabaseWalletDetails.
        :type database_wallet: str

        :param service_name:
            The value to assign to the service_name property of this DatabaseWalletDetails.
        :type service_name: str

        """
        self.swagger_types = {
            'database_wallet': 'str',
            'service_name': 'str'
        }
        self.attribute_map = {
            'database_wallet': 'databaseWallet',
            'service_name': 'serviceName'
        }
        self._database_wallet = None
        self._service_name = None

    @property
    def database_wallet(self):
        """
        **[Required]** Gets the database_wallet of this DatabaseWalletDetails.
        The database wallet configuration zip file.


        :return: The database_wallet of this DatabaseWalletDetails.
        :rtype: str
        """
        return self._database_wallet

    @database_wallet.setter
    def database_wallet(self, database_wallet):
        """
        Sets the database_wallet of this DatabaseWalletDetails.
        The database wallet configuration zip file.


        :param database_wallet: The database_wallet of this DatabaseWalletDetails.
        :type: str
        """
        self._database_wallet = database_wallet

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this DatabaseWalletDetails.
        Service name of the database.


        :return: The service_name of this DatabaseWalletDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this DatabaseWalletDetails.
        Service name of the database.


        :param service_name: The service_name of this DatabaseWalletDetails.
        :type: str
        """
        self._service_name = service_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
