# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330

from .metric_extension_update_query_properties import MetricExtensionUpdateQueryProperties
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpUpdateQueryProperties(MetricExtensionUpdateQueryProperties):
    """
    Query properties applicable to HTTP type of collection method
    """

    #: A constant which can be used with the response_content_type property of a HttpUpdateQueryProperties.
    #: This constant has a value of "TEXT_PLAIN"
    RESPONSE_CONTENT_TYPE_TEXT_PLAIN = "TEXT_PLAIN"

    #: A constant which can be used with the response_content_type property of a HttpUpdateQueryProperties.
    #: This constant has a value of "TEXT_HTML"
    RESPONSE_CONTENT_TYPE_TEXT_HTML = "TEXT_HTML"

    #: A constant which can be used with the response_content_type property of a HttpUpdateQueryProperties.
    #: This constant has a value of "APPLICATION_JSON"
    RESPONSE_CONTENT_TYPE_APPLICATION_JSON = "APPLICATION_JSON"

    #: A constant which can be used with the response_content_type property of a HttpUpdateQueryProperties.
    #: This constant has a value of "APPLICATION_XML"
    RESPONSE_CONTENT_TYPE_APPLICATION_XML = "APPLICATION_XML"

    #: A constant which can be used with the protocol_type property of a HttpUpdateQueryProperties.
    #: This constant has a value of "HTTP"
    PROTOCOL_TYPE_HTTP = "HTTP"

    #: A constant which can be used with the protocol_type property of a HttpUpdateQueryProperties.
    #: This constant has a value of "HTTPS"
    PROTOCOL_TYPE_HTTPS = "HTTPS"

    def __init__(self, **kwargs):
        """
        Initializes a new HttpUpdateQueryProperties object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.HttpUpdateQueryProperties.collection_method` attribute
        of this class is ``HTTP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param collection_method:
            The value to assign to the collection_method property of this HttpUpdateQueryProperties.
            Allowed values for this property are: "OS_COMMAND", "SQL", "JMX", "HTTP"
        :type collection_method: str

        :param url:
            The value to assign to the url property of this HttpUpdateQueryProperties.
        :type url: str

        :param response_content_type:
            The value to assign to the response_content_type property of this HttpUpdateQueryProperties.
            Allowed values for this property are: "TEXT_PLAIN", "TEXT_HTML", "APPLICATION_JSON", "APPLICATION_XML"
        :type response_content_type: str

        :param protocol_type:
            The value to assign to the protocol_type property of this HttpUpdateQueryProperties.
            Allowed values for this property are: "HTTP", "HTTPS"
        :type protocol_type: str

        :param script_details:
            The value to assign to the script_details property of this HttpUpdateQueryProperties.
        :type script_details: oci.stack_monitoring.models.UpdateHttpScriptFileDetails

        """
        self.swagger_types = {
            'collection_method': 'str',
            'url': 'str',
            'response_content_type': 'str',
            'protocol_type': 'str',
            'script_details': 'UpdateHttpScriptFileDetails'
        }
        self.attribute_map = {
            'collection_method': 'collectionMethod',
            'url': 'url',
            'response_content_type': 'responseContentType',
            'protocol_type': 'protocolType',
            'script_details': 'scriptDetails'
        }
        self._collection_method = None
        self._url = None
        self._response_content_type = None
        self._protocol_type = None
        self._script_details = None
        self._collection_method = 'HTTP'

    @property
    def url(self):
        """
        Gets the url of this HttpUpdateQueryProperties.
        Http(s) end point URL


        :return: The url of this HttpUpdateQueryProperties.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this HttpUpdateQueryProperties.
        Http(s) end point URL


        :param url: The url of this HttpUpdateQueryProperties.
        :type: str
        """
        self._url = url

    @property
    def response_content_type(self):
        """
        Gets the response_content_type of this HttpUpdateQueryProperties.
        Type of content response given by the http(s) URL

        Allowed values for this property are: "TEXT_PLAIN", "TEXT_HTML", "APPLICATION_JSON", "APPLICATION_XML"


        :return: The response_content_type of this HttpUpdateQueryProperties.
        :rtype: str
        """
        return self._response_content_type

    @response_content_type.setter
    def response_content_type(self, response_content_type):
        """
        Sets the response_content_type of this HttpUpdateQueryProperties.
        Type of content response given by the http(s) URL


        :param response_content_type: The response_content_type of this HttpUpdateQueryProperties.
        :type: str
        """
        allowed_values = ["TEXT_PLAIN", "TEXT_HTML", "APPLICATION_JSON", "APPLICATION_XML"]
        if not value_allowed_none_or_none_sentinel(response_content_type, allowed_values):
            raise ValueError(
                f"Invalid value for `response_content_type`, must be None or one of {allowed_values}"
            )
        self._response_content_type = response_content_type

    @property
    def protocol_type(self):
        """
        Gets the protocol_type of this HttpUpdateQueryProperties.
        Supported protocol of resources to be associated with this metric extension. This is optional and defaults to HTTPS, which uses secure connection to the URL

        Allowed values for this property are: "HTTP", "HTTPS"


        :return: The protocol_type of this HttpUpdateQueryProperties.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """
        Sets the protocol_type of this HttpUpdateQueryProperties.
        Supported protocol of resources to be associated with this metric extension. This is optional and defaults to HTTPS, which uses secure connection to the URL


        :param protocol_type: The protocol_type of this HttpUpdateQueryProperties.
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS"]
        if not value_allowed_none_or_none_sentinel(protocol_type, allowed_values):
            raise ValueError(
                f"Invalid value for `protocol_type`, must be None or one of {allowed_values}"
            )
        self._protocol_type = protocol_type

    @property
    def script_details(self):
        """
        Gets the script_details of this HttpUpdateQueryProperties.

        :return: The script_details of this HttpUpdateQueryProperties.
        :rtype: oci.stack_monitoring.models.UpdateHttpScriptFileDetails
        """
        return self._script_details

    @script_details.setter
    def script_details(self, script_details):
        """
        Sets the script_details of this HttpUpdateQueryProperties.

        :param script_details: The script_details of this HttpUpdateQueryProperties.
        :type: oci.stack_monitoring.models.UpdateHttpScriptFileDetails
        """
        self._script_details = script_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
