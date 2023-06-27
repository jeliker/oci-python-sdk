# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlCpuActivity(object):
    """
    The SQL CPU activity from the Exadata storage server.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlCpuActivity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_name:
            The value to assign to the database_name property of this SqlCpuActivity.
        :type database_name: str

        :param sql_id:
            The value to assign to the sql_id property of this SqlCpuActivity.
        :type sql_id: str

        :param cpu_activity:
            The value to assign to the cpu_activity property of this SqlCpuActivity.
        :type cpu_activity: float

        """
        self.swagger_types = {
            'database_name': 'str',
            'sql_id': 'str',
            'cpu_activity': 'float'
        }

        self.attribute_map = {
            'database_name': 'databaseName',
            'sql_id': 'sqlId',
            'cpu_activity': 'cpuActivity'
        }

        self._database_name = None
        self._sql_id = None
        self._cpu_activity = None

    @property
    def database_name(self):
        """
        Gets the database_name of this SqlCpuActivity.
        The database name.


        :return: The database_name of this SqlCpuActivity.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this SqlCpuActivity.
        The database name.


        :param database_name: The database_name of this SqlCpuActivity.
        :type: str
        """
        self._database_name = database_name

    @property
    def sql_id(self):
        """
        Gets the sql_id of this SqlCpuActivity.
        The SQL ID.


        :return: The sql_id of this SqlCpuActivity.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        """
        Sets the sql_id of this SqlCpuActivity.
        The SQL ID.


        :param sql_id: The sql_id of this SqlCpuActivity.
        :type: str
        """
        self._sql_id = sql_id

    @property
    def cpu_activity(self):
        """
        Gets the cpu_activity of this SqlCpuActivity.
        The CPU activity percentage.


        :return: The cpu_activity of this SqlCpuActivity.
        :rtype: float
        """
        return self._cpu_activity

    @cpu_activity.setter
    def cpu_activity(self, cpu_activity):
        """
        Sets the cpu_activity of this SqlCpuActivity.
        The CPU activity percentage.


        :param cpu_activity: The cpu_activity of this SqlCpuActivity.
        :type: float
        """
        self._cpu_activity = cpu_activity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
