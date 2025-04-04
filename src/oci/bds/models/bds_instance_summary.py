# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BdsInstanceSummary(object):
    """
    Summary details of the Big Data Service cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BdsInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BdsInstanceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BdsInstanceSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this BdsInstanceSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BdsInstanceSummary.
        :type lifecycle_state: str

        :param number_of_nodes:
            The value to assign to the number_of_nodes property of this BdsInstanceSummary.
        :type number_of_nodes: int

        :param number_of_nodes_requiring_maintenance_reboot:
            The value to assign to the number_of_nodes_requiring_maintenance_reboot property of this BdsInstanceSummary.
        :type number_of_nodes_requiring_maintenance_reboot: int

        :param cluster_version:
            The value to assign to the cluster_version property of this BdsInstanceSummary.
        :type cluster_version: str

        :param is_high_availability:
            The value to assign to the is_high_availability property of this BdsInstanceSummary.
        :type is_high_availability: bool

        :param is_secure:
            The value to assign to the is_secure property of this BdsInstanceSummary.
        :type is_secure: bool

        :param is_cloud_sql_configured:
            The value to assign to the is_cloud_sql_configured property of this BdsInstanceSummary.
        :type is_cloud_sql_configured: bool

        :param is_kafka_configured:
            The value to assign to the is_kafka_configured property of this BdsInstanceSummary.
        :type is_kafka_configured: bool

        :param cluster_profile:
            The value to assign to the cluster_profile property of this BdsInstanceSummary.
        :type cluster_profile: str

        :param time_created:
            The value to assign to the time_created property of this BdsInstanceSummary.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BdsInstanceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BdsInstanceSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'number_of_nodes': 'int',
            'number_of_nodes_requiring_maintenance_reboot': 'int',
            'cluster_version': 'str',
            'is_high_availability': 'bool',
            'is_secure': 'bool',
            'is_cloud_sql_configured': 'bool',
            'is_kafka_configured': 'bool',
            'cluster_profile': 'str',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'number_of_nodes': 'numberOfNodes',
            'number_of_nodes_requiring_maintenance_reboot': 'numberOfNodesRequiringMaintenanceReboot',
            'cluster_version': 'clusterVersion',
            'is_high_availability': 'isHighAvailability',
            'is_secure': 'isSecure',
            'is_cloud_sql_configured': 'isCloudSqlConfigured',
            'is_kafka_configured': 'isKafkaConfigured',
            'cluster_profile': 'clusterProfile',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._number_of_nodes = None
        self._number_of_nodes_requiring_maintenance_reboot = None
        self._cluster_version = None
        self._is_high_availability = None
        self._is_secure = None
        self._is_cloud_sql_configured = None
        self._is_kafka_configured = None
        self._cluster_profile = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BdsInstanceSummary.
        The OCID of the Big Data Service resource.


        :return: The id of this BdsInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BdsInstanceSummary.
        The OCID of the Big Data Service resource.


        :param id: The id of this BdsInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BdsInstanceSummary.
        The OCID of the compartment.


        :return: The compartment_id of this BdsInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BdsInstanceSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this BdsInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BdsInstanceSummary.
        The name of the cluster.


        :return: The display_name of this BdsInstanceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BdsInstanceSummary.
        The name of the cluster.


        :param display_name: The display_name of this BdsInstanceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BdsInstanceSummary.
        The state of the cluster.


        :return: The lifecycle_state of this BdsInstanceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BdsInstanceSummary.
        The state of the cluster.


        :param lifecycle_state: The lifecycle_state of this BdsInstanceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def number_of_nodes(self):
        """
        **[Required]** Gets the number_of_nodes of this BdsInstanceSummary.
        The number of nodes that form the cluster.


        :return: The number_of_nodes of this BdsInstanceSummary.
        :rtype: int
        """
        return self._number_of_nodes

    @number_of_nodes.setter
    def number_of_nodes(self, number_of_nodes):
        """
        Sets the number_of_nodes of this BdsInstanceSummary.
        The number of nodes that form the cluster.


        :param number_of_nodes: The number_of_nodes of this BdsInstanceSummary.
        :type: int
        """
        self._number_of_nodes = number_of_nodes

    @property
    def number_of_nodes_requiring_maintenance_reboot(self):
        """
        Gets the number_of_nodes_requiring_maintenance_reboot of this BdsInstanceSummary.
        Number of nodes that require a maintenance reboot


        :return: The number_of_nodes_requiring_maintenance_reboot of this BdsInstanceSummary.
        :rtype: int
        """
        return self._number_of_nodes_requiring_maintenance_reboot

    @number_of_nodes_requiring_maintenance_reboot.setter
    def number_of_nodes_requiring_maintenance_reboot(self, number_of_nodes_requiring_maintenance_reboot):
        """
        Sets the number_of_nodes_requiring_maintenance_reboot of this BdsInstanceSummary.
        Number of nodes that require a maintenance reboot


        :param number_of_nodes_requiring_maintenance_reboot: The number_of_nodes_requiring_maintenance_reboot of this BdsInstanceSummary.
        :type: int
        """
        self._number_of_nodes_requiring_maintenance_reboot = number_of_nodes_requiring_maintenance_reboot

    @property
    def cluster_version(self):
        """
        Gets the cluster_version of this BdsInstanceSummary.
        Version of the Hadoop distribution.


        :return: The cluster_version of this BdsInstanceSummary.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        """
        Sets the cluster_version of this BdsInstanceSummary.
        Version of the Hadoop distribution.


        :param cluster_version: The cluster_version of this BdsInstanceSummary.
        :type: str
        """
        self._cluster_version = cluster_version

    @property
    def is_high_availability(self):
        """
        **[Required]** Gets the is_high_availability of this BdsInstanceSummary.
        Boolean flag specifying whether or not the cluster is highly available(HA).


        :return: The is_high_availability of this BdsInstanceSummary.
        :rtype: bool
        """
        return self._is_high_availability

    @is_high_availability.setter
    def is_high_availability(self, is_high_availability):
        """
        Sets the is_high_availability of this BdsInstanceSummary.
        Boolean flag specifying whether or not the cluster is highly available(HA).


        :param is_high_availability: The is_high_availability of this BdsInstanceSummary.
        :type: bool
        """
        self._is_high_availability = is_high_availability

    @property
    def is_secure(self):
        """
        **[Required]** Gets the is_secure of this BdsInstanceSummary.
        Boolean flag specifying whether or not the cluster should be set up as secure.


        :return: The is_secure of this BdsInstanceSummary.
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure):
        """
        Sets the is_secure of this BdsInstanceSummary.
        Boolean flag specifying whether or not the cluster should be set up as secure.


        :param is_secure: The is_secure of this BdsInstanceSummary.
        :type: bool
        """
        self._is_secure = is_secure

    @property
    def is_cloud_sql_configured(self):
        """
        **[Required]** Gets the is_cloud_sql_configured of this BdsInstanceSummary.
        Boolean flag specifying whether Cloud SQL is configured or not.


        :return: The is_cloud_sql_configured of this BdsInstanceSummary.
        :rtype: bool
        """
        return self._is_cloud_sql_configured

    @is_cloud_sql_configured.setter
    def is_cloud_sql_configured(self, is_cloud_sql_configured):
        """
        Sets the is_cloud_sql_configured of this BdsInstanceSummary.
        Boolean flag specifying whether Cloud SQL is configured or not.


        :param is_cloud_sql_configured: The is_cloud_sql_configured of this BdsInstanceSummary.
        :type: bool
        """
        self._is_cloud_sql_configured = is_cloud_sql_configured

    @property
    def is_kafka_configured(self):
        """
        **[Required]** Gets the is_kafka_configured of this BdsInstanceSummary.
        Boolean flag specifying whether Kafka is configured or not.


        :return: The is_kafka_configured of this BdsInstanceSummary.
        :rtype: bool
        """
        return self._is_kafka_configured

    @is_kafka_configured.setter
    def is_kafka_configured(self, is_kafka_configured):
        """
        Sets the is_kafka_configured of this BdsInstanceSummary.
        Boolean flag specifying whether Kafka is configured or not.


        :param is_kafka_configured: The is_kafka_configured of this BdsInstanceSummary.
        :type: bool
        """
        self._is_kafka_configured = is_kafka_configured

    @property
    def cluster_profile(self):
        """
        Gets the cluster_profile of this BdsInstanceSummary.
        Profile of the Big Data Service cluster.


        :return: The cluster_profile of this BdsInstanceSummary.
        :rtype: str
        """
        return self._cluster_profile

    @cluster_profile.setter
    def cluster_profile(self, cluster_profile):
        """
        Sets the cluster_profile of this BdsInstanceSummary.
        Profile of the Big Data Service cluster.


        :param cluster_profile: The cluster_profile of this BdsInstanceSummary.
        :type: str
        """
        self._cluster_profile = cluster_profile

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BdsInstanceSummary.
        The time the cluster was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_created of this BdsInstanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BdsInstanceSummary.
        The time the cluster was created, shown as an RFC 3339 formatted datetime string.


        :param time_created: The time_created of this BdsInstanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BdsInstanceSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BdsInstanceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BdsInstanceSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BdsInstanceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BdsInstanceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BdsInstanceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BdsInstanceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BdsInstanceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
