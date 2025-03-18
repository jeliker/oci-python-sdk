# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetErrorSummary(object):
    """
    The summary of a fleet error.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FleetErrorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fleet_id:
            The value to assign to the fleet_id property of this FleetErrorSummary.
        :type fleet_id: str

        :param fleet_name:
            The value to assign to the fleet_name property of this FleetErrorSummary.
        :type fleet_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FleetErrorSummary.
        :type compartment_id: str

        :param errors:
            The value to assign to the errors property of this FleetErrorSummary.
        :type errors: list[oci.jms.models.FleetErrorDetails]

        :param time_first_seen:
            The value to assign to the time_first_seen property of this FleetErrorSummary.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this FleetErrorSummary.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'fleet_id': 'str',
            'fleet_name': 'str',
            'compartment_id': 'str',
            'errors': 'list[FleetErrorDetails]',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }
        self.attribute_map = {
            'fleet_id': 'fleetId',
            'fleet_name': 'fleetName',
            'compartment_id': 'compartmentId',
            'errors': 'errors',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }
        self._fleet_id = None
        self._fleet_name = None
        self._compartment_id = None
        self._errors = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this FleetErrorSummary.
        The `OCID`__ of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this FleetErrorSummary.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this FleetErrorSummary.
        The `OCID`__ of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this FleetErrorSummary.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def fleet_name(self):
        """
        **[Required]** Gets the fleet_name of this FleetErrorSummary.
        The display name of the Fleet.


        :return: The fleet_name of this FleetErrorSummary.
        :rtype: str
        """
        return self._fleet_name

    @fleet_name.setter
    def fleet_name(self, fleet_name):
        """
        Sets the fleet_name of this FleetErrorSummary.
        The display name of the Fleet.


        :param fleet_name: The fleet_name of this FleetErrorSummary.
        :type: str
        """
        self._fleet_name = fleet_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FleetErrorSummary.
        The compartment `OCID`__ of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this FleetErrorSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FleetErrorSummary.
        The compartment `OCID`__ of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this FleetErrorSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def errors(self):
        """
        **[Required]** Gets the errors of this FleetErrorSummary.
        List of fleet error details.


        :return: The errors of this FleetErrorSummary.
        :rtype: list[oci.jms.models.FleetErrorDetails]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this FleetErrorSummary.
        List of fleet error details.


        :param errors: The errors of this FleetErrorSummary.
        :type: list[oci.jms.models.FleetErrorDetails]
        """
        self._errors = errors

    @property
    def time_first_seen(self):
        """
        **[Required]** Gets the time_first_seen of this FleetErrorSummary.
        The timestamp of the first time an error was detected.


        :return: The time_first_seen of this FleetErrorSummary.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this FleetErrorSummary.
        The timestamp of the first time an error was detected.


        :param time_first_seen: The time_first_seen of this FleetErrorSummary.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        **[Required]** Gets the time_last_seen of this FleetErrorSummary.
        The timestamp of the last time an error was detected.


        :return: The time_last_seen of this FleetErrorSummary.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this FleetErrorSummary.
        The timestamp of the last time an error was detected.


        :param time_last_seen: The time_last_seen of this FleetErrorSummary.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
