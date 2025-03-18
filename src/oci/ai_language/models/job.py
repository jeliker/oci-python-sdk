# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Job(object):
    """
    Job details which contain input document details on which prediction need to run, features (which and all language services ) need to run and where to store results
    """

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Job object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Job.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Job.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Job.
        :type description: str

        :param input_location:
            The value to assign to the input_location property of this Job.
        :type input_location: oci.ai_language.models.InputLocation

        :param input_configuration:
            The value to assign to the input_configuration property of this Job.
        :type input_configuration: oci.ai_language.models.InputConfiguration

        :param model_metadata_details:
            The value to assign to the model_metadata_details property of this Job.
        :type model_metadata_details: list[oci.ai_language.models.ModelMetadataDetails]

        :param compartment_id:
            The value to assign to the compartment_id property of this Job.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Job.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Job.
        :type lifecycle_details: str

        :param percent_complete:
            The value to assign to the percent_complete property of this Job.
        :type percent_complete: int

        :param total_documents:
            The value to assign to the total_documents property of this Job.
        :type total_documents: int

        :param pending_documents:
            The value to assign to the pending_documents property of this Job.
        :type pending_documents: int

        :param completed_documents:
            The value to assign to the completed_documents property of this Job.
        :type completed_documents: int

        :param failed_documents:
            The value to assign to the failed_documents property of this Job.
        :type failed_documents: int

        :param warnings_count:
            The value to assign to the warnings_count property of this Job.
        :type warnings_count: int

        :param output_location:
            The value to assign to the output_location property of this Job.
        :type output_location: oci.ai_language.models.ObjectPrefixOutputLocation

        :param ttl_in_days:
            The value to assign to the ttl_in_days property of this Job.
        :type ttl_in_days: int

        :param created_by:
            The value to assign to the created_by property of this Job.
        :type created_by: str

        :param time_accepted:
            The value to assign to the time_accepted property of this Job.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this Job.
        :type time_started: datetime

        :param time_completed:
            The value to assign to the time_completed property of this Job.
        :type time_completed: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'input_location': 'InputLocation',
            'input_configuration': 'InputConfiguration',
            'model_metadata_details': 'list[ModelMetadataDetails]',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'percent_complete': 'int',
            'total_documents': 'int',
            'pending_documents': 'int',
            'completed_documents': 'int',
            'failed_documents': 'int',
            'warnings_count': 'int',
            'output_location': 'ObjectPrefixOutputLocation',
            'ttl_in_days': 'int',
            'created_by': 'str',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_completed': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'input_location': 'inputLocation',
            'input_configuration': 'inputConfiguration',
            'model_metadata_details': 'modelMetadataDetails',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'percent_complete': 'percentComplete',
            'total_documents': 'totalDocuments',
            'pending_documents': 'pendingDocuments',
            'completed_documents': 'completedDocuments',
            'failed_documents': 'failedDocuments',
            'warnings_count': 'warningsCount',
            'output_location': 'outputLocation',
            'ttl_in_days': 'ttlInDays',
            'created_by': 'createdBy',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_completed': 'timeCompleted'
        }
        self._id = None
        self._display_name = None
        self._description = None
        self._input_location = None
        self._input_configuration = None
        self._model_metadata_details = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._percent_complete = None
        self._total_documents = None
        self._pending_documents = None
        self._completed_documents = None
        self._failed_documents = None
        self._warnings_count = None
        self._output_location = None
        self._ttl_in_days = None
        self._created_by = None
        self._time_accepted = None
        self._time_started = None
        self._time_completed = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Job.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Job.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Job.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Job.
        A user-friendly display name for the job.


        :return: The display_name of this Job.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Job.
        A user-friendly display name for the job.


        :param display_name: The display_name of this Job.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Job.
        A short description of the job.


        :return: The description of this Job.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Job.
        A short description of the job.


        :param description: The description of this Job.
        :type: str
        """
        self._description = description

    @property
    def input_location(self):
        """
        **[Required]** Gets the input_location of this Job.

        :return: The input_location of this Job.
        :rtype: oci.ai_language.models.InputLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this Job.

        :param input_location: The input_location of this Job.
        :type: oci.ai_language.models.InputLocation
        """
        self._input_location = input_location

    @property
    def input_configuration(self):
        """
        Gets the input_configuration of this Job.

        :return: The input_configuration of this Job.
        :rtype: oci.ai_language.models.InputConfiguration
        """
        return self._input_configuration

    @input_configuration.setter
    def input_configuration(self, input_configuration):
        """
        Sets the input_configuration of this Job.

        :param input_configuration: The input_configuration of this Job.
        :type: oci.ai_language.models.InputConfiguration
        """
        self._input_configuration = input_configuration

    @property
    def model_metadata_details(self):
        """
        **[Required]** Gets the model_metadata_details of this Job.
        training model details
        For this release only one model is allowed to be input here.
        One of the three modelType, ModelId, endpointId should be given other wise error will be thrown from API


        :return: The model_metadata_details of this Job.
        :rtype: list[oci.ai_language.models.ModelMetadataDetails]
        """
        return self._model_metadata_details

    @model_metadata_details.setter
    def model_metadata_details(self, model_metadata_details):
        """
        Sets the model_metadata_details of this Job.
        training model details
        For this release only one model is allowed to be input here.
        One of the three modelType, ModelId, endpointId should be given other wise error will be thrown from API


        :param model_metadata_details: The model_metadata_details of this Job.
        :type: list[oci.ai_language.models.ModelMetadataDetails]
        """
        self._model_metadata_details = model_metadata_details

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Job.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Job.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Job.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Job.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Job.
        The current state of the Job.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Job.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Job.
        The current state of the Job.


        :param lifecycle_state: The lifecycle_state of this Job.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Job.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this Job.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Job.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this Job.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this Job.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :return: The percent_complete of this Job.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this Job.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :param percent_complete: The percent_complete of this Job.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def total_documents(self):
        """
        Gets the total_documents of this Job.
        Total number of documents given as input for prediction. For CSV this signifies number of rows and for TXT this signifies number of files.


        :return: The total_documents of this Job.
        :rtype: int
        """
        return self._total_documents

    @total_documents.setter
    def total_documents(self, total_documents):
        """
        Sets the total_documents of this Job.
        Total number of documents given as input for prediction. For CSV this signifies number of rows and for TXT this signifies number of files.


        :param total_documents: The total_documents of this Job.
        :type: int
        """
        self._total_documents = total_documents

    @property
    def pending_documents(self):
        """
        Gets the pending_documents of this Job.
        Number of documents still to process. For CSV this signifies number of rows and for TXT this signifies number of files.


        :return: The pending_documents of this Job.
        :rtype: int
        """
        return self._pending_documents

    @pending_documents.setter
    def pending_documents(self, pending_documents):
        """
        Sets the pending_documents of this Job.
        Number of documents still to process. For CSV this signifies number of rows and for TXT this signifies number of files.


        :param pending_documents: The pending_documents of this Job.
        :type: int
        """
        self._pending_documents = pending_documents

    @property
    def completed_documents(self):
        """
        Gets the completed_documents of this Job.
        Number of documents processed for prediction. For CSV this signifies number of rows and for TXT this signifies number of files.


        :return: The completed_documents of this Job.
        :rtype: int
        """
        return self._completed_documents

    @completed_documents.setter
    def completed_documents(self, completed_documents):
        """
        Sets the completed_documents of this Job.
        Number of documents processed for prediction. For CSV this signifies number of rows and for TXT this signifies number of files.


        :param completed_documents: The completed_documents of this Job.
        :type: int
        """
        self._completed_documents = completed_documents

    @property
    def failed_documents(self):
        """
        Gets the failed_documents of this Job.
        Number of documents failed for prediction. For CSV this signifies number of rows and for TXT this signifies number of files.


        :return: The failed_documents of this Job.
        :rtype: int
        """
        return self._failed_documents

    @failed_documents.setter
    def failed_documents(self, failed_documents):
        """
        Sets the failed_documents of this Job.
        Number of documents failed for prediction. For CSV this signifies number of rows and for TXT this signifies number of files.


        :param failed_documents: The failed_documents of this Job.
        :type: int
        """
        self._failed_documents = failed_documents

    @property
    def warnings_count(self):
        """
        Gets the warnings_count of this Job.
        warnings count


        :return: The warnings_count of this Job.
        :rtype: int
        """
        return self._warnings_count

    @warnings_count.setter
    def warnings_count(self, warnings_count):
        """
        Sets the warnings_count of this Job.
        warnings count


        :param warnings_count: The warnings_count of this Job.
        :type: int
        """
        self._warnings_count = warnings_count

    @property
    def output_location(self):
        """
        **[Required]** Gets the output_location of this Job.

        :return: The output_location of this Job.
        :rtype: oci.ai_language.models.ObjectPrefixOutputLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this Job.

        :param output_location: The output_location of this Job.
        :type: oci.ai_language.models.ObjectPrefixOutputLocation
        """
        self._output_location = output_location

    @property
    def ttl_in_days(self):
        """
        Gets the ttl_in_days of this Job.
        Time to live duration in days for Job. Job will be available till max 90 days.


        :return: The ttl_in_days of this Job.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        """
        Sets the ttl_in_days of this Job.
        Time to live duration in days for Job. Job will be available till max 90 days.


        :param ttl_in_days: The ttl_in_days of this Job.
        :type: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def created_by(self):
        """
        Gets the created_by of this Job.
        The `OCID`__ of the user who created the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The created_by of this Job.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Job.
        The `OCID`__ of the user who created the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this Job.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this Job.
        Job accepted time.


        :return: The time_accepted of this Job.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this Job.
        Job accepted time.


        :param time_accepted: The time_accepted of this Job.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this Job.
        Job started time.


        :return: The time_started of this Job.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this Job.
        Job started time.


        :param time_started: The time_started of this Job.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_completed(self):
        """
        Gets the time_completed of this Job.
        Job finished time.


        :return: The time_completed of this Job.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this Job.
        Job finished time.


        :param time_completed: The time_completed of this Job.
        :type: datetime
        """
        self._time_completed = time_completed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
