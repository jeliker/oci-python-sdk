# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaDownloadRecord(object):
    """
    A record of Java artifact download in a tenancy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JavaDownloadRecord object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param family_version:
            The value to assign to the family_version property of this JavaDownloadRecord.
        :type family_version: str

        :param family_display_name:
            The value to assign to the family_display_name property of this JavaDownloadRecord.
        :type family_display_name: str

        :param release_version:
            The value to assign to the release_version property of this JavaDownloadRecord.
        :type release_version: str

        :param os_family:
            The value to assign to the os_family property of this JavaDownloadRecord.
        :type os_family: str

        :param architecture:
            The value to assign to the architecture property of this JavaDownloadRecord.
        :type architecture: str

        :param package_type:
            The value to assign to the package_type property of this JavaDownloadRecord.
        :type package_type: str

        :param package_type_detail:
            The value to assign to the package_type_detail property of this JavaDownloadRecord.
        :type package_type_detail: str

        :param download_source_id:
            The value to assign to the download_source_id property of this JavaDownloadRecord.
        :type download_source_id: str

        :param time_downloaded:
            The value to assign to the time_downloaded property of this JavaDownloadRecord.
        :type time_downloaded: datetime

        :param download_type:
            The value to assign to the download_type property of this JavaDownloadRecord.
        :type download_type: str

        """
        self.swagger_types = {
            'family_version': 'str',
            'family_display_name': 'str',
            'release_version': 'str',
            'os_family': 'str',
            'architecture': 'str',
            'package_type': 'str',
            'package_type_detail': 'str',
            'download_source_id': 'str',
            'time_downloaded': 'datetime',
            'download_type': 'str'
        }
        self.attribute_map = {
            'family_version': 'familyVersion',
            'family_display_name': 'familyDisplayName',
            'release_version': 'releaseVersion',
            'os_family': 'osFamily',
            'architecture': 'architecture',
            'package_type': 'packageType',
            'package_type_detail': 'packageTypeDetail',
            'download_source_id': 'downloadSourceId',
            'time_downloaded': 'timeDownloaded',
            'download_type': 'downloadType'
        }
        self._family_version = None
        self._family_display_name = None
        self._release_version = None
        self._os_family = None
        self._architecture = None
        self._package_type = None
        self._package_type_detail = None
        self._download_source_id = None
        self._time_downloaded = None
        self._download_type = None

    @property
    def family_version(self):
        """
        Gets the family_version of this JavaDownloadRecord.
        The Java family version identifier.


        :return: The family_version of this JavaDownloadRecord.
        :rtype: str
        """
        return self._family_version

    @family_version.setter
    def family_version(self, family_version):
        """
        Sets the family_version of this JavaDownloadRecord.
        The Java family version identifier.


        :param family_version: The family_version of this JavaDownloadRecord.
        :type: str
        """
        self._family_version = family_version

    @property
    def family_display_name(self):
        """
        Gets the family_display_name of this JavaDownloadRecord.
        The Java family display name.


        :return: The family_display_name of this JavaDownloadRecord.
        :rtype: str
        """
        return self._family_display_name

    @family_display_name.setter
    def family_display_name(self, family_display_name):
        """
        Sets the family_display_name of this JavaDownloadRecord.
        The Java family display name.


        :param family_display_name: The family_display_name of this JavaDownloadRecord.
        :type: str
        """
        self._family_display_name = family_display_name

    @property
    def release_version(self):
        """
        Gets the release_version of this JavaDownloadRecord.
        The Java release version identifier.


        :return: The release_version of this JavaDownloadRecord.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """
        Sets the release_version of this JavaDownloadRecord.
        The Java release version identifier.


        :param release_version: The release_version of this JavaDownloadRecord.
        :type: str
        """
        self._release_version = release_version

    @property
    def os_family(self):
        """
        Gets the os_family of this JavaDownloadRecord.
        The target Operating System family for the artifact.


        :return: The os_family of this JavaDownloadRecord.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this JavaDownloadRecord.
        The target Operating System family for the artifact.


        :param os_family: The os_family of this JavaDownloadRecord.
        :type: str
        """
        self._os_family = os_family

    @property
    def architecture(self):
        """
        Gets the architecture of this JavaDownloadRecord.
        The target Operating System architecture for the artifact.


        :return: The architecture of this JavaDownloadRecord.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this JavaDownloadRecord.
        The target Operating System architecture for the artifact.


        :param architecture: The architecture of this JavaDownloadRecord.
        :type: str
        """
        self._architecture = architecture

    @property
    def package_type(self):
        """
        Gets the package_type of this JavaDownloadRecord.
        The package type (typically the file extension) of the artifact.


        :return: The package_type of this JavaDownloadRecord.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this JavaDownloadRecord.
        The package type (typically the file extension) of the artifact.


        :param package_type: The package_type of this JavaDownloadRecord.
        :type: str
        """
        self._package_type = package_type

    @property
    def package_type_detail(self):
        """
        Gets the package_type_detail of this JavaDownloadRecord.
        Additional information about the package type.


        :return: The package_type_detail of this JavaDownloadRecord.
        :rtype: str
        """
        return self._package_type_detail

    @package_type_detail.setter
    def package_type_detail(self, package_type_detail):
        """
        Sets the package_type_detail of this JavaDownloadRecord.
        Additional information about the package type.


        :param package_type_detail: The package_type_detail of this JavaDownloadRecord.
        :type: str
        """
        self._package_type_detail = package_type_detail

    @property
    def download_source_id(self):
        """
        **[Required]** Gets the download_source_id of this JavaDownloadRecord.
        Identifier of the source that downloaded the artifact.


        :return: The download_source_id of this JavaDownloadRecord.
        :rtype: str
        """
        return self._download_source_id

    @download_source_id.setter
    def download_source_id(self, download_source_id):
        """
        Sets the download_source_id of this JavaDownloadRecord.
        Identifier of the source that downloaded the artifact.


        :param download_source_id: The download_source_id of this JavaDownloadRecord.
        :type: str
        """
        self._download_source_id = download_source_id

    @property
    def time_downloaded(self):
        """
        **[Required]** Gets the time_downloaded of this JavaDownloadRecord.
        Timestamp of download.


        :return: The time_downloaded of this JavaDownloadRecord.
        :rtype: datetime
        """
        return self._time_downloaded

    @time_downloaded.setter
    def time_downloaded(self, time_downloaded):
        """
        Sets the time_downloaded of this JavaDownloadRecord.
        Timestamp of download.


        :param time_downloaded: The time_downloaded of this JavaDownloadRecord.
        :type: datetime
        """
        self._time_downloaded = time_downloaded

    @property
    def download_type(self):
        """
        **[Required]** Gets the download_type of this JavaDownloadRecord.
        Type of download.


        :return: The download_type of this JavaDownloadRecord.
        :rtype: str
        """
        return self._download_type

    @download_type.setter
    def download_type(self, download_type):
        """
        Sets the download_type of this JavaDownloadRecord.
        Type of download.


        :param download_type: The download_type of this JavaDownloadRecord.
        :type: str
        """
        self._download_type = download_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
