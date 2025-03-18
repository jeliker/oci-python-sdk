# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateProxyConfigurationDetails(object):
    """
    Provides the information used to update the proxy configuration for a management station.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateProxyConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateProxyConfigurationDetails.
        :type is_enabled: bool

        :param hosts:
            The value to assign to the hosts property of this UpdateProxyConfigurationDetails.
        :type hosts: list[str]

        :param port:
            The value to assign to the port property of this UpdateProxyConfigurationDetails.
        :type port: str

        :param forward:
            The value to assign to the forward property of this UpdateProxyConfigurationDetails.
        :type forward: str

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'hosts': 'list[str]',
            'port': 'str',
            'forward': 'str'
        }
        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'hosts': 'hosts',
            'port': 'port',
            'forward': 'forward'
        }
        self._is_enabled = None
        self._hosts = None
        self._port = None
        self._forward = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this UpdateProxyConfigurationDetails.
        Indicates if the proxy should be enabled or disabled. Default is enabled.


        :return: The is_enabled of this UpdateProxyConfigurationDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateProxyConfigurationDetails.
        Indicates if the proxy should be enabled or disabled. Default is enabled.


        :param is_enabled: The is_enabled of this UpdateProxyConfigurationDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def hosts(self):
        """
        Gets the hosts of this UpdateProxyConfigurationDetails.
        List of hosts.


        :return: The hosts of this UpdateProxyConfigurationDetails.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this UpdateProxyConfigurationDetails.
        List of hosts.


        :param hosts: The hosts of this UpdateProxyConfigurationDetails.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def port(self):
        """
        Gets the port of this UpdateProxyConfigurationDetails.
        Listening port used for the proxy.


        :return: The port of this UpdateProxyConfigurationDetails.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateProxyConfigurationDetails.
        Listening port used for the proxy.


        :param port: The port of this UpdateProxyConfigurationDetails.
        :type: str
        """
        self._port = port

    @property
    def forward(self):
        """
        Gets the forward of this UpdateProxyConfigurationDetails.
        The URL the proxy will forward to.


        :return: The forward of this UpdateProxyConfigurationDetails.
        :rtype: str
        """
        return self._forward

    @forward.setter
    def forward(self, forward):
        """
        Sets the forward of this UpdateProxyConfigurationDetails.
        The URL the proxy will forward to.


        :param forward: The forward of this UpdateProxyConfigurationDetails.
        :type: str
        """
        self._forward = forward

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
