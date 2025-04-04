# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CrossRegionIntegrationInstanceDetails(object):
    """
    Details of integration instance created in cross region for disaster recovery.
    """

    #: A constant which can be used with the role property of a CrossRegionIntegrationInstanceDetails.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a CrossRegionIntegrationInstanceDetails.
    #: This constant has a value of "SECONDARY"
    ROLE_SECONDARY = "SECONDARY"

    #: A constant which can be used with the role property of a CrossRegionIntegrationInstanceDetails.
    #: This constant has a value of "UNKNOWN"
    ROLE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new CrossRegionIntegrationInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this CrossRegionIntegrationInstanceDetails.
            Allowed values for this property are: "PRIMARY", "SECONDARY", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param id:
            The value to assign to the id property of this CrossRegionIntegrationInstanceDetails.
        :type id: str

        :param region:
            The value to assign to the region property of this CrossRegionIntegrationInstanceDetails.
        :type region: str

        :param time_role_changed:
            The value to assign to the time_role_changed property of this CrossRegionIntegrationInstanceDetails.
        :type time_role_changed: datetime

        """
        self.swagger_types = {
            'role': 'str',
            'id': 'str',
            'region': 'str',
            'time_role_changed': 'datetime'
        }
        self.attribute_map = {
            'role': 'role',
            'id': 'id',
            'region': 'region',
            'time_role_changed': 'timeRoleChanged'
        }
        self._role = None
        self._id = None
        self._region = None
        self._time_role_changed = None

    @property
    def role(self):
        """
        Gets the role of this CrossRegionIntegrationInstanceDetails.
        Role of the integration instance in the region

        Allowed values for this property are: "PRIMARY", "SECONDARY", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this CrossRegionIntegrationInstanceDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this CrossRegionIntegrationInstanceDetails.
        Role of the integration instance in the region


        :param role: The role of this CrossRegionIntegrationInstanceDetails.
        :type: str
        """
        allowed_values = ["PRIMARY", "SECONDARY", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def id(self):
        """
        Gets the id of this CrossRegionIntegrationInstanceDetails.
        Cross region integration instance identifier


        :return: The id of this CrossRegionIntegrationInstanceDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CrossRegionIntegrationInstanceDetails.
        Cross region integration instance identifier


        :param id: The id of this CrossRegionIntegrationInstanceDetails.
        :type: str
        """
        self._id = id

    @property
    def region(self):
        """
        Gets the region of this CrossRegionIntegrationInstanceDetails.
        Cross region where integration instance is created


        :return: The region of this CrossRegionIntegrationInstanceDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CrossRegionIntegrationInstanceDetails.
        Cross region where integration instance is created


        :param region: The region of this CrossRegionIntegrationInstanceDetails.
        :type: str
        """
        self._region = region

    @property
    def time_role_changed(self):
        """
        Gets the time_role_changed of this CrossRegionIntegrationInstanceDetails.
        Time when cross region integration instance role was changed


        :return: The time_role_changed of this CrossRegionIntegrationInstanceDetails.
        :rtype: datetime
        """
        return self._time_role_changed

    @time_role_changed.setter
    def time_role_changed(self, time_role_changed):
        """
        Sets the time_role_changed of this CrossRegionIntegrationInstanceDetails.
        Time when cross region integration instance role was changed


        :param time_role_changed: The time_role_changed of this CrossRegionIntegrationInstanceDetails.
        :type: datetime
        """
        self._time_role_changed = time_role_changed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
