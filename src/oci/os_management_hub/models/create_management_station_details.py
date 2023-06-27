# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagementStationDetails(object):
    """
    Information for creating an ManagementStation
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagementStationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateManagementStationDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateManagementStationDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateManagementStationDetails.
        :type description: str

        :param hostname:
            The value to assign to the hostname property of this CreateManagementStationDetails.
        :type hostname: str

        :param proxy:
            The value to assign to the proxy property of this CreateManagementStationDetails.
        :type proxy: oci.os_management_hub.models.CreateProxyConfigurationDetails

        :param mirror:
            The value to assign to the mirror property of this CreateManagementStationDetails.
        :type mirror: oci.os_management_hub.models.CreateMirrorConfigurationDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateManagementStationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateManagementStationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'hostname': 'str',
            'proxy': 'CreateProxyConfigurationDetails',
            'mirror': 'CreateMirrorConfigurationDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'hostname': 'hostname',
            'proxy': 'proxy',
            'mirror': 'mirror',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._hostname = None
        self._proxy = None
        self._mirror = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateManagementStationDetails.
        The OCID of the tenancy containing the Management Station.


        :return: The compartment_id of this CreateManagementStationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateManagementStationDetails.
        The OCID of the tenancy containing the Management Station.


        :param compartment_id: The compartment_id of this CreateManagementStationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateManagementStationDetails.
        Management Station name


        :return: The display_name of this CreateManagementStationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateManagementStationDetails.
        Management Station name


        :param display_name: The display_name of this CreateManagementStationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateManagementStationDetails.
        Details describing the Management Station config.


        :return: The description of this CreateManagementStationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateManagementStationDetails.
        Details describing the Management Station config.


        :param description: The description of this CreateManagementStationDetails.
        :type: str
        """
        self._description = description

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this CreateManagementStationDetails.
        Name of the host


        :return: The hostname of this CreateManagementStationDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CreateManagementStationDetails.
        Name of the host


        :param hostname: The hostname of this CreateManagementStationDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def proxy(self):
        """
        **[Required]** Gets the proxy of this CreateManagementStationDetails.

        :return: The proxy of this CreateManagementStationDetails.
        :rtype: oci.os_management_hub.models.CreateProxyConfigurationDetails
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """
        Sets the proxy of this CreateManagementStationDetails.

        :param proxy: The proxy of this CreateManagementStationDetails.
        :type: oci.os_management_hub.models.CreateProxyConfigurationDetails
        """
        self._proxy = proxy

    @property
    def mirror(self):
        """
        **[Required]** Gets the mirror of this CreateManagementStationDetails.

        :return: The mirror of this CreateManagementStationDetails.
        :rtype: oci.os_management_hub.models.CreateMirrorConfigurationDetails
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """
        Sets the mirror of this CreateManagementStationDetails.

        :param mirror: The mirror of this CreateManagementStationDetails.
        :type: oci.os_management_hub.models.CreateMirrorConfigurationDetails
        """
        self._mirror = mirror

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateManagementStationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateManagementStationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateManagementStationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateManagementStationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateManagementStationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateManagementStationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateManagementStationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateManagementStationDetails.
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
