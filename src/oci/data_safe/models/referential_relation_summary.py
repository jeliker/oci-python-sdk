# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReferentialRelationSummary(object):
    """
    A referential relation is a resource corresponding to a database columns.
    It's a subresource of sensitive data model resource and is always associated with a sensitive data model.
    """

    #: A constant which can be used with the lifecycle_state property of a ReferentialRelationSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ReferentialRelationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ReferentialRelationSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ReferentialRelationSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ReferentialRelationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the relation_type property of a ReferentialRelationSummary.
    #: This constant has a value of "NONE"
    RELATION_TYPE_NONE = "NONE"

    #: A constant which can be used with the relation_type property of a ReferentialRelationSummary.
    #: This constant has a value of "APP_DEFINED"
    RELATION_TYPE_APP_DEFINED = "APP_DEFINED"

    #: A constant which can be used with the relation_type property of a ReferentialRelationSummary.
    #: This constant has a value of "DB_DEFINED"
    RELATION_TYPE_DB_DEFINED = "DB_DEFINED"

    def __init__(self, **kwargs):
        """
        Initializes a new ReferentialRelationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ReferentialRelationSummary.
        :type key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ReferentialRelationSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param sensitive_data_model_id:
            The value to assign to the sensitive_data_model_id property of this ReferentialRelationSummary.
        :type sensitive_data_model_id: str

        :param relation_type:
            The value to assign to the relation_type property of this ReferentialRelationSummary.
            Allowed values for this property are: "NONE", "APP_DEFINED", "DB_DEFINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type relation_type: str

        :param parent:
            The value to assign to the parent property of this ReferentialRelationSummary.
        :type parent: oci.data_safe.models.ColumnsInfo

        :param child:
            The value to assign to the child property of this ReferentialRelationSummary.
        :type child: oci.data_safe.models.ColumnsInfo

        :param is_sensitive:
            The value to assign to the is_sensitive property of this ReferentialRelationSummary.
        :type is_sensitive: bool

        """
        self.swagger_types = {
            'key': 'str',
            'lifecycle_state': 'str',
            'sensitive_data_model_id': 'str',
            'relation_type': 'str',
            'parent': 'ColumnsInfo',
            'child': 'ColumnsInfo',
            'is_sensitive': 'bool'
        }
        self.attribute_map = {
            'key': 'key',
            'lifecycle_state': 'lifecycleState',
            'sensitive_data_model_id': 'sensitiveDataModelId',
            'relation_type': 'relationType',
            'parent': 'parent',
            'child': 'child',
            'is_sensitive': 'isSensitive'
        }
        self._key = None
        self._lifecycle_state = None
        self._sensitive_data_model_id = None
        self._relation_type = None
        self._parent = None
        self._child = None
        self._is_sensitive = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this ReferentialRelationSummary.
        The unique key that identifies the referential relation. It's numeric and unique within a sensitive data model.


        :return: The key of this ReferentialRelationSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ReferentialRelationSummary.
        The unique key that identifies the referential relation. It's numeric and unique within a sensitive data model.


        :param key: The key of this ReferentialRelationSummary.
        :type: str
        """
        self._key = key

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ReferentialRelationSummary.
        The current state of the referential relation.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ReferentialRelationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ReferentialRelationSummary.
        The current state of the referential relation.


        :param lifecycle_state: The lifecycle_state of this ReferentialRelationSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def sensitive_data_model_id(self):
        """
        **[Required]** Gets the sensitive_data_model_id of this ReferentialRelationSummary.
        The OCID of the sensitive data model that contains the sensitive column.


        :return: The sensitive_data_model_id of this ReferentialRelationSummary.
        :rtype: str
        """
        return self._sensitive_data_model_id

    @sensitive_data_model_id.setter
    def sensitive_data_model_id(self, sensitive_data_model_id):
        """
        Sets the sensitive_data_model_id of this ReferentialRelationSummary.
        The OCID of the sensitive data model that contains the sensitive column.


        :param sensitive_data_model_id: The sensitive_data_model_id of this ReferentialRelationSummary.
        :type: str
        """
        self._sensitive_data_model_id = sensitive_data_model_id

    @property
    def relation_type(self):
        """
        **[Required]** Gets the relation_type of this ReferentialRelationSummary.
        The type of referential relationship the sensitive column has with its parent. NONE indicates that the
        sensitive column does not have a parent. DB_DEFINED indicates that the relationship is defined in the database
        dictionary. APP_DEFINED indicates that the relationship is defined at the application level and not in the database dictionary.

        Allowed values for this property are: "NONE", "APP_DEFINED", "DB_DEFINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The relation_type of this ReferentialRelationSummary.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """
        Sets the relation_type of this ReferentialRelationSummary.
        The type of referential relationship the sensitive column has with its parent. NONE indicates that the
        sensitive column does not have a parent. DB_DEFINED indicates that the relationship is defined in the database
        dictionary. APP_DEFINED indicates that the relationship is defined at the application level and not in the database dictionary.


        :param relation_type: The relation_type of this ReferentialRelationSummary.
        :type: str
        """
        allowed_values = ["NONE", "APP_DEFINED", "DB_DEFINED"]
        if not value_allowed_none_or_none_sentinel(relation_type, allowed_values):
            relation_type = 'UNKNOWN_ENUM_VALUE'
        self._relation_type = relation_type

    @property
    def parent(self):
        """
        **[Required]** Gets the parent of this ReferentialRelationSummary.

        :return: The parent of this ReferentialRelationSummary.
        :rtype: oci.data_safe.models.ColumnsInfo
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ReferentialRelationSummary.

        :param parent: The parent of this ReferentialRelationSummary.
        :type: oci.data_safe.models.ColumnsInfo
        """
        self._parent = parent

    @property
    def child(self):
        """
        **[Required]** Gets the child of this ReferentialRelationSummary.

        :return: The child of this ReferentialRelationSummary.
        :rtype: oci.data_safe.models.ColumnsInfo
        """
        return self._child

    @child.setter
    def child(self, child):
        """
        Sets the child of this ReferentialRelationSummary.

        :param child: The child of this ReferentialRelationSummary.
        :type: oci.data_safe.models.ColumnsInfo
        """
        self._child = child

    @property
    def is_sensitive(self):
        """
        Gets the is_sensitive of this ReferentialRelationSummary.
        Determines if the columns present in the referential relation is present in the sensitive data model


        :return: The is_sensitive of this ReferentialRelationSummary.
        :rtype: bool
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        """
        Sets the is_sensitive of this ReferentialRelationSummary.
        Determines if the columns present in the referential relation is present in the sensitive data model


        :param is_sensitive: The is_sensitive of this ReferentialRelationSummary.
        :type: bool
        """
        self._is_sensitive = is_sensitive

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
