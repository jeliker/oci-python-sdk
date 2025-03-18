# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .create_software_source_details import CreateSoftwareSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVersionedCustomSoftwareSourceDetails(CreateSoftwareSourceDetails):
    """
    Provides the information used to create a versioned custom software source.
    """

    #: A constant which can be used with the software_source_sub_type property of a CreateVersionedCustomSoftwareSourceDetails.
    #: This constant has a value of "FILTER"
    SOFTWARE_SOURCE_SUB_TYPE_FILTER = "FILTER"

    #: A constant which can be used with the software_source_sub_type property of a CreateVersionedCustomSoftwareSourceDetails.
    #: This constant has a value of "MANIFEST"
    SOFTWARE_SOURCE_SUB_TYPE_MANIFEST = "MANIFEST"

    #: A constant which can be used with the software_source_sub_type property of a CreateVersionedCustomSoftwareSourceDetails.
    #: This constant has a value of "SNAPSHOT"
    SOFTWARE_SOURCE_SUB_TYPE_SNAPSHOT = "SNAPSHOT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVersionedCustomSoftwareSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.CreateVersionedCustomSoftwareSourceDetails.software_source_type` attribute
        of this class is ``VERSIONED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVersionedCustomSoftwareSourceDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateVersionedCustomSoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateVersionedCustomSoftwareSourceDetails.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this CreateVersionedCustomSoftwareSourceDetails.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", "PRIVATE", "THIRD_PARTY"
        :type software_source_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVersionedCustomSoftwareSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVersionedCustomSoftwareSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vendor_software_sources:
            The value to assign to the vendor_software_sources property of this CreateVersionedCustomSoftwareSourceDetails.
        :type vendor_software_sources: list[oci.os_management_hub.models.Id]

        :param custom_software_source_filter:
            The value to assign to the custom_software_source_filter property of this CreateVersionedCustomSoftwareSourceDetails.
        :type custom_software_source_filter: oci.os_management_hub.models.CustomSoftwareSourceFilter

        :param software_source_version:
            The value to assign to the software_source_version property of this CreateVersionedCustomSoftwareSourceDetails.
        :type software_source_version: str

        :param is_auto_resolve_dependencies:
            The value to assign to the is_auto_resolve_dependencies property of this CreateVersionedCustomSoftwareSourceDetails.
        :type is_auto_resolve_dependencies: bool

        :param is_created_from_package_list:
            The value to assign to the is_created_from_package_list property of this CreateVersionedCustomSoftwareSourceDetails.
        :type is_created_from_package_list: bool

        :param is_latest_content_only:
            The value to assign to the is_latest_content_only property of this CreateVersionedCustomSoftwareSourceDetails.
        :type is_latest_content_only: bool

        :param packages:
            The value to assign to the packages property of this CreateVersionedCustomSoftwareSourceDetails.
        :type packages: list[str]

        :param software_source_sub_type:
            The value to assign to the software_source_sub_type property of this CreateVersionedCustomSoftwareSourceDetails.
            Allowed values for this property are: "FILTER", "MANIFEST", "SNAPSHOT"
        :type software_source_sub_type: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'software_source_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vendor_software_sources': 'list[Id]',
            'custom_software_source_filter': 'CustomSoftwareSourceFilter',
            'software_source_version': 'str',
            'is_auto_resolve_dependencies': 'bool',
            'is_created_from_package_list': 'bool',
            'is_latest_content_only': 'bool',
            'packages': 'list[str]',
            'software_source_sub_type': 'str'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vendor_software_sources': 'vendorSoftwareSources',
            'custom_software_source_filter': 'customSoftwareSourceFilter',
            'software_source_version': 'softwareSourceVersion',
            'is_auto_resolve_dependencies': 'isAutoResolveDependencies',
            'is_created_from_package_list': 'isCreatedFromPackageList',
            'is_latest_content_only': 'isLatestContentOnly',
            'packages': 'packages',
            'software_source_sub_type': 'softwareSourceSubType'
        }
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._software_source_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vendor_software_sources = None
        self._custom_software_source_filter = None
        self._software_source_version = None
        self._is_auto_resolve_dependencies = None
        self._is_created_from_package_list = None
        self._is_latest_content_only = None
        self._packages = None
        self._software_source_sub_type = None
        self._software_source_type = 'VERSIONED'

    @property
    def vendor_software_sources(self):
        """
        **[Required]** Gets the vendor_software_sources of this CreateVersionedCustomSoftwareSourceDetails.
        List of vendor software sources.


        :return: The vendor_software_sources of this CreateVersionedCustomSoftwareSourceDetails.
        :rtype: list[oci.os_management_hub.models.Id]
        """
        return self._vendor_software_sources

    @vendor_software_sources.setter
    def vendor_software_sources(self, vendor_software_sources):
        """
        Sets the vendor_software_sources of this CreateVersionedCustomSoftwareSourceDetails.
        List of vendor software sources.


        :param vendor_software_sources: The vendor_software_sources of this CreateVersionedCustomSoftwareSourceDetails.
        :type: list[oci.os_management_hub.models.Id]
        """
        self._vendor_software_sources = vendor_software_sources

    @property
    def custom_software_source_filter(self):
        """
        Gets the custom_software_source_filter of this CreateVersionedCustomSoftwareSourceDetails.

        :return: The custom_software_source_filter of this CreateVersionedCustomSoftwareSourceDetails.
        :rtype: oci.os_management_hub.models.CustomSoftwareSourceFilter
        """
        return self._custom_software_source_filter

    @custom_software_source_filter.setter
    def custom_software_source_filter(self, custom_software_source_filter):
        """
        Sets the custom_software_source_filter of this CreateVersionedCustomSoftwareSourceDetails.

        :param custom_software_source_filter: The custom_software_source_filter of this CreateVersionedCustomSoftwareSourceDetails.
        :type: oci.os_management_hub.models.CustomSoftwareSourceFilter
        """
        self._custom_software_source_filter = custom_software_source_filter

    @property
    def software_source_version(self):
        """
        **[Required]** Gets the software_source_version of this CreateVersionedCustomSoftwareSourceDetails.
        The version to assign to this custom software source.


        :return: The software_source_version of this CreateVersionedCustomSoftwareSourceDetails.
        :rtype: str
        """
        return self._software_source_version

    @software_source_version.setter
    def software_source_version(self, software_source_version):
        """
        Sets the software_source_version of this CreateVersionedCustomSoftwareSourceDetails.
        The version to assign to this custom software source.


        :param software_source_version: The software_source_version of this CreateVersionedCustomSoftwareSourceDetails.
        :type: str
        """
        self._software_source_version = software_source_version

    @property
    def is_auto_resolve_dependencies(self):
        """
        Gets the is_auto_resolve_dependencies of this CreateVersionedCustomSoftwareSourceDetails.
        Indicates whether the service should automatically resolve package dependencies when including specific packages in the software source.


        :return: The is_auto_resolve_dependencies of this CreateVersionedCustomSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_auto_resolve_dependencies

    @is_auto_resolve_dependencies.setter
    def is_auto_resolve_dependencies(self, is_auto_resolve_dependencies):
        """
        Sets the is_auto_resolve_dependencies of this CreateVersionedCustomSoftwareSourceDetails.
        Indicates whether the service should automatically resolve package dependencies when including specific packages in the software source.


        :param is_auto_resolve_dependencies: The is_auto_resolve_dependencies of this CreateVersionedCustomSoftwareSourceDetails.
        :type: bool
        """
        self._is_auto_resolve_dependencies = is_auto_resolve_dependencies

    @property
    def is_created_from_package_list(self):
        """
        Gets the is_created_from_package_list of this CreateVersionedCustomSoftwareSourceDetails.
        Indicates whether the service should create the software source from a list of packages provided by the user.


        :return: The is_created_from_package_list of this CreateVersionedCustomSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_created_from_package_list

    @is_created_from_package_list.setter
    def is_created_from_package_list(self, is_created_from_package_list):
        """
        Sets the is_created_from_package_list of this CreateVersionedCustomSoftwareSourceDetails.
        Indicates whether the service should create the software source from a list of packages provided by the user.


        :param is_created_from_package_list: The is_created_from_package_list of this CreateVersionedCustomSoftwareSourceDetails.
        :type: bool
        """
        self._is_created_from_package_list = is_created_from_package_list

    @property
    def is_latest_content_only(self):
        """
        Gets the is_latest_content_only of this CreateVersionedCustomSoftwareSourceDetails.
        Indicates whether the software source will include only the latest versions of content from vendor software sources, while accounting for other constraints set in the custom or versioned custom software source (such as a package list or filters).
        * For a module filter that does not specify a stream, this will include all available streams, and within each stream only the latest version of packages.
        * For a module filter that does specify a stream, this will include only the latest version of packages for the specified stream.
        * For a package filter that does not specify a version, this will include only the latest available version of the package.
        * For a package filter that does specify a version, this will include only the specified version of the package (the isLatestContentOnly attribute is ignored).
        * For a package list, this will include only the specified version of packages and modules in the list (the isLatestContentOnly attribute is ignored).


        :return: The is_latest_content_only of this CreateVersionedCustomSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_latest_content_only

    @is_latest_content_only.setter
    def is_latest_content_only(self, is_latest_content_only):
        """
        Sets the is_latest_content_only of this CreateVersionedCustomSoftwareSourceDetails.
        Indicates whether the software source will include only the latest versions of content from vendor software sources, while accounting for other constraints set in the custom or versioned custom software source (such as a package list or filters).
        * For a module filter that does not specify a stream, this will include all available streams, and within each stream only the latest version of packages.
        * For a module filter that does specify a stream, this will include only the latest version of packages for the specified stream.
        * For a package filter that does not specify a version, this will include only the latest available version of the package.
        * For a package filter that does specify a version, this will include only the specified version of the package (the isLatestContentOnly attribute is ignored).
        * For a package list, this will include only the specified version of packages and modules in the list (the isLatestContentOnly attribute is ignored).


        :param is_latest_content_only: The is_latest_content_only of this CreateVersionedCustomSoftwareSourceDetails.
        :type: bool
        """
        self._is_latest_content_only = is_latest_content_only

    @property
    def packages(self):
        """
        Gets the packages of this CreateVersionedCustomSoftwareSourceDetails.
        A property used for compatibility only. It doesn't provide a complete list of packages. See :func:`add_packages_to_software_source_details` for providing the list of packages used to create the software source when isCreatedFromPackageList is set to true.


        :return: The packages of this CreateVersionedCustomSoftwareSourceDetails.
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this CreateVersionedCustomSoftwareSourceDetails.
        A property used for compatibility only. It doesn't provide a complete list of packages. See :func:`add_packages_to_software_source_details` for providing the list of packages used to create the software source when isCreatedFromPackageList is set to true.


        :param packages: The packages of this CreateVersionedCustomSoftwareSourceDetails.
        :type: list[str]
        """
        self._packages = packages

    @property
    def software_source_sub_type(self):
        """
        Gets the software_source_sub_type of this CreateVersionedCustomSoftwareSourceDetails.
        The creation type of a software source.

        Allowed values for this property are: "FILTER", "MANIFEST", "SNAPSHOT"


        :return: The software_source_sub_type of this CreateVersionedCustomSoftwareSourceDetails.
        :rtype: str
        """
        return self._software_source_sub_type

    @software_source_sub_type.setter
    def software_source_sub_type(self, software_source_sub_type):
        """
        Sets the software_source_sub_type of this CreateVersionedCustomSoftwareSourceDetails.
        The creation type of a software source.


        :param software_source_sub_type: The software_source_sub_type of this CreateVersionedCustomSoftwareSourceDetails.
        :type: str
        """
        allowed_values = ["FILTER", "MANIFEST", "SNAPSHOT"]
        if not value_allowed_none_or_none_sentinel(software_source_sub_type, allowed_values):
            raise ValueError(
                f"Invalid value for `software_source_sub_type`, must be None or one of {allowed_values}"
            )
        self._software_source_sub_type = software_source_sub_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
