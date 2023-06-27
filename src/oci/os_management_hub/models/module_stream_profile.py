# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStreamProfile(object):
    """
    A module stream profile provided by a software source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStreamProfile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStreamProfile.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this ModuleStreamProfile.
        :type stream_name: str

        :param name:
            The value to assign to the name property of this ModuleStreamProfile.
        :type name: str

        :param is_default:
            The value to assign to the is_default property of this ModuleStreamProfile.
        :type is_default: bool

        :param description:
            The value to assign to the description property of this ModuleStreamProfile.
        :type description: str

        :param packages:
            The value to assign to the packages property of this ModuleStreamProfile.
        :type packages: list[str]

        """
        self.swagger_types = {
            'module_name': 'str',
            'stream_name': 'str',
            'name': 'str',
            'is_default': 'bool',
            'description': 'str',
            'packages': 'list[str]'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'stream_name': 'streamName',
            'name': 'name',
            'is_default': 'isDefault',
            'description': 'description',
            'packages': 'packages'
        }

        self._module_name = None
        self._stream_name = None
        self._name = None
        self._is_default = None
        self._description = None
        self._packages = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStreamProfile.
        The name of the module that contains the stream profile.


        :return: The module_name of this ModuleStreamProfile.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStreamProfile.
        The name of the module that contains the stream profile.


        :param module_name: The module_name of this ModuleStreamProfile.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this ModuleStreamProfile.
        The name of the stream that contains the profile.


        :return: The stream_name of this ModuleStreamProfile.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ModuleStreamProfile.
        The name of the stream that contains the profile.


        :param stream_name: The stream_name of this ModuleStreamProfile.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ModuleStreamProfile.
        The name of the profile.


        :return: The name of this ModuleStreamProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModuleStreamProfile.
        The name of the profile.


        :param name: The name of this ModuleStreamProfile.
        :type: str
        """
        self._name = name

    @property
    def is_default(self):
        """
        Gets the is_default of this ModuleStreamProfile.
        Indicates if this profile is the default for its module stream.


        :return: The is_default of this ModuleStreamProfile.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this ModuleStreamProfile.
        Indicates if this profile is the default for its module stream.


        :param is_default: The is_default of this ModuleStreamProfile.
        :type: bool
        """
        self._is_default = is_default

    @property
    def description(self):
        """
        Gets the description of this ModuleStreamProfile.
        A description of the contents of the module stream profile.


        :return: The description of this ModuleStreamProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ModuleStreamProfile.
        A description of the contents of the module stream profile.


        :param description: The description of this ModuleStreamProfile.
        :type: str
        """
        self._description = description

    @property
    def packages(self):
        """
        **[Required]** Gets the packages of this ModuleStreamProfile.
        A list of packages that constitute the profile.  Each element
        in the list is the name of a package.  The name is suitable to
        use as an argument to other OS Management Hub APIs that interact
        directly with packages.


        :return: The packages of this ModuleStreamProfile.
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this ModuleStreamProfile.
        A list of packages that constitute the profile.  Each element
        in the list is the name of a package.  The name is suitable to
        use as an argument to other OS Management Hub APIs that interact
        directly with packages.


        :param packages: The packages of this ModuleStreamProfile.
        :type: list[str]
        """
        self._packages = packages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
