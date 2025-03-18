# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WlpAgentSummary(object):
    """
    WLP agent resource running on an on-premise resource.
    Example: `{\"id\": \"ocid1.wlpagent.oc1..exampleawwcufihrc62gpbcvbjizswgoj4w7rg5q4fwbg\",
    \"compartmentId\": \"ocid1.compartment.oc1..exampleawwcufihrc62gpbcvbjizswgoj4w7rg5q4fwbg2fauxvlcxbtliaa\",
    \"agentVersion\": \"1.0.11\",
    \"certificateId\": \"ocid1.certificate.oc1..exampleawwcufihrc62gpbcvbjizswgoj4w7oj4w7rg5q4fwbg2fauxv\"}`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WlpAgentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WlpAgentSummary.
        :type id: str

        :param host_id:
            The value to assign to the host_id property of this WlpAgentSummary.
        :type host_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this WlpAgentSummary.
        :type tenant_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WlpAgentSummary.
        :type compartment_id: str

        :param agent_version:
            The value to assign to the agent_version property of this WlpAgentSummary.
        :type agent_version: str

        :param certificate_id:
            The value to assign to the certificate_id property of this WlpAgentSummary.
        :type certificate_id: str

        :param time_created:
            The value to assign to the time_created property of this WlpAgentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this WlpAgentSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WlpAgentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WlpAgentSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this WlpAgentSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'host_id': 'str',
            'tenant_id': 'str',
            'compartment_id': 'str',
            'agent_version': 'str',
            'certificate_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'host_id': 'hostId',
            'tenant_id': 'tenantId',
            'compartment_id': 'compartmentId',
            'agent_version': 'agentVersion',
            'certificate_id': 'certificateId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._host_id = None
        self._tenant_id = None
        self._compartment_id = None
        self._agent_version = None
        self._certificate_id = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WlpAgentSummary.
        OCID for WlpAgent


        :return: The id of this WlpAgentSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WlpAgentSummary.
        OCID for WlpAgent


        :param id: The id of this WlpAgentSummary.
        :type: str
        """
        self._id = id

    @property
    def host_id(self):
        """
        Gets the host_id of this WlpAgentSummary.
        OCID for instance in which WlpAgent is installed


        :return: The host_id of this WlpAgentSummary.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this WlpAgentSummary.
        OCID for instance in which WlpAgent is installed


        :param host_id: The host_id of this WlpAgentSummary.
        :type: str
        """
        self._host_id = host_id

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this WlpAgentSummary.
        Tenant ID of the host


        :return: The tenant_id of this WlpAgentSummary.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this WlpAgentSummary.
        Tenant ID of the host


        :param tenant_id: The tenant_id of this WlpAgentSummary.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WlpAgentSummary.
        Compartment OCID of WlpAgent


        :return: The compartment_id of this WlpAgentSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WlpAgentSummary.
        Compartment OCID of WlpAgent


        :param compartment_id: The compartment_id of this WlpAgentSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def agent_version(self):
        """
        **[Required]** Gets the agent_version of this WlpAgentSummary.
        The version of the agent


        :return: The agent_version of this WlpAgentSummary.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """
        Sets the agent_version of this WlpAgentSummary.
        The version of the agent


        :param agent_version: The agent_version of this WlpAgentSummary.
        :type: str
        """
        self._agent_version = agent_version

    @property
    def certificate_id(self):
        """
        **[Required]** Gets the certificate_id of this WlpAgentSummary.
        The certificate ID returned by OCI certificates service


        :return: The certificate_id of this WlpAgentSummary.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this WlpAgentSummary.
        The certificate ID returned by OCI certificates service


        :param certificate_id: The certificate_id of this WlpAgentSummary.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def time_created(self):
        """
        Gets the time_created of this WlpAgentSummary.
        The date and time the WLP agent was created. Format defined by RFC3339.


        :return: The time_created of this WlpAgentSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WlpAgentSummary.
        The date and time the WLP agent was created. Format defined by RFC3339.


        :param time_created: The time_created of this WlpAgentSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this WlpAgentSummary.
        The date and time the WLP agent was updated. Format defined by RFC3339.


        :return: The time_updated of this WlpAgentSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this WlpAgentSummary.
        The date and time the WLP agent was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this WlpAgentSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this WlpAgentSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this WlpAgentSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this WlpAgentSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this WlpAgentSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this WlpAgentSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this WlpAgentSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this WlpAgentSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this WlpAgentSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this WlpAgentSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this WlpAgentSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this WlpAgentSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this WlpAgentSummary.
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
