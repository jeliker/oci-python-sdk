# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Level(object):
    """
    An object used to represent a level at which a property or resource or constraint is defined.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Level object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Level.
        :type name: str

        :param constraints:
            The value to assign to the constraints property of this Level.
        :type constraints: str

        """
        self.swagger_types = {
            'name': 'str',
            'constraints': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'constraints': 'constraints'
        }

        self._name = None
        self._constraints = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Level.
        The level name.


        :return: The name of this Level.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Level.
        The level name.


        :param name: The name of this Level.
        :type: str
        """
        self._name = name

    @property
    def constraints(self):
        """
        Gets the constraints of this Level.
        A string representation of constraints that apply at this level.
        For example, a property defined at SOURCE level could further be applicable only for SOURCE_TYPE:database_sql.


        :return: The constraints of this Level.
        :rtype: str
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """
        Sets the constraints of this Level.
        A string representation of constraints that apply at this level.
        For example, a property defined at SOURCE level could further be applicable only for SOURCE_TYPE:database_sql.


        :param constraints: The constraints of this Level.
        :type: str
        """
        self._constraints = constraints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other