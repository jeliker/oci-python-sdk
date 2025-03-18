# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .event_content import EventContent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KernelEventContent(EventContent):
    """
    Provides information collected for the kernel event.
    """

    #: A constant which can be used with the content_availability property of a KernelEventContent.
    #: This constant has a value of "NOT_AVAILABLE"
    CONTENT_AVAILABILITY_NOT_AVAILABLE = "NOT_AVAILABLE"

    #: A constant which can be used with the content_availability property of a KernelEventContent.
    #: This constant has a value of "AVAILABLE_ON_INSTANCE"
    CONTENT_AVAILABILITY_AVAILABLE_ON_INSTANCE = "AVAILABLE_ON_INSTANCE"

    #: A constant which can be used with the content_availability property of a KernelEventContent.
    #: This constant has a value of "AVAILABLE_ON_SERVICE"
    CONTENT_AVAILABILITY_AVAILABLE_ON_SERVICE = "AVAILABLE_ON_SERVICE"

    #: A constant which can be used with the content_availability property of a KernelEventContent.
    #: This constant has a value of "AVAILABLE_ON_INSTANCE_AND_SERVICE"
    CONTENT_AVAILABILITY_AVAILABLE_ON_INSTANCE_AND_SERVICE = "AVAILABLE_ON_INSTANCE_AND_SERVICE"

    #: A constant which can be used with the content_availability property of a KernelEventContent.
    #: This constant has a value of "AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS"
    CONTENT_AVAILABILITY_AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS = "AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new KernelEventContent object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.KernelEventContent.type` attribute
        of this class is ``KERNEL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this KernelEventContent.
            Allowed values for this property are: "KERNEL", "EXPLOIT_ATTEMPT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param content_availability:
            The value to assign to the content_availability property of this KernelEventContent.
            Allowed values for this property are: "NOT_AVAILABLE", "AVAILABLE_ON_INSTANCE", "AVAILABLE_ON_SERVICE", "AVAILABLE_ON_INSTANCE_AND_SERVICE", "AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type content_availability: str

        :param content_location:
            The value to assign to the content_location property of this KernelEventContent.
        :type content_location: str

        :param size:
            The value to assign to the size property of this KernelEventContent.
        :type size: int

        """
        self.swagger_types = {
            'type': 'str',
            'content_availability': 'str',
            'content_location': 'str',
            'size': 'int'
        }
        self.attribute_map = {
            'type': 'type',
            'content_availability': 'contentAvailability',
            'content_location': 'contentLocation',
            'size': 'size'
        }
        self._type = None
        self._content_availability = None
        self._content_location = None
        self._size = None
        self._type = 'KERNEL'

    @property
    def content_availability(self):
        """
        **[Required]** Gets the content_availability of this KernelEventContent.
        Crash content availability status:
            * 'NOT_AVAILABLE' indicates the content is not available on the instance nor in the service
            * 'AVAILABLE_ON_INSTANCE' indicates the content is only available on the instance.
            * 'AVAILABLE_ON_SERVICE' indicates the content is only available on the service.
            * 'AVAILABLE_ON_INSTANCE_AND_SERVICE' indicates the content is available both on the instance and the service
            * 'AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS' indicates the content is available on the instance and its upload to the service is in progress.

        Allowed values for this property are: "NOT_AVAILABLE", "AVAILABLE_ON_INSTANCE", "AVAILABLE_ON_SERVICE", "AVAILABLE_ON_INSTANCE_AND_SERVICE", "AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The content_availability of this KernelEventContent.
        :rtype: str
        """
        return self._content_availability

    @content_availability.setter
    def content_availability(self, content_availability):
        """
        Sets the content_availability of this KernelEventContent.
        Crash content availability status:
            * 'NOT_AVAILABLE' indicates the content is not available on the instance nor in the service
            * 'AVAILABLE_ON_INSTANCE' indicates the content is only available on the instance.
            * 'AVAILABLE_ON_SERVICE' indicates the content is only available on the service.
            * 'AVAILABLE_ON_INSTANCE_AND_SERVICE' indicates the content is available both on the instance and the service
            * 'AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS' indicates the content is available on the instance and its upload to the service is in progress.


        :param content_availability: The content_availability of this KernelEventContent.
        :type: str
        """
        allowed_values = ["NOT_AVAILABLE", "AVAILABLE_ON_INSTANCE", "AVAILABLE_ON_SERVICE", "AVAILABLE_ON_INSTANCE_AND_SERVICE", "AVAILABLE_ON_INSTANCE_UPLOAD_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(content_availability, allowed_values):
            content_availability = 'UNKNOWN_ENUM_VALUE'
        self._content_availability = content_availability

    @property
    def content_location(self):
        """
        **[Required]** Gets the content_location of this KernelEventContent.
        Location of the Kernel event content.


        :return: The content_location of this KernelEventContent.
        :rtype: str
        """
        return self._content_location

    @content_location.setter
    def content_location(self, content_location):
        """
        Sets the content_location of this KernelEventContent.
        Location of the Kernel event content.


        :param content_location: The content_location of this KernelEventContent.
        :type: str
        """
        self._content_location = content_location

    @property
    def size(self):
        """
        Gets the size of this KernelEventContent.
        Size of the event content.


        :return: The size of this KernelEventContent.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this KernelEventContent.
        Size of the event content.


        :param size: The size of this KernelEventContent.
        :type: int
        """
        self._size = size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
