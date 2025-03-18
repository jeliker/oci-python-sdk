# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240102


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VulnerabilitiesSummary(object):
    """
    Summary of vulnerabilities found in registered resources grouped by severity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VulnerabilitiesSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total:
            The value to assign to the total property of this VulnerabilitiesSummary.
        :type total: int

        :param critical:
            The value to assign to the critical property of this VulnerabilitiesSummary.
        :type critical: int

        :param high:
            The value to assign to the high property of this VulnerabilitiesSummary.
        :type high: int

        :param medium:
            The value to assign to the medium property of this VulnerabilitiesSummary.
        :type medium: int

        :param info:
            The value to assign to the info property of this VulnerabilitiesSummary.
        :type info: int

        :param low:
            The value to assign to the low property of this VulnerabilitiesSummary.
        :type low: int

        """
        self.swagger_types = {
            'total': 'int',
            'critical': 'int',
            'high': 'int',
            'medium': 'int',
            'info': 'int',
            'low': 'int'
        }
        self.attribute_map = {
            'total': 'total',
            'critical': 'critical',
            'high': 'high',
            'medium': 'medium',
            'info': 'info',
            'low': 'low'
        }
        self._total = None
        self._critical = None
        self._high = None
        self._medium = None
        self._info = None
        self._low = None

    @property
    def total(self):
        """
        **[Required]** Gets the total of this VulnerabilitiesSummary.
        Total number of vulnerabilities.


        :return: The total of this VulnerabilitiesSummary.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this VulnerabilitiesSummary.
        Total number of vulnerabilities.


        :param total: The total of this VulnerabilitiesSummary.
        :type: int
        """
        self._total = total

    @property
    def critical(self):
        """
        **[Required]** Gets the critical of this VulnerabilitiesSummary.
        Cummulative number of resources that have critical level vulnerabilities.


        :return: The critical of this VulnerabilitiesSummary.
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """
        Sets the critical of this VulnerabilitiesSummary.
        Cummulative number of resources that have critical level vulnerabilities.


        :param critical: The critical of this VulnerabilitiesSummary.
        :type: int
        """
        self._critical = critical

    @property
    def high(self):
        """
        **[Required]** Gets the high of this VulnerabilitiesSummary.
        Cummulative number of resources that have high level vulnerabilities.


        :return: The high of this VulnerabilitiesSummary.
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """
        Sets the high of this VulnerabilitiesSummary.
        Cummulative number of resources that have high level vulnerabilities.


        :param high: The high of this VulnerabilitiesSummary.
        :type: int
        """
        self._high = high

    @property
    def medium(self):
        """
        **[Required]** Gets the medium of this VulnerabilitiesSummary.
        Cummulative number of resources that have medium level vulnerabilities.


        :return: The medium of this VulnerabilitiesSummary.
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """
        Sets the medium of this VulnerabilitiesSummary.
        Cummulative number of resources that have medium level vulnerabilities.


        :param medium: The medium of this VulnerabilitiesSummary.
        :type: int
        """
        self._medium = medium

    @property
    def info(self):
        """
        **[Required]** Gets the info of this VulnerabilitiesSummary.
        Cummulative number of resources that have info level vulnerabilities.


        :return: The info of this VulnerabilitiesSummary.
        :rtype: int
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this VulnerabilitiesSummary.
        Cummulative number of resources that have info level vulnerabilities.


        :param info: The info of this VulnerabilitiesSummary.
        :type: int
        """
        self._info = info

    @property
    def low(self):
        """
        **[Required]** Gets the low of this VulnerabilitiesSummary.
        Cummulative number of resources that have low level vulnerabilities.


        :return: The low of this VulnerabilitiesSummary.
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """
        Sets the low of this VulnerabilitiesSummary.
        Cummulative number of resources that have low level vulnerabilities.


        :param low: The low of this VulnerabilitiesSummary.
        :type: int
        """
        self._low = low

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
