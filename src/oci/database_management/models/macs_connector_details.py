# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .connector_details import ConnectorDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MacsConnectorDetails(ConnectorDetails):
    """
    The management agent details required to connect to an Oracle cloud Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MacsConnectorDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.MacsConnectorDetails.connector_type` attribute
        of this class is ``MACS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_type:
            The value to assign to the connector_type property of this MacsConnectorDetails.
            Allowed values for this property are: "PE", "MACS", "EXTERNAL", "DIRECT"
        :type connector_type: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MacsConnectorDetails.
        :type management_agent_id: str

        """
        self.swagger_types = {
            'connector_type': 'str',
            'management_agent_id': 'str'
        }
        self.attribute_map = {
            'connector_type': 'connectorType',
            'management_agent_id': 'managementAgentId'
        }
        self._connector_type = None
        self._management_agent_id = None
        self._connector_type = 'MACS'

    @property
    def management_agent_id(self):
        """
        **[Required]** Gets the management_agent_id of this MacsConnectorDetails.
        The `OCID`__ of the management agent.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MacsConnectorDetails.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MacsConnectorDetails.
        The `OCID`__ of the management agent.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MacsConnectorDetails.
        :type: str
        """
        self._management_agent_id = management_agent_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
