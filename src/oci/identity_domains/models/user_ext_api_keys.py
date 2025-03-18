# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtApiKeys(object):
    """
    A list of API keys corresponding to user.

    **Added In:** 2012271618

    **SCIM++ Properties:**
    - idcsCompositeKey: [value]
    - idcsSearchable: true
    - multiValued: true
    - mutability: readOnly
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtApiKeys object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this UserExtApiKeys.
        :type key: str

        :param value:
            The value to assign to the value property of this UserExtApiKeys.
        :type value: str

        :param ocid:
            The value to assign to the ocid property of this UserExtApiKeys.
        :type ocid: str

        :param ref:
            The value to assign to the ref property of this UserExtApiKeys.
        :type ref: str

        """
        self.swagger_types = {
            'key': 'str',
            'value': 'str',
            'ocid': 'str',
            'ref': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'value': 'value',
            'ocid': 'ocid',
            'ref': '$ref'
        }
        self._key = None
        self._value = None
        self._ocid = None
        self._ref = None

    @property
    def key(self):
        """
        Gets the key of this UserExtApiKeys.
        The user's API key value.

        **Added In:** 2106240046

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The key of this UserExtApiKeys.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this UserExtApiKeys.
        The user's API key value.

        **Added In:** 2106240046

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param key: The key of this UserExtApiKeys.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """
        Gets the value of this UserExtApiKeys.
        The user's API key identifier.

        **Added In:** 2012271618

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this UserExtApiKeys.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtApiKeys.
        The user's API key identifier.

        **Added In:** 2012271618

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtApiKeys.
        :type: str
        """
        self._value = value

    @property
    def ocid(self):
        """
        Gets the ocid of this UserExtApiKeys.
        The user's API key OCID.

        **Added In:** 2012271618

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The ocid of this UserExtApiKeys.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this UserExtApiKeys.
        The user's API key OCID.

        **Added In:** 2012271618

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this UserExtApiKeys.
        :type: str
        """
        self._ocid = ocid

    @property
    def ref(self):
        """
        Gets the ref of this UserExtApiKeys.
        The URI of the corresponding ApiKey resource to which the user belongs.

        **Added In:** 2012271618

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtApiKeys.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtApiKeys.
        The URI of the corresponding ApiKey resource to which the user belongs.

        **Added In:** 2012271618

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtApiKeys.
        :type: str
        """
        self._ref = ref

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
