# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301

from .sharded_database_summary import ShardedDatabaseSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedShardedDatabaseSummary(ShardedDatabaseSummary):
    """
    Summary of ATP-D based sharded database.
    """

    #: A constant which can be used with the db_workload property of a DedicatedShardedDatabaseSummary.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a DedicatedShardedDatabaseSummary.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    #: A constant which can be used with the sharding_method property of a DedicatedShardedDatabaseSummary.
    #: This constant has a value of "USER"
    SHARDING_METHOD_USER = "USER"

    #: A constant which can be used with the sharding_method property of a DedicatedShardedDatabaseSummary.
    #: This constant has a value of "SYSTEM"
    SHARDING_METHOD_SYSTEM = "SYSTEM"

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedShardedDatabaseSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.globally_distributed_database.models.DedicatedShardedDatabaseSummary.db_deployment_type` attribute
        of this class is ``DEDICATED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DedicatedShardedDatabaseSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DedicatedShardedDatabaseSummary.
        :type compartment_id: str

        :param db_deployment_type:
            The value to assign to the db_deployment_type property of this DedicatedShardedDatabaseSummary.
            Allowed values for this property are: "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_deployment_type: str

        :param display_name:
            The value to assign to the display_name property of this DedicatedShardedDatabaseSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this DedicatedShardedDatabaseSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DedicatedShardedDatabaseSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DedicatedShardedDatabaseSummary.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this DedicatedShardedDatabaseSummary.
        :type lifecycle_state_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DedicatedShardedDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DedicatedShardedDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DedicatedShardedDatabaseSummary.
        :type system_tags: dict(str, dict(str, object))

        :param cluster_certificate_common_name:
            The value to assign to the cluster_certificate_common_name property of this DedicatedShardedDatabaseSummary.
        :type cluster_certificate_common_name: str

        :param db_workload:
            The value to assign to the db_workload property of this DedicatedShardedDatabaseSummary.
            Allowed values for this property are: "OLTP", "DW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_workload: str

        :param sharding_method:
            The value to assign to the sharding_method property of this DedicatedShardedDatabaseSummary.
            Allowed values for this property are: "USER", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type sharding_method: str

        :param character_set:
            The value to assign to the character_set property of this DedicatedShardedDatabaseSummary.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this DedicatedShardedDatabaseSummary.
        :type ncharacter_set: str

        :param chunks:
            The value to assign to the chunks property of this DedicatedShardedDatabaseSummary.
        :type chunks: int

        :param db_version:
            The value to assign to the db_version property of this DedicatedShardedDatabaseSummary.
        :type db_version: str

        :param listener_port:
            The value to assign to the listener_port property of this DedicatedShardedDatabaseSummary.
        :type listener_port: int

        :param listener_port_tls:
            The value to assign to the listener_port_tls property of this DedicatedShardedDatabaseSummary.
        :type listener_port_tls: int

        :param ons_port_local:
            The value to assign to the ons_port_local property of this DedicatedShardedDatabaseSummary.
        :type ons_port_local: int

        :param ons_port_remote:
            The value to assign to the ons_port_remote property of this DedicatedShardedDatabaseSummary.
        :type ons_port_remote: int

        :param prefix:
            The value to assign to the prefix property of this DedicatedShardedDatabaseSummary.
        :type prefix: str

        :param total_cpu_count:
            The value to assign to the total_cpu_count property of this DedicatedShardedDatabaseSummary.
        :type total_cpu_count: int

        :param total_data_storage_size_in_gbs:
            The value to assign to the total_data_storage_size_in_gbs property of this DedicatedShardedDatabaseSummary.
        :type total_data_storage_size_in_gbs: float

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'db_deployment_type': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'cluster_certificate_common_name': 'str',
            'db_workload': 'str',
            'sharding_method': 'str',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'chunks': 'int',
            'db_version': 'str',
            'listener_port': 'int',
            'listener_port_tls': 'int',
            'ons_port_local': 'int',
            'ons_port_remote': 'int',
            'prefix': 'str',
            'total_cpu_count': 'int',
            'total_data_storage_size_in_gbs': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'db_deployment_type': 'dbDeploymentType',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'cluster_certificate_common_name': 'clusterCertificateCommonName',
            'db_workload': 'dbWorkload',
            'sharding_method': 'shardingMethod',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'chunks': 'chunks',
            'db_version': 'dbVersion',
            'listener_port': 'listenerPort',
            'listener_port_tls': 'listenerPortTls',
            'ons_port_local': 'onsPortLocal',
            'ons_port_remote': 'onsPortRemote',
            'prefix': 'prefix',
            'total_cpu_count': 'totalCpuCount',
            'total_data_storage_size_in_gbs': 'totalDataStorageSizeInGbs'
        }

        self._id = None
        self._compartment_id = None
        self._db_deployment_type = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._cluster_certificate_common_name = None
        self._db_workload = None
        self._sharding_method = None
        self._character_set = None
        self._ncharacter_set = None
        self._chunks = None
        self._db_version = None
        self._listener_port = None
        self._listener_port_tls = None
        self._ons_port_local = None
        self._ons_port_remote = None
        self._prefix = None
        self._total_cpu_count = None
        self._total_data_storage_size_in_gbs = None
        self._db_deployment_type = 'DEDICATED'

    @property
    def cluster_certificate_common_name(self):
        """
        Gets the cluster_certificate_common_name of this DedicatedShardedDatabaseSummary.
        The certificate common name used in all cloudAutonomousVmClusters for the sharded database topology. Eg. Production.
        All the clusters used in one sharded database topology shall have same CABundle setup. Valid characterset for
        clusterCertificateCommonName include uppercase or lowercase letters, numbers, hyphens, underscores, and period.


        :return: The cluster_certificate_common_name of this DedicatedShardedDatabaseSummary.
        :rtype: str
        """
        return self._cluster_certificate_common_name

    @cluster_certificate_common_name.setter
    def cluster_certificate_common_name(self, cluster_certificate_common_name):
        """
        Sets the cluster_certificate_common_name of this DedicatedShardedDatabaseSummary.
        The certificate common name used in all cloudAutonomousVmClusters for the sharded database topology. Eg. Production.
        All the clusters used in one sharded database topology shall have same CABundle setup. Valid characterset for
        clusterCertificateCommonName include uppercase or lowercase letters, numbers, hyphens, underscores, and period.


        :param cluster_certificate_common_name: The cluster_certificate_common_name of this DedicatedShardedDatabaseSummary.
        :type: str
        """
        self._cluster_certificate_common_name = cluster_certificate_common_name

    @property
    def db_workload(self):
        """
        **[Required]** Gets the db_workload of this DedicatedShardedDatabaseSummary.
        Possible workload types.

        Allowed values for this property are: "OLTP", "DW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_workload of this DedicatedShardedDatabaseSummary.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this DedicatedShardedDatabaseSummary.
        Possible workload types.


        :param db_workload: The db_workload of this DedicatedShardedDatabaseSummary.
        :type: str
        """
        allowed_values = ["OLTP", "DW"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            db_workload = 'UNKNOWN_ENUM_VALUE'
        self._db_workload = db_workload

    @property
    def sharding_method(self):
        """
        **[Required]** Gets the sharding_method of this DedicatedShardedDatabaseSummary.
        Sharding Method.

        Allowed values for this property are: "USER", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The sharding_method of this DedicatedShardedDatabaseSummary.
        :rtype: str
        """
        return self._sharding_method

    @sharding_method.setter
    def sharding_method(self, sharding_method):
        """
        Sets the sharding_method of this DedicatedShardedDatabaseSummary.
        Sharding Method.


        :param sharding_method: The sharding_method of this DedicatedShardedDatabaseSummary.
        :type: str
        """
        allowed_values = ["USER", "SYSTEM"]
        if not value_allowed_none_or_none_sentinel(sharding_method, allowed_values):
            sharding_method = 'UNKNOWN_ENUM_VALUE'
        self._sharding_method = sharding_method

    @property
    def character_set(self):
        """
        **[Required]** Gets the character_set of this DedicatedShardedDatabaseSummary.
        The character set for the sharded database.


        :return: The character_set of this DedicatedShardedDatabaseSummary.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this DedicatedShardedDatabaseSummary.
        The character set for the sharded database.


        :param character_set: The character_set of this DedicatedShardedDatabaseSummary.
        :type: str
        """
        self._character_set = character_set

    @property
    def ncharacter_set(self):
        """
        **[Required]** Gets the ncharacter_set of this DedicatedShardedDatabaseSummary.
        The national character set for the sharded database.


        :return: The ncharacter_set of this DedicatedShardedDatabaseSummary.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this DedicatedShardedDatabaseSummary.
        The national character set for the sharded database.


        :param ncharacter_set: The ncharacter_set of this DedicatedShardedDatabaseSummary.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def chunks(self):
        """
        Gets the chunks of this DedicatedShardedDatabaseSummary.
        The default number of unique chunks in a shardspace. The value of chunks must be
        greater than 2 times the size of the largest shardgroup in any shardspace.


        :return: The chunks of this DedicatedShardedDatabaseSummary.
        :rtype: int
        """
        return self._chunks

    @chunks.setter
    def chunks(self, chunks):
        """
        Sets the chunks of this DedicatedShardedDatabaseSummary.
        The default number of unique chunks in a shardspace. The value of chunks must be
        greater than 2 times the size of the largest shardgroup in any shardspace.


        :param chunks: The chunks of this DedicatedShardedDatabaseSummary.
        :type: int
        """
        self._chunks = chunks

    @property
    def db_version(self):
        """
        Gets the db_version of this DedicatedShardedDatabaseSummary.
        Oracle Database version of the Autonomous Container Database.


        :return: The db_version of this DedicatedShardedDatabaseSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this DedicatedShardedDatabaseSummary.
        Oracle Database version of the Autonomous Container Database.


        :param db_version: The db_version of this DedicatedShardedDatabaseSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def listener_port(self):
        """
        Gets the listener_port of this DedicatedShardedDatabaseSummary.
        The listener port number for the sharded database.


        :return: The listener_port of this DedicatedShardedDatabaseSummary.
        :rtype: int
        """
        return self._listener_port

    @listener_port.setter
    def listener_port(self, listener_port):
        """
        Sets the listener_port of this DedicatedShardedDatabaseSummary.
        The listener port number for the sharded database.


        :param listener_port: The listener_port of this DedicatedShardedDatabaseSummary.
        :type: int
        """
        self._listener_port = listener_port

    @property
    def listener_port_tls(self):
        """
        Gets the listener_port_tls of this DedicatedShardedDatabaseSummary.
        The TLS listener port number for sharded database.


        :return: The listener_port_tls of this DedicatedShardedDatabaseSummary.
        :rtype: int
        """
        return self._listener_port_tls

    @listener_port_tls.setter
    def listener_port_tls(self, listener_port_tls):
        """
        Sets the listener_port_tls of this DedicatedShardedDatabaseSummary.
        The TLS listener port number for sharded database.


        :param listener_port_tls: The listener_port_tls of this DedicatedShardedDatabaseSummary.
        :type: int
        """
        self._listener_port_tls = listener_port_tls

    @property
    def ons_port_local(self):
        """
        Gets the ons_port_local of this DedicatedShardedDatabaseSummary.
        Ons local port number.


        :return: The ons_port_local of this DedicatedShardedDatabaseSummary.
        :rtype: int
        """
        return self._ons_port_local

    @ons_port_local.setter
    def ons_port_local(self, ons_port_local):
        """
        Sets the ons_port_local of this DedicatedShardedDatabaseSummary.
        Ons local port number.


        :param ons_port_local: The ons_port_local of this DedicatedShardedDatabaseSummary.
        :type: int
        """
        self._ons_port_local = ons_port_local

    @property
    def ons_port_remote(self):
        """
        Gets the ons_port_remote of this DedicatedShardedDatabaseSummary.
        Ons remote port number.


        :return: The ons_port_remote of this DedicatedShardedDatabaseSummary.
        :rtype: int
        """
        return self._ons_port_remote

    @ons_port_remote.setter
    def ons_port_remote(self, ons_port_remote):
        """
        Sets the ons_port_remote of this DedicatedShardedDatabaseSummary.
        Ons remote port number.


        :param ons_port_remote: The ons_port_remote of this DedicatedShardedDatabaseSummary.
        :type: int
        """
        self._ons_port_remote = ons_port_remote

    @property
    def prefix(self):
        """
        Gets the prefix of this DedicatedShardedDatabaseSummary.
        Name prefix for the sharded databases.


        :return: The prefix of this DedicatedShardedDatabaseSummary.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this DedicatedShardedDatabaseSummary.
        Name prefix for the sharded databases.


        :param prefix: The prefix of this DedicatedShardedDatabaseSummary.
        :type: str
        """
        self._prefix = prefix

    @property
    def total_cpu_count(self):
        """
        Gets the total_cpu_count of this DedicatedShardedDatabaseSummary.
        Total cpu count usage for shards and catalogs of the sharded database.


        :return: The total_cpu_count of this DedicatedShardedDatabaseSummary.
        :rtype: int
        """
        return self._total_cpu_count

    @total_cpu_count.setter
    def total_cpu_count(self, total_cpu_count):
        """
        Sets the total_cpu_count of this DedicatedShardedDatabaseSummary.
        Total cpu count usage for shards and catalogs of the sharded database.


        :param total_cpu_count: The total_cpu_count of this DedicatedShardedDatabaseSummary.
        :type: int
        """
        self._total_cpu_count = total_cpu_count

    @property
    def total_data_storage_size_in_gbs(self):
        """
        Gets the total_data_storage_size_in_gbs of this DedicatedShardedDatabaseSummary.
        The aggregarted value of dataStorageSizeInGbs for all shards and catalogs.


        :return: The total_data_storage_size_in_gbs of this DedicatedShardedDatabaseSummary.
        :rtype: float
        """
        return self._total_data_storage_size_in_gbs

    @total_data_storage_size_in_gbs.setter
    def total_data_storage_size_in_gbs(self, total_data_storage_size_in_gbs):
        """
        Sets the total_data_storage_size_in_gbs of this DedicatedShardedDatabaseSummary.
        The aggregarted value of dataStorageSizeInGbs for all shards and catalogs.


        :param total_data_storage_size_in_gbs: The total_data_storage_size_in_gbs of this DedicatedShardedDatabaseSummary.
        :type: float
        """
        self._total_data_storage_size_in_gbs = total_data_storage_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other