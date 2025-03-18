# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210101

from .input_details import InputDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectListInputDetails(InputDetails):
    """
    A list of object locations in Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectListInputDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.ObjectListInputDetails.input_type` attribute
        of this class is ``OBJECT_LIST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_type:
            The value to assign to the input_type property of this ObjectListInputDetails.
            Allowed values for this property are: "INLINE", "BASE64_ENCODED", "OBJECT_LIST"
        :type input_type: str

        :param object_locations:
            The value to assign to the object_locations property of this ObjectListInputDetails.
        :type object_locations: list[oci.ai_anomaly_detection.models.ObjectLocation]

        """
        self.swagger_types = {
            'input_type': 'str',
            'object_locations': 'list[ObjectLocation]'
        }
        self.attribute_map = {
            'input_type': 'inputType',
            'object_locations': 'objectLocations'
        }
        self._input_type = None
        self._object_locations = None
        self._input_type = 'OBJECT_LIST'

    @property
    def object_locations(self):
        """
        **[Required]** Gets the object_locations of this ObjectListInputDetails.
        List of ObjectLocations.


        :return: The object_locations of this ObjectListInputDetails.
        :rtype: list[oci.ai_anomaly_detection.models.ObjectLocation]
        """
        return self._object_locations

    @object_locations.setter
    def object_locations(self, object_locations):
        """
        Sets the object_locations of this ObjectListInputDetails.
        List of ObjectLocations.


        :param object_locations: The object_locations of this ObjectListInputDetails.
        :type: list[oci.ai_anomaly_detection.models.ObjectLocation]
        """
        self._object_locations = object_locations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
