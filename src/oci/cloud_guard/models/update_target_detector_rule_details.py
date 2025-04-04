# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetDetectorRuleDetails(object):
    """
    Parameters to update detector rule configuration details in a detector recipe attached to a target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetDetectorRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition_groups:
            The value to assign to the condition_groups property of this UpdateTargetDetectorRuleDetails.
        :type condition_groups: list[oci.cloud_guard.models.ConditionGroup]

        """
        self.swagger_types = {
            'condition_groups': 'list[ConditionGroup]'
        }
        self.attribute_map = {
            'condition_groups': 'conditionGroups'
        }
        self._condition_groups = None

    @property
    def condition_groups(self):
        """
        Gets the condition_groups of this UpdateTargetDetectorRuleDetails.
        Condition group corresponding to each compartment


        :return: The condition_groups of this UpdateTargetDetectorRuleDetails.
        :rtype: list[oci.cloud_guard.models.ConditionGroup]
        """
        return self._condition_groups

    @condition_groups.setter
    def condition_groups(self, condition_groups):
        """
        Sets the condition_groups of this UpdateTargetDetectorRuleDetails.
        Condition group corresponding to each compartment


        :param condition_groups: The condition_groups of this UpdateTargetDetectorRuleDetails.
        :type: list[oci.cloud_guard.models.ConditionGroup]
        """
        self._condition_groups = condition_groups

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
