# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .dbm_resource import DbmResource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalExadataInfrastructure(DbmResource):
    """
    The details of the Exadata infrastructure.
    """

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructure.
    #: This constant has a value of "FULL"
    RACK_SIZE_FULL = "FULL"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructure.
    #: This constant has a value of "HALF"
    RACK_SIZE_HALF = "HALF"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructure.
    #: This constant has a value of "QUARTER"
    RACK_SIZE_QUARTER = "QUARTER"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructure.
    #: This constant has a value of "EIGHTH"
    RACK_SIZE_EIGHTH = "EIGHTH"

    #: A constant which can be used with the license_model property of a ExternalExadataInfrastructure.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a ExternalExadataInfrastructure.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalExadataInfrastructure object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalExadataInfrastructure.resource_type` attribute
        of this class is ``INFRASTRUCTURE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalExadataInfrastructure.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalExadataInfrastructure.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalExadataInfrastructure.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalExadataInfrastructure.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalExadataInfrastructure.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalExadataInfrastructure.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ExternalExadataInfrastructure.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalExadataInfrastructure.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalExadataInfrastructure.
        :type lifecycle_details: str

        :param additional_details:
            The value to assign to the additional_details property of this ExternalExadataInfrastructure.
        :type additional_details: dict(str, str)

        :param resource_type:
            The value to assign to the resource_type property of this ExternalExadataInfrastructure.
            Allowed values for this property are: "INFRASTRUCTURE_SUMMARY", "INFRASTRUCTURE", "STORAGE_SERVER_SUMMARY", "STORAGE_SERVER", "STORAGE_GRID_SUMMARY", "STORAGE_GRID", "STORAGE_CONNECTOR_SUMMARY", "STORAGE_CONNECTOR", "DATABASE_SYSTEM_SUMMARY", "DATABASE_SUMMARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param rack_size:
            The value to assign to the rack_size property of this ExternalExadataInfrastructure.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rack_size: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalExadataInfrastructure.
        :type compartment_id: str

        :param license_model:
            The value to assign to the license_model property of this ExternalExadataInfrastructure.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param storage_grid:
            The value to assign to the storage_grid property of this ExternalExadataInfrastructure.
        :type storage_grid: oci.database_management.models.ExternalExadataStorageGridSummary

        :param database_systems:
            The value to assign to the database_systems property of this ExternalExadataInfrastructure.
        :type database_systems: list[oci.database_management.models.ExternalExadataDatabaseSystemSummary]

        :param database_compartments:
            The value to assign to the database_compartments property of this ExternalExadataInfrastructure.
        :type database_compartments: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExternalExadataInfrastructure.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExternalExadataInfrastructure.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ExternalExadataInfrastructure.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'additional_details': 'dict(str, str)',
            'resource_type': 'str',
            'rack_size': 'str',
            'compartment_id': 'str',
            'license_model': 'str',
            'storage_grid': 'ExternalExadataStorageGridSummary',
            'database_systems': 'list[ExternalExadataDatabaseSystemSummary]',
            'database_compartments': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'additional_details': 'additionalDetails',
            'resource_type': 'resourceType',
            'rack_size': 'rackSize',
            'compartment_id': 'compartmentId',
            'license_model': 'licenseModel',
            'storage_grid': 'storageGrid',
            'database_systems': 'databaseSystems',
            'database_compartments': 'databaseCompartments',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_details = None
        self._additional_details = None
        self._resource_type = None
        self._rack_size = None
        self._compartment_id = None
        self._license_model = None
        self._storage_grid = None
        self._database_systems = None
        self._database_compartments = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._resource_type = 'INFRASTRUCTURE'

    @property
    def rack_size(self):
        """
        Gets the rack_size of this ExternalExadataInfrastructure.
        The rack size of the Exadata infrastructure.

        Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rack_size of this ExternalExadataInfrastructure.
        :rtype: str
        """
        return self._rack_size

    @rack_size.setter
    def rack_size(self, rack_size):
        """
        Sets the rack_size of this ExternalExadataInfrastructure.
        The rack size of the Exadata infrastructure.


        :param rack_size: The rack_size of this ExternalExadataInfrastructure.
        :type: str
        """
        allowed_values = ["FULL", "HALF", "QUARTER", "EIGHTH"]
        if not value_allowed_none_or_none_sentinel(rack_size, allowed_values):
            rack_size = 'UNKNOWN_ENUM_VALUE'
        self._rack_size = rack_size

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ExternalExadataInfrastructure.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalExadataInfrastructure.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalExadataInfrastructure.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalExadataInfrastructure.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def license_model(self):
        """
        Gets the license_model of this ExternalExadataInfrastructure.
        The Oracle license model that applies to the database management resources.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this ExternalExadataInfrastructure.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this ExternalExadataInfrastructure.
        The Oracle license model that applies to the database management resources.


        :param license_model: The license_model of this ExternalExadataInfrastructure.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def storage_grid(self):
        """
        Gets the storage_grid of this ExternalExadataInfrastructure.

        :return: The storage_grid of this ExternalExadataInfrastructure.
        :rtype: oci.database_management.models.ExternalExadataStorageGridSummary
        """
        return self._storage_grid

    @storage_grid.setter
    def storage_grid(self, storage_grid):
        """
        Sets the storage_grid of this ExternalExadataInfrastructure.

        :param storage_grid: The storage_grid of this ExternalExadataInfrastructure.
        :type: oci.database_management.models.ExternalExadataStorageGridSummary
        """
        self._storage_grid = storage_grid

    @property
    def database_systems(self):
        """
        Gets the database_systems of this ExternalExadataInfrastructure.
        A list of DB systems.


        :return: The database_systems of this ExternalExadataInfrastructure.
        :rtype: list[oci.database_management.models.ExternalExadataDatabaseSystemSummary]
        """
        return self._database_systems

    @database_systems.setter
    def database_systems(self, database_systems):
        """
        Sets the database_systems of this ExternalExadataInfrastructure.
        A list of DB systems.


        :param database_systems: The database_systems of this ExternalExadataInfrastructure.
        :type: list[oci.database_management.models.ExternalExadataDatabaseSystemSummary]
        """
        self._database_systems = database_systems

    @property
    def database_compartments(self):
        """
        Gets the database_compartments of this ExternalExadataInfrastructure.
        The list of `OCIDs]`__ of the compartments.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_compartments of this ExternalExadataInfrastructure.
        :rtype: list[str]
        """
        return self._database_compartments

    @database_compartments.setter
    def database_compartments(self, database_compartments):
        """
        Sets the database_compartments of this ExternalExadataInfrastructure.
        The list of `OCIDs]`__ of the compartments.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_compartments: The database_compartments of this ExternalExadataInfrastructure.
        :type: list[str]
        """
        self._database_compartments = database_compartments

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExternalExadataInfrastructure.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExternalExadataInfrastructure.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExternalExadataInfrastructure.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExternalExadataInfrastructure.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExternalExadataInfrastructure.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExternalExadataInfrastructure.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExternalExadataInfrastructure.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExternalExadataInfrastructure.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ExternalExadataInfrastructure.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ExternalExadataInfrastructure.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ExternalExadataInfrastructure.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ExternalExadataInfrastructure.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
