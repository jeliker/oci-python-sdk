# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedDatabaseSummary(object):
    """
    Summary of a Database currently using a Private Endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AssociatedDatabaseSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this AssociatedDatabaseSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AssociatedDatabaseSummary.
        :type compartment_id: str

        :param time_registered:
            The value to assign to the time_registered property of this AssociatedDatabaseSummary.
        :type time_registered: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'time_registered': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'time_registered': 'timeRegistered'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._time_registered = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AssociatedDatabaseSummary.
        The OCID of the database.


        :return: The id of this AssociatedDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssociatedDatabaseSummary.
        The OCID of the database.


        :param id: The id of this AssociatedDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AssociatedDatabaseSummary.
        The name of the database.


        :return: The name of this AssociatedDatabaseSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssociatedDatabaseSummary.
        The name of the database.


        :param name: The name of this AssociatedDatabaseSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AssociatedDatabaseSummary.
        The compartment ID of the database.


        :return: The compartment_id of this AssociatedDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AssociatedDatabaseSummary.
        The compartment ID of the database.


        :param compartment_id: The compartment_id of this AssociatedDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_registered(self):
        """
        **[Required]** Gets the time_registered of this AssociatedDatabaseSummary.
        The time when the database was registered for Database Management.


        :return: The time_registered of this AssociatedDatabaseSummary.
        :rtype: datetime
        """
        return self._time_registered

    @time_registered.setter
    def time_registered(self, time_registered):
        """
        Sets the time_registered of this AssociatedDatabaseSummary.
        The time when the database was registered for Database Management.


        :param time_registered: The time_registered of this AssociatedDatabaseSummary.
        :type: datetime
        """
        self._time_registered = time_registered

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
