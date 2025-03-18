# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceBundle(object):
    """
    Resource Bundle associated with an Offer
    """

    #: A constant which can be used with the type property of a ResourceBundle.
    #: This constant has a value of "LISTING"
    TYPE_LISTING = "LISTING"

    #: A constant which can be used with the unit_of_measurement property of a ResourceBundle.
    #: This constant has a value of "OCPU_PER_HOUR"
    UNIT_OF_MEASUREMENT_OCPU_PER_HOUR = "OCPU_PER_HOUR"

    #: A constant which can be used with the unit_of_measurement property of a ResourceBundle.
    #: This constant has a value of "INSTANCE_PER_HOUR"
    UNIT_OF_MEASUREMENT_INSTANCE_PER_HOUR = "INSTANCE_PER_HOUR"

    #: A constant which can be used with the unit_of_measurement property of a ResourceBundle.
    #: This constant has a value of "CREDITS"
    UNIT_OF_MEASUREMENT_CREDITS = "CREDITS"

    #: A constant which can be used with the unit_of_measurement property of a ResourceBundle.
    #: This constant has a value of "INSTANCES"
    UNIT_OF_MEASUREMENT_INSTANCES = "INSTANCES"

    #: A constant which can be used with the unit_of_measurement property of a ResourceBundle.
    #: This constant has a value of "NODES"
    UNIT_OF_MEASUREMENT_NODES = "NODES"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceBundle object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ResourceBundle.
            Allowed values for this property are: "LISTING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param quantity:
            The value to assign to the quantity property of this ResourceBundle.
        :type quantity: int

        :param unit_of_measurement:
            The value to assign to the unit_of_measurement property of this ResourceBundle.
            Allowed values for this property are: "OCPU_PER_HOUR", "INSTANCE_PER_HOUR", "CREDITS", "INSTANCES", "NODES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit_of_measurement: str

        :param resource_ids:
            The value to assign to the resource_ids property of this ResourceBundle.
        :type resource_ids: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'quantity': 'int',
            'unit_of_measurement': 'str',
            'resource_ids': 'list[str]'
        }
        self.attribute_map = {
            'type': 'type',
            'quantity': 'quantity',
            'unit_of_measurement': 'unitOfMeasurement',
            'resource_ids': 'resourceIds'
        }
        self._type = None
        self._quantity = None
        self._unit_of_measurement = None
        self._resource_ids = None

    @property
    def type(self):
        """
        Gets the type of this ResourceBundle.
        The type of resources in the bundle

        Allowed values for this property are: "LISTING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ResourceBundle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ResourceBundle.
        The type of resources in the bundle


        :param type: The type of this ResourceBundle.
        :type: str
        """
        allowed_values = ["LISTING"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def quantity(self):
        """
        Gets the quantity of this ResourceBundle.
        The quantity of a resources associated with the bundle


        :return: The quantity of this ResourceBundle.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ResourceBundle.
        The quantity of a resources associated with the bundle


        :param quantity: The quantity of this ResourceBundle.
        :type: int
        """
        self._quantity = quantity

    @property
    def unit_of_measurement(self):
        """
        Gets the unit_of_measurement of this ResourceBundle.
        The unit of measurement for the resource bundle

        Allowed values for this property are: "OCPU_PER_HOUR", "INSTANCE_PER_HOUR", "CREDITS", "INSTANCES", "NODES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit_of_measurement of this ResourceBundle.
        :rtype: str
        """
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        """
        Sets the unit_of_measurement of this ResourceBundle.
        The unit of measurement for the resource bundle


        :param unit_of_measurement: The unit_of_measurement of this ResourceBundle.
        :type: str
        """
        allowed_values = ["OCPU_PER_HOUR", "INSTANCE_PER_HOUR", "CREDITS", "INSTANCES", "NODES"]
        if not value_allowed_none_or_none_sentinel(unit_of_measurement, allowed_values):
            unit_of_measurement = 'UNKNOWN_ENUM_VALUE'
        self._unit_of_measurement = unit_of_measurement

    @property
    def resource_ids(self):
        """
        Gets the resource_ids of this ResourceBundle.
        the ids of the resources in the Offer


        :return: The resource_ids of this ResourceBundle.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """
        Sets the resource_ids of this ResourceBundle.
        the ids of the resources in the Offer


        :param resource_ids: The resource_ids of this ResourceBundle.
        :type: list[str]
        """
        self._resource_ids = resource_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
