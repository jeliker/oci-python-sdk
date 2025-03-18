# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccAvailabilityCatalog(object):
    """
    Details of the availability catalog resource.
    """

    #: A constant which can be used with the namespace property of a OccAvailabilityCatalog.
    #: This constant has a value of "COMPUTE"
    NAMESPACE_COMPUTE = "COMPUTE"

    #: A constant which can be used with the catalog_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "NOT_UPLOADED"
    CATALOG_STATE_NOT_UPLOADED = "NOT_UPLOADED"

    #: A constant which can be used with the catalog_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "UPLOAD_FAILED"
    CATALOG_STATE_UPLOAD_FAILED = "UPLOAD_FAILED"

    #: A constant which can be used with the catalog_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "STAGED"
    CATALOG_STATE_STAGED = "STAGED"

    #: A constant which can be used with the catalog_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "PUBLISHED"
    CATALOG_STATE_PUBLISHED = "PUBLISHED"

    #: A constant which can be used with the catalog_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "OUTDATED"
    CATALOG_STATE_OUTDATED = "OUTDATED"

    #: A constant which can be used with the catalog_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "DELETED"
    CATALOG_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OccAvailabilityCatalog.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OccAvailabilityCatalog object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OccAvailabilityCatalog.
        :type id: str

        :param namespace:
            The value to assign to the namespace property of this OccAvailabilityCatalog.
            Allowed values for this property are: "COMPUTE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type namespace: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OccAvailabilityCatalog.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this OccAvailabilityCatalog.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OccAvailabilityCatalog.
        :type description: str

        :param occ_customer_group_id:
            The value to assign to the occ_customer_group_id property of this OccAvailabilityCatalog.
        :type occ_customer_group_id: str

        :param catalog_state:
            The value to assign to the catalog_state property of this OccAvailabilityCatalog.
            Allowed values for this property are: "NOT_UPLOADED", "UPLOAD_FAILED", "STAGED", "PUBLISHED", "OUTDATED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type catalog_state: str

        :param metadata_details:
            The value to assign to the metadata_details property of this OccAvailabilityCatalog.
        :type metadata_details: oci.capacity_management.models.MetadataDetails

        :param time_created:
            The value to assign to the time_created property of this OccAvailabilityCatalog.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OccAvailabilityCatalog.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OccAvailabilityCatalog.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OccAvailabilityCatalog.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OccAvailabilityCatalog.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OccAvailabilityCatalog.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OccAvailabilityCatalog.
        :type system_tags: dict(str, dict(str, object))

        :param details:
            The value to assign to the details property of this OccAvailabilityCatalog.
        :type details: list[oci.capacity_management.models.OccAvailabilitySummary]

        """
        self.swagger_types = {
            'id': 'str',
            'namespace': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'occ_customer_group_id': 'str',
            'catalog_state': 'str',
            'metadata_details': 'MetadataDetails',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'details': 'list[OccAvailabilitySummary]'
        }
        self.attribute_map = {
            'id': 'id',
            'namespace': 'namespace',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'occ_customer_group_id': 'occCustomerGroupId',
            'catalog_state': 'catalogState',
            'metadata_details': 'metadataDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'details': 'details'
        }
        self._id = None
        self._namespace = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._occ_customer_group_id = None
        self._catalog_state = None
        self._metadata_details = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OccAvailabilityCatalog.
        The OCID of the availability catalog.


        :return: The id of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OccAvailabilityCatalog.
        The OCID of the availability catalog.


        :param id: The id of this OccAvailabilityCatalog.
        :type: str
        """
        self._id = id

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this OccAvailabilityCatalog.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.

        Allowed values for this property are: "COMPUTE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The namespace of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OccAvailabilityCatalog.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.


        :param namespace: The namespace of this OccAvailabilityCatalog.
        :type: str
        """
        allowed_values = ["COMPUTE"]
        if not value_allowed_none_or_none_sentinel(namespace, allowed_values):
            namespace = 'UNKNOWN_ENUM_VALUE'
        self._namespace = namespace

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OccAvailabilityCatalog.
        The OCID of the tenancy where the availability catalog resides.


        :return: The compartment_id of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OccAvailabilityCatalog.
        The OCID of the tenancy where the availability catalog resides.


        :param compartment_id: The compartment_id of this OccAvailabilityCatalog.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OccAvailabilityCatalog.
        A user-friendly name for the availability catalog.


        :return: The display_name of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OccAvailabilityCatalog.
        A user-friendly name for the availability catalog.


        :param display_name: The display_name of this OccAvailabilityCatalog.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OccAvailabilityCatalog.
        Text information about the availability catalog.


        :return: The description of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OccAvailabilityCatalog.
        Text information about the availability catalog.


        :param description: The description of this OccAvailabilityCatalog.
        :type: str
        """
        self._description = description

    @property
    def occ_customer_group_id(self):
        """
        **[Required]** Gets the occ_customer_group_id of this OccAvailabilityCatalog.
        The customer group OCID to which the availability catalog belongs.


        :return: The occ_customer_group_id of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._occ_customer_group_id

    @occ_customer_group_id.setter
    def occ_customer_group_id(self, occ_customer_group_id):
        """
        Sets the occ_customer_group_id of this OccAvailabilityCatalog.
        The customer group OCID to which the availability catalog belongs.


        :param occ_customer_group_id: The occ_customer_group_id of this OccAvailabilityCatalog.
        :type: str
        """
        self._occ_customer_group_id = occ_customer_group_id

    @property
    def catalog_state(self):
        """
        **[Required]** Gets the catalog_state of this OccAvailabilityCatalog.
        The different states associated with the availability catalog.

        Allowed values for this property are: "NOT_UPLOADED", "UPLOAD_FAILED", "STAGED", "PUBLISHED", "OUTDATED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The catalog_state of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._catalog_state

    @catalog_state.setter
    def catalog_state(self, catalog_state):
        """
        Sets the catalog_state of this OccAvailabilityCatalog.
        The different states associated with the availability catalog.


        :param catalog_state: The catalog_state of this OccAvailabilityCatalog.
        :type: str
        """
        allowed_values = ["NOT_UPLOADED", "UPLOAD_FAILED", "STAGED", "PUBLISHED", "OUTDATED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(catalog_state, allowed_values):
            catalog_state = 'UNKNOWN_ENUM_VALUE'
        self._catalog_state = catalog_state

    @property
    def metadata_details(self):
        """
        **[Required]** Gets the metadata_details of this OccAvailabilityCatalog.

        :return: The metadata_details of this OccAvailabilityCatalog.
        :rtype: oci.capacity_management.models.MetadataDetails
        """
        return self._metadata_details

    @metadata_details.setter
    def metadata_details(self, metadata_details):
        """
        Sets the metadata_details of this OccAvailabilityCatalog.

        :param metadata_details: The metadata_details of this OccAvailabilityCatalog.
        :type: oci.capacity_management.models.MetadataDetails
        """
        self._metadata_details = metadata_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OccAvailabilityCatalog.
        The time when the availability catalog was created.


        :return: The time_created of this OccAvailabilityCatalog.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OccAvailabilityCatalog.
        The time when the availability catalog was created.


        :param time_created: The time_created of this OccAvailabilityCatalog.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this OccAvailabilityCatalog.
        The time when the availability catalog was last updated.


        :return: The time_updated of this OccAvailabilityCatalog.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OccAvailabilityCatalog.
        The time when the availability catalog was last updated.


        :param time_updated: The time_updated of this OccAvailabilityCatalog.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OccAvailabilityCatalog.
        The current lifecycle state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OccAvailabilityCatalog.
        The current lifecycle state of the resource.


        :param lifecycle_state: The lifecycle_state of this OccAvailabilityCatalog.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OccAvailabilityCatalog.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :return: The lifecycle_details of this OccAvailabilityCatalog.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OccAvailabilityCatalog.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed State.


        :param lifecycle_details: The lifecycle_details of this OccAvailabilityCatalog.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OccAvailabilityCatalog.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OccAvailabilityCatalog.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OccAvailabilityCatalog.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OccAvailabilityCatalog.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OccAvailabilityCatalog.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OccAvailabilityCatalog.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OccAvailabilityCatalog.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OccAvailabilityCatalog.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OccAvailabilityCatalog.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OccAvailabilityCatalog.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OccAvailabilityCatalog.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OccAvailabilityCatalog.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def details(self):
        """
        Gets the details of this OccAvailabilityCatalog.
        Details about capacity available for different resources in catalog.


        :return: The details of this OccAvailabilityCatalog.
        :rtype: list[oci.capacity_management.models.OccAvailabilitySummary]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this OccAvailabilityCatalog.
        Details about capacity available for different resources in catalog.


        :param details: The details of this OccAvailabilityCatalog.
        :type: list[oci.capacity_management.models.OccAvailabilitySummary]
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
