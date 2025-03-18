# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserActionDetails(object):
    """
    User action details.
    This can be performed on a failed/paused task or action group.
    """

    #: A constant which can be used with the level property of a UserActionDetails.
    #: This constant has a value of "ACTION_GROUP"
    LEVEL_ACTION_GROUP = "ACTION_GROUP"

    #: A constant which can be used with the level property of a UserActionDetails.
    #: This constant has a value of "STEP_NAME"
    LEVEL_STEP_NAME = "STEP_NAME"

    #: A constant which can be used with the action property of a UserActionDetails.
    #: This constant has a value of "RETRY"
    ACTION_RETRY = "RETRY"

    #: A constant which can be used with the action property of a UserActionDetails.
    #: This constant has a value of "RESUME"
    ACTION_RESUME = "RESUME"

    def __init__(self, **kwargs):
        """
        Initializes a new UserActionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_apps_management.models.StepBasedUserActionDetails`
        * :class:`~oci.fleet_apps_management.models.ActionGroupBasedUserActionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level:
            The value to assign to the level property of this UserActionDetails.
            Allowed values for this property are: "ACTION_GROUP", "STEP_NAME"
        :type level: str

        :param action:
            The value to assign to the action property of this UserActionDetails.
            Allowed values for this property are: "RETRY", "RESUME"
        :type action: str

        """
        self.swagger_types = {
            'level': 'str',
            'action': 'str'
        }
        self.attribute_map = {
            'level': 'level',
            'action': 'action'
        }
        self._level = None
        self._action = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['level']

        if type == 'STEP_NAME':
            return 'StepBasedUserActionDetails'

        if type == 'ACTION_GROUP':
            return 'ActionGroupBasedUserActionDetails'
        else:
            return 'UserActionDetails'

    @property
    def level(self):
        """
        **[Required]** Gets the level of this UserActionDetails.
        User action based On.

        Allowed values for this property are: "ACTION_GROUP", "STEP_NAME"


        :return: The level of this UserActionDetails.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this UserActionDetails.
        User action based On.


        :param level: The level of this UserActionDetails.
        :type: str
        """
        allowed_values = ["ACTION_GROUP", "STEP_NAME"]
        if not value_allowed_none_or_none_sentinel(level, allowed_values):
            raise ValueError(
                f"Invalid value for `level`, must be None or one of {allowed_values}"
            )
        self._level = level

    @property
    def action(self):
        """
        **[Required]** Gets the action of this UserActionDetails.
        Action to be Performed.

        Allowed values for this property are: "RETRY", "RESUME"


        :return: The action of this UserActionDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this UserActionDetails.
        Action to be Performed.


        :param action: The action of this UserActionDetails.
        :type: str
        """
        allowed_values = ["RETRY", "RESUME"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                f"Invalid value for `action`, must be None or one of {allowed_values}"
            )
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
