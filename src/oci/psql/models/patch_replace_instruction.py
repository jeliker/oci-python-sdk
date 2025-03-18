# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915

from .patch_instruction import PatchInstruction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchReplaceInstruction(PatchInstruction):
    """
    An operation that \"puts\" a value, replacing every item of the selection with it, or creating it if the selection is empty.
    NOT_FOUND exceptions are handled by creating the implied containing structure (but note that this may put the target in an invalid state,
    which can be prevented by use of precondition operations).
    To avoid referential errors if an item's descendant is also in the selection, items of the selection are processed in order of decreasing depth.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchReplaceInstruction object with values from keyword arguments. The default value of the :py:attr:`~oci.psql.models.PatchReplaceInstruction.operation` attribute
        of this class is ``REPLACE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PatchReplaceInstruction.
            Allowed values for this property are: "REQUIRE", "PROHIBIT", "REPLACE", "INSERT", "REMOVE", "MOVE", "MERGE"
        :type operation: str

        :param selection:
            The value to assign to the selection property of this PatchReplaceInstruction.
        :type selection: str

        :param value:
            The value to assign to the value property of this PatchReplaceInstruction.
        :type value: object

        """
        self.swagger_types = {
            'operation': 'str',
            'selection': 'str',
            'value': 'object'
        }
        self.attribute_map = {
            'operation': 'operation',
            'selection': 'selection',
            'value': 'value'
        }
        self._operation = None
        self._selection = None
        self._value = None
        self._operation = 'REPLACE'

    @property
    def value(self):
        """
        **[Required]** Gets the value of this PatchReplaceInstruction.
        A value to be added into the target.


        :return: The value of this PatchReplaceInstruction.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PatchReplaceInstruction.
        A value to be added into the target.


        :param value: The value of this PatchReplaceInstruction.
        :type: object
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
