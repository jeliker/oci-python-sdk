# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeKeyStoreTypeDetails(object):
    """
    Request details to change the source of the encryption key for the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeKeyStoreTypeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_store_id:
            The value to assign to the key_store_id property of this ChangeKeyStoreTypeDetails.
        :type key_store_id: str

        """
        self.swagger_types = {
            'key_store_id': 'str'
        }

        self.attribute_map = {
            'key_store_id': 'keyStoreId'
        }

        self._key_store_id = None

    @property
    def key_store_id(self):
        """
        **[Required]** Gets the key_store_id of this ChangeKeyStoreTypeDetails.
        The `OCID`__ of the key store.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_store_id of this ChangeKeyStoreTypeDetails.
        :rtype: str
        """
        return self._key_store_id

    @key_store_id.setter
    def key_store_id(self, key_store_id):
        """
        Sets the key_store_id of this ChangeKeyStoreTypeDetails.
        The `OCID`__ of the key store.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_store_id: The key_store_id of this ChangeKeyStoreTypeDetails.
        :type: str
        """
        self._key_store_id = key_store_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
