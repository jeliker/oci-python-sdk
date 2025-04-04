# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateEndpoint(object):
    """
    A private endpoint makes your service accessible through a private IP in the customer's private network. A private endpoint has a name and is associated with a namespace and a single compartment.
    """

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this PrivateEndpoint.
        :type name: str

        :param namespace:
            The value to assign to the namespace property of this PrivateEndpoint.
        :type namespace: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PrivateEndpoint.
        :type compartment_id: str

        :param created_by:
            The value to assign to the created_by property of this PrivateEndpoint.
        :type created_by: str

        :param time_created:
            The value to assign to the time_created property of this PrivateEndpoint.
        :type time_created: datetime

        :param time_modified:
            The value to assign to the time_modified property of this PrivateEndpoint.
        :type time_modified: datetime

        :param subnet_id:
            The value to assign to the subnet_id property of this PrivateEndpoint.
        :type subnet_id: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this PrivateEndpoint.
        :type private_endpoint_ip: str

        :param prefix:
            The value to assign to the prefix property of this PrivateEndpoint.
        :type prefix: str

        :param additional_prefixes:
            The value to assign to the additional_prefixes property of this PrivateEndpoint.
        :type additional_prefixes: list[str]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this PrivateEndpoint.
        :type nsg_ids: list[str]

        :param fqdns:
            The value to assign to the fqdns property of this PrivateEndpoint.
        :type fqdns: oci.object_storage.models.Fqdns

        :param etag:
            The value to assign to the etag property of this PrivateEndpoint.
        :type etag: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PrivateEndpoint.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param access_targets:
            The value to assign to the access_targets property of this PrivateEndpoint.
        :type access_targets: list[oci.object_storage.models.AccessTargetDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param id:
            The value to assign to the id property of this PrivateEndpoint.
        :type id: str

        """
        self.swagger_types = {
            'name': 'str',
            'namespace': 'str',
            'compartment_id': 'str',
            'created_by': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'subnet_id': 'str',
            'private_endpoint_ip': 'str',
            'prefix': 'str',
            'additional_prefixes': 'list[str]',
            'nsg_ids': 'list[str]',
            'fqdns': 'Fqdns',
            'etag': 'str',
            'lifecycle_state': 'str',
            'access_targets': 'list[AccessTargetDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'id': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'namespace': 'namespace',
            'compartment_id': 'compartmentId',
            'created_by': 'createdBy',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'subnet_id': 'subnetId',
            'private_endpoint_ip': 'privateEndpointIp',
            'prefix': 'prefix',
            'additional_prefixes': 'additionalPrefixes',
            'nsg_ids': 'nsgIds',
            'fqdns': 'fqdns',
            'etag': 'etag',
            'lifecycle_state': 'lifecycleState',
            'access_targets': 'accessTargets',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'id': 'id'
        }
        self._name = None
        self._namespace = None
        self._compartment_id = None
        self._created_by = None
        self._time_created = None
        self._time_modified = None
        self._subnet_id = None
        self._private_endpoint_ip = None
        self._prefix = None
        self._additional_prefixes = None
        self._nsg_ids = None
        self._fqdns = None
        self._etag = None
        self._lifecycle_state = None
        self._access_targets = None
        self._freeform_tags = None
        self._defined_tags = None
        self._id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PrivateEndpoint.
        This name associated with the endpoint. Valid characters are uppercase or lowercase letters, numbers, hyphens,
         underscores, and periods.
        Example: my-new-private-endpoint1


        :return: The name of this PrivateEndpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PrivateEndpoint.
        This name associated with the endpoint. Valid characters are uppercase or lowercase letters, numbers, hyphens,
         underscores, and periods.
        Example: my-new-private-endpoint1


        :param name: The name of this PrivateEndpoint.
        :type: str
        """
        self._name = name

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this PrivateEndpoint.
        The Object Storage namespace associated with the private enpoint.


        :return: The namespace of this PrivateEndpoint.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this PrivateEndpoint.
        The Object Storage namespace associated with the private enpoint.


        :param namespace: The namespace of this PrivateEndpoint.
        :type: str
        """
        self._namespace = namespace

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PrivateEndpoint.
        The compartment which is associated with the Private Endpoint.


        :return: The compartment_id of this PrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PrivateEndpoint.
        The compartment which is associated with the Private Endpoint.


        :param compartment_id: The compartment_id of this PrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this PrivateEndpoint.
        The `OCID`__ of the user who created the Private Endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The created_by of this PrivateEndpoint.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this PrivateEndpoint.
        The `OCID`__ of the user who created the Private Endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this PrivateEndpoint.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PrivateEndpoint.
        The date and time the Private Endpoint was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :return: The time_created of this PrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PrivateEndpoint.
        The date and time the Private Endpoint was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :param time_created: The time_created of this PrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        **[Required]** Gets the time_modified of this PrivateEndpoint.
        The date and time the Private Endpoint was updated, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :return: The time_modified of this PrivateEndpoint.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this PrivateEndpoint.
        The date and time the Private Endpoint was updated, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :param time_modified: The time_modified of this PrivateEndpoint.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this PrivateEndpoint.
        The OCID of the customer's subnet where the private endpoint VNIC will reside.


        :return: The subnet_id of this PrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PrivateEndpoint.
        The OCID of the customer's subnet where the private endpoint VNIC will reside.


        :param subnet_id: The subnet_id of this PrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_ip(self):
        """
        **[Required]** Gets the private_endpoint_ip of this PrivateEndpoint.
        The private IP address to assign to this private endpoint. If you provide a value,
        it must be an available IP address in the customer's subnet. If it's not available, an error
        is returned.

        If you do not provide a value, an available IP address in the subnet is automatically chosen.


        :return: The private_endpoint_ip of this PrivateEndpoint.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this PrivateEndpoint.
        The private IP address to assign to this private endpoint. If you provide a value,
        it must be an available IP address in the customer's subnet. If it's not available, an error
        is returned.

        If you do not provide a value, an available IP address in the subnet is automatically chosen.


        :param private_endpoint_ip: The private_endpoint_ip of this PrivateEndpoint.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def prefix(self):
        """
        **[Required]** Gets the prefix of this PrivateEndpoint.
        A prefix to use for the private endpoint. The customer VCN's DNS records are
        updated with this prefix. The prefix input from the customer will be the first sub-domain in the endpointFqdn.
        Example: If the prefix chosen is \"abc\", then the endpointFqdn will be 'abc.private.objectstorage.<region>.oraclecloud.com'


        :return: The prefix of this PrivateEndpoint.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this PrivateEndpoint.
        A prefix to use for the private endpoint. The customer VCN's DNS records are
        updated with this prefix. The prefix input from the customer will be the first sub-domain in the endpointFqdn.
        Example: If the prefix chosen is \"abc\", then the endpointFqdn will be 'abc.private.objectstorage.<region>.oraclecloud.com'


        :param prefix: The prefix of this PrivateEndpoint.
        :type: str
        """
        self._prefix = prefix

    @property
    def additional_prefixes(self):
        """
        Gets the additional_prefixes of this PrivateEndpoint.
        A list of additional prefix that you can provide along with any other prefix. These resulting endpointFqdn's are added to the
        customer VCN's DNS record.


        :return: The additional_prefixes of this PrivateEndpoint.
        :rtype: list[str]
        """
        return self._additional_prefixes

    @additional_prefixes.setter
    def additional_prefixes(self, additional_prefixes):
        """
        Sets the additional_prefixes of this PrivateEndpoint.
        A list of additional prefix that you can provide along with any other prefix. These resulting endpointFqdn's are added to the
        customer VCN's DNS record.


        :param additional_prefixes: The additional_prefixes of this PrivateEndpoint.
        :type: list[str]
        """
        self._additional_prefixes = additional_prefixes

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this PrivateEndpoint.
        A list of the OCIDs of the network security groups (NSGs) to add the private endpoint's VNIC to.
        For more information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this PrivateEndpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this PrivateEndpoint.
        A list of the OCIDs of the network security groups (NSGs) to add the private endpoint's VNIC to.
        For more information about NSGs, see
        :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this PrivateEndpoint.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def fqdns(self):
        """
        **[Required]** Gets the fqdns of this PrivateEndpoint.

        :return: The fqdns of this PrivateEndpoint.
        :rtype: oci.object_storage.models.Fqdns
        """
        return self._fqdns

    @fqdns.setter
    def fqdns(self, fqdns):
        """
        Sets the fqdns of this PrivateEndpoint.

        :param fqdns: The fqdns of this PrivateEndpoint.
        :type: oci.object_storage.models.Fqdns
        """
        self._fqdns = fqdns

    @property
    def etag(self):
        """
        **[Required]** Gets the etag of this PrivateEndpoint.
        The entity tag (ETag) for the Private Endpoint.


        :return: The etag of this PrivateEndpoint.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this PrivateEndpoint.
        The entity tag (ETag) for the Private Endpoint.


        :param etag: The etag of this PrivateEndpoint.
        :type: str
        """
        self._etag = etag

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this PrivateEndpoint.
        The Private Endpoint's lifecycle state.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PrivateEndpoint.
        The Private Endpoint's lifecycle state.


        :param lifecycle_state: The lifecycle_state of this PrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def access_targets(self):
        """
        **[Required]** Gets the access_targets of this PrivateEndpoint.
        A list of targets that can be accessed by the private endpoint. At least one or more access targets is required for a private endpoint.


        :return: The access_targets of this PrivateEndpoint.
        :rtype: list[oci.object_storage.models.AccessTargetDetails]
        """
        return self._access_targets

    @access_targets.setter
    def access_targets(self, access_targets):
        """
        Sets the access_targets of this PrivateEndpoint.
        A list of targets that can be accessed by the private endpoint. At least one or more access targets is required for a private endpoint.


        :param access_targets: The access_targets of this PrivateEndpoint.
        :type: list[oci.object_storage.models.AccessTargetDetails]
        """
        self._access_targets = access_targets

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PrivateEndpoint.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this PrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PrivateEndpoint.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this PrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this PrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this PrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def id(self):
        """
        Gets the id of this PrivateEndpoint.
        The `OCID`__ of the PrivateEndpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this PrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrivateEndpoint.
        The `OCID`__ of the PrivateEndpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this PrivateEndpoint.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
