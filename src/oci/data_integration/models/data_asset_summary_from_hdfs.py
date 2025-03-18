# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .data_asset_summary import DataAssetSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetSummaryFromHdfs(DataAssetSummary):
    """
    Summary details for the HDFS data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetSummaryFromHdfs object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataAssetSummaryFromHdfs.model_type` attribute
        of this class is ``HDFS_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataAssetSummaryFromHdfs.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_DATA_ASSET", "ORACLE_PEOPLESOFT_DATA_ASSET", "ORACLE_SIEBEL_DATA_ASSET", "ORACLE_EBS_DATA_ASSET", "HDFS_DATA_ASSET", "MYSQL_HEATWAVE_DATA_ASSET", "REST_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataAssetSummaryFromHdfs.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAssetSummaryFromHdfs.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DataAssetSummaryFromHdfs.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAssetSummaryFromHdfs.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAssetSummaryFromHdfs.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataAssetSummaryFromHdfs.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetSummaryFromHdfs.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAssetSummaryFromHdfs.
        :type asset_properties: dict(str, str)

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAssetSummaryFromHdfs.
        :type native_type_system: oci.data_integration.models.TypeSystem

        :param object_version:
            The value to assign to the object_version property of this DataAssetSummaryFromHdfs.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this DataAssetSummaryFromHdfs.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this DataAssetSummaryFromHdfs.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param host:
            The value to assign to the host property of this DataAssetSummaryFromHdfs.
        :type host: str

        :param port:
            The value to assign to the port property of this DataAssetSummaryFromHdfs.
        :type port: str

        :param protocol:
            The value to assign to the protocol property of this DataAssetSummaryFromHdfs.
        :type protocol: str

        :param validate_certificate:
            The value to assign to the validate_certificate property of this DataAssetSummaryFromHdfs.
        :type validate_certificate: bool

        :param default_connection:
            The value to assign to the default_connection property of this DataAssetSummaryFromHdfs.
        :type default_connection: oci.data_integration.models.ConnectionSummaryFromHdfs

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
            'host': 'str',
            'port': 'str',
            'protocol': 'str',
            'validate_certificate': 'bool',
            'default_connection': 'ConnectionSummaryFromHdfs'
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
            'host': 'host',
            'port': 'port',
            'protocol': 'protocol',
            'validate_certificate': 'validateCertificate',
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
        self._host = None
        self._port = None
        self._protocol = None
        self._validate_certificate = None
        self._default_connection = None
        self._model_type = 'HDFS_DATA_ASSET'

    @property
    def host(self):
        """
        **[Required]** Gets the host of this DataAssetSummaryFromHdfs.
        The HDFS hostname.


        :return: The host of this DataAssetSummaryFromHdfs.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this DataAssetSummaryFromHdfs.
        The HDFS hostname.


        :param host: The host of this DataAssetSummaryFromHdfs.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        **[Required]** Gets the port of this DataAssetSummaryFromHdfs.
        The HDFS port.


        :return: The port of this DataAssetSummaryFromHdfs.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this DataAssetSummaryFromHdfs.
        The HDFS port.


        :param port: The port of this DataAssetSummaryFromHdfs.
        :type: str
        """
        self._port = port

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this DataAssetSummaryFromHdfs.
        The HDFS Protocol name.


        :return: The protocol of this DataAssetSummaryFromHdfs.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this DataAssetSummaryFromHdfs.
        The HDFS Protocol name.


        :param protocol: The protocol of this DataAssetSummaryFromHdfs.
        :type: str
        """
        self._protocol = protocol

    @property
    def validate_certificate(self):
        """
        Gets the validate_certificate of this DataAssetSummaryFromHdfs.
        Specifies whether certificate validation is needed


        :return: The validate_certificate of this DataAssetSummaryFromHdfs.
        :rtype: bool
        """
        return self._validate_certificate

    @validate_certificate.setter
    def validate_certificate(self, validate_certificate):
        """
        Sets the validate_certificate of this DataAssetSummaryFromHdfs.
        Specifies whether certificate validation is needed


        :param validate_certificate: The validate_certificate of this DataAssetSummaryFromHdfs.
        :type: bool
        """
        self._validate_certificate = validate_certificate

    @property
    def default_connection(self):
        """
        **[Required]** Gets the default_connection of this DataAssetSummaryFromHdfs.

        :return: The default_connection of this DataAssetSummaryFromHdfs.
        :rtype: oci.data_integration.models.ConnectionSummaryFromHdfs
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this DataAssetSummaryFromHdfs.

        :param default_connection: The default_connection of this DataAssetSummaryFromHdfs.
        :type: oci.data_integration.models.ConnectionSummaryFromHdfs
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
