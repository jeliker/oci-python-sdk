# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OkeClusterManagedNodePoolConfiguration(object):
    """
    The managed node pool configuration properties for an OKE member.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OkeClusterManagedNodePoolConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OkeClusterManagedNodePoolConfiguration.
        :type id: str

        :param minimum:
            The value to assign to the minimum property of this OkeClusterManagedNodePoolConfiguration.
        :type minimum: int

        :param maximum:
            The value to assign to the maximum property of this OkeClusterManagedNodePoolConfiguration.
        :type maximum: int

        """
        self.swagger_types = {
            'id': 'str',
            'minimum': 'int',
            'maximum': 'int'
        }
        self.attribute_map = {
            'id': 'id',
            'minimum': 'minimum',
            'maximum': 'maximum'
        }
        self._id = None
        self._minimum = None
        self._maximum = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OkeClusterManagedNodePoolConfiguration.
        The OCID of the managed node pool in OKE cluster.


        :return: The id of this OkeClusterManagedNodePoolConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OkeClusterManagedNodePoolConfiguration.
        The OCID of the managed node pool in OKE cluster.


        :param id: The id of this OkeClusterManagedNodePoolConfiguration.
        :type: str
        """
        self._id = id

    @property
    def minimum(self):
        """
        Gets the minimum of this OkeClusterManagedNodePoolConfiguration.
        The minimum number to which nodes in the managed node pool could be scaled down.


        :return: The minimum of this OkeClusterManagedNodePoolConfiguration.
        :rtype: int
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """
        Sets the minimum of this OkeClusterManagedNodePoolConfiguration.
        The minimum number to which nodes in the managed node pool could be scaled down.


        :param minimum: The minimum of this OkeClusterManagedNodePoolConfiguration.
        :type: int
        """
        self._minimum = minimum

    @property
    def maximum(self):
        """
        Gets the maximum of this OkeClusterManagedNodePoolConfiguration.
        The maximum number to which nodes in the managed node pool could be scaled up.


        :return: The maximum of this OkeClusterManagedNodePoolConfiguration.
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """
        Sets the maximum of this OkeClusterManagedNodePoolConfiguration.
        The maximum number to which nodes in the managed node pool could be scaled up.


        :param maximum: The maximum of this OkeClusterManagedNodePoolConfiguration.
        :type: int
        """
        self._maximum = maximum

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
