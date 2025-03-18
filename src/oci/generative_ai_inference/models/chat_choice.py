# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChatChoice(object):
    """
    Represents a single instance of the chat response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChatChoice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param index:
            The value to assign to the index property of this ChatChoice.
        :type index: int

        :param message:
            The value to assign to the message property of this ChatChoice.
        :type message: oci.generative_ai_inference.models.Message

        :param finish_reason:
            The value to assign to the finish_reason property of this ChatChoice.
        :type finish_reason: str

        :param logprobs:
            The value to assign to the logprobs property of this ChatChoice.
        :type logprobs: oci.generative_ai_inference.models.Logprobs

        """
        self.swagger_types = {
            'index': 'int',
            'message': 'Message',
            'finish_reason': 'str',
            'logprobs': 'Logprobs'
        }
        self.attribute_map = {
            'index': 'index',
            'message': 'message',
            'finish_reason': 'finishReason',
            'logprobs': 'logprobs'
        }
        self._index = None
        self._message = None
        self._finish_reason = None
        self._logprobs = None

    @property
    def index(self):
        """
        **[Required]** Gets the index of this ChatChoice.
        The index of the chat.


        :return: The index of this ChatChoice.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this ChatChoice.
        The index of the chat.


        :param index: The index of this ChatChoice.
        :type: int
        """
        self._index = index

    @property
    def message(self):
        """
        **[Required]** Gets the message of this ChatChoice.

        :return: The message of this ChatChoice.
        :rtype: oci.generative_ai_inference.models.Message
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ChatChoice.

        :param message: The message of this ChatChoice.
        :type: oci.generative_ai_inference.models.Message
        """
        self._message = message

    @property
    def finish_reason(self):
        """
        **[Required]** Gets the finish_reason of this ChatChoice.
        The reason why the model stopped generating tokens.

        Stops if the model hits a natural stop point or a provided stop sequence. Returns the length if the tokens reach the specified maximum number of tokens.


        :return: The finish_reason of this ChatChoice.
        :rtype: str
        """
        return self._finish_reason

    @finish_reason.setter
    def finish_reason(self, finish_reason):
        """
        Sets the finish_reason of this ChatChoice.
        The reason why the model stopped generating tokens.

        Stops if the model hits a natural stop point or a provided stop sequence. Returns the length if the tokens reach the specified maximum number of tokens.


        :param finish_reason: The finish_reason of this ChatChoice.
        :type: str
        """
        self._finish_reason = finish_reason

    @property
    def logprobs(self):
        """
        Gets the logprobs of this ChatChoice.

        :return: The logprobs of this ChatChoice.
        :rtype: oci.generative_ai_inference.models.Logprobs
        """
        return self._logprobs

    @logprobs.setter
    def logprobs(self, logprobs):
        """
        Sets the logprobs of this ChatChoice.

        :param logprobs: The logprobs of this ChatChoice.
        :type: oci.generative_ai_inference.models.Logprobs
        """
        self._logprobs = logprobs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
