# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200202


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployPluginsDetails(object):
    """
    The information required to deploy new Management Agent Plugins.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployPluginsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plugin_ids:
            The value to assign to the plugin_ids property of this DeployPluginsDetails.
        :type plugin_ids: list[str]

        :param agent_compartment_id:
            The value to assign to the agent_compartment_id property of this DeployPluginsDetails.
        :type agent_compartment_id: str

        :param agent_ids:
            The value to assign to the agent_ids property of this DeployPluginsDetails.
        :type agent_ids: list[str]

        """
        self.swagger_types = {
            'plugin_ids': 'list[str]',
            'agent_compartment_id': 'str',
            'agent_ids': 'list[str]'
        }
        self.attribute_map = {
            'plugin_ids': 'pluginIds',
            'agent_compartment_id': 'agentCompartmentId',
            'agent_ids': 'agentIds'
        }
        self._plugin_ids = None
        self._agent_compartment_id = None
        self._agent_ids = None

    @property
    def plugin_ids(self):
        """
        **[Required]** Gets the plugin_ids of this DeployPluginsDetails.
        Plugin Id


        :return: The plugin_ids of this DeployPluginsDetails.
        :rtype: list[str]
        """
        return self._plugin_ids

    @plugin_ids.setter
    def plugin_ids(self, plugin_ids):
        """
        Sets the plugin_ids of this DeployPluginsDetails.
        Plugin Id


        :param plugin_ids: The plugin_ids of this DeployPluginsDetails.
        :type: list[str]
        """
        self._plugin_ids = plugin_ids

    @property
    def agent_compartment_id(self):
        """
        **[Required]** Gets the agent_compartment_id of this DeployPluginsDetails.
        Management Agent Compartment Identifier


        :return: The agent_compartment_id of this DeployPluginsDetails.
        :rtype: str
        """
        return self._agent_compartment_id

    @agent_compartment_id.setter
    def agent_compartment_id(self, agent_compartment_id):
        """
        Sets the agent_compartment_id of this DeployPluginsDetails.
        Management Agent Compartment Identifier


        :param agent_compartment_id: The agent_compartment_id of this DeployPluginsDetails.
        :type: str
        """
        self._agent_compartment_id = agent_compartment_id

    @property
    def agent_ids(self):
        """
        **[Required]** Gets the agent_ids of this DeployPluginsDetails.
        List of Agent identifiers


        :return: The agent_ids of this DeployPluginsDetails.
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        """
        Sets the agent_ids of this DeployPluginsDetails.
        List of Agent identifiers


        :param agent_ids: The agent_ids of this DeployPluginsDetails.
        :type: list[str]
        """
        self._agent_ids = agent_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
