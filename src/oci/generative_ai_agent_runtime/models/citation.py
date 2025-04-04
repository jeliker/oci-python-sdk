# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Citation(object):
    """
    The source of information for the agent's response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Citation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_text:
            The value to assign to the source_text property of this Citation.
        :type source_text: str

        :param source_location:
            The value to assign to the source_location property of this Citation.
        :type source_location: oci.generative_ai_agent_runtime.models.SourceLocation

        :param title:
            The value to assign to the title property of this Citation.
        :type title: str

        :param doc_id:
            The value to assign to the doc_id property of this Citation.
        :type doc_id: str

        :param page_numbers:
            The value to assign to the page_numbers property of this Citation.
        :type page_numbers: list[int]

        :param metadata:
            The value to assign to the metadata property of this Citation.
        :type metadata: dict(str, object)

        """
        self.swagger_types = {
            'source_text': 'str',
            'source_location': 'SourceLocation',
            'title': 'str',
            'doc_id': 'str',
            'page_numbers': 'list[int]',
            'metadata': 'dict(str, object)'
        }
        self.attribute_map = {
            'source_text': 'sourceText',
            'source_location': 'sourceLocation',
            'title': 'title',
            'doc_id': 'docId',
            'page_numbers': 'pageNumbers',
            'metadata': 'metadata'
        }
        self._source_text = None
        self._source_location = None
        self._title = None
        self._doc_id = None
        self._page_numbers = None
        self._metadata = None

    @property
    def source_text(self):
        """
        Gets the source_text of this Citation.
        The text that's the source for the agent's response.


        :return: The source_text of this Citation.
        :rtype: str
        """
        return self._source_text

    @source_text.setter
    def source_text(self, source_text):
        """
        Sets the source_text of this Citation.
        The text that's the source for the agent's response.


        :param source_text: The source_text of this Citation.
        :type: str
        """
        self._source_text = source_text

    @property
    def source_location(self):
        """
        Gets the source_location of this Citation.

        :return: The source_location of this Citation.
        :rtype: oci.generative_ai_agent_runtime.models.SourceLocation
        """
        return self._source_location

    @source_location.setter
    def source_location(self, source_location):
        """
        Sets the source_location of this Citation.

        :param source_location: The source_location of this Citation.
        :type: oci.generative_ai_agent_runtime.models.SourceLocation
        """
        self._source_location = source_location

    @property
    def title(self):
        """
        Gets the title of this Citation.
        The title of the source text, if available.


        :return: The title of this Citation.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Citation.
        The title of the source text, if available.


        :param title: The title of this Citation.
        :type: str
        """
        self._title = title

    @property
    def doc_id(self):
        """
        Gets the doc_id of this Citation.
        The id of the retrieved document, if available.


        :return: The doc_id of this Citation.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """
        Sets the doc_id of this Citation.
        The id of the retrieved document, if available.


        :param doc_id: The doc_id of this Citation.
        :type: str
        """
        self._doc_id = doc_id

    @property
    def page_numbers(self):
        """
        Gets the page_numbers of this Citation.
        The page numbers on the retrieved document, if available.


        :return: The page_numbers of this Citation.
        :rtype: list[int]
        """
        return self._page_numbers

    @page_numbers.setter
    def page_numbers(self, page_numbers):
        """
        Sets the page_numbers of this Citation.
        The page numbers on the retrieved document, if available.


        :param page_numbers: The page_numbers of this Citation.
        :type: list[int]
        """
        self._page_numbers = page_numbers

    @property
    def metadata(self):
        """
        Gets the metadata of this Citation.
        The metadata of the retrieved document, if available.


        :return: The metadata of this Citation.
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Citation.
        The metadata of the retrieved document, if available.


        :param metadata: The metadata of this Citation.
        :type: dict(str, object)
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
