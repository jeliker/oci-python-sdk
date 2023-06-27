# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopSqlCpuActivity(object):
    """
    A list of SQL IDs with most CPU activity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TopSqlCpuActivity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param activity:
            The value to assign to the activity property of this TopSqlCpuActivity.
        :type activity: list[oci.database_management.models.SqlCpuActivity]

        """
        self.swagger_types = {
            'activity': 'list[SqlCpuActivity]'
        }

        self.attribute_map = {
            'activity': 'activity'
        }

        self._activity = None

    @property
    def activity(self):
        """
        **[Required]** Gets the activity of this TopSqlCpuActivity.
        A list of sql CPU activity.


        :return: The activity of this TopSqlCpuActivity.
        :rtype: list[oci.database_management.models.SqlCpuActivity]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """
        Sets the activity of this TopSqlCpuActivity.
        A list of sql CPU activity.


        :param activity: The activity of this TopSqlCpuActivity.
        :type: list[oci.database_management.models.SqlCpuActivity]
        """
        self._activity = activity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
