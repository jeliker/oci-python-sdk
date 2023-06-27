# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagedInstanceGroupDetails(object):
    """
    The information about new managed instance group.
    """

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the vendor_name property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateManagedInstanceGroupDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateManagedInstanceGroupDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateManagedInstanceGroupDetails.
        :type compartment_id: str

        :param os_family:
            The value to assign to the os_family property of this CreateManagedInstanceGroupDetails.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this CreateManagedInstanceGroupDetails.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"
        :type arch_type: str

        :param vendor_name:
            The value to assign to the vendor_name property of this CreateManagedInstanceGroupDetails.
            Allowed values for this property are: "ORACLE"
        :type vendor_name: str

        :param software_source_ids:
            The value to assign to the software_source_ids property of this CreateManagedInstanceGroupDetails.
        :type software_source_ids: list[str]

        :param managed_instance_ids:
            The value to assign to the managed_instance_ids property of this CreateManagedInstanceGroupDetails.
        :type managed_instance_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateManagedInstanceGroupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateManagedInstanceGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'vendor_name': 'str',
            'software_source_ids': 'list[str]',
            'managed_instance_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'vendor_name': 'vendorName',
            'software_source_ids': 'softwareSourceIds',
            'managed_instance_ids': 'managedInstanceIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._os_family = None
        self._arch_type = None
        self._vendor_name = None
        self._software_source_ids = None
        self._managed_instance_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateManagedInstanceGroupDetails.
        A user-friendly name for the managed instance group. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateManagedInstanceGroupDetails.
        A user-friendly name for the managed instance group. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateManagedInstanceGroupDetails.
        Details about the managed instance group.


        :return: The description of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateManagedInstanceGroupDetails.
        Details about the managed instance group.


        :param description: The description of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateManagedInstanceGroupDetails.
        The OCID of the tenancy containing the managed instance group.


        :return: The compartment_id of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateManagedInstanceGroupDetails.
        The OCID of the tenancy containing the managed instance group.


        :param compartment_id: The compartment_id of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this CreateManagedInstanceGroupDetails.
        The operating system type of the managed instance(s) that this managed instance group will contain.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"


        :return: The os_family of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this CreateManagedInstanceGroupDetails.
        The operating system type of the managed instance(s) that this managed instance group will contain.


        :param os_family: The os_family of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            raise ValueError(
                "Invalid value for `os_family`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this CreateManagedInstanceGroupDetails.
        The CPU architecture type of the managed instance(s) that this managed instance group will contain.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"


        :return: The arch_type of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this CreateManagedInstanceGroupDetails.
        The CPU architecture type of the managed instance(s) that this managed instance group will contain.


        :param arch_type: The arch_type of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            raise ValueError(
                "Invalid value for `arch_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._arch_type = arch_type

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this CreateManagedInstanceGroupDetails.
        The software source vendor name.

        Allowed values for this property are: "ORACLE"


        :return: The vendor_name of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this CreateManagedInstanceGroupDetails.
        The software source vendor name.


        :param vendor_name: The vendor_name of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        allowed_values = ["ORACLE"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            raise ValueError(
                "Invalid value for `vendor_name`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._vendor_name = vendor_name

    @property
    def software_source_ids(self):
        """
        **[Required]** Gets the software_source_ids of this CreateManagedInstanceGroupDetails.
        The list of software source OCIDs available to the managed instances in the managed instance group.


        :return: The software_source_ids of this CreateManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this CreateManagedInstanceGroupDetails.
        The list of software source OCIDs available to the managed instances in the managed instance group.


        :param software_source_ids: The software_source_ids of this CreateManagedInstanceGroupDetails.
        :type: list[str]
        """
        self._software_source_ids = software_source_ids

    @property
    def managed_instance_ids(self):
        """
        Gets the managed_instance_ids of this CreateManagedInstanceGroupDetails.
        The list of managed instance OCIDs to be added to the managed instance group.


        :return: The managed_instance_ids of this CreateManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._managed_instance_ids

    @managed_instance_ids.setter
    def managed_instance_ids(self, managed_instance_ids):
        """
        Sets the managed_instance_ids of this CreateManagedInstanceGroupDetails.
        The list of managed instance OCIDs to be added to the managed instance group.


        :param managed_instance_ids: The managed_instance_ids of this CreateManagedInstanceGroupDetails.
        :type: list[str]
        """
        self._managed_instance_ids = managed_instance_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateManagedInstanceGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateManagedInstanceGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateManagedInstanceGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateManagedInstanceGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateManagedInstanceGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateManagedInstanceGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateManagedInstanceGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateManagedInstanceGroupDetails.
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
