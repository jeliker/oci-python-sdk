# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateListingRevisionDetails(object):
    """
    The model for an Oracle Cloud Infrastructure Marketplace Publisher listing revision.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateListingRevisionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateListingRevisionDetails.
        :type display_name: str

        :param version_details:
            The value to assign to the version_details property of this UpdateListingRevisionDetails.
        :type version_details: oci.marketplace_publisher.models.VersionDetails

        :param headline:
            The value to assign to the headline property of this UpdateListingRevisionDetails.
        :type headline: str

        :param tagline:
            The value to assign to the tagline property of this UpdateListingRevisionDetails.
        :type tagline: str

        :param keywords:
            The value to assign to the keywords property of this UpdateListingRevisionDetails.
        :type keywords: str

        :param short_description:
            The value to assign to the short_description property of this UpdateListingRevisionDetails.
        :type short_description: str

        :param usage_information:
            The value to assign to the usage_information property of this UpdateListingRevisionDetails.
        :type usage_information: str

        :param long_description:
            The value to assign to the long_description property of this UpdateListingRevisionDetails.
        :type long_description: str

        :param system_requirements:
            The value to assign to the system_requirements property of this UpdateListingRevisionDetails.
        :type system_requirements: str

        :param categories:
            The value to assign to the categories property of this UpdateListingRevisionDetails.
        :type categories: list[str]

        :param markets:
            The value to assign to the markets property of this UpdateListingRevisionDetails.
        :type markets: list[str]

        :param content_language:
            The value to assign to the content_language property of this UpdateListingRevisionDetails.
        :type content_language: oci.marketplace_publisher.models.LanguageItem

        :param supportedlanguages:
            The value to assign to the supportedlanguages property of this UpdateListingRevisionDetails.
        :type supportedlanguages: list[oci.marketplace_publisher.models.LanguageItem]

        :param support_contacts:
            The value to assign to the support_contacts property of this UpdateListingRevisionDetails.
        :type support_contacts: list[oci.marketplace_publisher.models.SupportContact]

        :param support_links:
            The value to assign to the support_links property of this UpdateListingRevisionDetails.
        :type support_links: list[oci.marketplace_publisher.models.NamedLink]

        :param pricing_type:
            The value to assign to the pricing_type property of this UpdateListingRevisionDetails.
        :type pricing_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateListingRevisionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateListingRevisionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'version_details': 'VersionDetails',
            'headline': 'str',
            'tagline': 'str',
            'keywords': 'str',
            'short_description': 'str',
            'usage_information': 'str',
            'long_description': 'str',
            'system_requirements': 'str',
            'categories': 'list[str]',
            'markets': 'list[str]',
            'content_language': 'LanguageItem',
            'supportedlanguages': 'list[LanguageItem]',
            'support_contacts': 'list[SupportContact]',
            'support_links': 'list[NamedLink]',
            'pricing_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'version_details': 'versionDetails',
            'headline': 'headline',
            'tagline': 'tagline',
            'keywords': 'keywords',
            'short_description': 'shortDescription',
            'usage_information': 'usageInformation',
            'long_description': 'longDescription',
            'system_requirements': 'systemRequirements',
            'categories': 'categories',
            'markets': 'markets',
            'content_language': 'contentLanguage',
            'supportedlanguages': 'supportedlanguages',
            'support_contacts': 'supportContacts',
            'support_links': 'supportLinks',
            'pricing_type': 'pricingType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._version_details = None
        self._headline = None
        self._tagline = None
        self._keywords = None
        self._short_description = None
        self._usage_information = None
        self._long_description = None
        self._system_requirements = None
        self._categories = None
        self._markets = None
        self._content_language = None
        self._supportedlanguages = None
        self._support_contacts = None
        self._support_links = None
        self._pricing_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateListingRevisionDetails.
        The name for the listing revision.


        :return: The display_name of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateListingRevisionDetails.
        The name for the listing revision.


        :param display_name: The display_name of this UpdateListingRevisionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def version_details(self):
        """
        Gets the version_details of this UpdateListingRevisionDetails.

        :return: The version_details of this UpdateListingRevisionDetails.
        :rtype: oci.marketplace_publisher.models.VersionDetails
        """
        return self._version_details

    @version_details.setter
    def version_details(self, version_details):
        """
        Sets the version_details of this UpdateListingRevisionDetails.

        :param version_details: The version_details of this UpdateListingRevisionDetails.
        :type: oci.marketplace_publisher.models.VersionDetails
        """
        self._version_details = version_details

    @property
    def headline(self):
        """
        Gets the headline of this UpdateListingRevisionDetails.
        Single line introduction for the listing revision.


        :return: The headline of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this UpdateListingRevisionDetails.
        Single line introduction for the listing revision.


        :param headline: The headline of this UpdateListingRevisionDetails.
        :type: str
        """
        self._headline = headline

    @property
    def tagline(self):
        """
        Gets the tagline of this UpdateListingRevisionDetails.
        The tagline for the listing revision.


        :return: The tagline of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._tagline

    @tagline.setter
    def tagline(self, tagline):
        """
        Sets the tagline of this UpdateListingRevisionDetails.
        The tagline for the listing revision.


        :param tagline: The tagline of this UpdateListingRevisionDetails.
        :type: str
        """
        self._tagline = tagline

    @property
    def keywords(self):
        """
        Gets the keywords of this UpdateListingRevisionDetails.
        Keywords associated for the listing revision.


        :return: The keywords of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this UpdateListingRevisionDetails.
        Keywords associated for the listing revision.


        :param keywords: The keywords of this UpdateListingRevisionDetails.
        :type: str
        """
        self._keywords = keywords

    @property
    def short_description(self):
        """
        Gets the short_description of this UpdateListingRevisionDetails.
        A short description for the listing revision.


        :return: The short_description of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this UpdateListingRevisionDetails.
        A short description for the listing revision.


        :param short_description: The short_description of this UpdateListingRevisionDetails.
        :type: str
        """
        self._short_description = short_description

    @property
    def usage_information(self):
        """
        Gets the usage_information of this UpdateListingRevisionDetails.
        Usage information for the listing revision.


        :return: The usage_information of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._usage_information

    @usage_information.setter
    def usage_information(self, usage_information):
        """
        Sets the usage_information of this UpdateListingRevisionDetails.
        Usage information for the listing revision.


        :param usage_information: The usage_information of this UpdateListingRevisionDetails.
        :type: str
        """
        self._usage_information = usage_information

    @property
    def long_description(self):
        """
        Gets the long_description of this UpdateListingRevisionDetails.
        A long description for the listing revision.


        :return: The long_description of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this UpdateListingRevisionDetails.
        A long description for the listing revision.


        :param long_description: The long_description of this UpdateListingRevisionDetails.
        :type: str
        """
        self._long_description = long_description

    @property
    def system_requirements(self):
        """
        Gets the system_requirements of this UpdateListingRevisionDetails.
        System requirements for the listing revision.


        :return: The system_requirements of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._system_requirements

    @system_requirements.setter
    def system_requirements(self, system_requirements):
        """
        Sets the system_requirements of this UpdateListingRevisionDetails.
        System requirements for the listing revision.


        :param system_requirements: The system_requirements of this UpdateListingRevisionDetails.
        :type: str
        """
        self._system_requirements = system_requirements

    @property
    def categories(self):
        """
        Gets the categories of this UpdateListingRevisionDetails.
        The categories for the listing revision.


        :return: The categories of this UpdateListingRevisionDetails.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this UpdateListingRevisionDetails.
        The categories for the listing revision.


        :param categories: The categories of this UpdateListingRevisionDetails.
        :type: list[str]
        """
        self._categories = categories

    @property
    def markets(self):
        """
        Gets the markets of this UpdateListingRevisionDetails.
        The markets supported by the listing revision.


        :return: The markets of this UpdateListingRevisionDetails.
        :rtype: list[str]
        """
        return self._markets

    @markets.setter
    def markets(self, markets):
        """
        Sets the markets of this UpdateListingRevisionDetails.
        The markets supported by the listing revision.


        :param markets: The markets of this UpdateListingRevisionDetails.
        :type: list[str]
        """
        self._markets = markets

    @property
    def content_language(self):
        """
        Gets the content_language of this UpdateListingRevisionDetails.

        :return: The content_language of this UpdateListingRevisionDetails.
        :rtype: oci.marketplace_publisher.models.LanguageItem
        """
        return self._content_language

    @content_language.setter
    def content_language(self, content_language):
        """
        Sets the content_language of this UpdateListingRevisionDetails.

        :param content_language: The content_language of this UpdateListingRevisionDetails.
        :type: oci.marketplace_publisher.models.LanguageItem
        """
        self._content_language = content_language

    @property
    def supportedlanguages(self):
        """
        Gets the supportedlanguages of this UpdateListingRevisionDetails.
        Languages supported by the listing revision.


        :return: The supportedlanguages of this UpdateListingRevisionDetails.
        :rtype: list[oci.marketplace_publisher.models.LanguageItem]
        """
        return self._supportedlanguages

    @supportedlanguages.setter
    def supportedlanguages(self, supportedlanguages):
        """
        Sets the supportedlanguages of this UpdateListingRevisionDetails.
        Languages supported by the listing revision.


        :param supportedlanguages: The supportedlanguages of this UpdateListingRevisionDetails.
        :type: list[oci.marketplace_publisher.models.LanguageItem]
        """
        self._supportedlanguages = supportedlanguages

    @property
    def support_contacts(self):
        """
        Gets the support_contacts of this UpdateListingRevisionDetails.
        Contact information to use to get support from the publisher for the listing revision.


        :return: The support_contacts of this UpdateListingRevisionDetails.
        :rtype: list[oci.marketplace_publisher.models.SupportContact]
        """
        return self._support_contacts

    @support_contacts.setter
    def support_contacts(self, support_contacts):
        """
        Sets the support_contacts of this UpdateListingRevisionDetails.
        Contact information to use to get support from the publisher for the listing revision.


        :param support_contacts: The support_contacts of this UpdateListingRevisionDetails.
        :type: list[oci.marketplace_publisher.models.SupportContact]
        """
        self._support_contacts = support_contacts

    @property
    def support_links(self):
        """
        Gets the support_links of this UpdateListingRevisionDetails.
        Links to support resources for the listing revision.


        :return: The support_links of this UpdateListingRevisionDetails.
        :rtype: list[oci.marketplace_publisher.models.NamedLink]
        """
        return self._support_links

    @support_links.setter
    def support_links(self, support_links):
        """
        Sets the support_links of this UpdateListingRevisionDetails.
        Links to support resources for the listing revision.


        :param support_links: The support_links of this UpdateListingRevisionDetails.
        :type: list[oci.marketplace_publisher.models.NamedLink]
        """
        self._support_links = support_links

    @property
    def pricing_type(self):
        """
        Gets the pricing_type of this UpdateListingRevisionDetails.
        The pricing model for the listing revision.


        :return: The pricing_type of this UpdateListingRevisionDetails.
        :rtype: str
        """
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, pricing_type):
        """
        Sets the pricing_type of this UpdateListingRevisionDetails.
        The pricing model for the listing revision.


        :param pricing_type: The pricing_type of this UpdateListingRevisionDetails.
        :type: str
        """
        self._pricing_type = pricing_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateListingRevisionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateListingRevisionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateListingRevisionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateListingRevisionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateListingRevisionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateListingRevisionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateListingRevisionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateListingRevisionDetails.
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
