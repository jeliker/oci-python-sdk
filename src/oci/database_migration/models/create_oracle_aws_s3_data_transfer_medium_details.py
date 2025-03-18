# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .create_oracle_data_transfer_medium_details import CreateOracleDataTransferMediumDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOracleAwsS3DataTransferMediumDetails(CreateOracleDataTransferMediumDetails):
    """
    AWS S3 bucket details used for source Connection resources with RDS_ORACLE type.
    Only supported for source Connection resources with RDS_ORACLE type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOracleAwsS3DataTransferMediumDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.CreateOracleAwsS3DataTransferMediumDetails.type` attribute
        of this class is ``AWS_S3`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateOracleAwsS3DataTransferMediumDetails.
            Allowed values for this property are: "DBLINK", "OBJECT_STORAGE", "AWS_S3", "NFS"
        :type type: str

        :param name:
            The value to assign to the name property of this CreateOracleAwsS3DataTransferMediumDetails.
        :type name: str

        :param region:
            The value to assign to the region property of this CreateOracleAwsS3DataTransferMediumDetails.
        :type region: str

        :param access_key_id:
            The value to assign to the access_key_id property of this CreateOracleAwsS3DataTransferMediumDetails.
        :type access_key_id: str

        :param secret_access_key:
            The value to assign to the secret_access_key property of this CreateOracleAwsS3DataTransferMediumDetails.
        :type secret_access_key: str

        :param object_storage_bucket:
            The value to assign to the object_storage_bucket property of this CreateOracleAwsS3DataTransferMediumDetails.
        :type object_storage_bucket: oci.database_migration.models.ObjectStoreBucket

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'region': 'str',
            'access_key_id': 'str',
            'secret_access_key': 'str',
            'object_storage_bucket': 'ObjectStoreBucket'
        }
        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'region': 'region',
            'access_key_id': 'accessKeyId',
            'secret_access_key': 'secretAccessKey',
            'object_storage_bucket': 'objectStorageBucket'
        }
        self._type = None
        self._name = None
        self._region = None
        self._access_key_id = None
        self._secret_access_key = None
        self._object_storage_bucket = None
        self._type = 'AWS_S3'

    @property
    def name(self):
        """
        Gets the name of this CreateOracleAwsS3DataTransferMediumDetails.
        S3 bucket name.


        :return: The name of this CreateOracleAwsS3DataTransferMediumDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateOracleAwsS3DataTransferMediumDetails.
        S3 bucket name.


        :param name: The name of this CreateOracleAwsS3DataTransferMediumDetails.
        :type: str
        """
        self._name = name

    @property
    def region(self):
        """
        Gets the region of this CreateOracleAwsS3DataTransferMediumDetails.
        AWS region code where the S3 bucket is located.
        Region code should match the documented available regions:
        https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions


        :return: The region of this CreateOracleAwsS3DataTransferMediumDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CreateOracleAwsS3DataTransferMediumDetails.
        AWS region code where the S3 bucket is located.
        Region code should match the documented available regions:
        https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions


        :param region: The region of this CreateOracleAwsS3DataTransferMediumDetails.
        :type: str
        """
        self._region = region

    @property
    def access_key_id(self):
        """
        Gets the access_key_id of this CreateOracleAwsS3DataTransferMediumDetails.
        AWS access key credentials identifier
        Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys


        :return: The access_key_id of this CreateOracleAwsS3DataTransferMediumDetails.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """
        Sets the access_key_id of this CreateOracleAwsS3DataTransferMediumDetails.
        AWS access key credentials identifier
        Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys


        :param access_key_id: The access_key_id of this CreateOracleAwsS3DataTransferMediumDetails.
        :type: str
        """
        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        """
        Gets the secret_access_key of this CreateOracleAwsS3DataTransferMediumDetails.
        AWS secret access key credentials
        Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys


        :return: The secret_access_key of this CreateOracleAwsS3DataTransferMediumDetails.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """
        Sets the secret_access_key of this CreateOracleAwsS3DataTransferMediumDetails.
        AWS secret access key credentials
        Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys


        :param secret_access_key: The secret_access_key of this CreateOracleAwsS3DataTransferMediumDetails.
        :type: str
        """
        self._secret_access_key = secret_access_key

    @property
    def object_storage_bucket(self):
        """
        Gets the object_storage_bucket of this CreateOracleAwsS3DataTransferMediumDetails.

        :return: The object_storage_bucket of this CreateOracleAwsS3DataTransferMediumDetails.
        :rtype: oci.database_migration.models.ObjectStoreBucket
        """
        return self._object_storage_bucket

    @object_storage_bucket.setter
    def object_storage_bucket(self, object_storage_bucket):
        """
        Sets the object_storage_bucket of this CreateOracleAwsS3DataTransferMediumDetails.

        :param object_storage_bucket: The object_storage_bucket of this CreateOracleAwsS3DataTransferMediumDetails.
        :type: oci.database_migration.models.ObjectStoreBucket
        """
        self._object_storage_bucket = object_storage_bucket

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
