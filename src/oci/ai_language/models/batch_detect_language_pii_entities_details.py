# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BatchDetectLanguagePiiEntitiesDetails(object):
    """
    The documents details to detect personal identification information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BatchDetectLanguagePiiEntitiesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param alias:
            The value to assign to the alias property of this BatchDetectLanguagePiiEntitiesDetails.
        :type alias: str

        :param endpoint_id:
            The value to assign to the endpoint_id property of this BatchDetectLanguagePiiEntitiesDetails.
        :type endpoint_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BatchDetectLanguagePiiEntitiesDetails.
        :type compartment_id: str

        :param documents:
            The value to assign to the documents property of this BatchDetectLanguagePiiEntitiesDetails.
        :type documents: list[oci.ai_language.models.TextDocument]

        :param masking:
            The value to assign to the masking property of this BatchDetectLanguagePiiEntitiesDetails.
        :type masking: dict(str, PiiEntityMasking)

        :param profile:
            The value to assign to the profile property of this BatchDetectLanguagePiiEntitiesDetails.
        :type profile: oci.ai_language.models.Profile

        """
        self.swagger_types = {
            'alias': 'str',
            'endpoint_id': 'str',
            'compartment_id': 'str',
            'documents': 'list[TextDocument]',
            'masking': 'dict(str, PiiEntityMasking)',
            'profile': 'Profile'
        }
        self.attribute_map = {
            'alias': 'alias',
            'endpoint_id': 'endpointId',
            'compartment_id': 'compartmentId',
            'documents': 'documents',
            'masking': 'masking',
            'profile': 'profile'
        }
        self._alias = None
        self._endpoint_id = None
        self._compartment_id = None
        self._documents = None
        self._masking = None
        self._profile = None

    @property
    def alias(self):
        """
        Gets the alias of this BatchDetectLanguagePiiEntitiesDetails.
        Unique name across user tenancy in a region to identify an endpoint to be used for inferencing.


        :return: The alias of this BatchDetectLanguagePiiEntitiesDetails.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this BatchDetectLanguagePiiEntitiesDetails.
        Unique name across user tenancy in a region to identify an endpoint to be used for inferencing.


        :param alias: The alias of this BatchDetectLanguagePiiEntitiesDetails.
        :type: str
        """
        self._alias = alias

    @property
    def endpoint_id(self):
        """
        Gets the endpoint_id of this BatchDetectLanguagePiiEntitiesDetails.
        The endpoint which have to be used for inferencing. If endpointId and compartmentId is provided, then inference will be served from custom model which is mapped to this Endpoint.


        :return: The endpoint_id of this BatchDetectLanguagePiiEntitiesDetails.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """
        Sets the endpoint_id of this BatchDetectLanguagePiiEntitiesDetails.
        The endpoint which have to be used for inferencing. If endpointId and compartmentId is provided, then inference will be served from custom model which is mapped to this Endpoint.


        :param endpoint_id: The endpoint_id of this BatchDetectLanguagePiiEntitiesDetails.
        :type: str
        """
        self._endpoint_id = endpoint_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this BatchDetectLanguagePiiEntitiesDetails.
        The `OCID`__ of the compartment that calls the API, inference will be served from pre trained model

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this BatchDetectLanguagePiiEntitiesDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BatchDetectLanguagePiiEntitiesDetails.
        The `OCID`__ of the compartment that calls the API, inference will be served from pre trained model

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this BatchDetectLanguagePiiEntitiesDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def documents(self):
        """
        **[Required]** Gets the documents of this BatchDetectLanguagePiiEntitiesDetails.
        List of documents to detect personal identification information.


        :return: The documents of this BatchDetectLanguagePiiEntitiesDetails.
        :rtype: list[oci.ai_language.models.TextDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this BatchDetectLanguagePiiEntitiesDetails.
        List of documents to detect personal identification information.


        :param documents: The documents of this BatchDetectLanguagePiiEntitiesDetails.
        :type: list[oci.ai_language.models.TextDocument]
        """
        self._documents = documents

    @property
    def masking(self):
        """
        Gets the masking of this BatchDetectLanguagePiiEntitiesDetails.
        Mask recognized PII entities with different modes.


        :return: The masking of this BatchDetectLanguagePiiEntitiesDetails.
        :rtype: dict(str, PiiEntityMasking)
        """
        return self._masking

    @masking.setter
    def masking(self, masking):
        """
        Sets the masking of this BatchDetectLanguagePiiEntitiesDetails.
        Mask recognized PII entities with different modes.


        :param masking: The masking of this BatchDetectLanguagePiiEntitiesDetails.
        :type: dict(str, PiiEntityMasking)
        """
        self._masking = masking

    @property
    def profile(self):
        """
        Gets the profile of this BatchDetectLanguagePiiEntitiesDetails.

        :return: The profile of this BatchDetectLanguagePiiEntitiesDetails.
        :rtype: oci.ai_language.models.Profile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this BatchDetectLanguagePiiEntitiesDetails.

        :param profile: The profile of this BatchDetectLanguagePiiEntitiesDetails.
        :type: oci.ai_language.models.Profile
        """
        self._profile = profile

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
