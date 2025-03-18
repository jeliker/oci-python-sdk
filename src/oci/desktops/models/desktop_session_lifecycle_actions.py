# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopSessionLifecycleActions(object):
    """
    Action to be triggered on inactivity or disconnect
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopSessionLifecycleActions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param inactivity:
            The value to assign to the inactivity property of this DesktopSessionLifecycleActions.
        :type inactivity: oci.desktops.models.InactivityConfig

        :param disconnect:
            The value to assign to the disconnect property of this DesktopSessionLifecycleActions.
        :type disconnect: oci.desktops.models.DisconnectConfig

        """
        self.swagger_types = {
            'inactivity': 'InactivityConfig',
            'disconnect': 'DisconnectConfig'
        }
        self.attribute_map = {
            'inactivity': 'inactivity',
            'disconnect': 'disconnect'
        }
        self._inactivity = None
        self._disconnect = None

    @property
    def inactivity(self):
        """
        Gets the inactivity of this DesktopSessionLifecycleActions.

        :return: The inactivity of this DesktopSessionLifecycleActions.
        :rtype: oci.desktops.models.InactivityConfig
        """
        return self._inactivity

    @inactivity.setter
    def inactivity(self, inactivity):
        """
        Sets the inactivity of this DesktopSessionLifecycleActions.

        :param inactivity: The inactivity of this DesktopSessionLifecycleActions.
        :type: oci.desktops.models.InactivityConfig
        """
        self._inactivity = inactivity

    @property
    def disconnect(self):
        """
        Gets the disconnect of this DesktopSessionLifecycleActions.

        :return: The disconnect of this DesktopSessionLifecycleActions.
        :rtype: oci.desktops.models.DisconnectConfig
        """
        return self._disconnect

    @disconnect.setter
    def disconnect(self, disconnect):
        """
        Sets the disconnect of this DesktopSessionLifecycleActions.

        :param disconnect: The disconnect of this DesktopSessionLifecycleActions.
        :type: oci.desktops.models.DisconnectConfig
        """
        self._disconnect = disconnect

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
