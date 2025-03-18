# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomizationInference(object):
    """
    Inference payload for using Customization in Realtime Speech or Async Speech
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomizationInference object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param customization_id:
            The value to assign to the customization_id property of this CustomizationInference.
        :type customization_id: str

        :param customization_alias:
            The value to assign to the customization_alias property of this CustomizationInference.
        :type customization_alias: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CustomizationInference.
        :type compartment_id: str

        :param entities:
            The value to assign to the entities property of this CustomizationInference.
        :type entities: list[oci.ai_speech.models.CustomizationInferenceEntity]

        """
        self.swagger_types = {
            'customization_id': 'str',
            'customization_alias': 'str',
            'compartment_id': 'str',
            'entities': 'list[CustomizationInferenceEntity]'
        }
        self.attribute_map = {
            'customization_id': 'customizationId',
            'customization_alias': 'customizationAlias',
            'compartment_id': 'compartmentId',
            'entities': 'entities'
        }
        self._customization_id = None
        self._customization_alias = None
        self._compartment_id = None
        self._entities = None

    @property
    def customization_id(self):
        """
        Gets the customization_id of this CustomizationInference.
        The `OCID`__ of the customization to use.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The customization_id of this CustomizationInference.
        :rtype: str
        """
        return self._customization_id

    @customization_id.setter
    def customization_id(self, customization_id):
        """
        Sets the customization_id of this CustomizationInference.
        The `OCID`__ of the customization to use.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param customization_id: The customization_id of this CustomizationInference.
        :type: str
        """
        self._customization_id = customization_id

    @property
    def customization_alias(self):
        """
        Gets the customization_alias of this CustomizationInference.
        Alias of the customization


        :return: The customization_alias of this CustomizationInference.
        :rtype: str
        """
        return self._customization_alias

    @customization_alias.setter
    def customization_alias(self, customization_alias):
        """
        Sets the customization_alias of this CustomizationInference.
        Alias of the customization


        :param customization_alias: The customization_alias of this CustomizationInference.
        :type: str
        """
        self._customization_alias = customization_alias

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CustomizationInference.
        The `OCID`__ of the compartment where customization is present

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CustomizationInference.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CustomizationInference.
        The `OCID`__ of the compartment where customization is present

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CustomizationInference.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def entities(self):
        """
        Gets the entities of this CustomizationInference.
        Entities present in the customization


        :return: The entities of this CustomizationInference.
        :rtype: list[oci.ai_speech.models.CustomizationInferenceEntity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this CustomizationInference.
        Entities present in the customization


        :param entities: The entities of this CustomizationInference.
        :type: list[oci.ai_speech.models.CustomizationInferenceEntity]
        """
        self._entities = entities

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
