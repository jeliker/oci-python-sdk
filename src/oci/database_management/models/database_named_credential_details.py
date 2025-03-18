# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .database_credential_details import DatabaseCredentialDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseNamedCredentialDetails(DatabaseCredentialDetails):
    """
    User provides a named credential OCID, which will be used to retrieve the password to connect to the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseNamedCredentialDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DatabaseNamedCredentialDetails.credential_type` attribute
        of this class is ``NAMED_CREDENTIAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this DatabaseNamedCredentialDetails.
            Allowed values for this property are: "SECRET", "PASSWORD", "NAMED_CREDENTIAL"
        :type credential_type: str

        :param named_credential_id:
            The value to assign to the named_credential_id property of this DatabaseNamedCredentialDetails.
        :type named_credential_id: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'named_credential_id': 'str'
        }
        self.attribute_map = {
            'credential_type': 'credentialType',
            'named_credential_id': 'namedCredentialId'
        }
        self._credential_type = None
        self._named_credential_id = None
        self._credential_type = 'NAMED_CREDENTIAL'

    @property
    def named_credential_id(self):
        """
        **[Required]** Gets the named_credential_id of this DatabaseNamedCredentialDetails.
        The `OCID`__ of the named credential
        where the database password metadata is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The named_credential_id of this DatabaseNamedCredentialDetails.
        :rtype: str
        """
        return self._named_credential_id

    @named_credential_id.setter
    def named_credential_id(self, named_credential_id):
        """
        Sets the named_credential_id of this DatabaseNamedCredentialDetails.
        The `OCID`__ of the named credential
        where the database password metadata is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param named_credential_id: The named_credential_id of this DatabaseNamedCredentialDetails.
        :type: str
        """
        self._named_credential_id = named_credential_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
