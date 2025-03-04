# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QuotaRuleSummary(object):
    """
    Summary information for a principal's usage and quota rule.
    """

    #: A constant which can be used with the principal_type property of a QuotaRuleSummary.
    #: This constant has a value of "FILE_SYSTEM_LEVEL"
    PRINCIPAL_TYPE_FILE_SYSTEM_LEVEL = "FILE_SYSTEM_LEVEL"

    #: A constant which can be used with the principal_type property of a QuotaRuleSummary.
    #: This constant has a value of "DEFAULT_GROUP"
    PRINCIPAL_TYPE_DEFAULT_GROUP = "DEFAULT_GROUP"

    #: A constant which can be used with the principal_type property of a QuotaRuleSummary.
    #: This constant has a value of "DEFAULT_USER"
    PRINCIPAL_TYPE_DEFAULT_USER = "DEFAULT_USER"

    #: A constant which can be used with the principal_type property of a QuotaRuleSummary.
    #: This constant has a value of "INDIVIDUAL_GROUP"
    PRINCIPAL_TYPE_INDIVIDUAL_GROUP = "INDIVIDUAL_GROUP"

    #: A constant which can be used with the principal_type property of a QuotaRuleSummary.
    #: This constant has a value of "INDIVIDUAL_USER"
    PRINCIPAL_TYPE_INDIVIDUAL_USER = "INDIVIDUAL_USER"

    def __init__(self, **kwargs):
        """
        Initializes a new QuotaRuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this QuotaRuleSummary.
        :type id: str

        :param file_system_id:
            The value to assign to the file_system_id property of this QuotaRuleSummary.
        :type file_system_id: str

        :param principal_type:
            The value to assign to the principal_type property of this QuotaRuleSummary.
            Allowed values for this property are: "FILE_SYSTEM_LEVEL", "DEFAULT_GROUP", "DEFAULT_USER", "INDIVIDUAL_GROUP", "INDIVIDUAL_USER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type principal_type: str

        :param principal_id:
            The value to assign to the principal_id property of this QuotaRuleSummary.
        :type principal_id: int

        :param is_hard_quota:
            The value to assign to the is_hard_quota property of this QuotaRuleSummary.
        :type is_hard_quota: bool

        :param display_name:
            The value to assign to the display_name property of this QuotaRuleSummary.
        :type display_name: str

        :param usage_in_bytes:
            The value to assign to the usage_in_bytes property of this QuotaRuleSummary.
        :type usage_in_bytes: int

        :param quota_limit_in_gigabytes:
            The value to assign to the quota_limit_in_gigabytes property of this QuotaRuleSummary.
        :type quota_limit_in_gigabytes: int

        :param time_created:
            The value to assign to the time_created property of this QuotaRuleSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this QuotaRuleSummary.
        :type time_updated: datetime

        :param are_violators_only:
            The value to assign to the are_violators_only property of this QuotaRuleSummary.
        :type are_violators_only: bool

        """
        self.swagger_types = {
            'id': 'str',
            'file_system_id': 'str',
            'principal_type': 'str',
            'principal_id': 'int',
            'is_hard_quota': 'bool',
            'display_name': 'str',
            'usage_in_bytes': 'int',
            'quota_limit_in_gigabytes': 'int',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'are_violators_only': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'file_system_id': 'fileSystemId',
            'principal_type': 'principalType',
            'principal_id': 'principalId',
            'is_hard_quota': 'isHardQuota',
            'display_name': 'displayName',
            'usage_in_bytes': 'usageInBytes',
            'quota_limit_in_gigabytes': 'quotaLimitInGigabytes',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'are_violators_only': 'areViolatorsOnly'
        }

        self._id = None
        self._file_system_id = None
        self._principal_type = None
        self._principal_id = None
        self._is_hard_quota = None
        self._display_name = None
        self._usage_in_bytes = None
        self._quota_limit_in_gigabytes = None
        self._time_created = None
        self._time_updated = None
        self._are_violators_only = None

    @property
    def id(self):
        """
        Gets the id of this QuotaRuleSummary.
        The identifier of the quota rule. It is the base64 encoded string of the tuple <principalId, principalType, isHardQuota>.


        :return: The id of this QuotaRuleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QuotaRuleSummary.
        The identifier of the quota rule. It is the base64 encoded string of the tuple <principalId, principalType, isHardQuota>.


        :param id: The id of this QuotaRuleSummary.
        :type: str
        """
        self._id = id

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this QuotaRuleSummary.
        The `OCID`__ of the file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The file_system_id of this QuotaRuleSummary.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this QuotaRuleSummary.
        The `OCID`__ of the file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param file_system_id: The file_system_id of this QuotaRuleSummary.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def principal_type(self):
        """
        **[Required]** Gets the principal_type of this QuotaRuleSummary.
        The type of the owner of this quota rule and usage.

        Allowed values for this property are: "FILE_SYSTEM_LEVEL", "DEFAULT_GROUP", "DEFAULT_USER", "INDIVIDUAL_GROUP", "INDIVIDUAL_USER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The principal_type of this QuotaRuleSummary.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        """
        Sets the principal_type of this QuotaRuleSummary.
        The type of the owner of this quota rule and usage.


        :param principal_type: The principal_type of this QuotaRuleSummary.
        :type: str
        """
        allowed_values = ["FILE_SYSTEM_LEVEL", "DEFAULT_GROUP", "DEFAULT_USER", "INDIVIDUAL_GROUP", "INDIVIDUAL_USER"]
        if not value_allowed_none_or_none_sentinel(principal_type, allowed_values):
            principal_type = 'UNKNOWN_ENUM_VALUE'
        self._principal_type = principal_type

    @property
    def principal_id(self):
        """
        **[Required]** Gets the principal_id of this QuotaRuleSummary.
        An identifier for the user or the group associated with quota rule and usage. UNIX-like operating systems use this integer value to
        identify a user or group to manage access control.


        :return: The principal_id of this QuotaRuleSummary.
        :rtype: int
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        """
        Sets the principal_id of this QuotaRuleSummary.
        An identifier for the user or the group associated with quota rule and usage. UNIX-like operating systems use this integer value to
        identify a user or group to manage access control.


        :param principal_id: The principal_id of this QuotaRuleSummary.
        :type: int
        """
        self._principal_id = principal_id

    @property
    def is_hard_quota(self):
        """
        Gets the is_hard_quota of this QuotaRuleSummary.
        Whether the quota rule will be enforced.
        If `isHardQuota` is true, the quota rule is enforced so that the write is blocked if usage
        exceeds the hard quota limit.
        If `isHardQuota` is false, writes succeed even if usage exceeds the soft quota limit, but the quota rule is violated.


        :return: The is_hard_quota of this QuotaRuleSummary.
        :rtype: bool
        """
        return self._is_hard_quota

    @is_hard_quota.setter
    def is_hard_quota(self, is_hard_quota):
        """
        Sets the is_hard_quota of this QuotaRuleSummary.
        Whether the quota rule will be enforced.
        If `isHardQuota` is true, the quota rule is enforced so that the write is blocked if usage
        exceeds the hard quota limit.
        If `isHardQuota` is false, writes succeed even if usage exceeds the soft quota limit, but the quota rule is violated.


        :param is_hard_quota: The is_hard_quota of this QuotaRuleSummary.
        :type: bool
        """
        self._is_hard_quota = is_hard_quota

    @property
    def display_name(self):
        """
        Gets the display_name of this QuotaRuleSummary.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.
        Example: `UserXYZ's quota`


        :return: The display_name of this QuotaRuleSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this QuotaRuleSummary.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.
        Example: `UserXYZ's quota`


        :param display_name: The display_name of this QuotaRuleSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def usage_in_bytes(self):
        """
        **[Required]** Gets the usage_in_bytes of this QuotaRuleSummary.
        The usage value corresponding to this principal in bytes.


        :return: The usage_in_bytes of this QuotaRuleSummary.
        :rtype: int
        """
        return self._usage_in_bytes

    @usage_in_bytes.setter
    def usage_in_bytes(self, usage_in_bytes):
        """
        Sets the usage_in_bytes of this QuotaRuleSummary.
        The usage value corresponding to this principal in bytes.


        :param usage_in_bytes: The usage_in_bytes of this QuotaRuleSummary.
        :type: int
        """
        self._usage_in_bytes = usage_in_bytes

    @property
    def quota_limit_in_gigabytes(self):
        """
        Gets the quota_limit_in_gigabytes of this QuotaRuleSummary.
        The value of the quota rule in gigabytes.


        :return: The quota_limit_in_gigabytes of this QuotaRuleSummary.
        :rtype: int
        """
        return self._quota_limit_in_gigabytes

    @quota_limit_in_gigabytes.setter
    def quota_limit_in_gigabytes(self, quota_limit_in_gigabytes):
        """
        Sets the quota_limit_in_gigabytes of this QuotaRuleSummary.
        The value of the quota rule in gigabytes.


        :param quota_limit_in_gigabytes: The quota_limit_in_gigabytes of this QuotaRuleSummary.
        :type: int
        """
        self._quota_limit_in_gigabytes = quota_limit_in_gigabytes

    @property
    def time_created(self):
        """
        Gets the time_created of this QuotaRuleSummary.
        The date and time the quota rule was created, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this QuotaRuleSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this QuotaRuleSummary.
        The date and time the quota rule was created, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this QuotaRuleSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this QuotaRuleSummary.
        The date and time the quota rule was last updated, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this QuotaRuleSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this QuotaRuleSummary.
        The date and time the quota rule was last updated, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this QuotaRuleSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def are_violators_only(self):
        """
        Gets the are_violators_only of this QuotaRuleSummary.
        An option to display only the users or groups that violate their quota rules.
        If `areViolatorsOnly` is false, results report all the quota and usage.
        If `areViolatorsOnly` is true, results only report the quota and usage for
        the users or groups that violate their quota rules.


        :return: The are_violators_only of this QuotaRuleSummary.
        :rtype: bool
        """
        return self._are_violators_only

    @are_violators_only.setter
    def are_violators_only(self, are_violators_only):
        """
        Sets the are_violators_only of this QuotaRuleSummary.
        An option to display only the users or groups that violate their quota rules.
        If `areViolatorsOnly` is false, results report all the quota and usage.
        If `areViolatorsOnly` is true, results only report the quota and usage for
        the users or groups that violate their quota rules.


        :param are_violators_only: The are_violators_only of this QuotaRuleSummary.
        :type: bool
        """
        self._are_violators_only = are_violators_only

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
