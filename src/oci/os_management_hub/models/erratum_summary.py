# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ErratumSummary(object):
    """
    Important changes for software. This can include security advisories, bug fixes, or enhancements.
    """

    #: A constant which can be used with the classification_type property of a ErratumSummary.
    #: This constant has a value of "SECURITY"
    CLASSIFICATION_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the classification_type property of a ErratumSummary.
    #: This constant has a value of "BUGFIX"
    CLASSIFICATION_TYPE_BUGFIX = "BUGFIX"

    #: A constant which can be used with the classification_type property of a ErratumSummary.
    #: This constant has a value of "ENHANCEMENT"
    CLASSIFICATION_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the classification_type property of a ErratumSummary.
    #: This constant has a value of "OTHER"
    CLASSIFICATION_TYPE_OTHER = "OTHER"

    #: A constant which can be used with the advisory_severity property of a ErratumSummary.
    #: This constant has a value of "LOW"
    ADVISORY_SEVERITY_LOW = "LOW"

    #: A constant which can be used with the advisory_severity property of a ErratumSummary.
    #: This constant has a value of "MODERATE"
    ADVISORY_SEVERITY_MODERATE = "MODERATE"

    #: A constant which can be used with the advisory_severity property of a ErratumSummary.
    #: This constant has a value of "IMPORTANT"
    ADVISORY_SEVERITY_IMPORTANT = "IMPORTANT"

    #: A constant which can be used with the advisory_severity property of a ErratumSummary.
    #: This constant has a value of "CRITICAL"
    ADVISORY_SEVERITY_CRITICAL = "CRITICAL"

    def __init__(self, **kwargs):
        """
        Initializes a new ErratumSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ErratumSummary.
        :type name: str

        :param synopsis:
            The value to assign to the synopsis property of this ErratumSummary.
        :type synopsis: str

        :param time_issued:
            The value to assign to the time_issued property of this ErratumSummary.
        :type time_issued: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ErratumSummary.
        :type time_updated: datetime

        :param classification_type:
            The value to assign to the classification_type property of this ErratumSummary.
            Allowed values for this property are: "SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type classification_type: str

        :param related_cves:
            The value to assign to the related_cves property of this ErratumSummary.
        :type related_cves: list[str]

        :param os_families:
            The value to assign to the os_families property of this ErratumSummary.
        :type os_families: list[oci.os_management_hub.models.OsFamily]

        :param advisory_severity:
            The value to assign to the advisory_severity property of this ErratumSummary.
            Allowed values for this property are: "LOW", "MODERATE", "IMPORTANT", "CRITICAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type advisory_severity: str

        """
        self.swagger_types = {
            'name': 'str',
            'synopsis': 'str',
            'time_issued': 'datetime',
            'time_updated': 'datetime',
            'classification_type': 'str',
            'related_cves': 'list[str]',
            'os_families': 'list[OsFamily]',
            'advisory_severity': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'synopsis': 'synopsis',
            'time_issued': 'timeIssued',
            'time_updated': 'timeUpdated',
            'classification_type': 'classificationType',
            'related_cves': 'relatedCves',
            'os_families': 'osFamilies',
            'advisory_severity': 'advisorySeverity'
        }

        self._name = None
        self._synopsis = None
        self._time_issued = None
        self._time_updated = None
        self._classification_type = None
        self._related_cves = None
        self._os_families = None
        self._advisory_severity = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ErratumSummary.
        Advisory name.


        :return: The name of this ErratumSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ErratumSummary.
        Advisory name.


        :param name: The name of this ErratumSummary.
        :type: str
        """
        self._name = name

    @property
    def synopsis(self):
        """
        Gets the synopsis of this ErratumSummary.
        Summary description of the erratum.


        :return: The synopsis of this ErratumSummary.
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """
        Sets the synopsis of this ErratumSummary.
        Summary description of the erratum.


        :param synopsis: The synopsis of this ErratumSummary.
        :type: str
        """
        self._synopsis = synopsis

    @property
    def time_issued(self):
        """
        Gets the time_issued of this ErratumSummary.
        Date the erratum was issued, as described
        in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_issued of this ErratumSummary.
        :rtype: datetime
        """
        return self._time_issued

    @time_issued.setter
    def time_issued(self, time_issued):
        """
        Sets the time_issued of this ErratumSummary.
        Date the erratum was issued, as described
        in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_issued: The time_issued of this ErratumSummary.
        :type: datetime
        """
        self._time_issued = time_issued

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ErratumSummary.
        Most recent date the erratum was updated, as described
        in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this ErratumSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ErratumSummary.
        Most recent date the erratum was updated, as described
        in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this ErratumSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def classification_type(self):
        """
        Gets the classification_type of this ErratumSummary.
        Type of the erratum.

        Allowed values for this property are: "SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The classification_type of this ErratumSummary.
        :rtype: str
        """
        return self._classification_type

    @classification_type.setter
    def classification_type(self, classification_type):
        """
        Sets the classification_type of this ErratumSummary.
        Type of the erratum.


        :param classification_type: The classification_type of this ErratumSummary.
        :type: str
        """
        allowed_values = ["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER"]
        if not value_allowed_none_or_none_sentinel(classification_type, allowed_values):
            classification_type = 'UNKNOWN_ENUM_VALUE'
        self._classification_type = classification_type

    @property
    def related_cves(self):
        """
        Gets the related_cves of this ErratumSummary.
        List of CVEs applicable to this erratum.


        :return: The related_cves of this ErratumSummary.
        :rtype: list[str]
        """
        return self._related_cves

    @related_cves.setter
    def related_cves(self, related_cves):
        """
        Sets the related_cves of this ErratumSummary.
        List of CVEs applicable to this erratum.


        :param related_cves: The related_cves of this ErratumSummary.
        :type: list[str]
        """
        self._related_cves = related_cves

    @property
    def os_families(self):
        """
        Gets the os_families of this ErratumSummary.
        List of affected OS families.


        :return: The os_families of this ErratumSummary.
        :rtype: list[oci.os_management_hub.models.OsFamily]
        """
        return self._os_families

    @os_families.setter
    def os_families(self, os_families):
        """
        Sets the os_families of this ErratumSummary.
        List of affected OS families.


        :param os_families: The os_families of this ErratumSummary.
        :type: list[oci.os_management_hub.models.OsFamily]
        """
        self._os_families = os_families

    @property
    def advisory_severity(self):
        """
        Gets the advisory_severity of this ErratumSummary.
        The severity advisory. Only valid for security type advisories.

        Allowed values for this property are: "LOW", "MODERATE", "IMPORTANT", "CRITICAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The advisory_severity of this ErratumSummary.
        :rtype: str
        """
        return self._advisory_severity

    @advisory_severity.setter
    def advisory_severity(self, advisory_severity):
        """
        Sets the advisory_severity of this ErratumSummary.
        The severity advisory. Only valid for security type advisories.


        :param advisory_severity: The advisory_severity of this ErratumSummary.
        :type: str
        """
        allowed_values = ["LOW", "MODERATE", "IMPORTANT", "CRITICAL"]
        if not value_allowed_none_or_none_sentinel(advisory_severity, allowed_values):
            advisory_severity = 'UNKNOWN_ENUM_VALUE'
        self._advisory_severity = advisory_severity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
