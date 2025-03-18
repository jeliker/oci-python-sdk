# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportPackageDetails(object):
    """
    The model for the parameters needed to export a listing.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExportPackageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ExportPackageDetails.
        :type compartment_id: str

        :param container_repository_path:
            The value to assign to the container_repository_path property of this ExportPackageDetails.
        :type container_repository_path: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'container_repository_path': 'str'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'container_repository_path': 'containerRepositoryPath'
        }
        self._compartment_id = None
        self._container_repository_path = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExportPackageDetails.
        The `OCID`__ of the compartment where you want to export container image or helm chart.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExportPackageDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExportPackageDetails.
        The `OCID`__ of the compartment where you want to export container image or helm chart.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExportPackageDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def container_repository_path(self):
        """
        **[Required]** Gets the container_repository_path of this ExportPackageDetails.
        The repository path (/Content/General/Concepts/identifiers.htm) of the container reposistory where the container image or helm chart should be exported.


        :return: The container_repository_path of this ExportPackageDetails.
        :rtype: str
        """
        return self._container_repository_path

    @container_repository_path.setter
    def container_repository_path(self, container_repository_path):
        """
        Sets the container_repository_path of this ExportPackageDetails.
        The repository path (/Content/General/Concepts/identifiers.htm) of the container reposistory where the container image or helm chart should be exported.


        :param container_repository_path: The container_repository_path of this ExportPackageDetails.
        :type: str
        """
        self._container_repository_path = container_repository_path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
