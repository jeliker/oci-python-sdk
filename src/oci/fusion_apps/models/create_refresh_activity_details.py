# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRefreshActivityDetails(object):
    """
    The information about current refresh.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRefreshActivityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_fusion_environment_id:
            The value to assign to the source_fusion_environment_id property of this CreateRefreshActivityDetails.
        :type source_fusion_environment_id: str

        :param is_data_masking_opted:
            The value to assign to the is_data_masking_opted property of this CreateRefreshActivityDetails.
        :type is_data_masking_opted: bool

        :param time_scheduled_start:
            The value to assign to the time_scheduled_start property of this CreateRefreshActivityDetails.
        :type time_scheduled_start: datetime

        """
        self.swagger_types = {
            'source_fusion_environment_id': 'str',
            'is_data_masking_opted': 'bool',
            'time_scheduled_start': 'datetime'
        }
        self.attribute_map = {
            'source_fusion_environment_id': 'sourceFusionEnvironmentId',
            'is_data_masking_opted': 'isDataMaskingOpted',
            'time_scheduled_start': 'timeScheduledStart'
        }
        self._source_fusion_environment_id = None
        self._is_data_masking_opted = None
        self._time_scheduled_start = None

    @property
    def source_fusion_environment_id(self):
        """
        **[Required]** Gets the source_fusion_environment_id of this CreateRefreshActivityDetails.
        The `OCID`__ of the source environment

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_fusion_environment_id of this CreateRefreshActivityDetails.
        :rtype: str
        """
        return self._source_fusion_environment_id

    @source_fusion_environment_id.setter
    def source_fusion_environment_id(self, source_fusion_environment_id):
        """
        Sets the source_fusion_environment_id of this CreateRefreshActivityDetails.
        The `OCID`__ of the source environment

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_fusion_environment_id: The source_fusion_environment_id of this CreateRefreshActivityDetails.
        :type: str
        """
        self._source_fusion_environment_id = source_fusion_environment_id

    @property
    def is_data_masking_opted(self):
        """
        Gets the is_data_masking_opted of this CreateRefreshActivityDetails.
        Represents if the customer opted for Data Masking or not during refreshActivity.


        :return: The is_data_masking_opted of this CreateRefreshActivityDetails.
        :rtype: bool
        """
        return self._is_data_masking_opted

    @is_data_masking_opted.setter
    def is_data_masking_opted(self, is_data_masking_opted):
        """
        Sets the is_data_masking_opted of this CreateRefreshActivityDetails.
        Represents if the customer opted for Data Masking or not during refreshActivity.


        :param is_data_masking_opted: The is_data_masking_opted of this CreateRefreshActivityDetails.
        :type: bool
        """
        self._is_data_masking_opted = is_data_masking_opted

    @property
    def time_scheduled_start(self):
        """
        Gets the time_scheduled_start of this CreateRefreshActivityDetails.
        Current time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.


        :return: The time_scheduled_start of this CreateRefreshActivityDetails.
        :rtype: datetime
        """
        return self._time_scheduled_start

    @time_scheduled_start.setter
    def time_scheduled_start(self, time_scheduled_start):
        """
        Sets the time_scheduled_start of this CreateRefreshActivityDetails.
        Current time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.


        :param time_scheduled_start: The time_scheduled_start of this CreateRefreshActivityDetails.
        :type: datetime
        """
        self._time_scheduled_start = time_scheduled_start

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
