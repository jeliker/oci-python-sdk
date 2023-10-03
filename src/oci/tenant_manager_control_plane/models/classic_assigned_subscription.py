# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230401

from .assigned_subscription import AssignedSubscription
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClassicAssignedSubscription(AssignedSubscription):
    """
    Assigned subscription information.
    """

    #: A constant which can be used with the lifecycle_state property of a ClassicAssignedSubscription.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ClassicAssignedSubscription.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ClassicAssignedSubscription.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ClassicAssignedSubscription.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ClassicAssignedSubscription.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ClassicAssignedSubscription.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ClassicAssignedSubscription.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ClassicAssignedSubscription object with values from keyword arguments. The default value of the :py:attr:`~oci.tenant_manager_control_plane.models.ClassicAssignedSubscription.entity_version` attribute
        of this class is ``V1`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_version:
            The value to assign to the entity_version property of this ClassicAssignedSubscription.
            Allowed values for this property are: "V1", "V2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_version: str

        :param id:
            The value to assign to the id property of this ClassicAssignedSubscription.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ClassicAssignedSubscription.
        :type compartment_id: str

        :param service_name:
            The value to assign to the service_name property of this ClassicAssignedSubscription.
        :type service_name: str

        :param time_created:
            The value to assign to the time_created property of this ClassicAssignedSubscription.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ClassicAssignedSubscription.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ClassicAssignedSubscription.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ClassicAssignedSubscription.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ClassicAssignedSubscription.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param classic_subscription_id:
            The value to assign to the classic_subscription_id property of this ClassicAssignedSubscription.
        :type classic_subscription_id: str

        :param is_classic_subscription:
            The value to assign to the is_classic_subscription property of this ClassicAssignedSubscription.
        :type is_classic_subscription: bool

        :param region_assignment:
            The value to assign to the region_assignment property of this ClassicAssignedSubscription.
        :type region_assignment: str

        :param skus:
            The value to assign to the skus property of this ClassicAssignedSubscription.
        :type skus: list[oci.tenant_manager_control_plane.models.SubscriptionSku]

        :param order_ids:
            The value to assign to the order_ids property of this ClassicAssignedSubscription.
        :type order_ids: list[str]

        :param program_type:
            The value to assign to the program_type property of this ClassicAssignedSubscription.
        :type program_type: str

        :param customer_country_code:
            The value to assign to the customer_country_code property of this ClassicAssignedSubscription.
        :type customer_country_code: str

        :param cloud_amount_currency:
            The value to assign to the cloud_amount_currency property of this ClassicAssignedSubscription.
        :type cloud_amount_currency: str

        :param csi_number:
            The value to assign to the csi_number property of this ClassicAssignedSubscription.
        :type csi_number: str

        :param subscription_tier:
            The value to assign to the subscription_tier property of this ClassicAssignedSubscription.
        :type subscription_tier: str

        :param is_government_subscription:
            The value to assign to the is_government_subscription property of this ClassicAssignedSubscription.
        :type is_government_subscription: bool

        :param promotion:
            The value to assign to the promotion property of this ClassicAssignedSubscription.
        :type promotion: list[oci.tenant_manager_control_plane.models.Promotion]

        :param purchase_entitlement_id:
            The value to assign to the purchase_entitlement_id property of this ClassicAssignedSubscription.
        :type purchase_entitlement_id: str

        :param start_date:
            The value to assign to the start_date property of this ClassicAssignedSubscription.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this ClassicAssignedSubscription.
        :type end_date: datetime

        """
        self.swagger_types = {
            'entity_version': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'service_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'classic_subscription_id': 'str',
            'is_classic_subscription': 'bool',
            'region_assignment': 'str',
            'skus': 'list[SubscriptionSku]',
            'order_ids': 'list[str]',
            'program_type': 'str',
            'customer_country_code': 'str',
            'cloud_amount_currency': 'str',
            'csi_number': 'str',
            'subscription_tier': 'str',
            'is_government_subscription': 'bool',
            'promotion': 'list[Promotion]',
            'purchase_entitlement_id': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime'
        }

        self.attribute_map = {
            'entity_version': 'entityVersion',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'service_name': 'serviceName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState',
            'classic_subscription_id': 'classicSubscriptionId',
            'is_classic_subscription': 'isClassicSubscription',
            'region_assignment': 'regionAssignment',
            'skus': 'skus',
            'order_ids': 'orderIds',
            'program_type': 'programType',
            'customer_country_code': 'customerCountryCode',
            'cloud_amount_currency': 'cloudAmountCurrency',
            'csi_number': 'csiNumber',
            'subscription_tier': 'subscriptionTier',
            'is_government_subscription': 'isGovernmentSubscription',
            'promotion': 'promotion',
            'purchase_entitlement_id': 'purchaseEntitlementId',
            'start_date': 'startDate',
            'end_date': 'endDate'
        }

        self._entity_version = None
        self._id = None
        self._compartment_id = None
        self._service_name = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_state = None
        self._classic_subscription_id = None
        self._is_classic_subscription = None
        self._region_assignment = None
        self._skus = None
        self._order_ids = None
        self._program_type = None
        self._customer_country_code = None
        self._cloud_amount_currency = None
        self._csi_number = None
        self._subscription_tier = None
        self._is_government_subscription = None
        self._promotion = None
        self._purchase_entitlement_id = None
        self._start_date = None
        self._end_date = None
        self._entity_version = 'V1'

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ClassicAssignedSubscription.
        Lifecycle state of the subscription.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ClassicAssignedSubscription.
        Lifecycle state of the subscription.


        :param lifecycle_state: The lifecycle_state of this ClassicAssignedSubscription.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def classic_subscription_id(self):
        """
        **[Required]** Gets the classic_subscription_id of this ClassicAssignedSubscription.
        Subscription ID.


        :return: The classic_subscription_id of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._classic_subscription_id

    @classic_subscription_id.setter
    def classic_subscription_id(self, classic_subscription_id):
        """
        Sets the classic_subscription_id of this ClassicAssignedSubscription.
        Subscription ID.


        :param classic_subscription_id: The classic_subscription_id of this ClassicAssignedSubscription.
        :type: str
        """
        self._classic_subscription_id = classic_subscription_id

    @property
    def is_classic_subscription(self):
        """
        Gets the is_classic_subscription of this ClassicAssignedSubscription.
        Specifies whether or not the subscription is legacy.


        :return: The is_classic_subscription of this ClassicAssignedSubscription.
        :rtype: bool
        """
        return self._is_classic_subscription

    @is_classic_subscription.setter
    def is_classic_subscription(self, is_classic_subscription):
        """
        Sets the is_classic_subscription of this ClassicAssignedSubscription.
        Specifies whether or not the subscription is legacy.


        :param is_classic_subscription: The is_classic_subscription of this ClassicAssignedSubscription.
        :type: bool
        """
        self._is_classic_subscription = is_classic_subscription

    @property
    def region_assignment(self):
        """
        Gets the region_assignment of this ClassicAssignedSubscription.
        Region for the subscription.


        :return: The region_assignment of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._region_assignment

    @region_assignment.setter
    def region_assignment(self, region_assignment):
        """
        Sets the region_assignment of this ClassicAssignedSubscription.
        Region for the subscription.


        :param region_assignment: The region_assignment of this ClassicAssignedSubscription.
        :type: str
        """
        self._region_assignment = region_assignment

    @property
    def skus(self):
        """
        Gets the skus of this ClassicAssignedSubscription.
        List of SKUs linked to the subscription.


        :return: The skus of this ClassicAssignedSubscription.
        :rtype: list[oci.tenant_manager_control_plane.models.SubscriptionSku]
        """
        return self._skus

    @skus.setter
    def skus(self, skus):
        """
        Sets the skus of this ClassicAssignedSubscription.
        List of SKUs linked to the subscription.


        :param skus: The skus of this ClassicAssignedSubscription.
        :type: list[oci.tenant_manager_control_plane.models.SubscriptionSku]
        """
        self._skus = skus

    @property
    def order_ids(self):
        """
        Gets the order_ids of this ClassicAssignedSubscription.
        List of subscription order OCIDs that contributed to this subscription.


        :return: The order_ids of this ClassicAssignedSubscription.
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """
        Sets the order_ids of this ClassicAssignedSubscription.
        List of subscription order OCIDs that contributed to this subscription.


        :param order_ids: The order_ids of this ClassicAssignedSubscription.
        :type: list[str]
        """
        self._order_ids = order_ids

    @property
    def program_type(self):
        """
        Gets the program_type of this ClassicAssignedSubscription.
        Specifies any program that is associated with the subscription.


        :return: The program_type of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._program_type

    @program_type.setter
    def program_type(self, program_type):
        """
        Sets the program_type of this ClassicAssignedSubscription.
        Specifies any program that is associated with the subscription.


        :param program_type: The program_type of this ClassicAssignedSubscription.
        :type: str
        """
        self._program_type = program_type

    @property
    def customer_country_code(self):
        """
        Gets the customer_country_code of this ClassicAssignedSubscription.
        The country code for the customer associated with the subscription.


        :return: The customer_country_code of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._customer_country_code

    @customer_country_code.setter
    def customer_country_code(self, customer_country_code):
        """
        Sets the customer_country_code of this ClassicAssignedSubscription.
        The country code for the customer associated with the subscription.


        :param customer_country_code: The customer_country_code of this ClassicAssignedSubscription.
        :type: str
        """
        self._customer_country_code = customer_country_code

    @property
    def cloud_amount_currency(self):
        """
        Gets the cloud_amount_currency of this ClassicAssignedSubscription.
        The currency code for the customer associated with the subscription.


        :return: The cloud_amount_currency of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._cloud_amount_currency

    @cloud_amount_currency.setter
    def cloud_amount_currency(self, cloud_amount_currency):
        """
        Sets the cloud_amount_currency of this ClassicAssignedSubscription.
        The currency code for the customer associated with the subscription.


        :param cloud_amount_currency: The cloud_amount_currency of this ClassicAssignedSubscription.
        :type: str
        """
        self._cloud_amount_currency = cloud_amount_currency

    @property
    def csi_number(self):
        """
        Gets the csi_number of this ClassicAssignedSubscription.
        Customer service identifier for the customer associated with the subscription.


        :return: The csi_number of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._csi_number

    @csi_number.setter
    def csi_number(self, csi_number):
        """
        Sets the csi_number of this ClassicAssignedSubscription.
        Customer service identifier for the customer associated with the subscription.


        :param csi_number: The csi_number of this ClassicAssignedSubscription.
        :type: str
        """
        self._csi_number = csi_number

    @property
    def subscription_tier(self):
        """
        Gets the subscription_tier of this ClassicAssignedSubscription.
        Tier for the subscription, whether a free promotion subscription or a paid subscription.


        :return: The subscription_tier of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._subscription_tier

    @subscription_tier.setter
    def subscription_tier(self, subscription_tier):
        """
        Sets the subscription_tier of this ClassicAssignedSubscription.
        Tier for the subscription, whether a free promotion subscription or a paid subscription.


        :param subscription_tier: The subscription_tier of this ClassicAssignedSubscription.
        :type: str
        """
        self._subscription_tier = subscription_tier

    @property
    def is_government_subscription(self):
        """
        Gets the is_government_subscription of this ClassicAssignedSubscription.
        Specifies whether or not the subscription is a government subscription.


        :return: The is_government_subscription of this ClassicAssignedSubscription.
        :rtype: bool
        """
        return self._is_government_subscription

    @is_government_subscription.setter
    def is_government_subscription(self, is_government_subscription):
        """
        Sets the is_government_subscription of this ClassicAssignedSubscription.
        Specifies whether or not the subscription is a government subscription.


        :param is_government_subscription: The is_government_subscription of this ClassicAssignedSubscription.
        :type: bool
        """
        self._is_government_subscription = is_government_subscription

    @property
    def promotion(self):
        """
        Gets the promotion of this ClassicAssignedSubscription.
        List of promotions related to the subscription.


        :return: The promotion of this ClassicAssignedSubscription.
        :rtype: list[oci.tenant_manager_control_plane.models.Promotion]
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """
        Sets the promotion of this ClassicAssignedSubscription.
        List of promotions related to the subscription.


        :param promotion: The promotion of this ClassicAssignedSubscription.
        :type: list[oci.tenant_manager_control_plane.models.Promotion]
        """
        self._promotion = promotion

    @property
    def purchase_entitlement_id(self):
        """
        Gets the purchase_entitlement_id of this ClassicAssignedSubscription.
        Purchase entitlement ID associated with the subscription.


        :return: The purchase_entitlement_id of this ClassicAssignedSubscription.
        :rtype: str
        """
        return self._purchase_entitlement_id

    @purchase_entitlement_id.setter
    def purchase_entitlement_id(self, purchase_entitlement_id):
        """
        Sets the purchase_entitlement_id of this ClassicAssignedSubscription.
        Purchase entitlement ID associated with the subscription.


        :param purchase_entitlement_id: The purchase_entitlement_id of this ClassicAssignedSubscription.
        :type: str
        """
        self._purchase_entitlement_id = purchase_entitlement_id

    @property
    def start_date(self):
        """
        Gets the start_date of this ClassicAssignedSubscription.
        Subscription start time.


        :return: The start_date of this ClassicAssignedSubscription.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this ClassicAssignedSubscription.
        Subscription start time.


        :param start_date: The start_date of this ClassicAssignedSubscription.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this ClassicAssignedSubscription.
        Subscription end time.


        :return: The end_date of this ClassicAssignedSubscription.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this ClassicAssignedSubscription.
        Subscription end time.


        :param end_date: The end_date of this ClassicAssignedSubscription.
        :type: datetime
        """
        self._end_date = end_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other