# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Dkim(object):
    """
    The properties that define a DKIM.
    """

    #: A constant which can be used with the lifecycle_state property of a Dkim.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Dkim.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Dkim.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Dkim.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Dkim.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Dkim.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Dkim.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a Dkim.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new Dkim object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Dkim.
        :type name: str

        :param id:
            The value to assign to the id property of this Dkim.
        :type id: str

        :param email_domain_id:
            The value to assign to the email_domain_id property of this Dkim.
        :type email_domain_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Dkim.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Dkim.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED", "INACTIVE", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Dkim.
        :type lifecycle_details: str

        :param description:
            The value to assign to the description property of this Dkim.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Dkim.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Dkim.
        :type time_updated: datetime

        :param dns_subdomain_name:
            The value to assign to the dns_subdomain_name property of this Dkim.
        :type dns_subdomain_name: str

        :param cname_record_value:
            The value to assign to the cname_record_value property of this Dkim.
        :type cname_record_value: str

        :param txt_record_value:
            The value to assign to the txt_record_value property of this Dkim.
        :type txt_record_value: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Dkim.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Dkim.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Dkim.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'email_domain_id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'dns_subdomain_name': 'str',
            'cname_record_value': 'str',
            'txt_record_value': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'email_domain_id': 'emailDomainId',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'dns_subdomain_name': 'dnsSubdomainName',
            'cname_record_value': 'cnameRecordValue',
            'txt_record_value': 'txtRecordValue',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._name = None
        self._id = None
        self._email_domain_id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._dns_subdomain_name = None
        self._cname_record_value = None
        self._txt_record_value = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Dkim.
        The DKIM selector.
        If the same domain is managed in more than one region, each region must use different selectors.


        :return: The name of this Dkim.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Dkim.
        The DKIM selector.
        If the same domain is managed in more than one region, each region must use different selectors.


        :param name: The name of this Dkim.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Dkim.
        The `OCID`__ of the DKIM.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Dkim.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Dkim.
        The `OCID`__ of the DKIM.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Dkim.
        :type: str
        """
        self._id = id

    @property
    def email_domain_id(self):
        """
        **[Required]** Gets the email_domain_id of this Dkim.
        The `OCID`__ of the email domain
        that this DKIM belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The email_domain_id of this Dkim.
        :rtype: str
        """
        return self._email_domain_id

    @email_domain_id.setter
    def email_domain_id(self, email_domain_id):
        """
        Sets the email_domain_id of this Dkim.
        The `OCID`__ of the email domain
        that this DKIM belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param email_domain_id: The email_domain_id of this Dkim.
        :type: str
        """
        self._email_domain_id = email_domain_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Dkim.
        The `OCID`__ of the compartment that contains this DKIM.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Dkim.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Dkim.
        The `OCID`__ of the compartment that contains this DKIM.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Dkim.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Dkim.
        The current state of the DKIM.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED", "INACTIVE", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Dkim.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Dkim.
        The current state of the DKIM.


        :param lifecycle_state: The lifecycle_state of this Dkim.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED", "INACTIVE", "NEEDS_ATTENTION", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Dkim.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource.


        :return: The lifecycle_details of this Dkim.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Dkim.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource.


        :param lifecycle_details: The lifecycle_details of this Dkim.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def description(self):
        """
        Gets the description of this Dkim.
        The description of the DKIM. Avoid entering confidential information.


        :return: The description of this Dkim.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Dkim.
        The description of the DKIM. Avoid entering confidential information.


        :param description: The description of this Dkim.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Dkim.
        The time the DKIM was created.
        Times are expressed in `RFC 3339`__
        timestamp format, \"YYYY-MM-ddThh:mmZ\".

        Example: `2021-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Dkim.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Dkim.
        The time the DKIM was created.
        Times are expressed in `RFC 3339`__
        timestamp format, \"YYYY-MM-ddThh:mmZ\".

        Example: `2021-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Dkim.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Dkim.
        The time of the last change to the DKIM configuration, due to a state change or
        an update operation.
        Times are expressed in `RFC 3339`__
        timestamp format, \"YYYY-MM-ddThh:mmZ\".

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Dkim.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Dkim.
        The time of the last change to the DKIM configuration, due to a state change or
        an update operation.
        Times are expressed in `RFC 3339`__
        timestamp format, \"YYYY-MM-ddThh:mmZ\".

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Dkim.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def dns_subdomain_name(self):
        """
        Gets the dns_subdomain_name of this Dkim.
        The name of the DNS subdomain that must be provisioned to enable email recipients to verify DKIM signatures.
        It is usually created with a CNAME record set to the cnameRecordValue


        :return: The dns_subdomain_name of this Dkim.
        :rtype: str
        """
        return self._dns_subdomain_name

    @dns_subdomain_name.setter
    def dns_subdomain_name(self, dns_subdomain_name):
        """
        Sets the dns_subdomain_name of this Dkim.
        The name of the DNS subdomain that must be provisioned to enable email recipients to verify DKIM signatures.
        It is usually created with a CNAME record set to the cnameRecordValue


        :param dns_subdomain_name: The dns_subdomain_name of this Dkim.
        :type: str
        """
        self._dns_subdomain_name = dns_subdomain_name

    @property
    def cname_record_value(self):
        """
        Gets the cname_record_value of this Dkim.
        The DNS CNAME record value to provision to the DKIM DNS subdomain, when using the CNAME method for DKIM setup (preferred).


        :return: The cname_record_value of this Dkim.
        :rtype: str
        """
        return self._cname_record_value

    @cname_record_value.setter
    def cname_record_value(self, cname_record_value):
        """
        Sets the cname_record_value of this Dkim.
        The DNS CNAME record value to provision to the DKIM DNS subdomain, when using the CNAME method for DKIM setup (preferred).


        :param cname_record_value: The cname_record_value of this Dkim.
        :type: str
        """
        self._cname_record_value = cname_record_value

    @property
    def txt_record_value(self):
        """
        Gets the txt_record_value of this Dkim.
        The DNS TXT record value to provision to the DKIM DNS subdomain in place of using a CNAME record.
        This is used in cases where a CNAME can not be used, such as when the cnameRecordValue would exceed the maximum length for a DNS entry.
        This can also be used by customers who have an existing procedure to directly provision TXT records for DKIM.
        Be aware that many DNS APIs will require you to break this string into segments of less than 255 characters.


        :return: The txt_record_value of this Dkim.
        :rtype: str
        """
        return self._txt_record_value

    @txt_record_value.setter
    def txt_record_value(self, txt_record_value):
        """
        Sets the txt_record_value of this Dkim.
        The DNS TXT record value to provision to the DKIM DNS subdomain in place of using a CNAME record.
        This is used in cases where a CNAME can not be used, such as when the cnameRecordValue would exceed the maximum length for a DNS entry.
        This can also be used by customers who have an existing procedure to directly provision TXT records for DKIM.
        Be aware that many DNS APIs will require you to break this string into segments of less than 255 characters.


        :param txt_record_value: The txt_record_value of this Dkim.
        :type: str
        """
        self._txt_record_value = txt_record_value

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Dkim.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Dkim.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Dkim.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Dkim.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Dkim.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Dkim.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Dkim.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Dkim.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Dkim.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Dkim.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Dkim.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Dkim.
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