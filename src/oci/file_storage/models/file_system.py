# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FileSystem(object):
    """
    An NFS file system. To allow access to a file system, add it
    to an export set and associate the export set with a mount
    target. The same file system can be in multiple export sets and
    associated with multiple mount targets.

    To use any of the API operations, you must be authorized in an
    IAM policy. If you're not authorized, talk to an
    administrator. If you're an administrator who needs to write
    policies to give users access, see `Getting Started with
    Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the clone_attach_status property of a FileSystem.
    #: This constant has a value of "ATTACHED"
    CLONE_ATTACH_STATUS_ATTACHED = "ATTACHED"

    #: A constant which can be used with the clone_attach_status property of a FileSystem.
    #: This constant has a value of "DETACHING"
    CLONE_ATTACH_STATUS_DETACHING = "DETACHING"

    #: A constant which can be used with the clone_attach_status property of a FileSystem.
    #: This constant has a value of "DETACHED"
    CLONE_ATTACH_STATUS_DETACHED = "DETACHED"

    #: A constant which can be used with the quota_enforcement_state property of a FileSystem.
    #: This constant has a value of "ENABLING"
    QUOTA_ENFORCEMENT_STATE_ENABLING = "ENABLING"

    #: A constant which can be used with the quota_enforcement_state property of a FileSystem.
    #: This constant has a value of "ENABLED"
    QUOTA_ENFORCEMENT_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the quota_enforcement_state property of a FileSystem.
    #: This constant has a value of "DISABLING"
    QUOTA_ENFORCEMENT_STATE_DISABLING = "DISABLING"

    #: A constant which can be used with the quota_enforcement_state property of a FileSystem.
    #: This constant has a value of "DISABLED"
    QUOTA_ENFORCEMENT_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the quota_enforcement_state property of a FileSystem.
    #: This constant has a value of "SYNCING"
    QUOTA_ENFORCEMENT_STATE_SYNCING = "SYNCING"

    #: A constant which can be used with the quota_enforcement_state property of a FileSystem.
    #: This constant has a value of "FAILED"
    QUOTA_ENFORCEMENT_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new FileSystem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this FileSystem.
        :type availability_domain: str

        :param metered_bytes:
            The value to assign to the metered_bytes property of this FileSystem.
        :type metered_bytes: int

        :param compartment_id:
            The value to assign to the compartment_id property of this FileSystem.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this FileSystem.
        :type display_name: str

        :param id:
            The value to assign to the id property of this FileSystem.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FileSystem.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this FileSystem.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FileSystem.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FileSystem.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this FileSystem.
        :type system_tags: dict(str, dict(str, object))

        :param kms_key_id:
            The value to assign to the kms_key_id property of this FileSystem.
        :type kms_key_id: str

        :param source_details:
            The value to assign to the source_details property of this FileSystem.
        :type source_details: oci.file_storage.models.SourceDetails

        :param is_clone_parent:
            The value to assign to the is_clone_parent property of this FileSystem.
        :type is_clone_parent: bool

        :param is_hydrated:
            The value to assign to the is_hydrated property of this FileSystem.
        :type is_hydrated: bool

        :param clone_count:
            The value to assign to the clone_count property of this FileSystem.
        :type clone_count: int

        :param clone_attach_status:
            The value to assign to the clone_attach_status property of this FileSystem.
            Allowed values for this property are: "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type clone_attach_status: str

        :param locks:
            The value to assign to the locks property of this FileSystem.
        :type locks: list[oci.file_storage.models.ResourceLock]

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FileSystem.
        :type lifecycle_details: str

        :param is_targetable:
            The value to assign to the is_targetable property of this FileSystem.
        :type is_targetable: bool

        :param replication_target_id:
            The value to assign to the replication_target_id property of this FileSystem.
        :type replication_target_id: str

        :param filesystem_snapshot_policy_id:
            The value to assign to the filesystem_snapshot_policy_id property of this FileSystem.
        :type filesystem_snapshot_policy_id: str

        :param are_quota_rules_enabled:
            The value to assign to the are_quota_rules_enabled property of this FileSystem.
        :type are_quota_rules_enabled: bool

        :param quota_enforcement_state:
            The value to assign to the quota_enforcement_state property of this FileSystem.
            Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "DISABLED", "SYNCING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type quota_enforcement_state: str

        :param replication_source_count:
            The value to assign to the replication_source_count property of this FileSystem.
        :type replication_source_count: int

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'metered_bytes': 'int',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'kms_key_id': 'str',
            'source_details': 'SourceDetails',
            'is_clone_parent': 'bool',
            'is_hydrated': 'bool',
            'clone_count': 'int',
            'clone_attach_status': 'str',
            'locks': 'list[ResourceLock]',
            'lifecycle_details': 'str',
            'is_targetable': 'bool',
            'replication_target_id': 'str',
            'filesystem_snapshot_policy_id': 'str',
            'are_quota_rules_enabled': 'bool',
            'quota_enforcement_state': 'str',
            'replication_source_count': 'int'
        }
        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'metered_bytes': 'meteredBytes',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'kms_key_id': 'kmsKeyId',
            'source_details': 'sourceDetails',
            'is_clone_parent': 'isCloneParent',
            'is_hydrated': 'isHydrated',
            'clone_count': 'cloneCount',
            'clone_attach_status': 'cloneAttachStatus',
            'locks': 'locks',
            'lifecycle_details': 'lifecycleDetails',
            'is_targetable': 'isTargetable',
            'replication_target_id': 'replicationTargetId',
            'filesystem_snapshot_policy_id': 'filesystemSnapshotPolicyId',
            'are_quota_rules_enabled': 'areQuotaRulesEnabled',
            'quota_enforcement_state': 'quotaEnforcementState',
            'replication_source_count': 'replicationSourceCount'
        }
        self._availability_domain = None
        self._metered_bytes = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._kms_key_id = None
        self._source_details = None
        self._is_clone_parent = None
        self._is_hydrated = None
        self._clone_count = None
        self._clone_attach_status = None
        self._locks = None
        self._lifecycle_details = None
        self._is_targetable = None
        self._replication_target_id = None
        self._filesystem_snapshot_policy_id = None
        self._are_quota_rules_enabled = None
        self._quota_enforcement_state = None
        self._replication_source_count = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this FileSystem.
        The availability domain the file system is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this FileSystem.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this FileSystem.
        The availability domain the file system is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this FileSystem.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def metered_bytes(self):
        """
        **[Required]** Gets the metered_bytes of this FileSystem.
        The number of bytes consumed by the file system, including
        any snapshots. This number reflects the metered size of the file
        system and is updated asynchronously with respect to
        updates to the file system.
        For more information, see `File System Usage and Metering`__.

        __ https://docs.cloud.oracle.com/Content/File/Concepts/FSutilization.htm


        :return: The metered_bytes of this FileSystem.
        :rtype: int
        """
        return self._metered_bytes

    @metered_bytes.setter
    def metered_bytes(self, metered_bytes):
        """
        Sets the metered_bytes of this FileSystem.
        The number of bytes consumed by the file system, including
        any snapshots. This number reflects the metered size of the file
        system and is updated asynchronously with respect to
        updates to the file system.
        For more information, see `File System Usage and Metering`__.

        __ https://docs.cloud.oracle.com/Content/File/Concepts/FSutilization.htm


        :param metered_bytes: The metered_bytes of this FileSystem.
        :type: int
        """
        self._metered_bytes = metered_bytes

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FileSystem.
        The `OCID`__ of the compartment that contains the file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this FileSystem.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FileSystem.
        The `OCID`__ of the compartment that contains the file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this FileSystem.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this FileSystem.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My file system`


        :return: The display_name of this FileSystem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FileSystem.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My file system`


        :param display_name: The display_name of this FileSystem.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FileSystem.
        The `OCID`__ of the file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this FileSystem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FileSystem.
        The `OCID`__ of the file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this FileSystem.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FileSystem.
        The current state of the file system.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FileSystem.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FileSystem.
        The current state of the file system.


        :param lifecycle_state: The lifecycle_state of this FileSystem.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this FileSystem.
        The date and time the file system was created, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this FileSystem.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FileSystem.
        The date and time the file system was created, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this FileSystem.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FileSystem.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this FileSystem.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FileSystem.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this FileSystem.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FileSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this FileSystem.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FileSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this FileSystem.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this FileSystem.
        System tags for this resource.
        System tags are applied to resources by internal OCI services.


        :return: The system_tags of this FileSystem.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this FileSystem.
        System tags for this resource.
        System tags are applied to resources by internal OCI services.


        :param system_tags: The system_tags of this FileSystem.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this FileSystem.
        The `OCID`__ of the KMS key which is the master encryption key for the file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_id of this FileSystem.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this FileSystem.
        The `OCID`__ of the KMS key which is the master encryption key for the file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_id: The kms_key_id of this FileSystem.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def source_details(self):
        """
        Gets the source_details of this FileSystem.

        :return: The source_details of this FileSystem.
        :rtype: oci.file_storage.models.SourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this FileSystem.

        :param source_details: The source_details of this FileSystem.
        :type: oci.file_storage.models.SourceDetails
        """
        self._source_details = source_details

    @property
    def is_clone_parent(self):
        """
        Gets the is_clone_parent of this FileSystem.
        Specifies whether the file system has been cloned.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :return: The is_clone_parent of this FileSystem.
        :rtype: bool
        """
        return self._is_clone_parent

    @is_clone_parent.setter
    def is_clone_parent(self, is_clone_parent):
        """
        Sets the is_clone_parent of this FileSystem.
        Specifies whether the file system has been cloned.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :param is_clone_parent: The is_clone_parent of this FileSystem.
        :type: bool
        """
        self._is_clone_parent = is_clone_parent

    @property
    def is_hydrated(self):
        """
        Gets the is_hydrated of this FileSystem.
        Specifies whether the data has finished copying from the source to the clone.
        Hydration can take up to several hours to complete depending on the size of the source.
        The source and clone remain available during hydration, but there may be some performance impact.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm#hydration


        :return: The is_hydrated of this FileSystem.
        :rtype: bool
        """
        return self._is_hydrated

    @is_hydrated.setter
    def is_hydrated(self, is_hydrated):
        """
        Sets the is_hydrated of this FileSystem.
        Specifies whether the data has finished copying from the source to the clone.
        Hydration can take up to several hours to complete depending on the size of the source.
        The source and clone remain available during hydration, but there may be some performance impact.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm#hydration


        :param is_hydrated: The is_hydrated of this FileSystem.
        :type: bool
        """
        self._is_hydrated = is_hydrated

    @property
    def clone_count(self):
        """
        Gets the clone_count of this FileSystem.
        Specifies the total number of children of a file system.


        :return: The clone_count of this FileSystem.
        :rtype: int
        """
        return self._clone_count

    @clone_count.setter
    def clone_count(self, clone_count):
        """
        Sets the clone_count of this FileSystem.
        Specifies the total number of children of a file system.


        :param clone_count: The clone_count of this FileSystem.
        :type: int
        """
        self._clone_count = clone_count

    @property
    def clone_attach_status(self):
        """
        Gets the clone_attach_status of this FileSystem.
        Specifies whether the file system is attached to its parent file system.

        Allowed values for this property are: "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The clone_attach_status of this FileSystem.
        :rtype: str
        """
        return self._clone_attach_status

    @clone_attach_status.setter
    def clone_attach_status(self, clone_attach_status):
        """
        Sets the clone_attach_status of this FileSystem.
        Specifies whether the file system is attached to its parent file system.


        :param clone_attach_status: The clone_attach_status of this FileSystem.
        :type: str
        """
        allowed_values = ["ATTACHED", "DETACHING", "DETACHED"]
        if not value_allowed_none_or_none_sentinel(clone_attach_status, allowed_values):
            clone_attach_status = 'UNKNOWN_ENUM_VALUE'
        self._clone_attach_status = clone_attach_status

    @property
    def locks(self):
        """
        Gets the locks of this FileSystem.
        Locks associated with this resource.


        :return: The locks of this FileSystem.
        :rtype: list[oci.file_storage.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this FileSystem.
        Locks associated with this resource.


        :param locks: The locks of this FileSystem.
        :type: list[oci.file_storage.models.ResourceLock]
        """
        self._locks = locks

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this FileSystem.
        Additional information about the current 'lifecycleState'.


        :return: The lifecycle_details of this FileSystem.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this FileSystem.
        Additional information about the current 'lifecycleState'.


        :param lifecycle_details: The lifecycle_details of this FileSystem.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def is_targetable(self):
        """
        Gets the is_targetable of this FileSystem.
        Specifies whether the file system can be used as a target file system for replication. The system sets this value to `true` if the file system is unexported, hasn't yet been specified as a target file system in any replication resource, and has no user snapshots. After the file system has been specified as a target in a replication, or if the file system contains user snapshots, the system sets this value to `false`.
        For more information, see `Using Replication`__.

        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/using-replication.htm


        :return: The is_targetable of this FileSystem.
        :rtype: bool
        """
        return self._is_targetable

    @is_targetable.setter
    def is_targetable(self, is_targetable):
        """
        Sets the is_targetable of this FileSystem.
        Specifies whether the file system can be used as a target file system for replication. The system sets this value to `true` if the file system is unexported, hasn't yet been specified as a target file system in any replication resource, and has no user snapshots. After the file system has been specified as a target in a replication, or if the file system contains user snapshots, the system sets this value to `false`.
        For more information, see `Using Replication`__.

        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/using-replication.htm


        :param is_targetable: The is_targetable of this FileSystem.
        :type: bool
        """
        self._is_targetable = is_targetable

    @property
    def replication_target_id(self):
        """
        Gets the replication_target_id of this FileSystem.
        The `OCID`__ of the replication target associated with the file system.
        Empty if the file system is not being used as target in a replication.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The replication_target_id of this FileSystem.
        :rtype: str
        """
        return self._replication_target_id

    @replication_target_id.setter
    def replication_target_id(self, replication_target_id):
        """
        Sets the replication_target_id of this FileSystem.
        The `OCID`__ of the replication target associated with the file system.
        Empty if the file system is not being used as target in a replication.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param replication_target_id: The replication_target_id of this FileSystem.
        :type: str
        """
        self._replication_target_id = replication_target_id

    @property
    def filesystem_snapshot_policy_id(self):
        """
        Gets the filesystem_snapshot_policy_id of this FileSystem.
        The `OCID`__ of the associated file system snapshot policy, which
        controls the frequency of snapshot creation and retention period of the taken snapshots.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The filesystem_snapshot_policy_id of this FileSystem.
        :rtype: str
        """
        return self._filesystem_snapshot_policy_id

    @filesystem_snapshot_policy_id.setter
    def filesystem_snapshot_policy_id(self, filesystem_snapshot_policy_id):
        """
        Sets the filesystem_snapshot_policy_id of this FileSystem.
        The `OCID`__ of the associated file system snapshot policy, which
        controls the frequency of snapshot creation and retention period of the taken snapshots.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param filesystem_snapshot_policy_id: The filesystem_snapshot_policy_id of this FileSystem.
        :type: str
        """
        self._filesystem_snapshot_policy_id = filesystem_snapshot_policy_id

    @property
    def are_quota_rules_enabled(self):
        """
        Gets the are_quota_rules_enabled of this FileSystem.
        Specifies the enforcement of quota rules on the file system.


        :return: The are_quota_rules_enabled of this FileSystem.
        :rtype: bool
        """
        return self._are_quota_rules_enabled

    @are_quota_rules_enabled.setter
    def are_quota_rules_enabled(self, are_quota_rules_enabled):
        """
        Sets the are_quota_rules_enabled of this FileSystem.
        Specifies the enforcement of quota rules on the file system.


        :param are_quota_rules_enabled: The are_quota_rules_enabled of this FileSystem.
        :type: bool
        """
        self._are_quota_rules_enabled = are_quota_rules_enabled

    @property
    def quota_enforcement_state(self):
        """
        Gets the quota_enforcement_state of this FileSystem.
        Displays the state of enforcement of quota rules on the file system.

        Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "DISABLED", "SYNCING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The quota_enforcement_state of this FileSystem.
        :rtype: str
        """
        return self._quota_enforcement_state

    @quota_enforcement_state.setter
    def quota_enforcement_state(self, quota_enforcement_state):
        """
        Sets the quota_enforcement_state of this FileSystem.
        Displays the state of enforcement of quota rules on the file system.


        :param quota_enforcement_state: The quota_enforcement_state of this FileSystem.
        :type: str
        """
        allowed_values = ["ENABLING", "ENABLED", "DISABLING", "DISABLED", "SYNCING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(quota_enforcement_state, allowed_values):
            quota_enforcement_state = 'UNKNOWN_ENUM_VALUE'
        self._quota_enforcement_state = quota_enforcement_state

    @property
    def replication_source_count(self):
        """
        Gets the replication_source_count of this FileSystem.
        Specifies the total number of replications for which this file system is a source.


        :return: The replication_source_count of this FileSystem.
        :rtype: int
        """
        return self._replication_source_count

    @replication_source_count.setter
    def replication_source_count(self, replication_source_count):
        """
        Sets the replication_source_count of this FileSystem.
        Specifies the total number of replications for which this file system is a source.


        :param replication_source_count: The replication_source_count of this FileSystem.
        :type: int
        """
        self._replication_source_count = replication_source_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
