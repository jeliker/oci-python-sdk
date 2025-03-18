# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppEditableAttributes(object):
    """
    App attributes editable by subject
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppEditableAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AppEditableAttributes.
        :type name: str

        """
        self.swagger_types = {
            'name': 'str'
        }
        self.attribute_map = {
            'name': 'name'
        }
        self._name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AppEditableAttributes.
        Name of the attribute. The attribute name will be qualified by schema name if any extension schema defines the attribute. The attribute name will not be qualified by schema name if the base schema defines the attribute.

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this AppEditableAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppEditableAttributes.
        Name of the attribute. The attribute name will be qualified by schema name if any extension schema defines the attribute. The attribute name will not be qualified by schema name if the base schema defines the attribute.

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this AppEditableAttributes.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
