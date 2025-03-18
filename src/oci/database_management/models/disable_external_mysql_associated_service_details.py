# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisableExternalMysqlAssociatedServiceDetails(object):
    """
    Details to disable an eMysql Associated Service.
    """

    #: A constant which can be used with the service_name property of a DisableExternalMysqlAssociatedServiceDetails.
    #: This constant has a value of "OPERATIONS_INSIGHTS"
    SERVICE_NAME_OPERATIONS_INSIGHTS = "OPERATIONS_INSIGHTS"

    def __init__(self, **kwargs):
        """
        Initializes a new DisableExternalMysqlAssociatedServiceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_resource_id:
            The value to assign to the service_resource_id property of this DisableExternalMysqlAssociatedServiceDetails.
        :type service_resource_id: str

        :param connector_id:
            The value to assign to the connector_id property of this DisableExternalMysqlAssociatedServiceDetails.
        :type connector_id: str

        :param service_name:
            The value to assign to the service_name property of this DisableExternalMysqlAssociatedServiceDetails.
            Allowed values for this property are: "OPERATIONS_INSIGHTS"
        :type service_name: str

        """
        self.swagger_types = {
            'service_resource_id': 'str',
            'connector_id': 'str',
            'service_name': 'str'
        }
        self.attribute_map = {
            'service_resource_id': 'serviceResourceId',
            'connector_id': 'connectorId',
            'service_name': 'serviceName'
        }
        self._service_resource_id = None
        self._connector_id = None
        self._service_name = None

    @property
    def service_resource_id(self):
        """
        **[Required]** Gets the service_resource_id of this DisableExternalMysqlAssociatedServiceDetails.
        OCID of the Service Resource.


        :return: The service_resource_id of this DisableExternalMysqlAssociatedServiceDetails.
        :rtype: str
        """
        return self._service_resource_id

    @service_resource_id.setter
    def service_resource_id(self, service_resource_id):
        """
        Sets the service_resource_id of this DisableExternalMysqlAssociatedServiceDetails.
        OCID of the Service Resource.


        :param service_resource_id: The service_resource_id of this DisableExternalMysqlAssociatedServiceDetails.
        :type: str
        """
        self._service_resource_id = service_resource_id

    @property
    def connector_id(self):
        """
        **[Required]** Gets the connector_id of this DisableExternalMysqlAssociatedServiceDetails.
        OCID of the External MySQL Database connector.


        :return: The connector_id of this DisableExternalMysqlAssociatedServiceDetails.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this DisableExternalMysqlAssociatedServiceDetails.
        OCID of the External MySQL Database connector.


        :param connector_id: The connector_id of this DisableExternalMysqlAssociatedServiceDetails.
        :type: str
        """
        self._connector_id = connector_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this DisableExternalMysqlAssociatedServiceDetails.
        Name of the Associated Service.

        Allowed values for this property are: "OPERATIONS_INSIGHTS"


        :return: The service_name of this DisableExternalMysqlAssociatedServiceDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this DisableExternalMysqlAssociatedServiceDetails.
        Name of the Associated Service.


        :param service_name: The service_name of this DisableExternalMysqlAssociatedServiceDetails.
        :type: str
        """
        allowed_values = ["OPERATIONS_INSIGHTS"]
        if not value_allowed_none_or_none_sentinel(service_name, allowed_values):
            raise ValueError(
                f"Invalid value for `service_name`, must be None or one of {allowed_values}"
            )
        self._service_name = service_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
