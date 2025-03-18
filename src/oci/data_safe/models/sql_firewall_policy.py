# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlFirewallPolicy(object):
    """
    The SQL Firewall policy resource contains the firewall policy metadata for a single user.
    """

    #: A constant which can be used with the sql_level property of a SqlFirewallPolicy.
    #: This constant has a value of "USER_ISSUED_SQL"
    SQL_LEVEL_USER_ISSUED_SQL = "USER_ISSUED_SQL"

    #: A constant which can be used with the sql_level property of a SqlFirewallPolicy.
    #: This constant has a value of "ALL_SQL"
    SQL_LEVEL_ALL_SQL = "ALL_SQL"

    #: A constant which can be used with the status property of a SqlFirewallPolicy.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a SqlFirewallPolicy.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the enforcement_scope property of a SqlFirewallPolicy.
    #: This constant has a value of "ENFORCE_CONTEXT"
    ENFORCEMENT_SCOPE_ENFORCE_CONTEXT = "ENFORCE_CONTEXT"

    #: A constant which can be used with the enforcement_scope property of a SqlFirewallPolicy.
    #: This constant has a value of "ENFORCE_SQL"
    ENFORCEMENT_SCOPE_ENFORCE_SQL = "ENFORCE_SQL"

    #: A constant which can be used with the enforcement_scope property of a SqlFirewallPolicy.
    #: This constant has a value of "ENFORCE_ALL"
    ENFORCEMENT_SCOPE_ENFORCE_ALL = "ENFORCE_ALL"

    #: A constant which can be used with the violation_action property of a SqlFirewallPolicy.
    #: This constant has a value of "BLOCK"
    VIOLATION_ACTION_BLOCK = "BLOCK"

    #: A constant which can be used with the violation_action property of a SqlFirewallPolicy.
    #: This constant has a value of "OBSERVE"
    VIOLATION_ACTION_OBSERVE = "OBSERVE"

    #: A constant which can be used with the violation_audit property of a SqlFirewallPolicy.
    #: This constant has a value of "ENABLED"
    VIOLATION_AUDIT_ENABLED = "ENABLED"

    #: A constant which can be used with the violation_audit property of a SqlFirewallPolicy.
    #: This constant has a value of "DISABLED"
    VIOLATION_AUDIT_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicy.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicy.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SqlFirewallPolicy.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlFirewallPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SqlFirewallPolicy.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SqlFirewallPolicy.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SqlFirewallPolicy.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SqlFirewallPolicy.
        :type description: str

        :param security_policy_id:
            The value to assign to the security_policy_id property of this SqlFirewallPolicy.
        :type security_policy_id: str

        :param db_user_name:
            The value to assign to the db_user_name property of this SqlFirewallPolicy.
        :type db_user_name: str

        :param sql_level:
            The value to assign to the sql_level property of this SqlFirewallPolicy.
            Allowed values for this property are: "USER_ISSUED_SQL", "ALL_SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type sql_level: str

        :param status:
            The value to assign to the status property of this SqlFirewallPolicy.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param enforcement_scope:
            The value to assign to the enforcement_scope property of this SqlFirewallPolicy.
            Allowed values for this property are: "ENFORCE_CONTEXT", "ENFORCE_SQL", "ENFORCE_ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type enforcement_scope: str

        :param violation_action:
            The value to assign to the violation_action property of this SqlFirewallPolicy.
            Allowed values for this property are: "BLOCK", "OBSERVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type violation_action: str

        :param violation_audit:
            The value to assign to the violation_audit property of this SqlFirewallPolicy.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type violation_audit: str

        :param allowed_client_ips:
            The value to assign to the allowed_client_ips property of this SqlFirewallPolicy.
        :type allowed_client_ips: list[str]

        :param allowed_client_os_usernames:
            The value to assign to the allowed_client_os_usernames property of this SqlFirewallPolicy.
        :type allowed_client_os_usernames: list[str]

        :param allowed_client_programs:
            The value to assign to the allowed_client_programs property of this SqlFirewallPolicy.
        :type allowed_client_programs: list[str]

        :param time_created:
            The value to assign to the time_created property of this SqlFirewallPolicy.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SqlFirewallPolicy.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SqlFirewallPolicy.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SqlFirewallPolicy.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SqlFirewallPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SqlFirewallPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SqlFirewallPolicy.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'security_policy_id': 'str',
            'db_user_name': 'str',
            'sql_level': 'str',
            'status': 'str',
            'enforcement_scope': 'str',
            'violation_action': 'str',
            'violation_audit': 'str',
            'allowed_client_ips': 'list[str]',
            'allowed_client_os_usernames': 'list[str]',
            'allowed_client_programs': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'security_policy_id': 'securityPolicyId',
            'db_user_name': 'dbUserName',
            'sql_level': 'sqlLevel',
            'status': 'status',
            'enforcement_scope': 'enforcementScope',
            'violation_action': 'violationAction',
            'violation_audit': 'violationAudit',
            'allowed_client_ips': 'allowedClientIps',
            'allowed_client_os_usernames': 'allowedClientOsUsernames',
            'allowed_client_programs': 'allowedClientPrograms',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._security_policy_id = None
        self._db_user_name = None
        self._sql_level = None
        self._status = None
        self._enforcement_scope = None
        self._violation_action = None
        self._violation_audit = None
        self._allowed_client_ips = None
        self._allowed_client_os_usernames = None
        self._allowed_client_programs = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SqlFirewallPolicy.
        The OCID of the SQL Firewall policy.


        :return: The id of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SqlFirewallPolicy.
        The OCID of the SQL Firewall policy.


        :param id: The id of this SqlFirewallPolicy.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SqlFirewallPolicy.
        The OCID of the compartment containing the SQL Firewall policy.


        :return: The compartment_id of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SqlFirewallPolicy.
        The OCID of the compartment containing the SQL Firewall policy.


        :param compartment_id: The compartment_id of this SqlFirewallPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SqlFirewallPolicy.
        The display name of the SQL Firewall policy.


        :return: The display_name of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SqlFirewallPolicy.
        The display name of the SQL Firewall policy.


        :param display_name: The display_name of this SqlFirewallPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SqlFirewallPolicy.
        The description of the SQL Firewall policy.


        :return: The description of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SqlFirewallPolicy.
        The description of the SQL Firewall policy.


        :param description: The description of this SqlFirewallPolicy.
        :type: str
        """
        self._description = description

    @property
    def security_policy_id(self):
        """
        **[Required]** Gets the security_policy_id of this SqlFirewallPolicy.
        The OCID of the security policy corresponding to the SQL Firewall policy.


        :return: The security_policy_id of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        """
        Sets the security_policy_id of this SqlFirewallPolicy.
        The OCID of the security policy corresponding to the SQL Firewall policy.


        :param security_policy_id: The security_policy_id of this SqlFirewallPolicy.
        :type: str
        """
        self._security_policy_id = security_policy_id

    @property
    def db_user_name(self):
        """
        **[Required]** Gets the db_user_name of this SqlFirewallPolicy.
        The database user name.


        :return: The db_user_name of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """
        Sets the db_user_name of this SqlFirewallPolicy.
        The database user name.


        :param db_user_name: The db_user_name of this SqlFirewallPolicy.
        :type: str
        """
        self._db_user_name = db_user_name

    @property
    def sql_level(self):
        """
        Gets the sql_level of this SqlFirewallPolicy.
        Specifies the level of SQL included for this SQL Firewall policy.
        USER_ISSUED_SQL - User issued SQL statements only.
        ALL_SQL - Includes all SQL statements including SQL statement issued inside PL/SQL units.

        Allowed values for this property are: "USER_ISSUED_SQL", "ALL_SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The sql_level of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._sql_level

    @sql_level.setter
    def sql_level(self, sql_level):
        """
        Sets the sql_level of this SqlFirewallPolicy.
        Specifies the level of SQL included for this SQL Firewall policy.
        USER_ISSUED_SQL - User issued SQL statements only.
        ALL_SQL - Includes all SQL statements including SQL statement issued inside PL/SQL units.


        :param sql_level: The sql_level of this SqlFirewallPolicy.
        :type: str
        """
        allowed_values = ["USER_ISSUED_SQL", "ALL_SQL"]
        if not value_allowed_none_or_none_sentinel(sql_level, allowed_values):
            sql_level = 'UNKNOWN_ENUM_VALUE'
        self._sql_level = sql_level

    @property
    def status(self):
        """
        **[Required]** Gets the status of this SqlFirewallPolicy.
        Specifies whether the SQL Firewall policy is enabled or disabled.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SqlFirewallPolicy.
        Specifies whether the SQL Firewall policy is enabled or disabled.


        :param status: The status of this SqlFirewallPolicy.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def enforcement_scope(self):
        """
        Gets the enforcement_scope of this SqlFirewallPolicy.
        Specifies the SQL Firewall policy enforcement option.

        Allowed values for this property are: "ENFORCE_CONTEXT", "ENFORCE_SQL", "ENFORCE_ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The enforcement_scope of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._enforcement_scope

    @enforcement_scope.setter
    def enforcement_scope(self, enforcement_scope):
        """
        Sets the enforcement_scope of this SqlFirewallPolicy.
        Specifies the SQL Firewall policy enforcement option.


        :param enforcement_scope: The enforcement_scope of this SqlFirewallPolicy.
        :type: str
        """
        allowed_values = ["ENFORCE_CONTEXT", "ENFORCE_SQL", "ENFORCE_ALL"]
        if not value_allowed_none_or_none_sentinel(enforcement_scope, allowed_values):
            enforcement_scope = 'UNKNOWN_ENUM_VALUE'
        self._enforcement_scope = enforcement_scope

    @property
    def violation_action(self):
        """
        Gets the violation_action of this SqlFirewallPolicy.
        Specifies the mode in which the SQL Firewall policy is enabled.

        Allowed values for this property are: "BLOCK", "OBSERVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The violation_action of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._violation_action

    @violation_action.setter
    def violation_action(self, violation_action):
        """
        Sets the violation_action of this SqlFirewallPolicy.
        Specifies the mode in which the SQL Firewall policy is enabled.


        :param violation_action: The violation_action of this SqlFirewallPolicy.
        :type: str
        """
        allowed_values = ["BLOCK", "OBSERVE"]
        if not value_allowed_none_or_none_sentinel(violation_action, allowed_values):
            violation_action = 'UNKNOWN_ENUM_VALUE'
        self._violation_action = violation_action

    @property
    def violation_audit(self):
        """
        Gets the violation_audit of this SqlFirewallPolicy.
        Specifies whether a unified audit policy should be enabled for auditing the SQL Firewall policy violations.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The violation_audit of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._violation_audit

    @violation_audit.setter
    def violation_audit(self, violation_audit):
        """
        Sets the violation_audit of this SqlFirewallPolicy.
        Specifies whether a unified audit policy should be enabled for auditing the SQL Firewall policy violations.


        :param violation_audit: The violation_audit of this SqlFirewallPolicy.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(violation_audit, allowed_values):
            violation_audit = 'UNKNOWN_ENUM_VALUE'
        self._violation_audit = violation_audit

    @property
    def allowed_client_ips(self):
        """
        Gets the allowed_client_ips of this SqlFirewallPolicy.
        The list of allowed ip addresses for the SQL Firewall policy.


        :return: The allowed_client_ips of this SqlFirewallPolicy.
        :rtype: list[str]
        """
        return self._allowed_client_ips

    @allowed_client_ips.setter
    def allowed_client_ips(self, allowed_client_ips):
        """
        Sets the allowed_client_ips of this SqlFirewallPolicy.
        The list of allowed ip addresses for the SQL Firewall policy.


        :param allowed_client_ips: The allowed_client_ips of this SqlFirewallPolicy.
        :type: list[str]
        """
        self._allowed_client_ips = allowed_client_ips

    @property
    def allowed_client_os_usernames(self):
        """
        Gets the allowed_client_os_usernames of this SqlFirewallPolicy.
        The list of allowed operating system user names for the SQL Firewall policy.


        :return: The allowed_client_os_usernames of this SqlFirewallPolicy.
        :rtype: list[str]
        """
        return self._allowed_client_os_usernames

    @allowed_client_os_usernames.setter
    def allowed_client_os_usernames(self, allowed_client_os_usernames):
        """
        Sets the allowed_client_os_usernames of this SqlFirewallPolicy.
        The list of allowed operating system user names for the SQL Firewall policy.


        :param allowed_client_os_usernames: The allowed_client_os_usernames of this SqlFirewallPolicy.
        :type: list[str]
        """
        self._allowed_client_os_usernames = allowed_client_os_usernames

    @property
    def allowed_client_programs(self):
        """
        Gets the allowed_client_programs of this SqlFirewallPolicy.
        The list of allowed client programs for the SQL Firewall policy.


        :return: The allowed_client_programs of this SqlFirewallPolicy.
        :rtype: list[str]
        """
        return self._allowed_client_programs

    @allowed_client_programs.setter
    def allowed_client_programs(self, allowed_client_programs):
        """
        Sets the allowed_client_programs of this SqlFirewallPolicy.
        The list of allowed client programs for the SQL Firewall policy.


        :param allowed_client_programs: The allowed_client_programs of this SqlFirewallPolicy.
        :type: list[str]
        """
        self._allowed_client_programs = allowed_client_programs

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SqlFirewallPolicy.
        The time that the SQL Firewall policy was created, in the format defined by RFC3339.


        :return: The time_created of this SqlFirewallPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlFirewallPolicy.
        The time that the SQL Firewall policy was created, in the format defined by RFC3339.


        :param time_created: The time_created of this SqlFirewallPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SqlFirewallPolicy.
        The date and time the SQL Firewall policy was last updated, in the format defined by RFC3339.


        :return: The time_updated of this SqlFirewallPolicy.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SqlFirewallPolicy.
        The date and time the SQL Firewall policy was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this SqlFirewallPolicy.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SqlFirewallPolicy.
        The current state of the SQL Firewall policy.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SqlFirewallPolicy.
        The current state of the SQL Firewall policy.


        :param lifecycle_state: The lifecycle_state of this SqlFirewallPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SqlFirewallPolicy.
        Details about the current state of the SQL Firewall policy in Data Safe.


        :return: The lifecycle_details of this SqlFirewallPolicy.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SqlFirewallPolicy.
        Details about the current state of the SQL Firewall policy in Data Safe.


        :param lifecycle_details: The lifecycle_details of this SqlFirewallPolicy.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SqlFirewallPolicy.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SqlFirewallPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SqlFirewallPolicy.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SqlFirewallPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SqlFirewallPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SqlFirewallPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SqlFirewallPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SqlFirewallPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SqlFirewallPolicy.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this SqlFirewallPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SqlFirewallPolicy.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this SqlFirewallPolicy.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
