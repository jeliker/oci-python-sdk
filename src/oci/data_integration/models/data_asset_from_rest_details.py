# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_asset import DataAsset
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetFromRestDetails(DataAsset):
    """
    Details for the Rest data asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetFromRestDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataAssetFromRestDetails.model_type` attribute
        of this class is ``REST_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataAssetFromRestDetails.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_HOUSE_DATA_ASSET", "REST_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataAssetFromRestDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAssetFromRestDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DataAssetFromRestDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAssetFromRestDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAssetFromRestDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataAssetFromRestDetails.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetFromRestDetails.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAssetFromRestDetails.
        :type asset_properties: dict(str, str)

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAssetFromRestDetails.
        :type native_type_system: oci.data_integration.models.TypeSystem

        :param object_version:
            The value to assign to the object_version property of this DataAssetFromRestDetails.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this DataAssetFromRestDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this DataAssetFromRestDetails.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this DataAssetFromRestDetails.
        :type key_map: dict(str, str)

        :param base_url:
            The value to assign to the base_url property of this DataAssetFromRestDetails.
        :type base_url: str

        :param manifest_file_content:
            The value to assign to the manifest_file_content property of this DataAssetFromRestDetails.
        :type manifest_file_content: str

        :param default_connection:
            The value to assign to the default_connection property of this DataAssetFromRestDetails.
        :type default_connection: oci.data_integration.models.ConnectionDetails

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'native_type_system': 'TypeSystem',
            'object_version': 'int',
            'parent_ref': 'ParentReference',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)',
            'base_url': 'str',
            'manifest_file_content': 'str',
            'default_connection': 'ConnectionDetails'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'native_type_system': 'nativeTypeSystem',
            'object_version': 'objectVersion',
            'parent_ref': 'parentRef',
            'metadata': 'metadata',
            'key_map': 'keyMap',
            'base_url': 'baseUrl',
            'manifest_file_content': 'manifestFileContent',
            'default_connection': 'defaultConnection'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._native_type_system = None
        self._object_version = None
        self._parent_ref = None
        self._metadata = None
        self._key_map = None
        self._base_url = None
        self._manifest_file_content = None
        self._default_connection = None
        self._model_type = 'REST_DATA_ASSET'

    @property
    def base_url(self):
        """
        Gets the base_url of this DataAssetFromRestDetails.
        The base url of the rest server.


        :return: The base_url of this DataAssetFromRestDetails.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """
        Sets the base_url of this DataAssetFromRestDetails.
        The base url of the rest server.


        :param base_url: The base_url of this DataAssetFromRestDetails.
        :type: str
        """
        self._base_url = base_url

    @property
    def manifest_file_content(self):
        """
        Gets the manifest_file_content of this DataAssetFromRestDetails.
        The manifest file content of the rest APIs.


        :return: The manifest_file_content of this DataAssetFromRestDetails.
        :rtype: str
        """
        return self._manifest_file_content

    @manifest_file_content.setter
    def manifest_file_content(self, manifest_file_content):
        """
        Sets the manifest_file_content of this DataAssetFromRestDetails.
        The manifest file content of the rest APIs.


        :param manifest_file_content: The manifest_file_content of this DataAssetFromRestDetails.
        :type: str
        """
        self._manifest_file_content = manifest_file_content

    @property
    def default_connection(self):
        """
        Gets the default_connection of this DataAssetFromRestDetails.

        :return: The default_connection of this DataAssetFromRestDetails.
        :rtype: oci.data_integration.models.ConnectionDetails
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this DataAssetFromRestDetails.

        :param default_connection: The default_connection of this DataAssetFromRestDetails.
        :type: oci.data_integration.models.ConnectionDetails
        """
        self._default_connection = default_connection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other