# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .update_oracle_data_transfer_medium_details import UpdateOracleDataTransferMediumDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOracleDbLinkDataTransferMediumDetails(UpdateOracleDataTransferMediumDetails):
    """
    Optional details for creating a network database link from OCI database to on-premise database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOracleDbLinkDataTransferMediumDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.UpdateOracleDbLinkDataTransferMediumDetails.type` attribute
        of this class is ``DBLINK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateOracleDbLinkDataTransferMediumDetails.
            Allowed values for this property are: "DBLINK", "OBJECT_STORAGE", "AWS_S3", "NFS"
        :type type: str

        :param object_storage_bucket:
            The value to assign to the object_storage_bucket property of this UpdateOracleDbLinkDataTransferMediumDetails.
        :type object_storage_bucket: oci.database_migration.models.UpdateObjectStoreBucket

        :param name:
            The value to assign to the name property of this UpdateOracleDbLinkDataTransferMediumDetails.
        :type name: str

        """
        self.swagger_types = {
            'type': 'str',
            'object_storage_bucket': 'UpdateObjectStoreBucket',
            'name': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'object_storage_bucket': 'objectStorageBucket',
            'name': 'name'
        }
        self._type = None
        self._object_storage_bucket = None
        self._name = None
        self._type = 'DBLINK'

    @property
    def object_storage_bucket(self):
        """
        Gets the object_storage_bucket of this UpdateOracleDbLinkDataTransferMediumDetails.

        :return: The object_storage_bucket of this UpdateOracleDbLinkDataTransferMediumDetails.
        :rtype: oci.database_migration.models.UpdateObjectStoreBucket
        """
        return self._object_storage_bucket

    @object_storage_bucket.setter
    def object_storage_bucket(self, object_storage_bucket):
        """
        Sets the object_storage_bucket of this UpdateOracleDbLinkDataTransferMediumDetails.

        :param object_storage_bucket: The object_storage_bucket of this UpdateOracleDbLinkDataTransferMediumDetails.
        :type: oci.database_migration.models.UpdateObjectStoreBucket
        """
        self._object_storage_bucket = object_storage_bucket

    @property
    def name(self):
        """
        Gets the name of this UpdateOracleDbLinkDataTransferMediumDetails.
        Name of database link from OCI database to on-premise database. ODMS will create link,
        if the link does not already exist.


        :return: The name of this UpdateOracleDbLinkDataTransferMediumDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateOracleDbLinkDataTransferMediumDetails.
        Name of database link from OCI database to on-premise database. ODMS will create link,
        if the link does not already exist.


        :param name: The name of this UpdateOracleDbLinkDataTransferMediumDetails.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
