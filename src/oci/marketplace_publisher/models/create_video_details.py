# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVideoDetails(object):
    """
    A link to a video on the internet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVideoDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content_url:
            The value to assign to the content_url property of this CreateVideoDetails.
        :type content_url: str

        """
        self.swagger_types = {
            'content_url': 'str'
        }
        self.attribute_map = {
            'content_url': 'contentUrl'
        }
        self._content_url = None

    @property
    def content_url(self):
        """
        **[Required]** Gets the content_url of this CreateVideoDetails.
        The URL of the video.


        :return: The content_url of this CreateVideoDetails.
        :rtype: str
        """
        return self._content_url

    @content_url.setter
    def content_url(self, content_url):
        """
        Sets the content_url of this CreateVideoDetails.
        The URL of the video.


        :param content_url: The content_url of this CreateVideoDetails.
        :type: str
        """
        self._content_url = content_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
