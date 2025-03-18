# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChatDetails(object):
    """
    Details of the conversation for the model to respond.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChatDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ChatDetails.
        :type compartment_id: str

        :param serving_mode:
            The value to assign to the serving_mode property of this ChatDetails.
        :type serving_mode: oci.generative_ai_inference.models.ServingMode

        :param chat_request:
            The value to assign to the chat_request property of this ChatDetails.
        :type chat_request: oci.generative_ai_inference.models.BaseChatRequest

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'serving_mode': 'ServingMode',
            'chat_request': 'BaseChatRequest'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'serving_mode': 'servingMode',
            'chat_request': 'chatRequest'
        }
        self._compartment_id = None
        self._serving_mode = None
        self._chat_request = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ChatDetails.
        The OCID of compartment in which to call the Generative AI service to chat.


        :return: The compartment_id of this ChatDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ChatDetails.
        The OCID of compartment in which to call the Generative AI service to chat.


        :param compartment_id: The compartment_id of this ChatDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def serving_mode(self):
        """
        **[Required]** Gets the serving_mode of this ChatDetails.

        :return: The serving_mode of this ChatDetails.
        :rtype: oci.generative_ai_inference.models.ServingMode
        """
        return self._serving_mode

    @serving_mode.setter
    def serving_mode(self, serving_mode):
        """
        Sets the serving_mode of this ChatDetails.

        :param serving_mode: The serving_mode of this ChatDetails.
        :type: oci.generative_ai_inference.models.ServingMode
        """
        self._serving_mode = serving_mode

    @property
    def chat_request(self):
        """
        **[Required]** Gets the chat_request of this ChatDetails.

        :return: The chat_request of this ChatDetails.
        :rtype: oci.generative_ai_inference.models.BaseChatRequest
        """
        return self._chat_request

    @chat_request.setter
    def chat_request(self, chat_request):
        """
        Sets the chat_request of this ChatDetails.

        :param chat_request: The chat_request of this ChatDetails.
        :type: oci.generative_ai_inference.models.BaseChatRequest
        """
        self._chat_request = chat_request

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
