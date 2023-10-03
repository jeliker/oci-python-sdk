# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMaintenanceConfigurationDetails(object):
    """
    Defines the maintenance configuration for create operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMaintenanceConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_interim_release_auto_upgrade_enabled:
            The value to assign to the is_interim_release_auto_upgrade_enabled property of this CreateMaintenanceConfigurationDetails.
        :type is_interim_release_auto_upgrade_enabled: bool

        :param interim_release_upgrade_period_in_days:
            The value to assign to the interim_release_upgrade_period_in_days property of this CreateMaintenanceConfigurationDetails.
        :type interim_release_upgrade_period_in_days: int

        :param bundle_release_upgrade_period_in_days:
            The value to assign to the bundle_release_upgrade_period_in_days property of this CreateMaintenanceConfigurationDetails.
        :type bundle_release_upgrade_period_in_days: int

        :param major_release_upgrade_period_in_days:
            The value to assign to the major_release_upgrade_period_in_days property of this CreateMaintenanceConfigurationDetails.
        :type major_release_upgrade_period_in_days: int

        :param security_patch_upgrade_period_in_days:
            The value to assign to the security_patch_upgrade_period_in_days property of this CreateMaintenanceConfigurationDetails.
        :type security_patch_upgrade_period_in_days: int

        """
        self.swagger_types = {
            'is_interim_release_auto_upgrade_enabled': 'bool',
            'interim_release_upgrade_period_in_days': 'int',
            'bundle_release_upgrade_period_in_days': 'int',
            'major_release_upgrade_period_in_days': 'int',
            'security_patch_upgrade_period_in_days': 'int'
        }

        self.attribute_map = {
            'is_interim_release_auto_upgrade_enabled': 'isInterimReleaseAutoUpgradeEnabled',
            'interim_release_upgrade_period_in_days': 'interimReleaseUpgradePeriodInDays',
            'bundle_release_upgrade_period_in_days': 'bundleReleaseUpgradePeriodInDays',
            'major_release_upgrade_period_in_days': 'majorReleaseUpgradePeriodInDays',
            'security_patch_upgrade_period_in_days': 'securityPatchUpgradePeriodInDays'
        }

        self._is_interim_release_auto_upgrade_enabled = None
        self._interim_release_upgrade_period_in_days = None
        self._bundle_release_upgrade_period_in_days = None
        self._major_release_upgrade_period_in_days = None
        self._security_patch_upgrade_period_in_days = None

    @property
    def is_interim_release_auto_upgrade_enabled(self):
        """
        Gets the is_interim_release_auto_upgrade_enabled of this CreateMaintenanceConfigurationDetails.
        By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release,
        you have to specify interimReleaseUpgradePeriodInDays too.


        :return: The is_interim_release_auto_upgrade_enabled of this CreateMaintenanceConfigurationDetails.
        :rtype: bool
        """
        return self._is_interim_release_auto_upgrade_enabled

    @is_interim_release_auto_upgrade_enabled.setter
    def is_interim_release_auto_upgrade_enabled(self, is_interim_release_auto_upgrade_enabled):
        """
        Sets the is_interim_release_auto_upgrade_enabled of this CreateMaintenanceConfigurationDetails.
        By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release,
        you have to specify interimReleaseUpgradePeriodInDays too.


        :param is_interim_release_auto_upgrade_enabled: The is_interim_release_auto_upgrade_enabled of this CreateMaintenanceConfigurationDetails.
        :type: bool
        """
        self._is_interim_release_auto_upgrade_enabled = is_interim_release_auto_upgrade_enabled

    @property
    def interim_release_upgrade_period_in_days(self):
        """
        Gets the interim_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.


        :return: The interim_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        :rtype: int
        """
        return self._interim_release_upgrade_period_in_days

    @interim_release_upgrade_period_in_days.setter
    def interim_release_upgrade_period_in_days(self, interim_release_upgrade_period_in_days):
        """
        Sets the interim_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.


        :param interim_release_upgrade_period_in_days: The interim_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        :type: int
        """
        self._interim_release_upgrade_period_in_days = interim_release_upgrade_period_in_days

    @property
    def bundle_release_upgrade_period_in_days(self):
        """
        Gets the bundle_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases.
        This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default.


        :return: The bundle_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        :rtype: int
        """
        return self._bundle_release_upgrade_period_in_days

    @bundle_release_upgrade_period_in_days.setter
    def bundle_release_upgrade_period_in_days(self, bundle_release_upgrade_period_in_days):
        """
        Sets the bundle_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases.
        This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default.


        :param bundle_release_upgrade_period_in_days: The bundle_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        :type: int
        """
        self._bundle_release_upgrade_period_in_days = bundle_release_upgrade_period_in_days

    @property
    def major_release_upgrade_period_in_days(self):
        """
        Gets the major_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases.
        Not passing this field during create will equate to using the service default.


        :return: The major_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        :rtype: int
        """
        return self._major_release_upgrade_period_in_days

    @major_release_upgrade_period_in_days.setter
    def major_release_upgrade_period_in_days(self, major_release_upgrade_period_in_days):
        """
        Sets the major_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases.
        Not passing this field during create will equate to using the service default.


        :param major_release_upgrade_period_in_days: The major_release_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        :type: int
        """
        self._major_release_upgrade_period_in_days = major_release_upgrade_period_in_days

    @property
    def security_patch_upgrade_period_in_days(self):
        """
        Gets the security_patch_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases.
        Not passing this field during create will equate to using the service default.


        :return: The security_patch_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        :rtype: int
        """
        return self._security_patch_upgrade_period_in_days

    @security_patch_upgrade_period_in_days.setter
    def security_patch_upgrade_period_in_days(self, security_patch_upgrade_period_in_days):
        """
        Sets the security_patch_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases.
        Not passing this field during create will equate to using the service default.


        :param security_patch_upgrade_period_in_days: The security_patch_upgrade_period_in_days of this CreateMaintenanceConfigurationDetails.
        :type: int
        """
        self._security_patch_upgrade_period_in_days = security_patch_upgrade_period_in_days

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other