# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeTypeShapeConfig(object):
    """
    Shape configuration at node type level. Start cluster will start all nodes as is if no config is specified.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeTypeShapeConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param node_type:
            The value to assign to the node_type property of this NodeTypeShapeConfig.
        :type node_type: str

        :param shape:
            The value to assign to the shape property of this NodeTypeShapeConfig.
        :type shape: str

        """
        self.swagger_types = {
            'node_type': 'str',
            'shape': 'str'
        }
        self.attribute_map = {
            'node_type': 'nodeType',
            'shape': 'shape'
        }
        self._node_type = None
        self._shape = None

    @property
    def node_type(self):
        """
        **[Required]** Gets the node_type of this NodeTypeShapeConfig.
        The Big Data Service cluster node type.


        :return: The node_type of this NodeTypeShapeConfig.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this NodeTypeShapeConfig.
        The Big Data Service cluster node type.


        :param node_type: The node_type of this NodeTypeShapeConfig.
        :type: str
        """
        self._node_type = node_type

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this NodeTypeShapeConfig.
        Shape of the node. This has to be specified when starting the cluster. Defaults to wn0 for homogeneous clusters and remains empty for heterogeneous clusters.
        If provided, all nodes in the node type will adopt the specified shape; otherwise, nodes retain their original shapes.


        :return: The shape of this NodeTypeShapeConfig.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this NodeTypeShapeConfig.
        Shape of the node. This has to be specified when starting the cluster. Defaults to wn0 for homogeneous clusters and remains empty for heterogeneous clusters.
        If provided, all nodes in the node type will adopt the specified shape; otherwise, nodes retain their original shapes.


        :param shape: The shape of this NodeTypeShapeConfig.
        :type: str
        """
        self._shape = shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
