# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNetworkLoadBalancerDetails(object):
    """
    The properties that define a network load balancer. For more information, see
    `Introduction to Network Load Balancer`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, then
    contact an administrator. If you are an administrator who writes policies to give users access, then see
    `Getting Started with Policies`__.

    For information about endpoints and signing API requests, see
    `About the API`__. For information about available SDKs and tools, see
    `SDKS and Other Tools`__.

    __ https://docs.cloud.oracle.com/Content/NetworkLoadBalancer/introduction.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm
    __ https://docs.cloud.oracle.com/Content/API/Concepts/sdks.htm
    """

    #: A constant which can be used with the nlb_ip_version property of a CreateNetworkLoadBalancerDetails.
    #: This constant has a value of "IPV4"
    NLB_IP_VERSION_IPV4 = "IPV4"

    #: A constant which can be used with the nlb_ip_version property of a CreateNetworkLoadBalancerDetails.
    #: This constant has a value of "IPV4_AND_IPV6"
    NLB_IP_VERSION_IPV4_AND_IPV6 = "IPV4_AND_IPV6"

    #: A constant which can be used with the nlb_ip_version property of a CreateNetworkLoadBalancerDetails.
    #: This constant has a value of "IPV6"
    NLB_IP_VERSION_IPV6 = "IPV6"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNetworkLoadBalancerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateNetworkLoadBalancerDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateNetworkLoadBalancerDetails.
        :type display_name: str

        :param is_preserve_source_destination:
            The value to assign to the is_preserve_source_destination property of this CreateNetworkLoadBalancerDetails.
        :type is_preserve_source_destination: bool

        :param is_symmetric_hash_enabled:
            The value to assign to the is_symmetric_hash_enabled property of this CreateNetworkLoadBalancerDetails.
        :type is_symmetric_hash_enabled: bool

        :param reserved_ips:
            The value to assign to the reserved_ips property of this CreateNetworkLoadBalancerDetails.
        :type reserved_ips: list[oci.network_load_balancer.models.ReservedIP]

        :param is_private:
            The value to assign to the is_private property of this CreateNetworkLoadBalancerDetails.
        :type is_private: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateNetworkLoadBalancerDetails.
        :type subnet_id: str

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this CreateNetworkLoadBalancerDetails.
        :type network_security_group_ids: list[str]

        :param nlb_ip_version:
            The value to assign to the nlb_ip_version property of this CreateNetworkLoadBalancerDetails.
            Allowed values for this property are: "IPV4", "IPV4_AND_IPV6", "IPV6"
        :type nlb_ip_version: str

        :param subnet_ipv6_cidr:
            The value to assign to the subnet_ipv6_cidr property of this CreateNetworkLoadBalancerDetails.
        :type subnet_ipv6_cidr: str

        :param assigned_private_ipv4:
            The value to assign to the assigned_private_ipv4 property of this CreateNetworkLoadBalancerDetails.
        :type assigned_private_ipv4: str

        :param assigned_ipv6:
            The value to assign to the assigned_ipv6 property of this CreateNetworkLoadBalancerDetails.
        :type assigned_ipv6: str

        :param listeners:
            The value to assign to the listeners property of this CreateNetworkLoadBalancerDetails.
        :type listeners: dict(str, ListenerDetails)

        :param backend_sets:
            The value to assign to the backend_sets property of this CreateNetworkLoadBalancerDetails.
        :type backend_sets: dict(str, BackendSetDetails)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNetworkLoadBalancerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNetworkLoadBalancerDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param security_attributes:
            The value to assign to the security_attributes property of this CreateNetworkLoadBalancerDetails.
        :type security_attributes: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'is_preserve_source_destination': 'bool',
            'is_symmetric_hash_enabled': 'bool',
            'reserved_ips': 'list[ReservedIP]',
            'is_private': 'bool',
            'subnet_id': 'str',
            'network_security_group_ids': 'list[str]',
            'nlb_ip_version': 'str',
            'subnet_ipv6_cidr': 'str',
            'assigned_private_ipv4': 'str',
            'assigned_ipv6': 'str',
            'listeners': 'dict(str, ListenerDetails)',
            'backend_sets': 'dict(str, BackendSetDetails)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'security_attributes': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'is_preserve_source_destination': 'isPreserveSourceDestination',
            'is_symmetric_hash_enabled': 'isSymmetricHashEnabled',
            'reserved_ips': 'reservedIps',
            'is_private': 'isPrivate',
            'subnet_id': 'subnetId',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'nlb_ip_version': 'nlbIpVersion',
            'subnet_ipv6_cidr': 'subnetIpv6Cidr',
            'assigned_private_ipv4': 'assignedPrivateIpv4',
            'assigned_ipv6': 'assignedIpv6',
            'listeners': 'listeners',
            'backend_sets': 'backendSets',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'security_attributes': 'securityAttributes'
        }
        self._compartment_id = None
        self._display_name = None
        self._is_preserve_source_destination = None
        self._is_symmetric_hash_enabled = None
        self._reserved_ips = None
        self._is_private = None
        self._subnet_id = None
        self._network_security_group_ids = None
        self._nlb_ip_version = None
        self._subnet_ipv6_cidr = None
        self._assigned_private_ipv4 = None
        self._assigned_ipv6 = None
        self._listeners = None
        self._backend_sets = None
        self._freeform_tags = None
        self._defined_tags = None
        self._security_attributes = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateNetworkLoadBalancerDetails.
        The `OCID`__ of the compartment containing the network load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateNetworkLoadBalancerDetails.
        The `OCID`__ of the compartment containing the network load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateNetworkLoadBalancerDetails.
        Network load balancer identifier, which can be renamed.


        :return: The display_name of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateNetworkLoadBalancerDetails.
        Network load balancer identifier, which can be renamed.


        :param display_name: The display_name of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_preserve_source_destination(self):
        """
        Gets the is_preserve_source_destination of this CreateNetworkLoadBalancerDetails.
        This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically
        enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.


        :return: The is_preserve_source_destination of this CreateNetworkLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_preserve_source_destination

    @is_preserve_source_destination.setter
    def is_preserve_source_destination(self, is_preserve_source_destination):
        """
        Sets the is_preserve_source_destination of this CreateNetworkLoadBalancerDetails.
        This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically
        enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.


        :param is_preserve_source_destination: The is_preserve_source_destination of this CreateNetworkLoadBalancerDetails.
        :type: bool
        """
        self._is_preserve_source_destination = is_preserve_source_destination

    @property
    def is_symmetric_hash_enabled(self):
        """
        Gets the is_symmetric_hash_enabled of this CreateNetworkLoadBalancerDetails.
        This can only be enabled when NLB is working in transparent mode with source destination header preservation enabled.
        This removes the additional dependency from NLB backends(like Firewalls) to perform SNAT.


        :return: The is_symmetric_hash_enabled of this CreateNetworkLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_symmetric_hash_enabled

    @is_symmetric_hash_enabled.setter
    def is_symmetric_hash_enabled(self, is_symmetric_hash_enabled):
        """
        Sets the is_symmetric_hash_enabled of this CreateNetworkLoadBalancerDetails.
        This can only be enabled when NLB is working in transparent mode with source destination header preservation enabled.
        This removes the additional dependency from NLB backends(like Firewalls) to perform SNAT.


        :param is_symmetric_hash_enabled: The is_symmetric_hash_enabled of this CreateNetworkLoadBalancerDetails.
        :type: bool
        """
        self._is_symmetric_hash_enabled = is_symmetric_hash_enabled

    @property
    def reserved_ips(self):
        """
        Gets the reserved_ips of this CreateNetworkLoadBalancerDetails.
        An array of reserved Ips.


        :return: The reserved_ips of this CreateNetworkLoadBalancerDetails.
        :rtype: list[oci.network_load_balancer.models.ReservedIP]
        """
        return self._reserved_ips

    @reserved_ips.setter
    def reserved_ips(self, reserved_ips):
        """
        Sets the reserved_ips of this CreateNetworkLoadBalancerDetails.
        An array of reserved Ips.


        :param reserved_ips: The reserved_ips of this CreateNetworkLoadBalancerDetails.
        :type: list[oci.network_load_balancer.models.ReservedIP]
        """
        self._reserved_ips = reserved_ips

    @property
    def is_private(self):
        """
        Gets the is_private of this CreateNetworkLoadBalancerDetails.
        Whether the network load balancer has a virtual cloud network-local (private) IP address.

        If \"true\", then the service assigns a private IP address to the network load balancer.

        If \"false\", then the service assigns a public IP address to the network load balancer.

        A public network load balancer is accessible from the internet, depending on the
        `security list rules`__ for your virtual cloud network. For more information about public and
        private network load balancers,
        see `Network Load Balancer Types`__.
        This value is true by default.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/NetworkLoadBalancer/introduction.htm#NetworkLoadBalancerTypes


        :return: The is_private of this CreateNetworkLoadBalancerDetails.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """
        Sets the is_private of this CreateNetworkLoadBalancerDetails.
        Whether the network load balancer has a virtual cloud network-local (private) IP address.

        If \"true\", then the service assigns a private IP address to the network load balancer.

        If \"false\", then the service assigns a public IP address to the network load balancer.

        A public network load balancer is accessible from the internet, depending on the
        `security list rules`__ for your virtual cloud network. For more information about public and
        private network load balancers,
        see `Network Load Balancer Types`__.
        This value is true by default.

        Example: `true`

        __ https://docs.cloud.oracle.com/Content/network/Concepts/securitylists.htm
        __ https://docs.cloud.oracle.com/Content/NetworkLoadBalancer/introduction.htm#NetworkLoadBalancerTypes


        :param is_private: The is_private of this CreateNetworkLoadBalancerDetails.
        :type: bool
        """
        self._is_private = is_private

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateNetworkLoadBalancerDetails.
        The subnet in which the network load balancer is spawned `OCIDs`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateNetworkLoadBalancerDetails.
        The subnet in which the network load balancer is spawned `OCIDs`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this CreateNetworkLoadBalancerDetails.
        An array of network security groups `OCIDs`__ associated with the network load
        balancer.

        During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups.

        The benefits of associating the network load balancer with network security groups include:

        *  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer.

        *  The network security rules of other resources can reference the network security groups associated with the network load balancer
           to ensure access.

        Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this CreateNetworkLoadBalancerDetails.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this CreateNetworkLoadBalancerDetails.
        An array of network security groups `OCIDs`__ associated with the network load
        balancer.

        During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups.

        The benefits of associating the network load balancer with network security groups include:

        *  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer.

        *  The network security rules of other resources can reference the network security groups associated with the network load balancer
           to ensure access.

        Example: [\"ocid1.nsg.oc1.phx.unique_ID\"]

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this CreateNetworkLoadBalancerDetails.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def nlb_ip_version(self):
        """
        Gets the nlb_ip_version of this CreateNetworkLoadBalancerDetails.
        IP version associated with the NLB.

        Allowed values for this property are: "IPV4", "IPV4_AND_IPV6", "IPV6"


        :return: The nlb_ip_version of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._nlb_ip_version

    @nlb_ip_version.setter
    def nlb_ip_version(self, nlb_ip_version):
        """
        Sets the nlb_ip_version of this CreateNetworkLoadBalancerDetails.
        IP version associated with the NLB.


        :param nlb_ip_version: The nlb_ip_version of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        allowed_values = ["IPV4", "IPV4_AND_IPV6", "IPV6"]
        if not value_allowed_none_or_none_sentinel(nlb_ip_version, allowed_values):
            raise ValueError(
                f"Invalid value for `nlb_ip_version`, must be None or one of {allowed_values}"
            )
        self._nlb_ip_version = nlb_ip_version

    @property
    def subnet_ipv6_cidr(self):
        """
        Gets the subnet_ipv6_cidr of this CreateNetworkLoadBalancerDetails.
        IPv6 subnet prefix selection. If Ipv6 subnet prefix is passed, Nlb Ipv6 Address would be assign within the cidr block. NLB has to be dual or single stack ipv6 to support this.


        :return: The subnet_ipv6_cidr of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._subnet_ipv6_cidr

    @subnet_ipv6_cidr.setter
    def subnet_ipv6_cidr(self, subnet_ipv6_cidr):
        """
        Sets the subnet_ipv6_cidr of this CreateNetworkLoadBalancerDetails.
        IPv6 subnet prefix selection. If Ipv6 subnet prefix is passed, Nlb Ipv6 Address would be assign within the cidr block. NLB has to be dual or single stack ipv6 to support this.


        :param subnet_ipv6_cidr: The subnet_ipv6_cidr of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._subnet_ipv6_cidr = subnet_ipv6_cidr

    @property
    def assigned_private_ipv4(self):
        """
        Gets the assigned_private_ipv4 of this CreateNetworkLoadBalancerDetails.
        Private IP address to be assigned to the network load balancer being created.
        This IP address has to be in the CIDR range of the subnet where network load balancer is being created
        Example: \"10.0.0.1\"


        :return: The assigned_private_ipv4 of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._assigned_private_ipv4

    @assigned_private_ipv4.setter
    def assigned_private_ipv4(self, assigned_private_ipv4):
        """
        Sets the assigned_private_ipv4 of this CreateNetworkLoadBalancerDetails.
        Private IP address to be assigned to the network load balancer being created.
        This IP address has to be in the CIDR range of the subnet where network load balancer is being created
        Example: \"10.0.0.1\"


        :param assigned_private_ipv4: The assigned_private_ipv4 of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._assigned_private_ipv4 = assigned_private_ipv4

    @property
    def assigned_ipv6(self):
        """
        Gets the assigned_ipv6 of this CreateNetworkLoadBalancerDetails.
        IPv6 address to be assigned to the network load balancer being created.
        This IP address has to be part of one of the prefixes supported by the subnet.
        Example: \"2607:9b80:9a0a:9a7e:abcd:ef01:2345:6789\"


        :return: The assigned_ipv6 of this CreateNetworkLoadBalancerDetails.
        :rtype: str
        """
        return self._assigned_ipv6

    @assigned_ipv6.setter
    def assigned_ipv6(self, assigned_ipv6):
        """
        Sets the assigned_ipv6 of this CreateNetworkLoadBalancerDetails.
        IPv6 address to be assigned to the network load balancer being created.
        This IP address has to be part of one of the prefixes supported by the subnet.
        Example: \"2607:9b80:9a0a:9a7e:abcd:ef01:2345:6789\"


        :param assigned_ipv6: The assigned_ipv6 of this CreateNetworkLoadBalancerDetails.
        :type: str
        """
        self._assigned_ipv6 = assigned_ipv6

    @property
    def listeners(self):
        """
        Gets the listeners of this CreateNetworkLoadBalancerDetails.
        Listeners associated with the network load balancer.


        :return: The listeners of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, ListenerDetails)
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """
        Sets the listeners of this CreateNetworkLoadBalancerDetails.
        Listeners associated with the network load balancer.


        :param listeners: The listeners of this CreateNetworkLoadBalancerDetails.
        :type: dict(str, ListenerDetails)
        """
        self._listeners = listeners

    @property
    def backend_sets(self):
        """
        Gets the backend_sets of this CreateNetworkLoadBalancerDetails.
        Backend sets associated with the network load balancer.


        :return: The backend_sets of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, BackendSetDetails)
        """
        return self._backend_sets

    @backend_sets.setter
    def backend_sets(self, backend_sets):
        """
        Sets the backend_sets of this CreateNetworkLoadBalancerDetails.
        Backend sets associated with the network load balancer.


        :param backend_sets: The backend_sets of this CreateNetworkLoadBalancerDetails.
        :type: dict(str, BackendSetDetails)
        """
        self._backend_sets = backend_sets

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateNetworkLoadBalancerDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateNetworkLoadBalancerDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateNetworkLoadBalancerDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateNetworkLoadBalancerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateNetworkLoadBalancerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateNetworkLoadBalancerDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def security_attributes(self):
        """
        Gets the security_attributes of this CreateNetworkLoadBalancerDetails.
        ZPR tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"oracle-zpr\": {\"td\": {\"value\": \"42\", \"mode\": \"audit\"}}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The security_attributes of this CreateNetworkLoadBalancerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._security_attributes

    @security_attributes.setter
    def security_attributes(self, security_attributes):
        """
        Sets the security_attributes of this CreateNetworkLoadBalancerDetails.
        ZPR tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"oracle-zpr\": {\"td\": {\"value\": \"42\", \"mode\": \"audit\"}}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param security_attributes: The security_attributes of this CreateNetworkLoadBalancerDetails.
        :type: dict(str, dict(str, object))
        """
        self._security_attributes = security_attributes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
