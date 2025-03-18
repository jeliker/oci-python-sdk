# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomizationDatasetDetails(object):
    """
    Customization Training Dataset
    """

    #: A constant which can be used with the dataset_type property of a CustomizationDatasetDetails.
    #: This constant has a value of "OBJECT_STORAGE"
    DATASET_TYPE_OBJECT_STORAGE = "OBJECT_STORAGE"

    #: A constant which can be used with the dataset_type property of a CustomizationDatasetDetails.
    #: This constant has a value of "ENTITY_LIST"
    DATASET_TYPE_ENTITY_LIST = "ENTITY_LIST"

    def __init__(self, **kwargs):
        """
        Initializes a new CustomizationDatasetDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_speech.models.ObjectStorageDataset`
        * :class:`~oci.ai_speech.models.EntityListDataset`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dataset_type:
            The value to assign to the dataset_type property of this CustomizationDatasetDetails.
            Allowed values for this property are: "OBJECT_STORAGE", "ENTITY_LIST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dataset_type: str

        """
        self.swagger_types = {
            'dataset_type': 'str'
        }
        self.attribute_map = {
            'dataset_type': 'datasetType'
        }
        self._dataset_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['datasetType']

        if type == 'OBJECT_STORAGE':
            return 'ObjectStorageDataset'

        if type == 'ENTITY_LIST':
            return 'EntityListDataset'
        else:
            return 'CustomizationDatasetDetails'

    @property
    def dataset_type(self):
        """
        **[Required]** Gets the dataset_type of this CustomizationDatasetDetails.
        Possible data sets

        Allowed values for this property are: "OBJECT_STORAGE", "ENTITY_LIST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dataset_type of this CustomizationDatasetDetails.
        :rtype: str
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        """
        Sets the dataset_type of this CustomizationDatasetDetails.
        Possible data sets


        :param dataset_type: The dataset_type of this CustomizationDatasetDetails.
        :type: str
        """
        allowed_values = ["OBJECT_STORAGE", "ENTITY_LIST"]
        if not value_allowed_none_or_none_sentinel(dataset_type, allowed_values):
            dataset_type = 'UNKNOWN_ENUM_VALUE'
        self._dataset_type = dataset_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
