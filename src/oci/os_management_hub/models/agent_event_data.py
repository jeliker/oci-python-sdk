# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AgentEventData(object):
    """
    Provides additional information for an agent event.
    """

    #: A constant which can be used with the operation_type property of a AgentEventData.
    #: This constant has a value of "LIST_PACKAGES"
    OPERATION_TYPE_LIST_PACKAGES = "LIST_PACKAGES"

    #: A constant which can be used with the operation_type property of a AgentEventData.
    #: This constant has a value of "UPLOAD_CONTENT"
    OPERATION_TYPE_UPLOAD_CONTENT = "UPLOAD_CONTENT"

    #: A constant which can be used with the operation_type property of a AgentEventData.
    #: This constant has a value of "SYNC_AGENT_CONFIG"
    OPERATION_TYPE_SYNC_AGENT_CONFIG = "SYNC_AGENT_CONFIG"

    #: A constant which can be used with the status property of a AgentEventData.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a AgentEventData.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AgentEventData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this AgentEventData.
            Allowed values for this property are: "LIST_PACKAGES", "UPLOAD_CONTENT", "SYNC_AGENT_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this AgentEventData.
            Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param additional_details:
            The value to assign to the additional_details property of this AgentEventData.
        :type additional_details: oci.os_management_hub.models.WorkRequestEventDataAdditionalDetails

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'additional_details': 'WorkRequestEventDataAdditionalDetails'
        }
        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'additional_details': 'additionalDetails'
        }
        self._operation_type = None
        self._status = None
        self._additional_details = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this AgentEventData.
        Type of agent operation.

        Allowed values for this property are: "LIST_PACKAGES", "UPLOAD_CONTENT", "SYNC_AGENT_CONFIG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this AgentEventData.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this AgentEventData.
        Type of agent operation.


        :param operation_type: The operation_type of this AgentEventData.
        :type: str
        """
        allowed_values = ["LIST_PACKAGES", "UPLOAD_CONTENT", "SYNC_AGENT_CONFIG"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AgentEventData.
        Status of the agent operation.

        Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AgentEventData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AgentEventData.
        Status of the agent operation.


        :param status: The status of this AgentEventData.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def additional_details(self):
        """
        Gets the additional_details of this AgentEventData.

        :return: The additional_details of this AgentEventData.
        :rtype: oci.os_management_hub.models.WorkRequestEventDataAdditionalDetails
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this AgentEventData.

        :param additional_details: The additional_details of this AgentEventData.
        :type: oci.os_management_hub.models.WorkRequestEventDataAdditionalDetails
        """
        self._additional_details = additional_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
