# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Resource(object):
    """
    Details about the ticket item object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Resource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param item:
            The value to assign to the item property of this Resource.
        :type item: oci.cims.models.Item

        :param region:
            The value to assign to the region property of this Resource.
        :type region: str

        """
        self.swagger_types = {
            'item': 'Item',
            'region': 'str'
        }
        self.attribute_map = {
            'item': 'item',
            'region': 'region'
        }
        self._item = None
        self._region = None

    @property
    def item(self):
        """
        Gets the item of this Resource.

        :return: The item of this Resource.
        :rtype: oci.cims.models.Item
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this Resource.

        :param item: The item of this Resource.
        :type: oci.cims.models.Item
        """
        self._item = item

    @property
    def region(self):
        """
        Gets the region of this Resource.
        The list of available Oracle Cloud Infrastructure regions.


        :return: The region of this Resource.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Resource.
        The list of available Oracle Cloud Infrastructure regions.


        :param region: The region of this Resource.
        :type: str
        """
        self._region = region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
