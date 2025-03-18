# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180608


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecretGenerationContext(object):
    """
    Captures a configurable set of secret generation rules such as length, base characters, additional characters, and so on.
    """

    #: A constant which can be used with the generation_type property of a SecretGenerationContext.
    #: This constant has a value of "PASSPHRASE"
    GENERATION_TYPE_PASSPHRASE = "PASSPHRASE"

    #: A constant which can be used with the generation_type property of a SecretGenerationContext.
    #: This constant has a value of "SSH_KEY"
    GENERATION_TYPE_SSH_KEY = "SSH_KEY"

    #: A constant which can be used with the generation_type property of a SecretGenerationContext.
    #: This constant has a value of "BYTES"
    GENERATION_TYPE_BYTES = "BYTES"

    def __init__(self, **kwargs):
        """
        Initializes a new SecretGenerationContext object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vault.models.PassphraseGenerationContext`
        * :class:`~oci.vault.models.SshKeyGenerationContext`
        * :class:`~oci.vault.models.BytesGenerationContext`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param generation_type:
            The value to assign to the generation_type property of this SecretGenerationContext.
            Allowed values for this property are: "PASSPHRASE", "SSH_KEY", "BYTES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type generation_type: str

        :param secret_template:
            The value to assign to the secret_template property of this SecretGenerationContext.
        :type secret_template: str

        """
        self.swagger_types = {
            'generation_type': 'str',
            'secret_template': 'str'
        }
        self.attribute_map = {
            'generation_type': 'generationType',
            'secret_template': 'secretTemplate'
        }
        self._generation_type = None
        self._secret_template = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['generationType']

        if type == 'PASSPHRASE':
            return 'PassphraseGenerationContext'

        if type == 'SSH_KEY':
            return 'SshKeyGenerationContext'

        if type == 'BYTES':
            return 'BytesGenerationContext'
        else:
            return 'SecretGenerationContext'

    @property
    def generation_type(self):
        """
        **[Required]** Gets the generation_type of this SecretGenerationContext.
        Name of the predefined secret generation type.

        Allowed values for this property are: "PASSPHRASE", "SSH_KEY", "BYTES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The generation_type of this SecretGenerationContext.
        :rtype: str
        """
        return self._generation_type

    @generation_type.setter
    def generation_type(self, generation_type):
        """
        Sets the generation_type of this SecretGenerationContext.
        Name of the predefined secret generation type.


        :param generation_type: The generation_type of this SecretGenerationContext.
        :type: str
        """
        allowed_values = ["PASSPHRASE", "SSH_KEY", "BYTES"]
        if not value_allowed_none_or_none_sentinel(generation_type, allowed_values):
            generation_type = 'UNKNOWN_ENUM_VALUE'
        self._generation_type = generation_type

    @property
    def secret_template(self):
        """
        Gets the secret_template of this SecretGenerationContext.
        SecretTemplate captures structure in which customer wants to store secrets. This is optional and a default structure is available for each secret type.
        The template can have any structure with static values that are not generated. Within the template, you can insert predefined placeholders to store secrets.
        These placeholders are later replaced with the generated content and saved as a Base64 encoded content.


        :return: The secret_template of this SecretGenerationContext.
        :rtype: str
        """
        return self._secret_template

    @secret_template.setter
    def secret_template(self, secret_template):
        """
        Sets the secret_template of this SecretGenerationContext.
        SecretTemplate captures structure in which customer wants to store secrets. This is optional and a default structure is available for each secret type.
        The template can have any structure with static values that are not generated. Within the template, you can insert predefined placeholders to store secrets.
        These placeholders are later replaced with the generated content and saved as a Base64 encoded content.


        :param secret_template: The secret_template of this SecretGenerationContext.
        :type: str
        """
        self._secret_template = secret_template

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
