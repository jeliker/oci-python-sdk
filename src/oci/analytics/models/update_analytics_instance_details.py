# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190331


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAnalyticsInstanceDetails(object):
    """
    Input payload to update an Analytics instance. Fields that are not provided
    will not be updated.
    """

    #: A constant which can be used with the license_type property of a UpdateAnalyticsInstanceDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_TYPE_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_type property of a UpdateAnalyticsInstanceDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the update_channel property of a UpdateAnalyticsInstanceDetails.
    #: This constant has a value of "REGULAR"
    UPDATE_CHANNEL_REGULAR = "REGULAR"

    #: A constant which can be used with the update_channel property of a UpdateAnalyticsInstanceDetails.
    #: This constant has a value of "EARLY"
    UPDATE_CHANNEL_EARLY = "EARLY"

    #: A constant which can be used with the update_channel property of a UpdateAnalyticsInstanceDetails.
    #: This constant has a value of "PHASE_2"
    UPDATE_CHANNEL_PHASE_2 = "PHASE_2"

    #: A constant which can be used with the update_channel property of a UpdateAnalyticsInstanceDetails.
    #: This constant has a value of "PHASE_1"
    UPDATE_CHANNEL_PHASE_1 = "PHASE_1"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAnalyticsInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateAnalyticsInstanceDetails.
        :type description: str

        :param email_notification:
            The value to assign to the email_notification property of this UpdateAnalyticsInstanceDetails.
        :type email_notification: str

        :param license_type:
            The value to assign to the license_type property of this UpdateAnalyticsInstanceDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_type: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAnalyticsInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAnalyticsInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param update_channel:
            The value to assign to the update_channel property of this UpdateAnalyticsInstanceDetails.
            Allowed values for this property are: "REGULAR", "EARLY", "PHASE_2", "PHASE_1"
        :type update_channel: str

        """
        self.swagger_types = {
            'description': 'str',
            'email_notification': 'str',
            'license_type': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'update_channel': 'str'
        }
        self.attribute_map = {
            'description': 'description',
            'email_notification': 'emailNotification',
            'license_type': 'licenseType',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'update_channel': 'updateChannel'
        }
        self._description = None
        self._email_notification = None
        self._license_type = None
        self._defined_tags = None
        self._freeform_tags = None
        self._update_channel = None

    @property
    def description(self):
        """
        Gets the description of this UpdateAnalyticsInstanceDetails.
        Optional description.


        :return: The description of this UpdateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateAnalyticsInstanceDetails.
        Optional description.


        :param description: The description of this UpdateAnalyticsInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def email_notification(self):
        """
        Gets the email_notification of this UpdateAnalyticsInstanceDetails.
        Email address receiving notifications.


        :return: The email_notification of this UpdateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """
        Sets the email_notification of this UpdateAnalyticsInstanceDetails.
        Email address receiving notifications.


        :param email_notification: The email_notification of this UpdateAnalyticsInstanceDetails.
        :type: str
        """
        self._email_notification = email_notification

    @property
    def license_type(self):
        """
        Gets the license_type of this UpdateAnalyticsInstanceDetails.
        The license used for the service.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_type of this UpdateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this UpdateAnalyticsInstanceDetails.
        The license used for the service.


        :param license_type: The license_type of this UpdateAnalyticsInstanceDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            raise ValueError(
                f"Invalid value for `license_type`, must be None or one of {allowed_values}"
            )
        self._license_type = license_type

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAnalyticsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAnalyticsInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAnalyticsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAnalyticsInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAnalyticsInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAnalyticsInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAnalyticsInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAnalyticsInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def update_channel(self):
        """
        Gets the update_channel of this UpdateAnalyticsInstanceDetails.
        Analytics instance update channel.

        Allowed values for this property are: "REGULAR", "EARLY", "PHASE_2", "PHASE_1"


        :return: The update_channel of this UpdateAnalyticsInstanceDetails.
        :rtype: str
        """
        return self._update_channel

    @update_channel.setter
    def update_channel(self, update_channel):
        """
        Sets the update_channel of this UpdateAnalyticsInstanceDetails.
        Analytics instance update channel.


        :param update_channel: The update_channel of this UpdateAnalyticsInstanceDetails.
        :type: str
        """
        allowed_values = ["REGULAR", "EARLY", "PHASE_2", "PHASE_1"]
        if not value_allowed_none_or_none_sentinel(update_channel, allowed_values):
            raise ValueError(
                f"Invalid value for `update_channel`, must be None or one of {allowed_values}"
            )
        self._update_channel = update_channel

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
