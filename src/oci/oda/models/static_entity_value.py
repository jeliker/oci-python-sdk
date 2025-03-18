# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StaticEntityValue(object):
    """
    Value in a static entity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StaticEntityValue object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param canonical_name:
            The value to assign to the canonical_name property of this StaticEntityValue.
        :type canonical_name: str

        :param natural_language_mapping:
            The value to assign to the natural_language_mapping property of this StaticEntityValue.
        :type natural_language_mapping: oci.oda.models.StaticEntityValueNaturalLanguageMapping

        """
        self.swagger_types = {
            'canonical_name': 'str',
            'natural_language_mapping': 'StaticEntityValueNaturalLanguageMapping'
        }
        self.attribute_map = {
            'canonical_name': 'canonicalName',
            'natural_language_mapping': 'naturalLanguageMapping'
        }
        self._canonical_name = None
        self._natural_language_mapping = None

    @property
    def canonical_name(self):
        """
        **[Required]** Gets the canonical_name of this StaticEntityValue.
        Value for a static entity.


        :return: The canonical_name of this StaticEntityValue.
        :rtype: str
        """
        return self._canonical_name

    @canonical_name.setter
    def canonical_name(self, canonical_name):
        """
        Sets the canonical_name of this StaticEntityValue.
        Value for a static entity.


        :param canonical_name: The canonical_name of this StaticEntityValue.
        :type: str
        """
        self._canonical_name = canonical_name

    @property
    def natural_language_mapping(self):
        """
        Gets the natural_language_mapping of this StaticEntityValue.

        :return: The natural_language_mapping of this StaticEntityValue.
        :rtype: oci.oda.models.StaticEntityValueNaturalLanguageMapping
        """
        return self._natural_language_mapping

    @natural_language_mapping.setter
    def natural_language_mapping(self, natural_language_mapping):
        """
        Sets the natural_language_mapping of this StaticEntityValue.

        :param natural_language_mapping: The natural_language_mapping of this StaticEntityValue.
        :type: oci.oda.models.StaticEntityValueNaturalLanguageMapping
        """
        self._natural_language_mapping = natural_language_mapping

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
