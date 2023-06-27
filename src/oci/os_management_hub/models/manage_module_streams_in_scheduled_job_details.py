# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManageModuleStreamsInScheduledJobDetails(object):
    """
    The set of changes to make to the state of the modules, streams, and profiles on the managed target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManageModuleStreamsInScheduledJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param enable:
            The value to assign to the enable property of this ManageModuleStreamsInScheduledJobDetails.
        :type enable: list[oci.os_management_hub.models.ModuleStreamDetails]

        :param disable:
            The value to assign to the disable property of this ManageModuleStreamsInScheduledJobDetails.
        :type disable: list[oci.os_management_hub.models.ModuleStreamDetails]

        :param install:
            The value to assign to the install property of this ManageModuleStreamsInScheduledJobDetails.
        :type install: list[oci.os_management_hub.models.ModuleStreamProfileDetails]

        :param remove:
            The value to assign to the remove property of this ManageModuleStreamsInScheduledJobDetails.
        :type remove: list[oci.os_management_hub.models.ModuleStreamProfileDetails]

        """
        self.swagger_types = {
            'enable': 'list[ModuleStreamDetails]',
            'disable': 'list[ModuleStreamDetails]',
            'install': 'list[ModuleStreamProfileDetails]',
            'remove': 'list[ModuleStreamProfileDetails]'
        }

        self.attribute_map = {
            'enable': 'enable',
            'disable': 'disable',
            'install': 'install',
            'remove': 'remove'
        }

        self._enable = None
        self._disable = None
        self._install = None
        self._remove = None

    @property
    def enable(self):
        """
        Gets the enable of this ManageModuleStreamsInScheduledJobDetails.
        The set of module streams to enable.


        :return: The enable of this ManageModuleStreamsInScheduledJobDetails.
        :rtype: list[oci.os_management_hub.models.ModuleStreamDetails]
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """
        Sets the enable of this ManageModuleStreamsInScheduledJobDetails.
        The set of module streams to enable.


        :param enable: The enable of this ManageModuleStreamsInScheduledJobDetails.
        :type: list[oci.os_management_hub.models.ModuleStreamDetails]
        """
        self._enable = enable

    @property
    def disable(self):
        """
        Gets the disable of this ManageModuleStreamsInScheduledJobDetails.
        The set of module streams to disable.


        :return: The disable of this ManageModuleStreamsInScheduledJobDetails.
        :rtype: list[oci.os_management_hub.models.ModuleStreamDetails]
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        """
        Sets the disable of this ManageModuleStreamsInScheduledJobDetails.
        The set of module streams to disable.


        :param disable: The disable of this ManageModuleStreamsInScheduledJobDetails.
        :type: list[oci.os_management_hub.models.ModuleStreamDetails]
        """
        self._disable = disable

    @property
    def install(self):
        """
        Gets the install of this ManageModuleStreamsInScheduledJobDetails.
        The set of module stream profiles to install.


        :return: The install of this ManageModuleStreamsInScheduledJobDetails.
        :rtype: list[oci.os_management_hub.models.ModuleStreamProfileDetails]
        """
        return self._install

    @install.setter
    def install(self, install):
        """
        Sets the install of this ManageModuleStreamsInScheduledJobDetails.
        The set of module stream profiles to install.


        :param install: The install of this ManageModuleStreamsInScheduledJobDetails.
        :type: list[oci.os_management_hub.models.ModuleStreamProfileDetails]
        """
        self._install = install

    @property
    def remove(self):
        """
        Gets the remove of this ManageModuleStreamsInScheduledJobDetails.
        The set of module stream profiles to remove.


        :return: The remove of this ManageModuleStreamsInScheduledJobDetails.
        :rtype: list[oci.os_management_hub.models.ModuleStreamProfileDetails]
        """
        return self._remove

    @remove.setter
    def remove(self, remove):
        """
        Sets the remove of this ManageModuleStreamsInScheduledJobDetails.
        The set of module stream profiles to remove.


        :param remove: The remove of this ManageModuleStreamsInScheduledJobDetails.
        :type: list[oci.os_management_hub.models.ModuleStreamProfileDetails]
        """
        self._remove = remove

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
