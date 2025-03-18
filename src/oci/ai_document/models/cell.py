# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Cell(object):
    """
    A single cell in a table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Cell object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text:
            The value to assign to the text property of this Cell.
        :type text: str

        :param row_index:
            The value to assign to the row_index property of this Cell.
        :type row_index: int

        :param column_index:
            The value to assign to the column_index property of this Cell.
        :type column_index: int

        :param confidence:
            The value to assign to the confidence property of this Cell.
        :type confidence: float

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this Cell.
        :type bounding_polygon: oci.ai_document.models.BoundingPolygon

        :param word_indexes:
            The value to assign to the word_indexes property of this Cell.
        :type word_indexes: list[int]

        """
        self.swagger_types = {
            'text': 'str',
            'row_index': 'int',
            'column_index': 'int',
            'confidence': 'float',
            'bounding_polygon': 'BoundingPolygon',
            'word_indexes': 'list[int]'
        }
        self.attribute_map = {
            'text': 'text',
            'row_index': 'rowIndex',
            'column_index': 'columnIndex',
            'confidence': 'confidence',
            'bounding_polygon': 'boundingPolygon',
            'word_indexes': 'wordIndexes'
        }
        self._text = None
        self._row_index = None
        self._column_index = None
        self._confidence = None
        self._bounding_polygon = None
        self._word_indexes = None

    @property
    def text(self):
        """
        **[Required]** Gets the text of this Cell.
        The text recognized in the cell.


        :return: The text of this Cell.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Cell.
        The text recognized in the cell.


        :param text: The text of this Cell.
        :type: str
        """
        self._text = text

    @property
    def row_index(self):
        """
        **[Required]** Gets the row_index of this Cell.
        The index of the cell inside the row.


        :return: The row_index of this Cell.
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """
        Sets the row_index of this Cell.
        The index of the cell inside the row.


        :param row_index: The row_index of this Cell.
        :type: int
        """
        self._row_index = row_index

    @property
    def column_index(self):
        """
        **[Required]** Gets the column_index of this Cell.
        The index of the cell inside the column.


        :return: The column_index of this Cell.
        :rtype: int
        """
        return self._column_index

    @column_index.setter
    def column_index(self, column_index):
        """
        Sets the column_index of this Cell.
        The index of the cell inside the column.


        :param column_index: The column_index of this Cell.
        :type: int
        """
        self._column_index = column_index

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this Cell.
        The confidence score between 0 and 1.


        :return: The confidence of this Cell.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Cell.
        The confidence score between 0 and 1.


        :param confidence: The confidence of this Cell.
        :type: float
        """
        self._confidence = confidence

    @property
    def bounding_polygon(self):
        """
        **[Required]** Gets the bounding_polygon of this Cell.

        :return: The bounding_polygon of this Cell.
        :rtype: oci.ai_document.models.BoundingPolygon
        """
        return self._bounding_polygon

    @bounding_polygon.setter
    def bounding_polygon(self, bounding_polygon):
        """
        Sets the bounding_polygon of this Cell.

        :param bounding_polygon: The bounding_polygon of this Cell.
        :type: oci.ai_document.models.BoundingPolygon
        """
        self._bounding_polygon = bounding_polygon

    @property
    def word_indexes(self):
        """
        **[Required]** Gets the word_indexes of this Cell.
        The words detected in the cell.


        :return: The word_indexes of this Cell.
        :rtype: list[int]
        """
        return self._word_indexes

    @word_indexes.setter
    def word_indexes(self, word_indexes):
        """
        Sets the word_indexes of this Cell.
        The words detected in the cell.


        :param word_indexes: The word_indexes of this Cell.
        :type: list[int]
        """
        self._word_indexes = word_indexes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
