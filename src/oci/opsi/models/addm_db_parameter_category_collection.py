# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmDbParameterCategoryCollection(object):
    """
    List of database parameter categories
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmDbParameterCategoryCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_details_items:
            The value to assign to the database_details_items property of this AddmDbParameterCategoryCollection.
        :type database_details_items: list[oci.opsi.models.DatabaseDetails]

        :param items:
            The value to assign to the items property of this AddmDbParameterCategoryCollection.
        :type items: list[oci.opsi.models.AddmDbParameterCategorySummary]

        """
        self.swagger_types = {
            'database_details_items': 'list[DatabaseDetails]',
            'items': 'list[AddmDbParameterCategorySummary]'
        }
        self.attribute_map = {
            'database_details_items': 'databaseDetailsItems',
            'items': 'items'
        }
        self._database_details_items = None
        self._items = None

    @property
    def database_details_items(self):
        """
        **[Required]** Gets the database_details_items of this AddmDbParameterCategoryCollection.
        List of database details data


        :return: The database_details_items of this AddmDbParameterCategoryCollection.
        :rtype: list[oci.opsi.models.DatabaseDetails]
        """
        return self._database_details_items

    @database_details_items.setter
    def database_details_items(self, database_details_items):
        """
        Sets the database_details_items of this AddmDbParameterCategoryCollection.
        List of database details data


        :param database_details_items: The database_details_items of this AddmDbParameterCategoryCollection.
        :type: list[oci.opsi.models.DatabaseDetails]
        """
        self._database_details_items = database_details_items

    @property
    def items(self):
        """
        **[Required]** Gets the items of this AddmDbParameterCategoryCollection.
        List of database parameter categories


        :return: The items of this AddmDbParameterCategoryCollection.
        :rtype: list[oci.opsi.models.AddmDbParameterCategorySummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AddmDbParameterCategoryCollection.
        List of database parameter categories


        :param items: The items of this AddmDbParameterCategoryCollection.
        :type: list[oci.opsi.models.AddmDbParameterCategorySummary]
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
