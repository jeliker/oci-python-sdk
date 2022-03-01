# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddDataFilesDetails(object):
    """
    The details required to add data files or temp files to the tablespace.
    """

    #: A constant which can be used with the file_type property of a AddDataFilesDetails.
    #: This constant has a value of "DATAFILE"
    FILE_TYPE_DATAFILE = "DATAFILE"

    #: A constant which can be used with the file_type property of a AddDataFilesDetails.
    #: This constant has a value of "TEMPFILE"
    FILE_TYPE_TEMPFILE = "TEMPFILE"

    def __init__(self, **kwargs):
        """
        Initializes a new AddDataFilesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this AddDataFilesDetails.
        :type credential_details: oci.database_management.models.TablespaceAdminCredentialDetails

        :param file_type:
            The value to assign to the file_type property of this AddDataFilesDetails.
            Allowed values for this property are: "DATAFILE", "TEMPFILE"
        :type file_type: str

        :param data_files:
            The value to assign to the data_files property of this AddDataFilesDetails.
        :type data_files: list[str]

        :param file_count:
            The value to assign to the file_count property of this AddDataFilesDetails.
        :type file_count: int

        :param file_size:
            The value to assign to the file_size property of this AddDataFilesDetails.
        :type file_size: oci.database_management.models.TablespaceStorageSize

        :param is_reusable:
            The value to assign to the is_reusable property of this AddDataFilesDetails.
        :type is_reusable: bool

        :param is_auto_extensible:
            The value to assign to the is_auto_extensible property of this AddDataFilesDetails.
        :type is_auto_extensible: bool

        :param auto_extend_next_size:
            The value to assign to the auto_extend_next_size property of this AddDataFilesDetails.
        :type auto_extend_next_size: oci.database_management.models.TablespaceStorageSize

        :param auto_extend_max_size:
            The value to assign to the auto_extend_max_size property of this AddDataFilesDetails.
        :type auto_extend_max_size: oci.database_management.models.TablespaceStorageSize

        :param is_max_size_unlimited:
            The value to assign to the is_max_size_unlimited property of this AddDataFilesDetails.
        :type is_max_size_unlimited: bool

        """
        self.swagger_types = {
            'credential_details': 'TablespaceAdminCredentialDetails',
            'file_type': 'str',
            'data_files': 'list[str]',
            'file_count': 'int',
            'file_size': 'TablespaceStorageSize',
            'is_reusable': 'bool',
            'is_auto_extensible': 'bool',
            'auto_extend_next_size': 'TablespaceStorageSize',
            'auto_extend_max_size': 'TablespaceStorageSize',
            'is_max_size_unlimited': 'bool'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'file_type': 'fileType',
            'data_files': 'dataFiles',
            'file_count': 'fileCount',
            'file_size': 'fileSize',
            'is_reusable': 'isReusable',
            'is_auto_extensible': 'isAutoExtensible',
            'auto_extend_next_size': 'autoExtendNextSize',
            'auto_extend_max_size': 'autoExtendMaxSize',
            'is_max_size_unlimited': 'isMaxSizeUnlimited'
        }

        self._credential_details = None
        self._file_type = None
        self._data_files = None
        self._file_count = None
        self._file_size = None
        self._is_reusable = None
        self._is_auto_extensible = None
        self._auto_extend_next_size = None
        self._auto_extend_max_size = None
        self._is_max_size_unlimited = None

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this AddDataFilesDetails.

        :return: The credential_details of this AddDataFilesDetails.
        :rtype: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this AddDataFilesDetails.

        :param credential_details: The credential_details of this AddDataFilesDetails.
        :type: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def file_type(self):
        """
        **[Required]** Gets the file_type of this AddDataFilesDetails.
        Specifies whether the file is a data file or temp file.

        Allowed values for this property are: "DATAFILE", "TEMPFILE"


        :return: The file_type of this AddDataFilesDetails.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """
        Sets the file_type of this AddDataFilesDetails.
        Specifies whether the file is a data file or temp file.


        :param file_type: The file_type of this AddDataFilesDetails.
        :type: str
        """
        allowed_values = ["DATAFILE", "TEMPFILE"]
        if not value_allowed_none_or_none_sentinel(file_type, allowed_values):
            raise ValueError(
                "Invalid value for `file_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._file_type = file_type

    @property
    def data_files(self):
        """
        Gets the data_files of this AddDataFilesDetails.
        The list of data files or temp files added to the tablespace.


        :return: The data_files of this AddDataFilesDetails.
        :rtype: list[str]
        """
        return self._data_files

    @data_files.setter
    def data_files(self, data_files):
        """
        Sets the data_files of this AddDataFilesDetails.
        The list of data files or temp files added to the tablespace.


        :param data_files: The data_files of this AddDataFilesDetails.
        :type: list[str]
        """
        self._data_files = data_files

    @property
    def file_count(self):
        """
        Gets the file_count of this AddDataFilesDetails.
        The number of data files or temp files to be added for the tablespace. This is for Oracle Managed Files only.


        :return: The file_count of this AddDataFilesDetails.
        :rtype: int
        """
        return self._file_count

    @file_count.setter
    def file_count(self, file_count):
        """
        Sets the file_count of this AddDataFilesDetails.
        The number of data files or temp files to be added for the tablespace. This is for Oracle Managed Files only.


        :param file_count: The file_count of this AddDataFilesDetails.
        :type: int
        """
        self._file_count = file_count

    @property
    def file_size(self):
        """
        Gets the file_size of this AddDataFilesDetails.
        The size of each data file or temp file.


        :return: The file_size of this AddDataFilesDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """
        Sets the file_size of this AddDataFilesDetails.
        The size of each data file or temp file.


        :param file_size: The file_size of this AddDataFilesDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._file_size = file_size

    @property
    def is_reusable(self):
        """
        Gets the is_reusable of this AddDataFilesDetails.
        Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.


        :return: The is_reusable of this AddDataFilesDetails.
        :rtype: bool
        """
        return self._is_reusable

    @is_reusable.setter
    def is_reusable(self, is_reusable):
        """
        Sets the is_reusable of this AddDataFilesDetails.
        Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.


        :param is_reusable: The is_reusable of this AddDataFilesDetails.
        :type: bool
        """
        self._is_reusable = is_reusable

    @property
    def is_auto_extensible(self):
        """
        Gets the is_auto_extensible of this AddDataFilesDetails.
        Specifies whether the data file or temp file can be extended automatically.


        :return: The is_auto_extensible of this AddDataFilesDetails.
        :rtype: bool
        """
        return self._is_auto_extensible

    @is_auto_extensible.setter
    def is_auto_extensible(self, is_auto_extensible):
        """
        Sets the is_auto_extensible of this AddDataFilesDetails.
        Specifies whether the data file or temp file can be extended automatically.


        :param is_auto_extensible: The is_auto_extensible of this AddDataFilesDetails.
        :type: bool
        """
        self._is_auto_extensible = is_auto_extensible

    @property
    def auto_extend_next_size(self):
        """
        Gets the auto_extend_next_size of this AddDataFilesDetails.
        The size of the next increment of disk space to be allocated automatically when more extents are required.


        :return: The auto_extend_next_size of this AddDataFilesDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._auto_extend_next_size

    @auto_extend_next_size.setter
    def auto_extend_next_size(self, auto_extend_next_size):
        """
        Sets the auto_extend_next_size of this AddDataFilesDetails.
        The size of the next increment of disk space to be allocated automatically when more extents are required.


        :param auto_extend_next_size: The auto_extend_next_size of this AddDataFilesDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._auto_extend_next_size = auto_extend_next_size

    @property
    def auto_extend_max_size(self):
        """
        Gets the auto_extend_max_size of this AddDataFilesDetails.
        The maximum disk space allowed for automatic extension of the data files or temp files.


        :return: The auto_extend_max_size of this AddDataFilesDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._auto_extend_max_size

    @auto_extend_max_size.setter
    def auto_extend_max_size(self, auto_extend_max_size):
        """
        Sets the auto_extend_max_size of this AddDataFilesDetails.
        The maximum disk space allowed for automatic extension of the data files or temp files.


        :param auto_extend_max_size: The auto_extend_max_size of this AddDataFilesDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._auto_extend_max_size = auto_extend_max_size

    @property
    def is_max_size_unlimited(self):
        """
        Gets the is_max_size_unlimited of this AddDataFilesDetails.
        Specifies whether the disk space of the data file or temp file can be limited.


        :return: The is_max_size_unlimited of this AddDataFilesDetails.
        :rtype: bool
        """
        return self._is_max_size_unlimited

    @is_max_size_unlimited.setter
    def is_max_size_unlimited(self, is_max_size_unlimited):
        """
        Sets the is_max_size_unlimited of this AddDataFilesDetails.
        Specifies whether the disk space of the data file or temp file can be limited.


        :param is_max_size_unlimited: The is_max_size_unlimited of this AddDataFilesDetails.
        :type: bool
        """
        self._is_max_size_unlimited = is_max_size_unlimited

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other