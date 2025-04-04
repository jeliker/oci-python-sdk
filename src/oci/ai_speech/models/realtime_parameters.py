# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RealtimeParameters(object):
    """
    Parameters to be sent to the realtime speech service over a websocket connection.
    """

    #: A constant which can be used with the stabilize_partial_results property of a RealtimeParameters.
    #: This constant has a value of "NONE"
    STABILIZE_PARTIAL_RESULTS_NONE = "NONE"

    #: A constant which can be used with the stabilize_partial_results property of a RealtimeParameters.
    #: This constant has a value of "LOW"
    STABILIZE_PARTIAL_RESULTS_LOW = "LOW"

    #: A constant which can be used with the stabilize_partial_results property of a RealtimeParameters.
    #: This constant has a value of "MEDIUM"
    STABILIZE_PARTIAL_RESULTS_MEDIUM = "MEDIUM"

    #: A constant which can be used with the stabilize_partial_results property of a RealtimeParameters.
    #: This constant has a value of "HIGH"
    STABILIZE_PARTIAL_RESULTS_HIGH = "HIGH"

    #: A constant which can be used with the model_domain property of a RealtimeParameters.
    #: This constant has a value of "GENERIC"
    MODEL_DOMAIN_GENERIC = "GENERIC"

    #: A constant which can be used with the model_domain property of a RealtimeParameters.
    #: This constant has a value of "MEDICAL"
    MODEL_DOMAIN_MEDICAL = "MEDICAL"

    #: A constant which can be used with the punctuation property of a RealtimeParameters.
    #: This constant has a value of "NONE"
    PUNCTUATION_NONE = "NONE"

    #: A constant which can be used with the punctuation property of a RealtimeParameters.
    #: This constant has a value of "SPOKEN"
    PUNCTUATION_SPOKEN = "SPOKEN"

    #: A constant which can be used with the punctuation property of a RealtimeParameters.
    #: This constant has a value of "AUTO"
    PUNCTUATION_AUTO = "AUTO"

    def __init__(self, **kwargs):
        """
        Initializes a new RealtimeParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encoding:
            The value to assign to the encoding property of this RealtimeParameters.
        :type encoding: str

        :param is_ack_enabled:
            The value to assign to the is_ack_enabled property of this RealtimeParameters.
        :type is_ack_enabled: bool

        :param partial_silence_threshold_in_ms:
            The value to assign to the partial_silence_threshold_in_ms property of this RealtimeParameters.
        :type partial_silence_threshold_in_ms: int

        :param final_silence_threshold_in_ms:
            The value to assign to the final_silence_threshold_in_ms property of this RealtimeParameters.
        :type final_silence_threshold_in_ms: int

        :param stabilize_partial_results:
            The value to assign to the stabilize_partial_results property of this RealtimeParameters.
            Allowed values for this property are: "NONE", "LOW", "MEDIUM", "HIGH"
        :type stabilize_partial_results: str

        :param model_domain:
            The value to assign to the model_domain property of this RealtimeParameters.
            Allowed values for this property are: "GENERIC", "MEDICAL"
        :type model_domain: str

        :param language_code:
            The value to assign to the language_code property of this RealtimeParameters.
        :type language_code: str

        :param should_ignore_invalid_customizations:
            The value to assign to the should_ignore_invalid_customizations property of this RealtimeParameters.
        :type should_ignore_invalid_customizations: bool

        :param customizations:
            The value to assign to the customizations property of this RealtimeParameters.
        :type customizations: list[oci.ai_speech.models.CustomizationInference]

        :param punctuation:
            The value to assign to the punctuation property of this RealtimeParameters.
            Allowed values for this property are: "NONE", "SPOKEN", "AUTO"
        :type punctuation: str

        """
        self.swagger_types = {
            'encoding': 'str',
            'is_ack_enabled': 'bool',
            'partial_silence_threshold_in_ms': 'int',
            'final_silence_threshold_in_ms': 'int',
            'stabilize_partial_results': 'str',
            'model_domain': 'str',
            'language_code': 'str',
            'should_ignore_invalid_customizations': 'bool',
            'customizations': 'list[CustomizationInference]',
            'punctuation': 'str'
        }
        self.attribute_map = {
            'encoding': 'encoding',
            'is_ack_enabled': 'isAckEnabled',
            'partial_silence_threshold_in_ms': 'partialSilenceThresholdInMs',
            'final_silence_threshold_in_ms': 'finalSilenceThresholdInMs',
            'stabilize_partial_results': 'stabilizePartialResults',
            'model_domain': 'modelDomain',
            'language_code': 'languageCode',
            'should_ignore_invalid_customizations': 'shouldIgnoreInvalidCustomizations',
            'customizations': 'customizations',
            'punctuation': 'punctuation'
        }
        self._encoding = None
        self._is_ack_enabled = None
        self._partial_silence_threshold_in_ms = None
        self._final_silence_threshold_in_ms = None
        self._stabilize_partial_results = None
        self._model_domain = None
        self._language_code = None
        self._should_ignore_invalid_customizations = None
        self._customizations = None
        self._punctuation = None

    @property
    def encoding(self):
        """
        Gets the encoding of this RealtimeParameters.
        Audio encoding to use
        - audio/raw;rate=16000
        - audio/raw;rate=8000
        - audio/raw;rate=8000;codec=mulaw
        - audio/raw;rate=8000;codec=alaw


        :return: The encoding of this RealtimeParameters.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this RealtimeParameters.
        Audio encoding to use
        - audio/raw;rate=16000
        - audio/raw;rate=8000
        - audio/raw;rate=8000;codec=mulaw
        - audio/raw;rate=8000;codec=alaw


        :param encoding: The encoding of this RealtimeParameters.
        :type: str
        """
        self._encoding = encoding

    @property
    def is_ack_enabled(self):
        """
        Gets the is_ack_enabled of this RealtimeParameters.
        Toggle for ack messages.


        :return: The is_ack_enabled of this RealtimeParameters.
        :rtype: bool
        """
        return self._is_ack_enabled

    @is_ack_enabled.setter
    def is_ack_enabled(self, is_ack_enabled):
        """
        Sets the is_ack_enabled of this RealtimeParameters.
        Toggle for ack messages.


        :param is_ack_enabled: The is_ack_enabled of this RealtimeParameters.
        :type: bool
        """
        self._is_ack_enabled = is_ack_enabled

    @property
    def partial_silence_threshold_in_ms(self):
        """
        Gets the partial_silence_threshold_in_ms of this RealtimeParameters.
        Silence threshold for Realtime Speech partial results in milliseconds.


        :return: The partial_silence_threshold_in_ms of this RealtimeParameters.
        :rtype: int
        """
        return self._partial_silence_threshold_in_ms

    @partial_silence_threshold_in_ms.setter
    def partial_silence_threshold_in_ms(self, partial_silence_threshold_in_ms):
        """
        Sets the partial_silence_threshold_in_ms of this RealtimeParameters.
        Silence threshold for Realtime Speech partial results in milliseconds.


        :param partial_silence_threshold_in_ms: The partial_silence_threshold_in_ms of this RealtimeParameters.
        :type: int
        """
        self._partial_silence_threshold_in_ms = partial_silence_threshold_in_ms

    @property
    def final_silence_threshold_in_ms(self):
        """
        Gets the final_silence_threshold_in_ms of this RealtimeParameters.
        Silence threshold for Realtime Speech final results in milliseconds.


        :return: The final_silence_threshold_in_ms of this RealtimeParameters.
        :rtype: int
        """
        return self._final_silence_threshold_in_ms

    @final_silence_threshold_in_ms.setter
    def final_silence_threshold_in_ms(self, final_silence_threshold_in_ms):
        """
        Sets the final_silence_threshold_in_ms of this RealtimeParameters.
        Silence threshold for Realtime Speech final results in milliseconds.


        :param final_silence_threshold_in_ms: The final_silence_threshold_in_ms of this RealtimeParameters.
        :type: int
        """
        self._final_silence_threshold_in_ms = final_silence_threshold_in_ms

    @property
    def stabilize_partial_results(self):
        """
        Gets the stabilize_partial_results of this RealtimeParameters.
        When enabled sets the amount of confidence required for latest tokens before returning them as part of a new partial result

        Allowed values for this property are: "NONE", "LOW", "MEDIUM", "HIGH"


        :return: The stabilize_partial_results of this RealtimeParameters.
        :rtype: str
        """
        return self._stabilize_partial_results

    @stabilize_partial_results.setter
    def stabilize_partial_results(self, stabilize_partial_results):
        """
        Sets the stabilize_partial_results of this RealtimeParameters.
        When enabled sets the amount of confidence required for latest tokens before returning them as part of a new partial result


        :param stabilize_partial_results: The stabilize_partial_results of this RealtimeParameters.
        :type: str
        """
        allowed_values = ["NONE", "LOW", "MEDIUM", "HIGH"]
        if not value_allowed_none_or_none_sentinel(stabilize_partial_results, allowed_values):
            raise ValueError(
                f"Invalid value for `stabilize_partial_results`, must be None or one of {allowed_values}"
            )
        self._stabilize_partial_results = stabilize_partial_results

    @property
    def model_domain(self):
        """
        Gets the model_domain of this RealtimeParameters.
        Model Domain.

        Allowed values for this property are: "GENERIC", "MEDICAL"


        :return: The model_domain of this RealtimeParameters.
        :rtype: str
        """
        return self._model_domain

    @model_domain.setter
    def model_domain(self, model_domain):
        """
        Sets the model_domain of this RealtimeParameters.
        Model Domain.


        :param model_domain: The model_domain of this RealtimeParameters.
        :type: str
        """
        allowed_values = ["GENERIC", "MEDICAL"]
        if not value_allowed_none_or_none_sentinel(model_domain, allowed_values):
            raise ValueError(
                f"Invalid value for `model_domain`, must be None or one of {allowed_values}"
            )
        self._model_domain = model_domain

    @property
    def language_code(self):
        """
        Gets the language_code of this RealtimeParameters.
        Locale value as per given in [https://datatracker.ietf.org/doc/html/rfc5646].
        - en-US: English - United States
        - es-ES: Spanish - Spain
        - pt-BR: Portuguese - Brazil
        - en-GB: English - Great Britain
        - en-AU: English - Australia
        - en-IN: English - India
        - hi-IN: Hindi - India
        - fr-FR: French - France
        - de-DE: German - Germany
        - it-IT: Italian - Italy


        :return: The language_code of this RealtimeParameters.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this RealtimeParameters.
        Locale value as per given in [https://datatracker.ietf.org/doc/html/rfc5646].
        - en-US: English - United States
        - es-ES: Spanish - Spain
        - pt-BR: Portuguese - Brazil
        - en-GB: English - Great Britain
        - en-AU: English - Australia
        - en-IN: English - India
        - hi-IN: Hindi - India
        - fr-FR: French - France
        - de-DE: German - Germany
        - it-IT: Italian - Italy


        :param language_code: The language_code of this RealtimeParameters.
        :type: str
        """
        self._language_code = language_code

    @property
    def should_ignore_invalid_customizations(self):
        """
        Gets the should_ignore_invalid_customizations of this RealtimeParameters.
        If set to true, the service will not fail connection attempt if it encounters any issues that prevent the loading of all specified user customizations. Any invalid customizations will simply be ignored and connection will continue being established with the default base model and any remaining valid customizations.
        If set to false, if the service is unable to load any of the specified customizations, an error detailing why will be returned and the session will end.


        :return: The should_ignore_invalid_customizations of this RealtimeParameters.
        :rtype: bool
        """
        return self._should_ignore_invalid_customizations

    @should_ignore_invalid_customizations.setter
    def should_ignore_invalid_customizations(self, should_ignore_invalid_customizations):
        """
        Sets the should_ignore_invalid_customizations of this RealtimeParameters.
        If set to true, the service will not fail connection attempt if it encounters any issues that prevent the loading of all specified user customizations. Any invalid customizations will simply be ignored and connection will continue being established with the default base model and any remaining valid customizations.
        If set to false, if the service is unable to load any of the specified customizations, an error detailing why will be returned and the session will end.


        :param should_ignore_invalid_customizations: The should_ignore_invalid_customizations of this RealtimeParameters.
        :type: bool
        """
        self._should_ignore_invalid_customizations = should_ignore_invalid_customizations

    @property
    def customizations(self):
        """
        Gets the customizations of this RealtimeParameters.
        Array of customization objects.


        :return: The customizations of this RealtimeParameters.
        :rtype: list[oci.ai_speech.models.CustomizationInference]
        """
        return self._customizations

    @customizations.setter
    def customizations(self, customizations):
        """
        Sets the customizations of this RealtimeParameters.
        Array of customization objects.


        :param customizations: The customizations of this RealtimeParameters.
        :type: list[oci.ai_speech.models.CustomizationInference]
        """
        self._customizations = customizations

    @property
    def punctuation(self):
        """
        Gets the punctuation of this RealtimeParameters.
        Configure punctuations in the generated transcriptions. Disabled by default.
        - NONE: No punctuation in the transcription response
        - SPOKEN: Punctuations in response only when verbally spoken
        - AUTO: Automatic punctuation in the response, spoken punctuations are disabled

        Allowed values for this property are: "NONE", "SPOKEN", "AUTO"


        :return: The punctuation of this RealtimeParameters.
        :rtype: str
        """
        return self._punctuation

    @punctuation.setter
    def punctuation(self, punctuation):
        """
        Sets the punctuation of this RealtimeParameters.
        Configure punctuations in the generated transcriptions. Disabled by default.
        - NONE: No punctuation in the transcription response
        - SPOKEN: Punctuations in response only when verbally spoken
        - AUTO: Automatic punctuation in the response, spoken punctuations are disabled


        :param punctuation: The punctuation of this RealtimeParameters.
        :type: str
        """
        allowed_values = ["NONE", "SPOKEN", "AUTO"]
        if not value_allowed_none_or_none_sentinel(punctuation, allowed_values):
            raise ValueError(
                f"Invalid value for `punctuation`, must be None or one of {allowed_values}"
            )
        self._punctuation = punctuation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
