# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831

from .product_stack_sub_category_details import ProductStackSubCategoryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProductStackAsProductSubCategoryDetails(ProductStackSubCategoryDetails):
    """
    Consider Product stack as product.To be provided if the product stack should be considered as a Product also.
    Allows compliance reporting and patching against the product stack target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProductStackAsProductSubCategoryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.ProductStackAsProductSubCategoryDetails.sub_category` attribute
        of this class is ``PRODUCT_STACK_AS_PRODUCT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sub_category:
            The value to assign to the sub_category property of this ProductStackAsProductSubCategoryDetails.
            Allowed values for this property are: "PRODUCT_STACK_GENERIC", "PRODUCT_STACK_AS_PRODUCT"
        :type sub_category: str

        :param versions:
            The value to assign to the versions property of this ProductStackAsProductSubCategoryDetails.
        :type versions: list[str]

        :param credentials:
            The value to assign to the credentials property of this ProductStackAsProductSubCategoryDetails.
        :type credentials: list[oci.fleet_apps_management.models.ConfigAssociationDetails]

        :param components:
            The value to assign to the components property of this ProductStackAsProductSubCategoryDetails.
        :type components: list[str]

        :param patch_types:
            The value to assign to the patch_types property of this ProductStackAsProductSubCategoryDetails.
        :type patch_types: list[oci.fleet_apps_management.models.ConfigAssociationDetails]

        """
        self.swagger_types = {
            'sub_category': 'str',
            'versions': 'list[str]',
            'credentials': 'list[ConfigAssociationDetails]',
            'components': 'list[str]',
            'patch_types': 'list[ConfigAssociationDetails]'
        }
        self.attribute_map = {
            'sub_category': 'subCategory',
            'versions': 'versions',
            'credentials': 'credentials',
            'components': 'components',
            'patch_types': 'patchTypes'
        }
        self._sub_category = None
        self._versions = None
        self._credentials = None
        self._components = None
        self._patch_types = None
        self._sub_category = 'PRODUCT_STACK_AS_PRODUCT'

    @property
    def versions(self):
        """
        **[Required]** Gets the versions of this ProductStackAsProductSubCategoryDetails.
        Versions associated with the PRODUCT .


        :return: The versions of this ProductStackAsProductSubCategoryDetails.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """
        Sets the versions of this ProductStackAsProductSubCategoryDetails.
        Versions associated with the PRODUCT .


        :param versions: The versions of this ProductStackAsProductSubCategoryDetails.
        :type: list[str]
        """
        self._versions = versions

    @property
    def credentials(self):
        """
        Gets the credentials of this ProductStackAsProductSubCategoryDetails.
        OCID for the Credential name to be associated with the Product Stack.
        These are useful for target discovery or lifecycle management activities, for example, Oracle WebLogic admin credentials for Oracle WebLogic Application server.


        :return: The credentials of this ProductStackAsProductSubCategoryDetails.
        :rtype: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ProductStackAsProductSubCategoryDetails.
        OCID for the Credential name to be associated with the Product Stack.
        These are useful for target discovery or lifecycle management activities, for example, Oracle WebLogic admin credentials for Oracle WebLogic Application server.


        :param credentials: The credentials of this ProductStackAsProductSubCategoryDetails.
        :type: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        self._credentials = credentials

    @property
    def components(self):
        """
        Gets the components of this ProductStackAsProductSubCategoryDetails.
        Various components of the Product.
        For example:The administration server or node manager can be the components of the Oracle WebLogic Application server.
        Forms server or concurrent manager can be the components of the Oracle E-Business Suite.


        :return: The components of this ProductStackAsProductSubCategoryDetails.
        :rtype: list[str]
        """
        return self._components

    @components.setter
    def components(self, components):
        """
        Sets the components of this ProductStackAsProductSubCategoryDetails.
        Various components of the Product.
        For example:The administration server or node manager can be the components of the Oracle WebLogic Application server.
        Forms server or concurrent manager can be the components of the Oracle E-Business Suite.


        :param components: The components of this ProductStackAsProductSubCategoryDetails.
        :type: list[str]
        """
        self._components = components

    @property
    def patch_types(self):
        """
        Gets the patch_types of this ProductStackAsProductSubCategoryDetails.
        Patch Types associated with this Product Stack which will be considered as Product.


        :return: The patch_types of this ProductStackAsProductSubCategoryDetails.
        :rtype: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        return self._patch_types

    @patch_types.setter
    def patch_types(self, patch_types):
        """
        Sets the patch_types of this ProductStackAsProductSubCategoryDetails.
        Patch Types associated with this Product Stack which will be considered as Product.


        :param patch_types: The patch_types of this ProductStackAsProductSubCategoryDetails.
        :type: list[oci.fleet_apps_management.models.ConfigAssociationDetails]
        """
        self._patch_types = patch_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
