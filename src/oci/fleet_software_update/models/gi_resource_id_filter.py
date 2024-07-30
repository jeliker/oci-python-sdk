# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .gi_fleet_discovery_filter import GiFleetDiscoveryFilter
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GiResourceIdFilter(GiFleetDiscoveryFilter):
    """
    Related resource Ids to include in the discovery.
    """

    #: A constant which can be used with the entity_type property of a GiResourceIdFilter.
    #: This constant has a value of "DATABASESOFTWAREIMAGE"
    ENTITY_TYPE_DATABASESOFTWAREIMAGE = "DATABASESOFTWAREIMAGE"

    #: A constant which can be used with the entity_type property of a GiResourceIdFilter.
    #: This constant has a value of "EXADATAINFRASTRUCTURE"
    ENTITY_TYPE_EXADATAINFRASTRUCTURE = "EXADATAINFRASTRUCTURE"

    #: A constant which can be used with the entity_type property of a GiResourceIdFilter.
    #: This constant has a value of "CLOUDEXADATAINFRASTRUCTURE"
    ENTITY_TYPE_CLOUDEXADATAINFRASTRUCTURE = "CLOUDEXADATAINFRASTRUCTURE"

    #: A constant which can be used with the entity_type property of a GiResourceIdFilter.
    #: This constant has a value of "VMCLUSTER"
    ENTITY_TYPE_VMCLUSTER = "VMCLUSTER"

    #: A constant which can be used with the entity_type property of a GiResourceIdFilter.
    #: This constant has a value of "CLOUDVMCLUSTER"
    ENTITY_TYPE_CLOUDVMCLUSTER = "CLOUDVMCLUSTER"

    #: A constant which can be used with the entity_type property of a GiResourceIdFilter.
    #: This constant has a value of "FSUCOLLECTION"
    ENTITY_TYPE_FSUCOLLECTION = "FSUCOLLECTION"

    #: A constant which can be used with the operator property of a GiResourceIdFilter.
    #: This constant has a value of "AND"
    OPERATOR_AND = "AND"

    #: A constant which can be used with the operator property of a GiResourceIdFilter.
    #: This constant has a value of "OR"
    OPERATOR_OR = "OR"

    def __init__(self, **kwargs):
        """
        Initializes a new GiResourceIdFilter object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.GiResourceIdFilter.type` attribute
        of this class is ``RESOURCE_ID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this GiResourceIdFilter.
            Allowed values for this property are: "COMPARTMENT_ID", "VERSION", "FREEFORM_TAG", "DEFINED_TAG", "RESOURCE_ID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param mode:
            The value to assign to the mode property of this GiResourceIdFilter.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mode: str

        :param entity_type:
            The value to assign to the entity_type property of this GiResourceIdFilter.
            Allowed values for this property are: "DATABASESOFTWAREIMAGE", "EXADATAINFRASTRUCTURE", "CLOUDEXADATAINFRASTRUCTURE", "VMCLUSTER", "CLOUDVMCLUSTER", "FSUCOLLECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param identifiers:
            The value to assign to the identifiers property of this GiResourceIdFilter.
        :type identifiers: list[str]

        :param operator:
            The value to assign to the operator property of this GiResourceIdFilter.
            Allowed values for this property are: "AND", "OR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operator: str

        """
        self.swagger_types = {
            'type': 'str',
            'mode': 'str',
            'entity_type': 'str',
            'identifiers': 'list[str]',
            'operator': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'mode': 'mode',
            'entity_type': 'entityType',
            'identifiers': 'identifiers',
            'operator': 'operator'
        }

        self._type = None
        self._mode = None
        self._entity_type = None
        self._identifiers = None
        self._operator = None
        self._type = 'RESOURCE_ID'

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this GiResourceIdFilter.
        Type of resource to match in the discovery.

        Allowed values for this property are: "DATABASESOFTWAREIMAGE", "EXADATAINFRASTRUCTURE", "CLOUDEXADATAINFRASTRUCTURE", "VMCLUSTER", "CLOUDVMCLUSTER", "FSUCOLLECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this GiResourceIdFilter.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this GiResourceIdFilter.
        Type of resource to match in the discovery.


        :param entity_type: The entity_type of this GiResourceIdFilter.
        :type: str
        """
        allowed_values = ["DATABASESOFTWAREIMAGE", "EXADATAINFRASTRUCTURE", "CLOUDEXADATAINFRASTRUCTURE", "VMCLUSTER", "CLOUDVMCLUSTER", "FSUCOLLECTION"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    @property
    def identifiers(self):
        """
        **[Required]** Gets the identifiers of this GiResourceIdFilter.
        Related resource Ids to include in the discovery.
        All must match the specified entityType.


        :return: The identifiers of this GiResourceIdFilter.
        :rtype: list[str]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """
        Sets the identifiers of this GiResourceIdFilter.
        Related resource Ids to include in the discovery.
        All must match the specified entityType.


        :param identifiers: The identifiers of this GiResourceIdFilter.
        :type: list[str]
        """
        self._identifiers = identifiers

    @property
    def operator(self):
        """
        Gets the operator of this GiResourceIdFilter.
        Type of join for each element in this filter.

        Allowed values for this property are: "AND", "OR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operator of this GiResourceIdFilter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this GiResourceIdFilter.
        Type of join for each element in this filter.


        :param operator: The operator of this GiResourceIdFilter.
        :type: str
        """
        allowed_values = ["AND", "OR"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            operator = 'UNKNOWN_ENUM_VALUE'
        self._operator = operator

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
