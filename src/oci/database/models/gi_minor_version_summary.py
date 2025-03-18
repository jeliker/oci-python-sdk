# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GiMinorVersionSummary(object):
    """
    The Oracle Grid Infrastructure (GI) minor version.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GiMinorVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this GiMinorVersionSummary.
        :type version: str

        :param grid_image_id:
            The value to assign to the grid_image_id property of this GiMinorVersionSummary.
        :type grid_image_id: str

        """
        self.swagger_types = {
            'version': 'str',
            'grid_image_id': 'str'
        }
        self.attribute_map = {
            'version': 'version',
            'grid_image_id': 'gridImageId'
        }
        self._version = None
        self._grid_image_id = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this GiMinorVersionSummary.
        A valid Oracle Grid Infrastructure (GI) software version.


        :return: The version of this GiMinorVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this GiMinorVersionSummary.
        A valid Oracle Grid Infrastructure (GI) software version.


        :param version: The version of this GiMinorVersionSummary.
        :type: str
        """
        self._version = version

    @property
    def grid_image_id(self):
        """
        Gets the grid_image_id of this GiMinorVersionSummary.
        Grid Infrastructure Image Id


        :return: The grid_image_id of this GiMinorVersionSummary.
        :rtype: str
        """
        return self._grid_image_id

    @grid_image_id.setter
    def grid_image_id(self, grid_image_id):
        """
        Sets the grid_image_id of this GiMinorVersionSummary.
        Grid Infrastructure Image Id


        :param grid_image_id: The grid_image_id of this GiMinorVersionSummary.
        :type: str
        """
        self._grid_image_id = grid_image_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
