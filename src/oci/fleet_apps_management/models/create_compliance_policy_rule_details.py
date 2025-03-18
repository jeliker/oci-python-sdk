# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230831


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCompliancePolicyRuleDetails(object):
    """
    The data to create a CompliancePolicyRule.
    """

    #: A constant which can be used with the severity property of a CreateCompliancePolicyRuleDetails.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a CreateCompliancePolicyRuleDetails.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a CreateCompliancePolicyRuleDetails.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a CreateCompliancePolicyRuleDetails.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCompliancePolicyRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateCompliancePolicyRuleDetails.
        :type display_name: str

        :param compliance_policy_id:
            The value to assign to the compliance_policy_id property of this CreateCompliancePolicyRuleDetails.
        :type compliance_policy_id: str

        :param product_version:
            The value to assign to the product_version property of this CreateCompliancePolicyRuleDetails.
        :type product_version: oci.fleet_apps_management.models.ProductVersionDetails

        :param patch_type:
            The value to assign to the patch_type property of this CreateCompliancePolicyRuleDetails.
        :type patch_type: list[str]

        :param severity:
            The value to assign to the severity property of this CreateCompliancePolicyRuleDetails.
            Allowed values for items in this list are: "CRITICAL", "HIGH", "MEDIUM", "LOW"
        :type severity: list[str]

        :param patch_selection:
            The value to assign to the patch_selection property of this CreateCompliancePolicyRuleDetails.
        :type patch_selection: oci.fleet_apps_management.models.PatchSelectionDetails

        :param grace_period:
            The value to assign to the grace_period property of this CreateCompliancePolicyRuleDetails.
        :type grace_period: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCompliancePolicyRuleDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCompliancePolicyRuleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCompliancePolicyRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compliance_policy_id': 'str',
            'product_version': 'ProductVersionDetails',
            'patch_type': 'list[str]',
            'severity': 'list[str]',
            'patch_selection': 'PatchSelectionDetails',
            'grace_period': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'compliance_policy_id': 'compliancePolicyId',
            'product_version': 'productVersion',
            'patch_type': 'patchType',
            'severity': 'severity',
            'patch_selection': 'patchSelection',
            'grace_period': 'gracePeriod',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._compliance_policy_id = None
        self._product_version = None
        self._patch_type = None
        self._severity = None
        self._patch_selection = None
        self._grace_period = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateCompliancePolicyRuleDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateCompliancePolicyRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCompliancePolicyRuleDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateCompliancePolicyRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compliance_policy_id(self):
        """
        Gets the compliance_policy_id of this CreateCompliancePolicyRuleDetails.
        Unique OCID of the CompliancePolicy this CompliancePolicyRule belongs to.


        :return: The compliance_policy_id of this CreateCompliancePolicyRuleDetails.
        :rtype: str
        """
        return self._compliance_policy_id

    @compliance_policy_id.setter
    def compliance_policy_id(self, compliance_policy_id):
        """
        Sets the compliance_policy_id of this CreateCompliancePolicyRuleDetails.
        Unique OCID of the CompliancePolicy this CompliancePolicyRule belongs to.


        :param compliance_policy_id: The compliance_policy_id of this CreateCompliancePolicyRuleDetails.
        :type: str
        """
        self._compliance_policy_id = compliance_policy_id

    @property
    def product_version(self):
        """
        **[Required]** Gets the product_version of this CreateCompliancePolicyRuleDetails.

        :return: The product_version of this CreateCompliancePolicyRuleDetails.
        :rtype: oci.fleet_apps_management.models.ProductVersionDetails
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """
        Sets the product_version of this CreateCompliancePolicyRuleDetails.

        :param product_version: The product_version of this CreateCompliancePolicyRuleDetails.
        :type: oci.fleet_apps_management.models.ProductVersionDetails
        """
        self._product_version = product_version

    @property
    def patch_type(self):
        """
        **[Required]** Gets the patch_type of this CreateCompliancePolicyRuleDetails.
        PlatformConfiguration OCID for the patch type to which this CompliancePolicyRule applies.


        :return: The patch_type of this CreateCompliancePolicyRuleDetails.
        :rtype: list[str]
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """
        Sets the patch_type of this CreateCompliancePolicyRuleDetails.
        PlatformConfiguration OCID for the patch type to which this CompliancePolicyRule applies.


        :param patch_type: The patch_type of this CreateCompliancePolicyRuleDetails.
        :type: list[str]
        """
        self._patch_type = patch_type

    @property
    def severity(self):
        """
        Gets the severity of this CreateCompliancePolicyRuleDetails.
        Severity to which this CompliancePolicyRule applies.

        Allowed values for items in this list are: "CRITICAL", "HIGH", "MEDIUM", "LOW"


        :return: The severity of this CreateCompliancePolicyRuleDetails.
        :rtype: list[str]
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this CreateCompliancePolicyRuleDetails.
        Severity to which this CompliancePolicyRule applies.


        :param severity: The severity of this CreateCompliancePolicyRuleDetails.
        :type: list[str]
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]

        if severity and severity is not NONE_SENTINEL:
            for value in severity:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        f"Invalid value for `severity`, must be None or one of {allowed_values}"
                    )
        self._severity = severity

    @property
    def patch_selection(self):
        """
        **[Required]** Gets the patch_selection of this CreateCompliancePolicyRuleDetails.

        :return: The patch_selection of this CreateCompliancePolicyRuleDetails.
        :rtype: oci.fleet_apps_management.models.PatchSelectionDetails
        """
        return self._patch_selection

    @patch_selection.setter
    def patch_selection(self, patch_selection):
        """
        Sets the patch_selection of this CreateCompliancePolicyRuleDetails.

        :param patch_selection: The patch_selection of this CreateCompliancePolicyRuleDetails.
        :type: oci.fleet_apps_management.models.PatchSelectionDetails
        """
        self._patch_selection = patch_selection

    @property
    def grace_period(self):
        """
        Gets the grace_period of this CreateCompliancePolicyRuleDetails.
        Grace period in days,weeks,months or years the exemption is applicable for the rule.
        This enables a grace period when Fleet Application Management doesn't report the product as noncompliant when patch is not applied.


        :return: The grace_period of this CreateCompliancePolicyRuleDetails.
        :rtype: str
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        """
        Sets the grace_period of this CreateCompliancePolicyRuleDetails.
        Grace period in days,weeks,months or years the exemption is applicable for the rule.
        This enables a grace period when Fleet Application Management doesn't report the product as noncompliant when patch is not applied.


        :param grace_period: The grace_period of this CreateCompliancePolicyRuleDetails.
        :type: str
        """
        self._grace_period = grace_period

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCompliancePolicyRuleDetails.
        The OCID of the compartment the CompliancePolicyRule belongs to.


        :return: The compartment_id of this CreateCompliancePolicyRuleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCompliancePolicyRuleDetails.
        The OCID of the compartment the CompliancePolicyRule belongs to.


        :param compartment_id: The compartment_id of this CreateCompliancePolicyRuleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCompliancePolicyRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateCompliancePolicyRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCompliancePolicyRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateCompliancePolicyRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCompliancePolicyRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateCompliancePolicyRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCompliancePolicyRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateCompliancePolicyRuleDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
