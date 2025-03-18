# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareSourceAvailability(object):
    """
    An object that defines the `OCID`__ and the availability of a vendor software source.

    __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
    """

    #: A constant which can be used with the availability property of a SoftwareSourceAvailability.
    #: This constant has a value of "AVAILABLE"
    AVAILABILITY_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the availability property of a SoftwareSourceAvailability.
    #: This constant has a value of "SELECTED"
    AVAILABILITY_SELECTED = "SELECTED"

    #: A constant which can be used with the availability property of a SoftwareSourceAvailability.
    #: This constant has a value of "RESTRICTED"
    AVAILABILITY_RESTRICTED = "RESTRICTED"

    #: A constant which can be used with the availability property of a SoftwareSourceAvailability.
    #: This constant has a value of "UNAVAILABLE"
    AVAILABILITY_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the availability_at_oci property of a SoftwareSourceAvailability.
    #: This constant has a value of "AVAILABLE"
    AVAILABILITY_AT_OCI_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the availability_at_oci property of a SoftwareSourceAvailability.
    #: This constant has a value of "SELECTED"
    AVAILABILITY_AT_OCI_SELECTED = "SELECTED"

    #: A constant which can be used with the availability_at_oci property of a SoftwareSourceAvailability.
    #: This constant has a value of "RESTRICTED"
    AVAILABILITY_AT_OCI_RESTRICTED = "RESTRICTED"

    #: A constant which can be used with the availability_at_oci property of a SoftwareSourceAvailability.
    #: This constant has a value of "UNAVAILABLE"
    AVAILABILITY_AT_OCI_UNAVAILABLE = "UNAVAILABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareSourceAvailability object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_source_id:
            The value to assign to the software_source_id property of this SoftwareSourceAvailability.
        :type software_source_id: str

        :param availability:
            The value to assign to the availability property of this SoftwareSourceAvailability.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"
        :type availability: str

        :param availability_at_oci:
            The value to assign to the availability_at_oci property of this SoftwareSourceAvailability.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"
        :type availability_at_oci: str

        """
        self.swagger_types = {
            'software_source_id': 'str',
            'availability': 'str',
            'availability_at_oci': 'str'
        }
        self.attribute_map = {
            'software_source_id': 'softwareSourceId',
            'availability': 'availability',
            'availability_at_oci': 'availabilityAtOci'
        }
        self._software_source_id = None
        self._availability = None
        self._availability_at_oci = None

    @property
    def software_source_id(self):
        """
        **[Required]** Gets the software_source_id of this SoftwareSourceAvailability.
        The `OCID`__ of the vendor software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The software_source_id of this SoftwareSourceAvailability.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this SoftwareSourceAvailability.
        The `OCID`__ of the vendor software source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param software_source_id: The software_source_id of this SoftwareSourceAvailability.
        :type: str
        """
        self._software_source_id = software_source_id

    @property
    def availability(self):
        """
        Gets the availability of this SoftwareSourceAvailability.
        Availability of the software source to instances in private data centers or third-party clouds.

        Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"


        :return: The availability of this SoftwareSourceAvailability.
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """
        Sets the availability of this SoftwareSourceAvailability.
        Availability of the software source to instances in private data centers or third-party clouds.


        :param availability: The availability of this SoftwareSourceAvailability.
        :type: str
        """
        allowed_values = ["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(availability, allowed_values):
            raise ValueError(
                f"Invalid value for `availability`, must be None or one of {allowed_values}"
            )
        self._availability = availability

    @property
    def availability_at_oci(self):
        """
        Gets the availability_at_oci of this SoftwareSourceAvailability.
        Availability of the software source to OCI instances.

        Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"


        :return: The availability_at_oci of this SoftwareSourceAvailability.
        :rtype: str
        """
        return self._availability_at_oci

    @availability_at_oci.setter
    def availability_at_oci(self, availability_at_oci):
        """
        Sets the availability_at_oci of this SoftwareSourceAvailability.
        Availability of the software source to OCI instances.


        :param availability_at_oci: The availability_at_oci of this SoftwareSourceAvailability.
        :type: str
        """
        allowed_values = ["AVAILABLE", "SELECTED", "RESTRICTED", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(availability_at_oci, allowed_values):
            raise ValueError(
                f"Invalid value for `availability_at_oci`, must be None or one of {allowed_values}"
            )
        self._availability_at_oci = availability_at_oci

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
