# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Configuration(object):
    """
    Specifies several key settings for a Cloud Guard tenancy, identified by tenancy root compartment OCID.
    """

    #: A constant which can be used with the status property of a Configuration.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a Configuration.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new Configuration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reporting_region:
            The value to assign to the reporting_region property of this Configuration.
        :type reporting_region: str

        :param status:
            The value to assign to the status property of this Configuration.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param service_configurations:
            The value to assign to the service_configurations property of this Configuration.
        :type service_configurations: list[oci.cloud_guard.models.ServiceConfiguration]

        :param self_manage_resources:
            The value to assign to the self_manage_resources property of this Configuration.
        :type self_manage_resources: bool

        """
        self.swagger_types = {
            'reporting_region': 'str',
            'status': 'str',
            'service_configurations': 'list[ServiceConfiguration]',
            'self_manage_resources': 'bool'
        }
        self.attribute_map = {
            'reporting_region': 'reportingRegion',
            'status': 'status',
            'service_configurations': 'serviceConfigurations',
            'self_manage_resources': 'selfManageResources'
        }
        self._reporting_region = None
        self._status = None
        self._service_configurations = None
        self._self_manage_resources = None

    @property
    def reporting_region(self):
        """
        **[Required]** Gets the reporting_region of this Configuration.
        The reporting region


        :return: The reporting_region of this Configuration.
        :rtype: str
        """
        return self._reporting_region

    @reporting_region.setter
    def reporting_region(self, reporting_region):
        """
        Sets the reporting_region of this Configuration.
        The reporting region


        :param reporting_region: The reporting_region of this Configuration.
        :type: str
        """
        self._reporting_region = reporting_region

    @property
    def status(self):
        """
        Gets the status of this Configuration.
        Status of the Cloud Guard tenant

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this Configuration.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Configuration.
        Status of the Cloud Guard tenant


        :param status: The status of this Configuration.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def service_configurations(self):
        """
        Gets the service_configurations of this Configuration.
        List of service configurations for this tenant


        :return: The service_configurations of this Configuration.
        :rtype: list[oci.cloud_guard.models.ServiceConfiguration]
        """
        return self._service_configurations

    @service_configurations.setter
    def service_configurations(self, service_configurations):
        """
        Sets the service_configurations of this Configuration.
        List of service configurations for this tenant


        :param service_configurations: The service_configurations of this Configuration.
        :type: list[oci.cloud_guard.models.ServiceConfiguration]
        """
        self._service_configurations = service_configurations

    @property
    def self_manage_resources(self):
        """
        Gets the self_manage_resources of this Configuration.
        Were Oracle-managed resources created by customer?


        :return: The self_manage_resources of this Configuration.
        :rtype: bool
        """
        return self._self_manage_resources

    @self_manage_resources.setter
    def self_manage_resources(self, self_manage_resources):
        """
        Sets the self_manage_resources of this Configuration.
        Were Oracle-managed resources created by customer?


        :param self_manage_resources: The self_manage_resources of this Configuration.
        :type: bool
        """
        self._self_manage_resources = self_manage_resources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
