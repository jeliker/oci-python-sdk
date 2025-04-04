# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudGateMapping(object):
    """
    Resource representing a Cloud Gate mapping
    """

    #: A constant which can be used with the idcs_prevented_operations property of a CloudGateMapping.
    #: This constant has a value of "replace"
    IDCS_PREVENTED_OPERATIONS_REPLACE = "replace"

    #: A constant which can be used with the idcs_prevented_operations property of a CloudGateMapping.
    #: This constant has a value of "update"
    IDCS_PREVENTED_OPERATIONS_UPDATE = "update"

    #: A constant which can be used with the idcs_prevented_operations property of a CloudGateMapping.
    #: This constant has a value of "delete"
    IDCS_PREVENTED_OPERATIONS_DELETE = "delete"

    def __init__(self, **kwargs):
        """
        Initializes a new CloudGateMapping object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CloudGateMapping.
        :type id: str

        :param ocid:
            The value to assign to the ocid property of this CloudGateMapping.
        :type ocid: str

        :param schemas:
            The value to assign to the schemas property of this CloudGateMapping.
        :type schemas: list[str]

        :param meta:
            The value to assign to the meta property of this CloudGateMapping.
        :type meta: oci.identity_domains.models.Meta

        :param idcs_created_by:
            The value to assign to the idcs_created_by property of this CloudGateMapping.
        :type idcs_created_by: oci.identity_domains.models.IdcsCreatedBy

        :param idcs_last_modified_by:
            The value to assign to the idcs_last_modified_by property of this CloudGateMapping.
        :type idcs_last_modified_by: oci.identity_domains.models.IdcsLastModifiedBy

        :param idcs_prevented_operations:
            The value to assign to the idcs_prevented_operations property of this CloudGateMapping.
            Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type idcs_prevented_operations: list[str]

        :param tags:
            The value to assign to the tags property of this CloudGateMapping.
        :type tags: list[oci.identity_domains.models.Tags]

        :param delete_in_progress:
            The value to assign to the delete_in_progress property of this CloudGateMapping.
        :type delete_in_progress: bool

        :param idcs_last_upgraded_in_release:
            The value to assign to the idcs_last_upgraded_in_release property of this CloudGateMapping.
        :type idcs_last_upgraded_in_release: str

        :param domain_ocid:
            The value to assign to the domain_ocid property of this CloudGateMapping.
        :type domain_ocid: str

        :param compartment_ocid:
            The value to assign to the compartment_ocid property of this CloudGateMapping.
        :type compartment_ocid: str

        :param tenancy_ocid:
            The value to assign to the tenancy_ocid property of this CloudGateMapping.
        :type tenancy_ocid: str

        :param is_opc_service:
            The value to assign to the is_opc_service property of this CloudGateMapping.
        :type is_opc_service: bool

        :param description:
            The value to assign to the description property of this CloudGateMapping.
        :type description: str

        :param resource_prefix:
            The value to assign to the resource_prefix property of this CloudGateMapping.
        :type resource_prefix: str

        :param proxy_pass:
            The value to assign to the proxy_pass property of this CloudGateMapping.
        :type proxy_pass: str

        :param nginx_settings:
            The value to assign to the nginx_settings property of this CloudGateMapping.
        :type nginx_settings: str

        :param policy_name:
            The value to assign to the policy_name property of this CloudGateMapping.
        :type policy_name: str

        :param upstream_server_group:
            The value to assign to the upstream_server_group property of this CloudGateMapping.
        :type upstream_server_group: oci.identity_domains.models.CloudGateMappingUpstreamServerGroup

        :param server:
            The value to assign to the server property of this CloudGateMapping.
        :type server: oci.identity_domains.models.CloudGateMappingServer

        :param gateway_app:
            The value to assign to the gateway_app property of this CloudGateMapping.
        :type gateway_app: oci.identity_domains.models.CloudGateMappingGatewayApp

        :param cloud_gate:
            The value to assign to the cloud_gate property of this CloudGateMapping.
        :type cloud_gate: oci.identity_domains.models.CloudGateMappingCloudGate

        """
        self.swagger_types = {
            'id': 'str',
            'ocid': 'str',
            'schemas': 'list[str]',
            'meta': 'Meta',
            'idcs_created_by': 'IdcsCreatedBy',
            'idcs_last_modified_by': 'IdcsLastModifiedBy',
            'idcs_prevented_operations': 'list[str]',
            'tags': 'list[Tags]',
            'delete_in_progress': 'bool',
            'idcs_last_upgraded_in_release': 'str',
            'domain_ocid': 'str',
            'compartment_ocid': 'str',
            'tenancy_ocid': 'str',
            'is_opc_service': 'bool',
            'description': 'str',
            'resource_prefix': 'str',
            'proxy_pass': 'str',
            'nginx_settings': 'str',
            'policy_name': 'str',
            'upstream_server_group': 'CloudGateMappingUpstreamServerGroup',
            'server': 'CloudGateMappingServer',
            'gateway_app': 'CloudGateMappingGatewayApp',
            'cloud_gate': 'CloudGateMappingCloudGate'
        }
        self.attribute_map = {
            'id': 'id',
            'ocid': 'ocid',
            'schemas': 'schemas',
            'meta': 'meta',
            'idcs_created_by': 'idcsCreatedBy',
            'idcs_last_modified_by': 'idcsLastModifiedBy',
            'idcs_prevented_operations': 'idcsPreventedOperations',
            'tags': 'tags',
            'delete_in_progress': 'deleteInProgress',
            'idcs_last_upgraded_in_release': 'idcsLastUpgradedInRelease',
            'domain_ocid': 'domainOcid',
            'compartment_ocid': 'compartmentOcid',
            'tenancy_ocid': 'tenancyOcid',
            'is_opc_service': 'isOPCService',
            'description': 'description',
            'resource_prefix': 'resourcePrefix',
            'proxy_pass': 'proxyPass',
            'nginx_settings': 'nginxSettings',
            'policy_name': 'policyName',
            'upstream_server_group': 'upstreamServerGroup',
            'server': 'server',
            'gateway_app': 'gatewayApp',
            'cloud_gate': 'cloudGate'
        }
        self._id = None
        self._ocid = None
        self._schemas = None
        self._meta = None
        self._idcs_created_by = None
        self._idcs_last_modified_by = None
        self._idcs_prevented_operations = None
        self._tags = None
        self._delete_in_progress = None
        self._idcs_last_upgraded_in_release = None
        self._domain_ocid = None
        self._compartment_ocid = None
        self._tenancy_ocid = None
        self._is_opc_service = None
        self._description = None
        self._resource_prefix = None
        self._proxy_pass = None
        self._nginx_settings = None
        self._policy_name = None
        self._upstream_server_group = None
        self._server = None
        self._gateway_app = None
        self._cloud_gate = None

    @property
    def id(self):
        """
        Gets the id of this CloudGateMapping.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :return: The id of this CloudGateMapping.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudGateMapping.
        Unique identifier for the SCIM Resource as defined by the Service Provider. Each representation of the Resource MUST include a non-empty id value. This identifier MUST be unique across the Service Provider's entire set of Resources. It MUST be a stable, non-reassignable identifier that does not change when the same Resource is returned in subsequent requests. The value of the id attribute is always issued by the Service Provider and MUST never be specified by the Service Consumer. bulkId: is a reserved keyword and MUST NOT be used in the unique identifier.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: global


        :param id: The id of this CloudGateMapping.
        :type: str
        """
        self._id = id

    @property
    def ocid(self):
        """
        Gets the ocid of this CloudGateMapping.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :return: The ocid of this CloudGateMapping.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this CloudGateMapping.
        Unique OCI identifier for the SCIM Resource.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: global


        :param ocid: The ocid of this CloudGateMapping.
        :type: str
        """
        self._ocid = ocid

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this CloudGateMapping.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The schemas of this CloudGateMapping.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this CloudGateMapping.
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\\"enterprise\\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: true
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param schemas: The schemas of this CloudGateMapping.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def meta(self):
        """
        Gets the meta of this CloudGateMapping.

        :return: The meta of this CloudGateMapping.
        :rtype: oci.identity_domains.models.Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this CloudGateMapping.

        :param meta: The meta of this CloudGateMapping.
        :type: oci.identity_domains.models.Meta
        """
        self._meta = meta

    @property
    def idcs_created_by(self):
        """
        Gets the idcs_created_by of this CloudGateMapping.

        :return: The idcs_created_by of this CloudGateMapping.
        :rtype: oci.identity_domains.models.IdcsCreatedBy
        """
        return self._idcs_created_by

    @idcs_created_by.setter
    def idcs_created_by(self, idcs_created_by):
        """
        Sets the idcs_created_by of this CloudGateMapping.

        :param idcs_created_by: The idcs_created_by of this CloudGateMapping.
        :type: oci.identity_domains.models.IdcsCreatedBy
        """
        self._idcs_created_by = idcs_created_by

    @property
    def idcs_last_modified_by(self):
        """
        Gets the idcs_last_modified_by of this CloudGateMapping.

        :return: The idcs_last_modified_by of this CloudGateMapping.
        :rtype: oci.identity_domains.models.IdcsLastModifiedBy
        """
        return self._idcs_last_modified_by

    @idcs_last_modified_by.setter
    def idcs_last_modified_by(self, idcs_last_modified_by):
        """
        Sets the idcs_last_modified_by of this CloudGateMapping.

        :param idcs_last_modified_by: The idcs_last_modified_by of this CloudGateMapping.
        :type: oci.identity_domains.models.IdcsLastModifiedBy
        """
        self._idcs_last_modified_by = idcs_last_modified_by

    @property
    def idcs_prevented_operations(self):
        """
        Gets the idcs_prevented_operations of this CloudGateMapping.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for items in this list are: "replace", "update", "delete", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The idcs_prevented_operations of this CloudGateMapping.
        :rtype: list[str]
        """
        return self._idcs_prevented_operations

    @idcs_prevented_operations.setter
    def idcs_prevented_operations(self, idcs_prevented_operations):
        """
        Sets the idcs_prevented_operations of this CloudGateMapping.
        Each value of this attribute specifies an operation that only an internal client may perform on this particular resource.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_prevented_operations: The idcs_prevented_operations of this CloudGateMapping.
        :type: list[str]
        """
        allowed_values = ["replace", "update", "delete"]
        if idcs_prevented_operations:
            idcs_prevented_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in idcs_prevented_operations]
        self._idcs_prevented_operations = idcs_prevented_operations

    @property
    def tags(self):
        """
        Gets the tags of this CloudGateMapping.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The tags of this CloudGateMapping.
        :rtype: list[oci.identity_domains.models.Tags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CloudGateMapping.
        A list of tags on this resource.

        **SCIM++ Properties:**
         - idcsCompositeKey: [key, value]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param tags: The tags of this CloudGateMapping.
        :type: list[oci.identity_domains.models.Tags]
        """
        self._tags = tags

    @property
    def delete_in_progress(self):
        """
        Gets the delete_in_progress of this CloudGateMapping.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The delete_in_progress of this CloudGateMapping.
        :rtype: bool
        """
        return self._delete_in_progress

    @delete_in_progress.setter
    def delete_in_progress(self, delete_in_progress):
        """
        Sets the delete_in_progress of this CloudGateMapping.
        A boolean flag indicating this resource in the process of being deleted. Usually set to true when synchronous deletion of the resource would take too long.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param delete_in_progress: The delete_in_progress of this CloudGateMapping.
        :type: bool
        """
        self._delete_in_progress = delete_in_progress

    @property
    def idcs_last_upgraded_in_release(self):
        """
        Gets the idcs_last_upgraded_in_release of this CloudGateMapping.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The idcs_last_upgraded_in_release of this CloudGateMapping.
        :rtype: str
        """
        return self._idcs_last_upgraded_in_release

    @idcs_last_upgraded_in_release.setter
    def idcs_last_upgraded_in_release(self, idcs_last_upgraded_in_release):
        """
        Sets the idcs_last_upgraded_in_release of this CloudGateMapping.
        The release number when the resource was upgraded.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param idcs_last_upgraded_in_release: The idcs_last_upgraded_in_release of this CloudGateMapping.
        :type: str
        """
        self._idcs_last_upgraded_in_release = idcs_last_upgraded_in_release

    @property
    def domain_ocid(self):
        """
        Gets the domain_ocid of this CloudGateMapping.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The domain_ocid of this CloudGateMapping.
        :rtype: str
        """
        return self._domain_ocid

    @domain_ocid.setter
    def domain_ocid(self, domain_ocid):
        """
        Sets the domain_ocid of this CloudGateMapping.
        OCI Domain Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param domain_ocid: The domain_ocid of this CloudGateMapping.
        :type: str
        """
        self._domain_ocid = domain_ocid

    @property
    def compartment_ocid(self):
        """
        Gets the compartment_ocid of this CloudGateMapping.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The compartment_ocid of this CloudGateMapping.
        :rtype: str
        """
        return self._compartment_ocid

    @compartment_ocid.setter
    def compartment_ocid(self, compartment_ocid):
        """
        Sets the compartment_ocid of this CloudGateMapping.
        OCI Compartment Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param compartment_ocid: The compartment_ocid of this CloudGateMapping.
        :type: str
        """
        self._compartment_ocid = compartment_ocid

    @property
    def tenancy_ocid(self):
        """
        Gets the tenancy_ocid of this CloudGateMapping.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The tenancy_ocid of this CloudGateMapping.
        :rtype: str
        """
        return self._tenancy_ocid

    @tenancy_ocid.setter
    def tenancy_ocid(self, tenancy_ocid):
        """
        Sets the tenancy_ocid of this CloudGateMapping.
        OCI Tenant Id (ocid) in which the resource lives.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param tenancy_ocid: The tenancy_ocid of this CloudGateMapping.
        :type: str
        """
        self._tenancy_ocid = tenancy_ocid

    @property
    def is_opc_service(self):
        """
        Gets the is_opc_service of this CloudGateMapping.
        Indicates whether this resource was created by OPC

        **Added In:** 19.3.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: boolean
         - uniqueness: none


        :return: The is_opc_service of this CloudGateMapping.
        :rtype: bool
        """
        return self._is_opc_service

    @is_opc_service.setter
    def is_opc_service(self, is_opc_service):
        """
        Sets the is_opc_service of this CloudGateMapping.
        Indicates whether this resource was created by OPC

        **Added In:** 19.3.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: boolean
         - uniqueness: none


        :param is_opc_service: The is_opc_service of this CloudGateMapping.
        :type: bool
        """
        self._is_opc_service = is_opc_service

    @property
    def description(self):
        """
        Gets the description of this CloudGateMapping.
        Brief description for this Cloud Gate

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The description of this CloudGateMapping.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CloudGateMapping.
        Brief description for this Cloud Gate

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param description: The description of this CloudGateMapping.
        :type: str
        """
        self._description = description

    @property
    def resource_prefix(self):
        """
        **[Required]** Gets the resource_prefix of this CloudGateMapping.
        Resource prefix for this mapping.  This will be used to define the location block

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The resource_prefix of this CloudGateMapping.
        :rtype: str
        """
        return self._resource_prefix

    @resource_prefix.setter
    def resource_prefix(self, resource_prefix):
        """
        Sets the resource_prefix of this CloudGateMapping.
        Resource prefix for this mapping.  This will be used to define the location block

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param resource_prefix: The resource_prefix of this CloudGateMapping.
        :type: str
        """
        self._resource_prefix = resource_prefix

    @property
    def proxy_pass(self):
        """
        Gets the proxy_pass of this CloudGateMapping.
        NGINX ProxyPass entry for this Mapping

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The proxy_pass of this CloudGateMapping.
        :rtype: str
        """
        return self._proxy_pass

    @proxy_pass.setter
    def proxy_pass(self, proxy_pass):
        """
        Sets the proxy_pass of this CloudGateMapping.
        NGINX ProxyPass entry for this Mapping

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param proxy_pass: The proxy_pass of this CloudGateMapping.
        :type: str
        """
        self._proxy_pass = proxy_pass

    @property
    def nginx_settings(self):
        """
        Gets the nginx_settings of this CloudGateMapping.
        More NGINX Settings. JSON encoded key value pairs similar to WTP encoding

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The nginx_settings of this CloudGateMapping.
        :rtype: str
        """
        return self._nginx_settings

    @nginx_settings.setter
    def nginx_settings(self, nginx_settings):
        """
        Sets the nginx_settings of this CloudGateMapping.
        More NGINX Settings. JSON encoded key value pairs similar to WTP encoding

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param nginx_settings: The nginx_settings of this CloudGateMapping.
        :type: str
        """
        self._nginx_settings = nginx_settings

    @property
    def policy_name(self):
        """
        **[Required]** Gets the policy_name of this CloudGateMapping.
        The Web Tier policy name used for the App that is mapped to the owning Cloud Gate

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The policy_name of this CloudGateMapping.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this CloudGateMapping.
        The Web Tier policy name used for the App that is mapped to the owning Cloud Gate

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param policy_name: The policy_name of this CloudGateMapping.
        :type: str
        """
        self._policy_name = policy_name

    @property
    def upstream_server_group(self):
        """
        Gets the upstream_server_group of this CloudGateMapping.

        :return: The upstream_server_group of this CloudGateMapping.
        :rtype: oci.identity_domains.models.CloudGateMappingUpstreamServerGroup
        """
        return self._upstream_server_group

    @upstream_server_group.setter
    def upstream_server_group(self, upstream_server_group):
        """
        Sets the upstream_server_group of this CloudGateMapping.

        :param upstream_server_group: The upstream_server_group of this CloudGateMapping.
        :type: oci.identity_domains.models.CloudGateMappingUpstreamServerGroup
        """
        self._upstream_server_group = upstream_server_group

    @property
    def server(self):
        """
        **[Required]** Gets the server of this CloudGateMapping.

        :return: The server of this CloudGateMapping.
        :rtype: oci.identity_domains.models.CloudGateMappingServer
        """
        return self._server

    @server.setter
    def server(self, server):
        """
        Sets the server of this CloudGateMapping.

        :param server: The server of this CloudGateMapping.
        :type: oci.identity_domains.models.CloudGateMappingServer
        """
        self._server = server

    @property
    def gateway_app(self):
        """
        **[Required]** Gets the gateway_app of this CloudGateMapping.

        :return: The gateway_app of this CloudGateMapping.
        :rtype: oci.identity_domains.models.CloudGateMappingGatewayApp
        """
        return self._gateway_app

    @gateway_app.setter
    def gateway_app(self, gateway_app):
        """
        Sets the gateway_app of this CloudGateMapping.

        :param gateway_app: The gateway_app of this CloudGateMapping.
        :type: oci.identity_domains.models.CloudGateMappingGatewayApp
        """
        self._gateway_app = gateway_app

    @property
    def cloud_gate(self):
        """
        **[Required]** Gets the cloud_gate of this CloudGateMapping.

        :return: The cloud_gate of this CloudGateMapping.
        :rtype: oci.identity_domains.models.CloudGateMappingCloudGate
        """
        return self._cloud_gate

    @cloud_gate.setter
    def cloud_gate(self, cloud_gate):
        """
        Sets the cloud_gate of this CloudGateMapping.

        :param cloud_gate: The cloud_gate of this CloudGateMapping.
        :type: oci.identity_domains.models.CloudGateMappingCloudGate
        """
        self._cloud_gate = cloud_gate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
