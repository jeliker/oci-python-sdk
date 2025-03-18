# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSchedulingWindowDetails(object):
    """
    Describes the modification parameters for the Scheduling Window.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSchedulingWindowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param window_preference:
            The value to assign to the window_preference property of this UpdateSchedulingWindowDetails.
        :type window_preference: oci.database.models.WindowPreferenceDetail

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSchedulingWindowDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSchedulingWindowDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'window_preference': 'WindowPreferenceDetail',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'window_preference': 'windowPreference',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._window_preference = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def window_preference(self):
        """
        Gets the window_preference of this UpdateSchedulingWindowDetails.

        :return: The window_preference of this UpdateSchedulingWindowDetails.
        :rtype: oci.database.models.WindowPreferenceDetail
        """
        return self._window_preference

    @window_preference.setter
    def window_preference(self, window_preference):
        """
        Sets the window_preference of this UpdateSchedulingWindowDetails.

        :param window_preference: The window_preference of this UpdateSchedulingWindowDetails.
        :type: oci.database.models.WindowPreferenceDetail
        """
        self._window_preference = window_preference

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSchedulingWindowDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSchedulingWindowDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSchedulingWindowDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSchedulingWindowDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSchedulingWindowDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSchedulingWindowDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSchedulingWindowDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSchedulingWindowDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
