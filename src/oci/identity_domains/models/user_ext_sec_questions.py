# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtSecQuestions(object):
    """
    The schema used to mnage security question and answers provided by a user for account recovery and/or MFA. While setting up security questions, a user can also provide a hint for the answer.

    **SCIM++ Properties:**
    - idcsCompositeKey: [value]
    - multiValued: true
    - mutability: readWrite
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtSecQuestions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserExtSecQuestions.
        :type value: str

        :param ref:
            The value to assign to the ref property of this UserExtSecQuestions.
        :type ref: str

        :param answer:
            The value to assign to the answer property of this UserExtSecQuestions.
        :type answer: str

        :param hint_text:
            The value to assign to the hint_text property of this UserExtSecQuestions.
        :type hint_text: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'answer': 'str',
            'hint_text': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'answer': 'answer',
            'hint_text': 'hintText'
        }
        self._value = None
        self._ref = None
        self._answer = None
        self._hint_text = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserExtSecQuestions.
        The identifier of the question selected by the user when setting up a security question.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this UserExtSecQuestions.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtSecQuestions.
        The identifier of the question selected by the user when setting up a security question.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtSecQuestions.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this UserExtSecQuestions.
        The URI of the corresponding Security Question resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtSecQuestions.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtSecQuestions.
        The URI of the corresponding Security Question resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtSecQuestions.
        :type: str
        """
        self._ref = ref

    @property
    def answer(self):
        """
        **[Required]** Gets the answer of this UserExtSecQuestions.
        The answer provided by a user for a security question.

        **SCIM++ Properties:**
         - idcsCsvAttributeName: Answer
         - idcsSearchable: false
         - idcsSensitive: hash
         - multiValued: false
         - mutability: writeOnly
         - required: true
         - returned: never
         - type: string
         - uniqueness: none
         - idcsPii: true


        :return: The answer of this UserExtSecQuestions.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """
        Sets the answer of this UserExtSecQuestions.
        The answer provided by a user for a security question.

        **SCIM++ Properties:**
         - idcsCsvAttributeName: Answer
         - idcsSearchable: false
         - idcsSensitive: hash
         - multiValued: false
         - mutability: writeOnly
         - required: true
         - returned: never
         - type: string
         - uniqueness: none
         - idcsPii: true


        :param answer: The answer of this UserExtSecQuestions.
        :type: str
        """
        self._answer = answer

    @property
    def hint_text(self):
        """
        Gets the hint_text of this UserExtSecQuestions.
        The hint for an answer that's given by user when setting up a security question.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The hint_text of this UserExtSecQuestions.
        :rtype: str
        """
        return self._hint_text

    @hint_text.setter
    def hint_text(self, hint_text):
        """
        Sets the hint_text of this UserExtSecQuestions.
        The hint for an answer that's given by user when setting up a security question.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param hint_text: The hint_text of this UserExtSecQuestions.
        :type: str
        """
        self._hint_text = hint_text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
