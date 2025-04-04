# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506

from .create_channel_result import CreateChannelResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAppEventChannelResult(CreateChannelResult):
    """
    The configuration for an Application Event channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAppEventChannelResult object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateAppEventChannelResult.type` attribute
        of this class is ``APPEVENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CreateAppEventChannelResult.
        :type id: str

        :param name:
            The value to assign to the name property of this CreateAppEventChannelResult.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateAppEventChannelResult.
        :type description: str

        :param category:
            The value to assign to the category property of this CreateAppEventChannelResult.
            Allowed values for this property are: "AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"
        :type category: str

        :param type:
            The value to assign to the type property of this CreateAppEventChannelResult.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateAppEventChannelResult.
        :type session_expiry_duration_in_milliseconds: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateAppEventChannelResult.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this CreateAppEventChannelResult.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CreateAppEventChannelResult.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAppEventChannelResult.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAppEventChannelResult.
        :type defined_tags: dict(str, dict(str, object))

        :param secret_key:
            The value to assign to the secret_key property of this CreateAppEventChannelResult.
        :type secret_key: str

        :param outbound_url:
            The value to assign to the outbound_url property of this CreateAppEventChannelResult.
        :type outbound_url: str

        :param event_sink_bot_ids:
            The value to assign to the event_sink_bot_ids property of this CreateAppEventChannelResult.
        :type event_sink_bot_ids: list[str]

        :param webhook_url:
            The value to assign to the webhook_url property of this CreateAppEventChannelResult.
        :type webhook_url: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'category': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'secret_key': 'str',
            'outbound_url': 'str',
            'event_sink_bot_ids': 'list[str]',
            'webhook_url': 'str'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'category': 'category',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'secret_key': 'secretKey',
            'outbound_url': 'outboundUrl',
            'event_sink_bot_ids': 'eventSinkBotIds',
            'webhook_url': 'webhookUrl'
        }
        self._id = None
        self._name = None
        self._description = None
        self._category = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._secret_key = None
        self._outbound_url = None
        self._event_sink_bot_ids = None
        self._webhook_url = None
        self._type = 'APPEVENT'

    @property
    def secret_key(self):
        """
        **[Required]** Gets the secret_key of this CreateAppEventChannelResult.
        The secret key used to verify the authenticity of received messages.
        This is only returned this once.  If it is lost the keys will need to be rotated to generate a new key.


        :return: The secret_key of this CreateAppEventChannelResult.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """
        Sets the secret_key of this CreateAppEventChannelResult.
        The secret key used to verify the authenticity of received messages.
        This is only returned this once.  If it is lost the keys will need to be rotated to generate a new key.


        :param secret_key: The secret_key of this CreateAppEventChannelResult.
        :type: str
        """
        self._secret_key = secret_key

    @property
    def outbound_url(self):
        """
        **[Required]** Gets the outbound_url of this CreateAppEventChannelResult.
        The URL for sending errors and responses to.


        :return: The outbound_url of this CreateAppEventChannelResult.
        :rtype: str
        """
        return self._outbound_url

    @outbound_url.setter
    def outbound_url(self, outbound_url):
        """
        Sets the outbound_url of this CreateAppEventChannelResult.
        The URL for sending errors and responses to.


        :param outbound_url: The outbound_url of this CreateAppEventChannelResult.
        :type: str
        """
        self._outbound_url = outbound_url

    @property
    def event_sink_bot_ids(self):
        """
        Gets the event_sink_bot_ids of this CreateAppEventChannelResult.
        The IDs of the Skills and Digital Assistants that the Channel is routed to.


        :return: The event_sink_bot_ids of this CreateAppEventChannelResult.
        :rtype: list[str]
        """
        return self._event_sink_bot_ids

    @event_sink_bot_ids.setter
    def event_sink_bot_ids(self, event_sink_bot_ids):
        """
        Sets the event_sink_bot_ids of this CreateAppEventChannelResult.
        The IDs of the Skills and Digital Assistants that the Channel is routed to.


        :param event_sink_bot_ids: The event_sink_bot_ids of this CreateAppEventChannelResult.
        :type: list[str]
        """
        self._event_sink_bot_ids = event_sink_bot_ids

    @property
    def webhook_url(self):
        """
        **[Required]** Gets the webhook_url of this CreateAppEventChannelResult.
        The URL to use to send messages to this channel.
        This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.


        :return: The webhook_url of this CreateAppEventChannelResult.
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """
        Sets the webhook_url of this CreateAppEventChannelResult.
        The URL to use to send messages to this channel.
        This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.


        :param webhook_url: The webhook_url of this CreateAppEventChannelResult.
        :type: str
        """
        self._webhook_url = webhook_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
