# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeNetworkBlockSummary(object):
    """
    Summary information for a compute network block.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeNetworkBlockSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compute_capacity_topology_id:
            The value to assign to the compute_capacity_topology_id property of this ComputeNetworkBlockSummary.
        :type compute_capacity_topology_id: str

        :param compute_hpc_island_id:
            The value to assign to the compute_hpc_island_id property of this ComputeNetworkBlockSummary.
        :type compute_hpc_island_id: str

        :param id:
            The value to assign to the id property of this ComputeNetworkBlockSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ComputeNetworkBlockSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ComputeNetworkBlockSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ComputeNetworkBlockSummary.
        :type time_updated: datetime

        :param total_compute_bare_metal_host_count:
            The value to assign to the total_compute_bare_metal_host_count property of this ComputeNetworkBlockSummary.
        :type total_compute_bare_metal_host_count: int

        """
        self.swagger_types = {
            'compute_capacity_topology_id': 'str',
            'compute_hpc_island_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'total_compute_bare_metal_host_count': 'int'
        }
        self.attribute_map = {
            'compute_capacity_topology_id': 'computeCapacityTopologyId',
            'compute_hpc_island_id': 'computeHpcIslandId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'total_compute_bare_metal_host_count': 'totalComputeBareMetalHostCount'
        }
        self._compute_capacity_topology_id = None
        self._compute_hpc_island_id = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._total_compute_bare_metal_host_count = None

    @property
    def compute_capacity_topology_id(self):
        """
        **[Required]** Gets the compute_capacity_topology_id of this ComputeNetworkBlockSummary.
        The `OCID`__ of the compute capacity topology.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compute_capacity_topology_id of this ComputeNetworkBlockSummary.
        :rtype: str
        """
        return self._compute_capacity_topology_id

    @compute_capacity_topology_id.setter
    def compute_capacity_topology_id(self, compute_capacity_topology_id):
        """
        Sets the compute_capacity_topology_id of this ComputeNetworkBlockSummary.
        The `OCID`__ of the compute capacity topology.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compute_capacity_topology_id: The compute_capacity_topology_id of this ComputeNetworkBlockSummary.
        :type: str
        """
        self._compute_capacity_topology_id = compute_capacity_topology_id

    @property
    def compute_hpc_island_id(self):
        """
        **[Required]** Gets the compute_hpc_island_id of this ComputeNetworkBlockSummary.
        The `OCID`__ of the compute HPC island.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compute_hpc_island_id of this ComputeNetworkBlockSummary.
        :rtype: str
        """
        return self._compute_hpc_island_id

    @compute_hpc_island_id.setter
    def compute_hpc_island_id(self, compute_hpc_island_id):
        """
        Sets the compute_hpc_island_id of this ComputeNetworkBlockSummary.
        The `OCID`__ of the compute HPC island.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compute_hpc_island_id: The compute_hpc_island_id of this ComputeNetworkBlockSummary.
        :type: str
        """
        self._compute_hpc_island_id = compute_hpc_island_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ComputeNetworkBlockSummary.
        The `OCID`__ of the compute network block.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ComputeNetworkBlockSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComputeNetworkBlockSummary.
        The `OCID`__ of the compute network block.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ComputeNetworkBlockSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ComputeNetworkBlockSummary.
        The current state of the compute network block.


        :return: The lifecycle_state of this ComputeNetworkBlockSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ComputeNetworkBlockSummary.
        The current state of the compute network block.


        :param lifecycle_state: The lifecycle_state of this ComputeNetworkBlockSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ComputeNetworkBlockSummary.
        The date and time that the compute network block was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ComputeNetworkBlockSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ComputeNetworkBlockSummary.
        The date and time that the compute network block was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ComputeNetworkBlockSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ComputeNetworkBlockSummary.
        The date and time that the compute network block was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ComputeNetworkBlockSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ComputeNetworkBlockSummary.
        The date and time that the compute network block was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ComputeNetworkBlockSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def total_compute_bare_metal_host_count(self):
        """
        **[Required]** Gets the total_compute_bare_metal_host_count of this ComputeNetworkBlockSummary.
        The total number of compute bare metal hosts located in the compute network block.


        :return: The total_compute_bare_metal_host_count of this ComputeNetworkBlockSummary.
        :rtype: int
        """
        return self._total_compute_bare_metal_host_count

    @total_compute_bare_metal_host_count.setter
    def total_compute_bare_metal_host_count(self, total_compute_bare_metal_host_count):
        """
        Sets the total_compute_bare_metal_host_count of this ComputeNetworkBlockSummary.
        The total number of compute bare metal hosts located in the compute network block.


        :param total_compute_bare_metal_host_count: The total_compute_bare_metal_host_count of this ComputeNetworkBlockSummary.
        :type: int
        """
        self._total_compute_bare_metal_host_count = total_compute_bare_metal_host_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
