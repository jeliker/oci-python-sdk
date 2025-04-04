# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceMovableFileSystemOperation(object):
    """
    The details of operations performed on a file system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceMovableFileSystemOperation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_path:
            The value to assign to the export_path property of this ComputeInstanceMovableFileSystemOperation.
        :type export_path: str

        :param mount_point:
            The value to assign to the mount_point property of this ComputeInstanceMovableFileSystemOperation.
        :type mount_point: str

        :param mount_details:
            The value to assign to the mount_details property of this ComputeInstanceMovableFileSystemOperation.
        :type mount_details: oci.disaster_recovery.models.FileSystemMountDetails

        :param unmount_details:
            The value to assign to the unmount_details property of this ComputeInstanceMovableFileSystemOperation.
        :type unmount_details: oci.disaster_recovery.models.FileSystemUnmountDetails

        """
        self.swagger_types = {
            'export_path': 'str',
            'mount_point': 'str',
            'mount_details': 'FileSystemMountDetails',
            'unmount_details': 'FileSystemUnmountDetails'
        }
        self.attribute_map = {
            'export_path': 'exportPath',
            'mount_point': 'mountPoint',
            'mount_details': 'mountDetails',
            'unmount_details': 'unmountDetails'
        }
        self._export_path = None
        self._mount_point = None
        self._mount_details = None
        self._unmount_details = None

    @property
    def export_path(self):
        """
        **[Required]** Gets the export_path of this ComputeInstanceMovableFileSystemOperation.
        The export path of the file system.

        Example: `/fs-export-path`


        :return: The export_path of this ComputeInstanceMovableFileSystemOperation.
        :rtype: str
        """
        return self._export_path

    @export_path.setter
    def export_path(self, export_path):
        """
        Sets the export_path of this ComputeInstanceMovableFileSystemOperation.
        The export path of the file system.

        Example: `/fs-export-path`


        :param export_path: The export_path of this ComputeInstanceMovableFileSystemOperation.
        :type: str
        """
        self._export_path = export_path

    @property
    def mount_point(self):
        """
        **[Required]** Gets the mount_point of this ComputeInstanceMovableFileSystemOperation.
        The physical mount point of the file system on a host.

        Example: `/mnt/yourmountpoint`


        :return: The mount_point of this ComputeInstanceMovableFileSystemOperation.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """
        Sets the mount_point of this ComputeInstanceMovableFileSystemOperation.
        The physical mount point of the file system on a host.

        Example: `/mnt/yourmountpoint`


        :param mount_point: The mount_point of this ComputeInstanceMovableFileSystemOperation.
        :type: str
        """
        self._mount_point = mount_point

    @property
    def mount_details(self):
        """
        **[Required]** Gets the mount_details of this ComputeInstanceMovableFileSystemOperation.

        :return: The mount_details of this ComputeInstanceMovableFileSystemOperation.
        :rtype: oci.disaster_recovery.models.FileSystemMountDetails
        """
        return self._mount_details

    @mount_details.setter
    def mount_details(self, mount_details):
        """
        Sets the mount_details of this ComputeInstanceMovableFileSystemOperation.

        :param mount_details: The mount_details of this ComputeInstanceMovableFileSystemOperation.
        :type: oci.disaster_recovery.models.FileSystemMountDetails
        """
        self._mount_details = mount_details

    @property
    def unmount_details(self):
        """
        **[Required]** Gets the unmount_details of this ComputeInstanceMovableFileSystemOperation.

        :return: The unmount_details of this ComputeInstanceMovableFileSystemOperation.
        :rtype: oci.disaster_recovery.models.FileSystemUnmountDetails
        """
        return self._unmount_details

    @unmount_details.setter
    def unmount_details(self, unmount_details):
        """
        Sets the unmount_details of this ComputeInstanceMovableFileSystemOperation.

        :param unmount_details: The unmount_details of this ComputeInstanceMovableFileSystemOperation.
        :type: oci.disaster_recovery.models.FileSystemUnmountDetails
        """
        self._unmount_details = unmount_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
