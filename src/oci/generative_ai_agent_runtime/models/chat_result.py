# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChatResult(object):
    """
    The response of a chat request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChatResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this ChatResult.
        :type message: oci.generative_ai_agent_runtime.models.Message

        :param traces:
            The value to assign to the traces property of this ChatResult.
        :type traces: list[oci.generative_ai_agent_runtime.models.Trace]

        """
        self.swagger_types = {
            'message': 'Message',
            'traces': 'list[Trace]'
        }
        self.attribute_map = {
            'message': 'message',
            'traces': 'traces'
        }
        self._message = None
        self._traces = None

    @property
    def message(self):
        """
        Gets the message of this ChatResult.

        :return: The message of this ChatResult.
        :rtype: oci.generative_ai_agent_runtime.models.Message
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ChatResult.

        :param message: The message of this ChatResult.
        :type: oci.generative_ai_agent_runtime.models.Message
        """
        self._message = message

    @property
    def traces(self):
        """
        Gets the traces of this ChatResult.
        The trace that displays the internal progression, such as reasoning and actions during an execution.


        :return: The traces of this ChatResult.
        :rtype: list[oci.generative_ai_agent_runtime.models.Trace]
        """
        return self._traces

    @traces.setter
    def traces(self, traces):
        """
        Sets the traces of this ChatResult.
        The trace that displays the internal progression, such as reasoning and actions during an execution.


        :param traces: The traces of this ChatResult.
        :type: list[oci.generative_ai_agent_runtime.models.Trace]
        """
        self._traces = traces

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
