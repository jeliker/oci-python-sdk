# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceAnalyticSummary(object):
    """
    A metric emitted by managed instance resource.
    """

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "TOTAL_INSTANCE_COUNT"
    NAME_TOTAL_INSTANCE_COUNT = "TOTAL_INSTANCE_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT"
    NAME_INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT = "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT"
    NAME_INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT = "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "NORMAL_INSTANCE_COUNT"
    NAME_NORMAL_INSTANCE_COUNT = "NORMAL_INSTANCE_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "ERROR_INSTANCE_COUNT"
    NAME_ERROR_INSTANCE_COUNT = "ERROR_INSTANCE_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "WARNING_INSTANCE_COUNT"
    NAME_WARNING_INSTANCE_COUNT = "WARNING_INSTANCE_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "UNREACHABLE_INSTANCE_COUNT"
    NAME_UNREACHABLE_INSTANCE_COUNT = "UNREACHABLE_INSTANCE_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "REGISTRATION_FAILED_INSTANCE_COUNT"
    NAME_REGISTRATION_FAILED_INSTANCE_COUNT = "REGISTRATION_FAILED_INSTANCE_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "INSTANCE_SECURITY_UPDATES_COUNT"
    NAME_INSTANCE_SECURITY_UPDATES_COUNT = "INSTANCE_SECURITY_UPDATES_COUNT"

    #: A constant which can be used with the name property of a ManagedInstanceAnalyticSummary.
    #: This constant has a value of "INSTANCE_BUGFIX_UPDATES_COUNT"
    NAME_INSTANCE_BUGFIX_UPDATES_COUNT = "INSTANCE_BUGFIX_UPDATES_COUNT"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceAnalyticSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ManagedInstanceAnalyticSummary.
            Allowed values for this property are: "TOTAL_INSTANCE_COUNT", "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT", "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT", "NORMAL_INSTANCE_COUNT", "ERROR_INSTANCE_COUNT", "WARNING_INSTANCE_COUNT", "UNREACHABLE_INSTANCE_COUNT", "REGISTRATION_FAILED_INSTANCE_COUNT", "INSTANCE_SECURITY_UPDATES_COUNT", "INSTANCE_BUGFIX_UPDATES_COUNT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param dimensions:
            The value to assign to the dimensions property of this ManagedInstanceAnalyticSummary.
        :type dimensions: dict(str, str)

        :param count:
            The value to assign to the count property of this ManagedInstanceAnalyticSummary.
        :type count: int

        """
        self.swagger_types = {
            'name': 'str',
            'dimensions': 'dict(str, str)',
            'count': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'dimensions': 'dimensions',
            'count': 'count'
        }

        self._name = None
        self._dimensions = None
        self._count = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedInstanceAnalyticSummary.
        The name of this metric.

        Allowed values for this property are: "TOTAL_INSTANCE_COUNT", "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT", "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT", "NORMAL_INSTANCE_COUNT", "ERROR_INSTANCE_COUNT", "WARNING_INSTANCE_COUNT", "UNREACHABLE_INSTANCE_COUNT", "REGISTRATION_FAILED_INSTANCE_COUNT", "INSTANCE_SECURITY_UPDATES_COUNT", "INSTANCE_BUGFIX_UPDATES_COUNT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this ManagedInstanceAnalyticSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedInstanceAnalyticSummary.
        The name of this metric.


        :param name: The name of this ManagedInstanceAnalyticSummary.
        :type: str
        """
        allowed_values = ["TOTAL_INSTANCE_COUNT", "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT", "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT", "NORMAL_INSTANCE_COUNT", "ERROR_INSTANCE_COUNT", "WARNING_INSTANCE_COUNT", "UNREACHABLE_INSTANCE_COUNT", "REGISTRATION_FAILED_INSTANCE_COUNT", "INSTANCE_SECURITY_UPDATES_COUNT", "INSTANCE_BUGFIX_UPDATES_COUNT"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def dimensions(self):
        """
        **[Required]** Gets the dimensions of this ManagedInstanceAnalyticSummary.
        Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.
        Each dimension takes the form of a key-value pair.

        Example: `\"managedInstanceId\": \"ocid1.managementagent.123\"`


        :return: The dimensions of this ManagedInstanceAnalyticSummary.
        :rtype: dict(str, str)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this ManagedInstanceAnalyticSummary.
        Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.
        Each dimension takes the form of a key-value pair.

        Example: `\"managedInstanceId\": \"ocid1.managementagent.123\"`


        :param dimensions: The dimensions of this ManagedInstanceAnalyticSummary.
        :type: dict(str, str)
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """
        **[Required]** Gets the count of this ManagedInstanceAnalyticSummary.
        The value of this metric.


        :return: The count of this ManagedInstanceAnalyticSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ManagedInstanceAnalyticSummary.
        The value of this metric.


        :param count: The count of this ManagedInstanceAnalyticSummary.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
