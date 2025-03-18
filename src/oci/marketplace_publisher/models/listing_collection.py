# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListingCollection(object):
    """
    Results of listing search. Contains Listing items.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ListingCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this ListingCollection.
        :type items: list[oci.marketplace_publisher.models.ListingSummary]

        """
        self.swagger_types = {
            'items': 'list[ListingSummary]'
        }
        self.attribute_map = {
            'items': 'items'
        }
        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this ListingCollection.
        List of listing summary.


        :return: The items of this ListingCollection.
        :rtype: list[oci.marketplace_publisher.models.ListingSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ListingCollection.
        List of listing summary.


        :param items: The items of this ListingCollection.
        :type: list[oci.marketplace_publisher.models.ListingSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
