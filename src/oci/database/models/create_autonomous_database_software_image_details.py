# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDatabaseSoftwareImageDetails(object):
    """
    Parameters for creating a Autonomous Database Software Image
    """

    #: A constant which can be used with the image_shape_family property of a CreateAutonomousDatabaseSoftwareImageDetails.
    #: This constant has a value of "EXADATA_SHAPE"
    IMAGE_SHAPE_FAMILY_EXADATA_SHAPE = "EXADATA_SHAPE"

    #: A constant which can be used with the image_shape_family property of a CreateAutonomousDatabaseSoftwareImageDetails.
    #: This constant has a value of "EXACC_SHAPE"
    IMAGE_SHAPE_FAMILY_EXACC_SHAPE = "EXACC_SHAPE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDatabaseSoftwareImageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type display_name: str

        :param source_cdb_id:
            The value to assign to the source_cdb_id property of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type source_cdb_id: str

        :param image_shape_family:
            The value to assign to the image_shape_family property of this CreateAutonomousDatabaseSoftwareImageDetails.
            Allowed values for this property are: "EXADATA_SHAPE", "EXACC_SHAPE"
        :type image_shape_family: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'source_cdb_id': 'str',
            'image_shape_family': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'source_cdb_id': 'sourceCdbId',
            'image_shape_family': 'imageShapeFamily',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._compartment_id = None
        self._display_name = None
        self._source_cdb_id = None
        self._image_shape_family = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAutonomousDatabaseSoftwareImageDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAutonomousDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAutonomousDatabaseSoftwareImageDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAutonomousDatabaseSoftwareImageDetails.
        The user-friendly name for the Autonomous Database Software Image. The name does not have to be unique.


        :return: The display_name of this CreateAutonomousDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutonomousDatabaseSoftwareImageDetails.
        The user-friendly name for the Autonomous Database Software Image. The name does not have to be unique.


        :param display_name: The display_name of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def source_cdb_id(self):
        """
        **[Required]** Gets the source_cdb_id of this CreateAutonomousDatabaseSoftwareImageDetails.
        The source Autonomous Container Database `OCID`__ from which to create Autonomous Database Software Image.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_cdb_id of this CreateAutonomousDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._source_cdb_id

    @source_cdb_id.setter
    def source_cdb_id(self, source_cdb_id):
        """
        Sets the source_cdb_id of this CreateAutonomousDatabaseSoftwareImageDetails.
        The source Autonomous Container Database `OCID`__ from which to create Autonomous Database Software Image.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_cdb_id: The source_cdb_id of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type: str
        """
        self._source_cdb_id = source_cdb_id

    @property
    def image_shape_family(self):
        """
        **[Required]** Gets the image_shape_family of this CreateAutonomousDatabaseSoftwareImageDetails.
        To what shape the image is meant for.

        Allowed values for this property are: "EXADATA_SHAPE", "EXACC_SHAPE"


        :return: The image_shape_family of this CreateAutonomousDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._image_shape_family

    @image_shape_family.setter
    def image_shape_family(self, image_shape_family):
        """
        Sets the image_shape_family of this CreateAutonomousDatabaseSoftwareImageDetails.
        To what shape the image is meant for.


        :param image_shape_family: The image_shape_family of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type: str
        """
        allowed_values = ["EXADATA_SHAPE", "EXACC_SHAPE"]
        if not value_allowed_none_or_none_sentinel(image_shape_family, allowed_values):
            raise ValueError(
                f"Invalid value for `image_shape_family`, must be None or one of {allowed_values}"
            )
        self._image_shape_family = image_shape_family

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAutonomousDatabaseSoftwareImageDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAutonomousDatabaseSoftwareImageDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAutonomousDatabaseSoftwareImageDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAutonomousDatabaseSoftwareImageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAutonomousDatabaseSoftwareImageDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAutonomousDatabaseSoftwareImageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAutonomousDatabaseSoftwareImageDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
