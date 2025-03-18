# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBackendSetDetails(object):
    """
    The configuration details for updating a load balancer backend set.
    For more information about backend set configuration, see
    `Backend Sets for Network Load Balancers`__.

    **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/NetworkLoadBalancer/BackendSets/backend-set-management.htm
    """

    #: A constant which can be used with the ip_version property of a UpdateBackendSetDetails.
    #: This constant has a value of "IPV4"
    IP_VERSION_IPV4 = "IPV4"

    #: A constant which can be used with the ip_version property of a UpdateBackendSetDetails.
    #: This constant has a value of "IPV6"
    IP_VERSION_IPV6 = "IPV6"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBackendSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this UpdateBackendSetDetails.
        :type policy: str

        :param is_preserve_source:
            The value to assign to the is_preserve_source property of this UpdateBackendSetDetails.
        :type is_preserve_source: bool

        :param is_fail_open:
            The value to assign to the is_fail_open property of this UpdateBackendSetDetails.
        :type is_fail_open: bool

        :param is_instant_failover_enabled:
            The value to assign to the is_instant_failover_enabled property of this UpdateBackendSetDetails.
        :type is_instant_failover_enabled: bool

        :param is_instant_failover_tcp_reset_enabled:
            The value to assign to the is_instant_failover_tcp_reset_enabled property of this UpdateBackendSetDetails.
        :type is_instant_failover_tcp_reset_enabled: bool

        :param are_operationally_active_backends_preferred:
            The value to assign to the are_operationally_active_backends_preferred property of this UpdateBackendSetDetails.
        :type are_operationally_active_backends_preferred: bool

        :param ip_version:
            The value to assign to the ip_version property of this UpdateBackendSetDetails.
            Allowed values for this property are: "IPV4", "IPV6"
        :type ip_version: str

        :param backends:
            The value to assign to the backends property of this UpdateBackendSetDetails.
        :type backends: list[oci.network_load_balancer.models.BackendDetails]

        :param health_checker:
            The value to assign to the health_checker property of this UpdateBackendSetDetails.
        :type health_checker: oci.network_load_balancer.models.HealthCheckerDetails

        """
        self.swagger_types = {
            'policy': 'str',
            'is_preserve_source': 'bool',
            'is_fail_open': 'bool',
            'is_instant_failover_enabled': 'bool',
            'is_instant_failover_tcp_reset_enabled': 'bool',
            'are_operationally_active_backends_preferred': 'bool',
            'ip_version': 'str',
            'backends': 'list[BackendDetails]',
            'health_checker': 'HealthCheckerDetails'
        }
        self.attribute_map = {
            'policy': 'policy',
            'is_preserve_source': 'isPreserveSource',
            'is_fail_open': 'isFailOpen',
            'is_instant_failover_enabled': 'isInstantFailoverEnabled',
            'is_instant_failover_tcp_reset_enabled': 'isInstantFailoverTcpResetEnabled',
            'are_operationally_active_backends_preferred': 'areOperationallyActiveBackendsPreferred',
            'ip_version': 'ipVersion',
            'backends': 'backends',
            'health_checker': 'healthChecker'
        }
        self._policy = None
        self._is_preserve_source = None
        self._is_fail_open = None
        self._is_instant_failover_enabled = None
        self._is_instant_failover_tcp_reset_enabled = None
        self._are_operationally_active_backends_preferred = None
        self._ip_version = None
        self._backends = None
        self._health_checker = None

    @property
    def policy(self):
        """
        Gets the policy of this UpdateBackendSetDetails.
        The network load balancer policy for the backend set. To get a list of available policies, use the
        :func:`list_network_load_balancers_policies` operation.

        Example: `FIVE_TUPLE`


        :return: The policy of this UpdateBackendSetDetails.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this UpdateBackendSetDetails.
        The network load balancer policy for the backend set. To get a list of available policies, use the
        :func:`list_network_load_balancers_policies` operation.

        Example: `FIVE_TUPLE`


        :param policy: The policy of this UpdateBackendSetDetails.
        :type: str
        """
        self._policy = policy

    @property
    def is_preserve_source(self):
        """
        Gets the is_preserve_source of this UpdateBackendSetDetails.
        If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
        Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled.
        The value is true by default.


        :return: The is_preserve_source of this UpdateBackendSetDetails.
        :rtype: bool
        """
        return self._is_preserve_source

    @is_preserve_source.setter
    def is_preserve_source(self, is_preserve_source):
        """
        Sets the is_preserve_source of this UpdateBackendSetDetails.
        If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
        Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled.
        The value is true by default.


        :param is_preserve_source: The is_preserve_source of this UpdateBackendSetDetails.
        :type: bool
        """
        self._is_preserve_source = is_preserve_source

    @property
    def is_fail_open(self):
        """
        Gets the is_fail_open of this UpdateBackendSetDetails.
        If enabled, the network load balancer will continue to distribute traffic in the configured distribution in the event all backends are unhealthy.
        The value is false by default.


        :return: The is_fail_open of this UpdateBackendSetDetails.
        :rtype: bool
        """
        return self._is_fail_open

    @is_fail_open.setter
    def is_fail_open(self, is_fail_open):
        """
        Sets the is_fail_open of this UpdateBackendSetDetails.
        If enabled, the network load balancer will continue to distribute traffic in the configured distribution in the event all backends are unhealthy.
        The value is false by default.


        :param is_fail_open: The is_fail_open of this UpdateBackendSetDetails.
        :type: bool
        """
        self._is_fail_open = is_fail_open

    @property
    def is_instant_failover_enabled(self):
        """
        Gets the is_instant_failover_enabled of this UpdateBackendSetDetails.
        If enabled existing connections will be forwarded to an alternative healthy backend as soon as current backend becomes unhealthy.


        :return: The is_instant_failover_enabled of this UpdateBackendSetDetails.
        :rtype: bool
        """
        return self._is_instant_failover_enabled

    @is_instant_failover_enabled.setter
    def is_instant_failover_enabled(self, is_instant_failover_enabled):
        """
        Sets the is_instant_failover_enabled of this UpdateBackendSetDetails.
        If enabled existing connections will be forwarded to an alternative healthy backend as soon as current backend becomes unhealthy.


        :param is_instant_failover_enabled: The is_instant_failover_enabled of this UpdateBackendSetDetails.
        :type: bool
        """
        self._is_instant_failover_enabled = is_instant_failover_enabled

    @property
    def is_instant_failover_tcp_reset_enabled(self):
        """
        Gets the is_instant_failover_tcp_reset_enabled of this UpdateBackendSetDetails.
        If enabled along with instant failover, the network load balancer will send TCP RST to the clients for the existing connections instead of failing over to a healthy backend. This only applies when using the instant failover.


        :return: The is_instant_failover_tcp_reset_enabled of this UpdateBackendSetDetails.
        :rtype: bool
        """
        return self._is_instant_failover_tcp_reset_enabled

    @is_instant_failover_tcp_reset_enabled.setter
    def is_instant_failover_tcp_reset_enabled(self, is_instant_failover_tcp_reset_enabled):
        """
        Sets the is_instant_failover_tcp_reset_enabled of this UpdateBackendSetDetails.
        If enabled along with instant failover, the network load balancer will send TCP RST to the clients for the existing connections instead of failing over to a healthy backend. This only applies when using the instant failover.


        :param is_instant_failover_tcp_reset_enabled: The is_instant_failover_tcp_reset_enabled of this UpdateBackendSetDetails.
        :type: bool
        """
        self._is_instant_failover_tcp_reset_enabled = is_instant_failover_tcp_reset_enabled

    @property
    def are_operationally_active_backends_preferred(self):
        """
        Gets the are_operationally_active_backends_preferred of this UpdateBackendSetDetails.
        If enabled, NLB supports active-standby backends. The standby backend takes over the traffic when the active node fails, and continues to serve the traffic even when the old active node is back healthy.


        :return: The are_operationally_active_backends_preferred of this UpdateBackendSetDetails.
        :rtype: bool
        """
        return self._are_operationally_active_backends_preferred

    @are_operationally_active_backends_preferred.setter
    def are_operationally_active_backends_preferred(self, are_operationally_active_backends_preferred):
        """
        Sets the are_operationally_active_backends_preferred of this UpdateBackendSetDetails.
        If enabled, NLB supports active-standby backends. The standby backend takes over the traffic when the active node fails, and continues to serve the traffic even when the old active node is back healthy.


        :param are_operationally_active_backends_preferred: The are_operationally_active_backends_preferred of this UpdateBackendSetDetails.
        :type: bool
        """
        self._are_operationally_active_backends_preferred = are_operationally_active_backends_preferred

    @property
    def ip_version(self):
        """
        Gets the ip_version of this UpdateBackendSetDetails.
        The IP version associated with the backend set.

        Allowed values for this property are: "IPV4", "IPV6"


        :return: The ip_version of this UpdateBackendSetDetails.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """
        Sets the ip_version of this UpdateBackendSetDetails.
        The IP version associated with the backend set.


        :param ip_version: The ip_version of this UpdateBackendSetDetails.
        :type: str
        """
        allowed_values = ["IPV4", "IPV6"]
        if not value_allowed_none_or_none_sentinel(ip_version, allowed_values):
            raise ValueError(
                f"Invalid value for `ip_version`, must be None or one of {allowed_values}"
            )
        self._ip_version = ip_version

    @property
    def backends(self):
        """
        Gets the backends of this UpdateBackendSetDetails.
        An array of backends associated with the backend set.


        :return: The backends of this UpdateBackendSetDetails.
        :rtype: list[oci.network_load_balancer.models.BackendDetails]
        """
        return self._backends

    @backends.setter
    def backends(self, backends):
        """
        Sets the backends of this UpdateBackendSetDetails.
        An array of backends associated with the backend set.


        :param backends: The backends of this UpdateBackendSetDetails.
        :type: list[oci.network_load_balancer.models.BackendDetails]
        """
        self._backends = backends

    @property
    def health_checker(self):
        """
        Gets the health_checker of this UpdateBackendSetDetails.

        :return: The health_checker of this UpdateBackendSetDetails.
        :rtype: oci.network_load_balancer.models.HealthCheckerDetails
        """
        return self._health_checker

    @health_checker.setter
    def health_checker(self, health_checker):
        """
        Sets the health_checker of this UpdateBackendSetDetails.

        :param health_checker: The health_checker of this UpdateBackendSetDetails.
        :type: oci.network_load_balancer.models.HealthCheckerDetails
        """
        self._health_checker = health_checker

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
