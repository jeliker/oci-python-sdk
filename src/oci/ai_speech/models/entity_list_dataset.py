# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101

from .customization_dataset_details import CustomizationDatasetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityListDataset(CustomizationDatasetDetails):
    """
    Entity List Dataset
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityListDataset object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_speech.models.EntityListDataset.dataset_type` attribute
        of this class is ``ENTITY_LIST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dataset_type:
            The value to assign to the dataset_type property of this EntityListDataset.
            Allowed values for this property are: "OBJECT_STORAGE", "ENTITY_LIST"
        :type dataset_type: str

        :param reference_examples:
            The value to assign to the reference_examples property of this EntityListDataset.
        :type reference_examples: list[str]

        :param entity_list:
            The value to assign to the entity_list property of this EntityListDataset.
        :type entity_list: list[oci.ai_speech.models.EntityList]

        """
        self.swagger_types = {
            'dataset_type': 'str',
            'reference_examples': 'list[str]',
            'entity_list': 'list[EntityList]'
        }

        self.attribute_map = {
            'dataset_type': 'datasetType',
            'reference_examples': 'referenceExamples',
            'entity_list': 'entityList'
        }

        self._dataset_type = None
        self._reference_examples = None
        self._entity_list = None
        self._dataset_type = 'ENTITY_LIST'

    @property
    def reference_examples(self):
        """
        Gets the reference_examples of this EntityListDataset.
        List of sentences referencing 1 or more entityType matching those defined in the linked entityLists, used to improve accuracy by providing model training context of where/how an entity may appear in a sentence.
        EntityTypes referenced in sentences should be written in all caps surrounded by angled braces (i.e \"<PATIENT>\" if entityType=patient)


        :return: The reference_examples of this EntityListDataset.
        :rtype: list[str]
        """
        return self._reference_examples

    @reference_examples.setter
    def reference_examples(self, reference_examples):
        """
        Sets the reference_examples of this EntityListDataset.
        List of sentences referencing 1 or more entityType matching those defined in the linked entityLists, used to improve accuracy by providing model training context of where/how an entity may appear in a sentence.
        EntityTypes referenced in sentences should be written in all caps surrounded by angled braces (i.e \"<PATIENT>\" if entityType=patient)


        :param reference_examples: The reference_examples of this EntityListDataset.
        :type: list[str]
        """
        self._reference_examples = reference_examples

    @property
    def entity_list(self):
        """
        Gets the entity_list of this EntityListDataset.
        Array of entityLists


        :return: The entity_list of this EntityListDataset.
        :rtype: list[oci.ai_speech.models.EntityList]
        """
        return self._entity_list

    @entity_list.setter
    def entity_list(self, entity_list):
        """
        Sets the entity_list of this EntityListDataset.
        Array of entityLists


        :param entity_list: The entity_list of this EntityListDataset.
        :type: list[oci.ai_speech.models.EntityList]
        """
        self._entity_list = entity_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
