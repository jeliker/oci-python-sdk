# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertPolicyRule(object):
    """
    A rule associated with a alert policy.
    """

    #: A constant which can be used with the lifecycle_state property of a AlertPolicyRule.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicyRule.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicyRule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicyRule.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AlertPolicyRule.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AlertPolicyRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this AlertPolicyRule.
        :type key: str

        :param description:
            The value to assign to the description property of this AlertPolicyRule.
        :type description: str

        :param expression:
            The value to assign to the expression property of this AlertPolicyRule.
        :type expression: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AlertPolicyRule.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this AlertPolicyRule.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this AlertPolicyRule.
        :type time_created: datetime

        """
        self.swagger_types = {
            'key': 'str',
            'description': 'str',
            'expression': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'key': 'key',
            'description': 'description',
            'expression': 'expression',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'time_created': 'timeCreated'
        }

        self._key = None
        self._description = None
        self._expression = None
        self._lifecycle_state = None
        self._display_name = None
        self._time_created = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this AlertPolicyRule.
        The unique key of the alert policy rule.


        :return: The key of this AlertPolicyRule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AlertPolicyRule.
        The unique key of the alert policy rule.


        :param key: The key of this AlertPolicyRule.
        :type: str
        """
        self._key = key

    @property
    def description(self):
        """
        Gets the description of this AlertPolicyRule.
        Describes the alert policy rule.


        :return: The description of this AlertPolicyRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AlertPolicyRule.
        Describes the alert policy rule.


        :param description: The description of this AlertPolicyRule.
        :type: str
        """
        self._description = description

    @property
    def expression(self):
        """
        **[Required]** Gets the expression of this AlertPolicyRule.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :return: The expression of this AlertPolicyRule.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this AlertPolicyRule.
        The conditional expression of the alert policy rule which evaluates to boolean value.


        :param expression: The expression of this AlertPolicyRule.
        :type: str
        """
        self._expression = expression

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AlertPolicyRule.
        The current state of the alert policy rule.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AlertPolicyRule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AlertPolicyRule.
        The current state of the alert policy rule.


        :param lifecycle_state: The lifecycle_state of this AlertPolicyRule.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        Gets the display_name of this AlertPolicyRule.
        The display name of the alert policy rule.


        :return: The display_name of this AlertPolicyRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AlertPolicyRule.
        The display name of the alert policy rule.


        :param display_name: The display_name of this AlertPolicyRule.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this AlertPolicyRule.
        Creation date and time of the alert policy rule, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AlertPolicyRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AlertPolicyRule.
        Creation date and time of the alert policy rule, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AlertPolicyRule.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
