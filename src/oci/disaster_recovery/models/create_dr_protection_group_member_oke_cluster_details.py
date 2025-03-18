# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .create_dr_protection_group_member_details import CreateDrProtectionGroupMemberDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrProtectionGroupMemberOkeClusterDetails(CreateDrProtectionGroupMemberDetails):
    """
    Create properties for an OKE member.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrProtectionGroupMemberOkeClusterDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberOkeClusterDetails.member_type` attribute
        of this class is ``OKE_CLUSTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this CreateDrProtectionGroupMemberOkeClusterDetails.
            Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "AUTONOMOUS_CONTAINER_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM", "OKE_CLUSTER", "OBJECT_STORAGE_BUCKET"
        :type member_type: str

        :param peer_cluster_id:
            The value to assign to the peer_cluster_id property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type peer_cluster_id: str

        :param jump_host_id:
            The value to assign to the jump_host_id property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type jump_host_id: str

        :param backup_location:
            The value to assign to the backup_location property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type backup_location: oci.disaster_recovery.models.CreateOkeBackupLocationDetails

        :param backup_config:
            The value to assign to the backup_config property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type backup_config: oci.disaster_recovery.models.CreateOkeClusterBackupConfigDetails

        :param load_balancer_mappings:
            The value to assign to the load_balancer_mappings property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type load_balancer_mappings: list[oci.disaster_recovery.models.CreateOkeClusterLoadBalancerMappingDetails]

        :param network_load_balancer_mappings:
            The value to assign to the network_load_balancer_mappings property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type network_load_balancer_mappings: list[oci.disaster_recovery.models.CreateOkeClusterNetworkLoadBalancerMappingDetails]

        :param vault_mappings:
            The value to assign to the vault_mappings property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type vault_mappings: list[oci.disaster_recovery.models.CreateOkeClusterVaultMappingDetails]

        :param managed_node_pool_configs:
            The value to assign to the managed_node_pool_configs property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type managed_node_pool_configs: list[oci.disaster_recovery.models.CreateOkeClusterManagedNodePoolConfigurationDetails]

        :param virtual_node_pool_configs:
            The value to assign to the virtual_node_pool_configs property of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type virtual_node_pool_configs: list[oci.disaster_recovery.models.CreateOkeClusterVirtualNodePoolConfigurationDetails]

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'peer_cluster_id': 'str',
            'jump_host_id': 'str',
            'backup_location': 'CreateOkeBackupLocationDetails',
            'backup_config': 'CreateOkeClusterBackupConfigDetails',
            'load_balancer_mappings': 'list[CreateOkeClusterLoadBalancerMappingDetails]',
            'network_load_balancer_mappings': 'list[CreateOkeClusterNetworkLoadBalancerMappingDetails]',
            'vault_mappings': 'list[CreateOkeClusterVaultMappingDetails]',
            'managed_node_pool_configs': 'list[CreateOkeClusterManagedNodePoolConfigurationDetails]',
            'virtual_node_pool_configs': 'list[CreateOkeClusterVirtualNodePoolConfigurationDetails]'
        }
        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'peer_cluster_id': 'peerClusterId',
            'jump_host_id': 'jumpHostId',
            'backup_location': 'backupLocation',
            'backup_config': 'backupConfig',
            'load_balancer_mappings': 'loadBalancerMappings',
            'network_load_balancer_mappings': 'networkLoadBalancerMappings',
            'vault_mappings': 'vaultMappings',
            'managed_node_pool_configs': 'managedNodePoolConfigs',
            'virtual_node_pool_configs': 'virtualNodePoolConfigs'
        }
        self._member_id = None
        self._member_type = None
        self._peer_cluster_id = None
        self._jump_host_id = None
        self._backup_location = None
        self._backup_config = None
        self._load_balancer_mappings = None
        self._network_load_balancer_mappings = None
        self._vault_mappings = None
        self._managed_node_pool_configs = None
        self._virtual_node_pool_configs = None
        self._member_type = 'OKE_CLUSTER'

    @property
    def peer_cluster_id(self):
        """
        Gets the peer_cluster_id of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The OCID of the peer OKE cluster.
        This property applies to the OKE cluster member in both the primary and standby region.

        Example: `ocid1.cluster.oc1..uniqueID`


        :return: The peer_cluster_id of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: str
        """
        return self._peer_cluster_id

    @peer_cluster_id.setter
    def peer_cluster_id(self, peer_cluster_id):
        """
        Sets the peer_cluster_id of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The OCID of the peer OKE cluster.
        This property applies to the OKE cluster member in both the primary and standby region.

        Example: `ocid1.cluster.oc1..uniqueID`


        :param peer_cluster_id: The peer_cluster_id of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: str
        """
        self._peer_cluster_id = peer_cluster_id

    @property
    def jump_host_id(self):
        """
        Gets the jump_host_id of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The OCID of the compute instance member that is designated as a jump host.
        This compute instance will be used to perform DR operations on the cluster using Oracle Cloud Agent's Run Command feature.

        Example: `ocid1.instance.oc1..uniqueID`


        :return: The jump_host_id of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: str
        """
        return self._jump_host_id

    @jump_host_id.setter
    def jump_host_id(self, jump_host_id):
        """
        Sets the jump_host_id of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The OCID of the compute instance member that is designated as a jump host.
        This compute instance will be used to perform DR operations on the cluster using Oracle Cloud Agent's Run Command feature.

        Example: `ocid1.instance.oc1..uniqueID`


        :param jump_host_id: The jump_host_id of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: str
        """
        self._jump_host_id = jump_host_id

    @property
    def backup_location(self):
        """
        Gets the backup_location of this CreateDrProtectionGroupMemberOkeClusterDetails.

        :return: The backup_location of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: oci.disaster_recovery.models.CreateOkeBackupLocationDetails
        """
        return self._backup_location

    @backup_location.setter
    def backup_location(self, backup_location):
        """
        Sets the backup_location of this CreateDrProtectionGroupMemberOkeClusterDetails.

        :param backup_location: The backup_location of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: oci.disaster_recovery.models.CreateOkeBackupLocationDetails
        """
        self._backup_location = backup_location

    @property
    def backup_config(self):
        """
        Gets the backup_config of this CreateDrProtectionGroupMemberOkeClusterDetails.

        :return: The backup_config of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: oci.disaster_recovery.models.CreateOkeClusterBackupConfigDetails
        """
        return self._backup_config

    @backup_config.setter
    def backup_config(self, backup_config):
        """
        Sets the backup_config of this CreateDrProtectionGroupMemberOkeClusterDetails.

        :param backup_config: The backup_config of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: oci.disaster_recovery.models.CreateOkeClusterBackupConfigDetails
        """
        self._backup_config = backup_config

    @property
    def load_balancer_mappings(self):
        """
        Gets the load_balancer_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of source-to-destination load balancer mappings required for DR operations.
        This property applies to the OKE cluster member in primary region.


        :return: The load_balancer_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: list[oci.disaster_recovery.models.CreateOkeClusterLoadBalancerMappingDetails]
        """
        return self._load_balancer_mappings

    @load_balancer_mappings.setter
    def load_balancer_mappings(self, load_balancer_mappings):
        """
        Sets the load_balancer_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of source-to-destination load balancer mappings required for DR operations.
        This property applies to the OKE cluster member in primary region.


        :param load_balancer_mappings: The load_balancer_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: list[oci.disaster_recovery.models.CreateOkeClusterLoadBalancerMappingDetails]
        """
        self._load_balancer_mappings = load_balancer_mappings

    @property
    def network_load_balancer_mappings(self):
        """
        Gets the network_load_balancer_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of source-to-destination network load balancer mappings required for DR operations.
        This property applies to the OKE cluster member in primary region.


        :return: The network_load_balancer_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: list[oci.disaster_recovery.models.CreateOkeClusterNetworkLoadBalancerMappingDetails]
        """
        return self._network_load_balancer_mappings

    @network_load_balancer_mappings.setter
    def network_load_balancer_mappings(self, network_load_balancer_mappings):
        """
        Sets the network_load_balancer_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of source-to-destination network load balancer mappings required for DR operations.
        This property applies to the OKE cluster member in primary region.


        :param network_load_balancer_mappings: The network_load_balancer_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: list[oci.disaster_recovery.models.CreateOkeClusterNetworkLoadBalancerMappingDetails]
        """
        self._network_load_balancer_mappings = network_load_balancer_mappings

    @property
    def vault_mappings(self):
        """
        Gets the vault_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of source-to-destination vault mappings required for DR operations.
        This property applies to the OKE cluster member in primary region.


        :return: The vault_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: list[oci.disaster_recovery.models.CreateOkeClusterVaultMappingDetails]
        """
        return self._vault_mappings

    @vault_mappings.setter
    def vault_mappings(self, vault_mappings):
        """
        Sets the vault_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of source-to-destination vault mappings required for DR operations.
        This property applies to the OKE cluster member in primary region.


        :param vault_mappings: The vault_mappings of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: list[oci.disaster_recovery.models.CreateOkeClusterVaultMappingDetails]
        """
        self._vault_mappings = vault_mappings

    @property
    def managed_node_pool_configs(self):
        """
        Gets the managed_node_pool_configs of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of managed node pools with configurations for minimum and maximum node counts.
        This property applies to the OKE cluster member in both the primary and standby region.


        :return: The managed_node_pool_configs of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: list[oci.disaster_recovery.models.CreateOkeClusterManagedNodePoolConfigurationDetails]
        """
        return self._managed_node_pool_configs

    @managed_node_pool_configs.setter
    def managed_node_pool_configs(self, managed_node_pool_configs):
        """
        Sets the managed_node_pool_configs of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of managed node pools with configurations for minimum and maximum node counts.
        This property applies to the OKE cluster member in both the primary and standby region.


        :param managed_node_pool_configs: The managed_node_pool_configs of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: list[oci.disaster_recovery.models.CreateOkeClusterManagedNodePoolConfigurationDetails]
        """
        self._managed_node_pool_configs = managed_node_pool_configs

    @property
    def virtual_node_pool_configs(self):
        """
        Gets the virtual_node_pool_configs of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of virtual node pools with configurations for minimum and maximum node counts.
        This property applies to the OKE cluster member in both the primary and standby region.


        :return: The virtual_node_pool_configs of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :rtype: list[oci.disaster_recovery.models.CreateOkeClusterVirtualNodePoolConfigurationDetails]
        """
        return self._virtual_node_pool_configs

    @virtual_node_pool_configs.setter
    def virtual_node_pool_configs(self, virtual_node_pool_configs):
        """
        Sets the virtual_node_pool_configs of this CreateDrProtectionGroupMemberOkeClusterDetails.
        The list of virtual node pools with configurations for minimum and maximum node counts.
        This property applies to the OKE cluster member in both the primary and standby region.


        :param virtual_node_pool_configs: The virtual_node_pool_configs of this CreateDrProtectionGroupMemberOkeClusterDetails.
        :type: list[oci.disaster_recovery.models.CreateOkeClusterVirtualNodePoolConfigurationDetails]
        """
        self._virtual_node_pool_configs = virtual_node_pool_configs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
