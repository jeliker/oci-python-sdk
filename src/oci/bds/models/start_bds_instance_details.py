# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StartBdsInstanceDetails(object):
    """
    The request body for starting a BDS cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StartBdsInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this StartBdsInstanceDetails.
        :type cluster_admin_password: str

        :param start_cluster_shape_configs:
            The value to assign to the start_cluster_shape_configs property of this StartBdsInstanceDetails.
        :type start_cluster_shape_configs: oci.bds.models.StartClusterShapeConfigs

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'start_cluster_shape_configs': 'StartClusterShapeConfigs'
        }
        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'start_cluster_shape_configs': 'startClusterShapeConfigs'
        }
        self._cluster_admin_password = None
        self._start_cluster_shape_configs = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this StartBdsInstanceDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this StartBdsInstanceDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this StartBdsInstanceDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this StartBdsInstanceDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def start_cluster_shape_configs(self):
        """
        Gets the start_cluster_shape_configs of this StartBdsInstanceDetails.

        :return: The start_cluster_shape_configs of this StartBdsInstanceDetails.
        :rtype: oci.bds.models.StartClusterShapeConfigs
        """
        return self._start_cluster_shape_configs

    @start_cluster_shape_configs.setter
    def start_cluster_shape_configs(self, start_cluster_shape_configs):
        """
        Sets the start_cluster_shape_configs of this StartBdsInstanceDetails.

        :param start_cluster_shape_configs: The start_cluster_shape_configs of this StartBdsInstanceDetails.
        :type: oci.bds.models.StartClusterShapeConfigs
        """
        self._start_cluster_shape_configs = start_cluster_shape_configs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
