# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Resource(object):
    """
    Details of cloud guard resource
    """

    #: A constant which can be used with the risk_level property of a Resource.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a Resource.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a Resource.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a Resource.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a Resource.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    #: A constant which can be used with the risk_level property of a Resource.
    #: This constant has a value of "NONE"
    RISK_LEVEL_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new Resource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Resource.
        :type id: str

        :param resource_name:
            The value to assign to the resource_name property of this Resource.
        :type resource_name: str

        :param resource_type:
            The value to assign to the resource_type property of this Resource.
        :type resource_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Resource.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this Resource.
        :type target_id: str

        :param target_name:
            The value to assign to the target_name property of this Resource.
        :type target_name: str

        :param region:
            The value to assign to the region property of this Resource.
        :type region: str

        :param risk_level:
            The value to assign to the risk_level property of this Resource.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param time_first_monitored:
            The value to assign to the time_first_monitored property of this Resource.
        :type time_first_monitored: datetime

        :param time_last_monitored:
            The value to assign to the time_last_monitored property of this Resource.
        :type time_last_monitored: datetime

        :param problem_count:
            The value to assign to the problem_count property of this Resource.
        :type problem_count: int

        :param vulnerability_count:
            The value to assign to the vulnerability_count property of this Resource.
        :type vulnerability_count: int

        :param open_ports_count:
            The value to assign to the open_ports_count property of this Resource.
        :type open_ports_count: int

        :param additional_details:
            The value to assign to the additional_details property of this Resource.
        :type additional_details: oci.cloud_guard.models.ResourceAdditionalDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Resource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Resource.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Resource.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'resource_name': 'str',
            'resource_type': 'str',
            'compartment_id': 'str',
            'target_id': 'str',
            'target_name': 'str',
            'region': 'str',
            'risk_level': 'str',
            'time_first_monitored': 'datetime',
            'time_last_monitored': 'datetime',
            'problem_count': 'int',
            'vulnerability_count': 'int',
            'open_ports_count': 'int',
            'additional_details': 'ResourceAdditionalDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'resource_name': 'resourceName',
            'resource_type': 'resourceType',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'target_name': 'targetName',
            'region': 'region',
            'risk_level': 'riskLevel',
            'time_first_monitored': 'timeFirstMonitored',
            'time_last_monitored': 'timeLastMonitored',
            'problem_count': 'problemCount',
            'vulnerability_count': 'vulnerabilityCount',
            'open_ports_count': 'openPortsCount',
            'additional_details': 'additionalDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._resource_name = None
        self._resource_type = None
        self._compartment_id = None
        self._target_id = None
        self._target_name = None
        self._region = None
        self._risk_level = None
        self._time_first_monitored = None
        self._time_last_monitored = None
        self._problem_count = None
        self._vulnerability_count = None
        self._open_ports_count = None
        self._additional_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Resource.
        Ocid for CG resource


        :return: The id of this Resource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Resource.
        Ocid for CG resource


        :param id: The id of this Resource.
        :type: str
        """
        self._id = id

    @property
    def resource_name(self):
        """
        Gets the resource_name of this Resource.
        Name for the CG resource


        :return: The resource_name of this Resource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this Resource.
        Name for the CG resource


        :param resource_name: The resource_name of this Resource.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this Resource.
        resource type of the CG resource


        :return: The resource_type of this Resource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this Resource.
        resource type of the CG resource


        :param resource_type: The resource_type of this Resource.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Resource.
        CompartmentId of CG Resource


        :return: The compartment_id of this Resource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Resource.
        CompartmentId of CG Resource


        :param compartment_id: The compartment_id of this Resource.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this Resource.
        TargetId of CG Resource


        :return: The target_id of this Resource.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this Resource.
        TargetId of CG Resource


        :param target_id: The target_id of this Resource.
        :type: str
        """
        self._target_id = target_id

    @property
    def target_name(self):
        """
        Gets the target_name of this Resource.
        Target name for the CG Resource


        :return: The target_name of this Resource.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """
        Sets the target_name of this Resource.
        Target name for the CG Resource


        :param target_name: The target_name of this Resource.
        :type: str
        """
        self._target_name = target_name

    @property
    def region(self):
        """
        **[Required]** Gets the region of this Resource.
        region of CG Resource


        :return: The region of this Resource.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Resource.
        region of CG Resource


        :param region: The region of this Resource.
        :type: str
        """
        self._region = region

    @property
    def risk_level(self):
        """
        Gets the risk_level of this Resource.
        The Risk Level

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this Resource.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this Resource.
        The Risk Level


        :param risk_level: The risk_level of this Resource.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", "NONE"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def time_first_monitored(self):
        """
        Gets the time_first_monitored of this Resource.
        First monitored time


        :return: The time_first_monitored of this Resource.
        :rtype: datetime
        """
        return self._time_first_monitored

    @time_first_monitored.setter
    def time_first_monitored(self, time_first_monitored):
        """
        Sets the time_first_monitored of this Resource.
        First monitored time


        :param time_first_monitored: The time_first_monitored of this Resource.
        :type: datetime
        """
        self._time_first_monitored = time_first_monitored

    @property
    def time_last_monitored(self):
        """
        Gets the time_last_monitored of this Resource.
        Last monitored time


        :return: The time_last_monitored of this Resource.
        :rtype: datetime
        """
        return self._time_last_monitored

    @time_last_monitored.setter
    def time_last_monitored(self, time_last_monitored):
        """
        Sets the time_last_monitored of this Resource.
        Last monitored time


        :param time_last_monitored: The time_last_monitored of this Resource.
        :type: datetime
        """
        self._time_last_monitored = time_last_monitored

    @property
    def problem_count(self):
        """
        Gets the problem_count of this Resource.
        Count of existing problems for a resource


        :return: The problem_count of this Resource.
        :rtype: int
        """
        return self._problem_count

    @problem_count.setter
    def problem_count(self, problem_count):
        """
        Sets the problem_count of this Resource.
        Count of existing problems for a resource


        :param problem_count: The problem_count of this Resource.
        :type: int
        """
        self._problem_count = problem_count

    @property
    def vulnerability_count(self):
        """
        Gets the vulnerability_count of this Resource.
        Count of existing number of vulnerabilities in the resource


        :return: The vulnerability_count of this Resource.
        :rtype: int
        """
        return self._vulnerability_count

    @vulnerability_count.setter
    def vulnerability_count(self, vulnerability_count):
        """
        Sets the vulnerability_count of this Resource.
        Count of existing number of vulnerabilities in the resource


        :param vulnerability_count: The vulnerability_count of this Resource.
        :type: int
        """
        self._vulnerability_count = vulnerability_count

    @property
    def open_ports_count(self):
        """
        Gets the open_ports_count of this Resource.
        Number of open ports in a resource


        :return: The open_ports_count of this Resource.
        :rtype: int
        """
        return self._open_ports_count

    @open_ports_count.setter
    def open_ports_count(self, open_ports_count):
        """
        Sets the open_ports_count of this Resource.
        Number of open ports in a resource


        :param open_ports_count: The open_ports_count of this Resource.
        :type: int
        """
        self._open_ports_count = open_ports_count

    @property
    def additional_details(self):
        """
        Gets the additional_details of this Resource.

        :return: The additional_details of this Resource.
        :rtype: oci.cloud_guard.models.ResourceAdditionalDetails
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this Resource.

        :param additional_details: The additional_details of this Resource.
        :type: oci.cloud_guard.models.ResourceAdditionalDetails
        """
        self._additional_details = additional_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Resource.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this Resource.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Resource.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this Resource.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Resource.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Resource.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Resource.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Resource.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Resource.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Resource.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Resource.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Resource.
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
