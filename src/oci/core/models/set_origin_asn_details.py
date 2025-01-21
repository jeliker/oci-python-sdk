# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SetOriginAsnDetails(object):
    """
    Update Origin ASN of a BYOIP Range
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SetOriginAsnDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param byoasn_id:
            The value to assign to the byoasn_id property of this SetOriginAsnDetails.
        :type byoasn_id: str

        :param as_path_prepend_length:
            The value to assign to the as_path_prepend_length property of this SetOriginAsnDetails.
        :type as_path_prepend_length: int

        """
        self.swagger_types = {
            'byoasn_id': 'str',
            'as_path_prepend_length': 'int'
        }

        self.attribute_map = {
            'byoasn_id': 'byoasnId',
            'as_path_prepend_length': 'asPathPrependLength'
        }

        self._byoasn_id = None
        self._as_path_prepend_length = None

    @property
    def byoasn_id(self):
        """
        **[Required]** Gets the byoasn_id of this SetOriginAsnDetails.
        The `OCID`__ of the `Byoasn` Resource to be associated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The byoasn_id of this SetOriginAsnDetails.
        :rtype: str
        """
        return self._byoasn_id

    @byoasn_id.setter
    def byoasn_id(self, byoasn_id):
        """
        Sets the byoasn_id of this SetOriginAsnDetails.
        The `OCID`__ of the `Byoasn` Resource to be associated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param byoasn_id: The byoasn_id of this SetOriginAsnDetails.
        :type: str
        """
        self._byoasn_id = byoasn_id

    @property
    def as_path_prepend_length(self):
        """
        Gets the as_path_prepend_length of this SetOriginAsnDetails.
        The as path prepend length.


        :return: The as_path_prepend_length of this SetOriginAsnDetails.
        :rtype: int
        """
        return self._as_path_prepend_length

    @as_path_prepend_length.setter
    def as_path_prepend_length(self, as_path_prepend_length):
        """
        Sets the as_path_prepend_length of this SetOriginAsnDetails.
        The as path prepend length.


        :param as_path_prepend_length: The as_path_prepend_length of this SetOriginAsnDetails.
        :type: int
        """
        self._as_path_prepend_length = as_path_prepend_length

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
