# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FindingAnalyticsDimensions(object):
    """
    The scope of analytics data.
    """

    #: A constant which can be used with the top_finding_status property of a FindingAnalyticsDimensions.
    #: This constant has a value of "RISK"
    TOP_FINDING_STATUS_RISK = "RISK"

    #: A constant which can be used with the top_finding_status property of a FindingAnalyticsDimensions.
    #: This constant has a value of "EVALUATE"
    TOP_FINDING_STATUS_EVALUATE = "EVALUATE"

    #: A constant which can be used with the top_finding_status property of a FindingAnalyticsDimensions.
    #: This constant has a value of "ADVISORY"
    TOP_FINDING_STATUS_ADVISORY = "ADVISORY"

    #: A constant which can be used with the top_finding_status property of a FindingAnalyticsDimensions.
    #: This constant has a value of "PASS"
    TOP_FINDING_STATUS_PASS = "PASS"

    #: A constant which can be used with the top_finding_status property of a FindingAnalyticsDimensions.
    #: This constant has a value of "DEFERRED"
    TOP_FINDING_STATUS_DEFERRED = "DEFERRED"

    #: A constant which can be used with the severity property of a FindingAnalyticsDimensions.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a FindingAnalyticsDimensions.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a FindingAnalyticsDimensions.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    #: A constant which can be used with the severity property of a FindingAnalyticsDimensions.
    #: This constant has a value of "EVALUATE"
    SEVERITY_EVALUATE = "EVALUATE"

    #: A constant which can be used with the severity property of a FindingAnalyticsDimensions.
    #: This constant has a value of "ADVISORY"
    SEVERITY_ADVISORY = "ADVISORY"

    #: A constant which can be used with the severity property of a FindingAnalyticsDimensions.
    #: This constant has a value of "PASS"
    SEVERITY_PASS = "PASS"

    #: A constant which can be used with the severity property of a FindingAnalyticsDimensions.
    #: This constant has a value of "DEFERRED"
    SEVERITY_DEFERRED = "DEFERRED"

    def __init__(self, **kwargs):
        """
        Initializes a new FindingAnalyticsDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this FindingAnalyticsDimensions.
        :type key: str

        :param top_finding_category:
            The value to assign to the top_finding_category property of this FindingAnalyticsDimensions.
        :type top_finding_category: str

        :param title:
            The value to assign to the title property of this FindingAnalyticsDimensions.
        :type title: str

        :param top_finding_status:
            The value to assign to the top_finding_status property of this FindingAnalyticsDimensions.
            Allowed values for this property are: "RISK", "EVALUATE", "ADVISORY", "PASS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type top_finding_status: str

        :param severity:
            The value to assign to the severity property of this FindingAnalyticsDimensions.
            Allowed values for this property are: "HIGH", "MEDIUM", "LOW", "EVALUATE", "ADVISORY", "PASS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param target_id:
            The value to assign to the target_id property of this FindingAnalyticsDimensions.
        :type target_id: str

        """
        self.swagger_types = {
            'key': 'str',
            'top_finding_category': 'str',
            'title': 'str',
            'top_finding_status': 'str',
            'severity': 'str',
            'target_id': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'top_finding_category': 'topFindingCategory',
            'title': 'title',
            'top_finding_status': 'topFindingStatus',
            'severity': 'severity',
            'target_id': 'targetId'
        }
        self._key = None
        self._top_finding_category = None
        self._title = None
        self._top_finding_status = None
        self._severity = None
        self._target_id = None

    @property
    def key(self):
        """
        Gets the key of this FindingAnalyticsDimensions.
        Each finding in security assessment has an associated key (think of key as a finding's name).
        For a given finding, the key will be the same across targets. The user can use these keys to filter the findings.


        :return: The key of this FindingAnalyticsDimensions.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FindingAnalyticsDimensions.
        Each finding in security assessment has an associated key (think of key as a finding's name).
        For a given finding, the key will be the same across targets. The user can use these keys to filter the findings.


        :param key: The key of this FindingAnalyticsDimensions.
        :type: str
        """
        self._key = key

    @property
    def top_finding_category(self):
        """
        Gets the top_finding_category of this FindingAnalyticsDimensions.
        The category of the top finding.


        :return: The top_finding_category of this FindingAnalyticsDimensions.
        :rtype: str
        """
        return self._top_finding_category

    @top_finding_category.setter
    def top_finding_category(self, top_finding_category):
        """
        Sets the top_finding_category of this FindingAnalyticsDimensions.
        The category of the top finding.


        :param top_finding_category: The top_finding_category of this FindingAnalyticsDimensions.
        :type: str
        """
        self._top_finding_category = top_finding_category

    @property
    def title(self):
        """
        Gets the title of this FindingAnalyticsDimensions.
        The short title of the finding.


        :return: The title of this FindingAnalyticsDimensions.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this FindingAnalyticsDimensions.
        The short title of the finding.


        :param title: The title of this FindingAnalyticsDimensions.
        :type: str
        """
        self._title = title

    @property
    def top_finding_status(self):
        """
        Gets the top_finding_status of this FindingAnalyticsDimensions.
        The status of the top finding.
        All findings will have \"severity\" to indicate the risk level, but only top findings will have \"status\".
        Possible status: Pass / Risk (Low, Medium, High)/ Evaluate / Advisory / Deferred
        Instead of having \"Low, Medium, High\" in severity, \"Risk\" will include these three situations in status.

        Allowed values for this property are: "RISK", "EVALUATE", "ADVISORY", "PASS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The top_finding_status of this FindingAnalyticsDimensions.
        :rtype: str
        """
        return self._top_finding_status

    @top_finding_status.setter
    def top_finding_status(self, top_finding_status):
        """
        Sets the top_finding_status of this FindingAnalyticsDimensions.
        The status of the top finding.
        All findings will have \"severity\" to indicate the risk level, but only top findings will have \"status\".
        Possible status: Pass / Risk (Low, Medium, High)/ Evaluate / Advisory / Deferred
        Instead of having \"Low, Medium, High\" in severity, \"Risk\" will include these three situations in status.


        :param top_finding_status: The top_finding_status of this FindingAnalyticsDimensions.
        :type: str
        """
        allowed_values = ["RISK", "EVALUATE", "ADVISORY", "PASS", "DEFERRED"]
        if not value_allowed_none_or_none_sentinel(top_finding_status, allowed_values):
            top_finding_status = 'UNKNOWN_ENUM_VALUE'
        self._top_finding_status = top_finding_status

    @property
    def severity(self):
        """
        Gets the severity of this FindingAnalyticsDimensions.
        The severity (risk level) of the finding.

        Allowed values for this property are: "HIGH", "MEDIUM", "LOW", "EVALUATE", "ADVISORY", "PASS", "DEFERRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this FindingAnalyticsDimensions.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this FindingAnalyticsDimensions.
        The severity (risk level) of the finding.


        :param severity: The severity of this FindingAnalyticsDimensions.
        :type: str
        """
        allowed_values = ["HIGH", "MEDIUM", "LOW", "EVALUATE", "ADVISORY", "PASS", "DEFERRED"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def target_id(self):
        """
        Gets the target_id of this FindingAnalyticsDimensions.
        The OCID of the target database.


        :return: The target_id of this FindingAnalyticsDimensions.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this FindingAnalyticsDimensions.
        The OCID of the target database.


        :param target_id: The target_id of this FindingAnalyticsDimensions.
        :type: str
        """
        self._target_id = target_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
