# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOkeBackupLocationDetails(object):
    """
    The details for updating the backup location of an OKE Cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOkeBackupLocationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this UpdateOkeBackupLocationDetails.
        :type namespace: str

        :param bucket:
            The value to assign to the bucket property of this UpdateOkeBackupLocationDetails.
        :type bucket: str

        """
        self.swagger_types = {
            'namespace': 'str',
            'bucket': 'str'
        }
        self.attribute_map = {
            'namespace': 'namespace',
            'bucket': 'bucket'
        }
        self._namespace = None
        self._bucket = None

    @property
    def namespace(self):
        """
        Gets the namespace of this UpdateOkeBackupLocationDetails.
        The namespace in the object storage backup location (Note - this is usually the tenancy name).

        Example: `myocitenancy`


        :return: The namespace of this UpdateOkeBackupLocationDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UpdateOkeBackupLocationDetails.
        The namespace in the object storage backup location (Note - this is usually the tenancy name).

        Example: `myocitenancy`


        :param namespace: The namespace of this UpdateOkeBackupLocationDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket(self):
        """
        Gets the bucket of this UpdateOkeBackupLocationDetails.
        The bucket name inside the object storage namespace.

        Example: `operation_logs`


        :return: The bucket of this UpdateOkeBackupLocationDetails.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this UpdateOkeBackupLocationDetails.
        The bucket name inside the object storage namespace.

        Example: `operation_logs`


        :param bucket: The bucket of this UpdateOkeBackupLocationDetails.
        :type: str
        """
        self._bucket = bucket

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
