# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployedApplicationInstallationUsageSummary(object):
    """
    Summarize usage information about an application deployed on Java servers including installation information during a specified time period. The main difference between DeployedApplicationInstallationUsageSummary and DeployedApplicationUsage is the presence of the applicationSourcePath. DeployedApplicationUsage provides only an aggregated view to the deployed applications without installation information. DeployedApplicationUsage does not distinguish between applications with the identical deployment information deployed to different paths. DeployedApplicationInstallationUsageSummary contains installation information used to select target actions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployedApplicationInstallationUsageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param application_installation_key:
            The value to assign to the application_installation_key property of this DeployedApplicationInstallationUsageSummary.
        :type application_installation_key: str

        :param application_key:
            The value to assign to the application_key property of this DeployedApplicationInstallationUsageSummary.
        :type application_key: str

        :param fleet_id:
            The value to assign to the fleet_id property of this DeployedApplicationInstallationUsageSummary.
        :type fleet_id: str

        :param application_name:
            The value to assign to the application_name property of this DeployedApplicationInstallationUsageSummary.
        :type application_name: str

        :param application_type:
            The value to assign to the application_type property of this DeployedApplicationInstallationUsageSummary.
        :type application_type: str

        :param application_source_path:
            The value to assign to the application_source_path property of this DeployedApplicationInstallationUsageSummary.
        :type application_source_path: str

        :param is_clustered:
            The value to assign to the is_clustered property of this DeployedApplicationInstallationUsageSummary.
        :type is_clustered: bool

        :param approximate_java_server_instance_count:
            The value to assign to the approximate_java_server_instance_count property of this DeployedApplicationInstallationUsageSummary.
        :type approximate_java_server_instance_count: int

        :param approximate_library_count:
            The value to assign to the approximate_library_count property of this DeployedApplicationInstallationUsageSummary.
        :type approximate_library_count: int

        :param time_start:
            The value to assign to the time_start property of this DeployedApplicationInstallationUsageSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this DeployedApplicationInstallationUsageSummary.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this DeployedApplicationInstallationUsageSummary.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this DeployedApplicationInstallationUsageSummary.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'application_installation_key': 'str',
            'application_key': 'str',
            'fleet_id': 'str',
            'application_name': 'str',
            'application_type': 'str',
            'application_source_path': 'str',
            'is_clustered': 'bool',
            'approximate_java_server_instance_count': 'int',
            'approximate_library_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }
        self.attribute_map = {
            'application_installation_key': 'applicationInstallationKey',
            'application_key': 'applicationKey',
            'fleet_id': 'fleetId',
            'application_name': 'applicationName',
            'application_type': 'applicationType',
            'application_source_path': 'applicationSourcePath',
            'is_clustered': 'isClustered',
            'approximate_java_server_instance_count': 'approximateJavaServerInstanceCount',
            'approximate_library_count': 'approximateLibraryCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }
        self._application_installation_key = None
        self._application_key = None
        self._fleet_id = None
        self._application_name = None
        self._application_type = None
        self._application_source_path = None
        self._is_clustered = None
        self._approximate_java_server_instance_count = None
        self._approximate_library_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def application_installation_key(self):
        """
        **[Required]** Gets the application_installation_key of this DeployedApplicationInstallationUsageSummary.
        The internal identifier of the deployed application installation.


        :return: The application_installation_key of this DeployedApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._application_installation_key

    @application_installation_key.setter
    def application_installation_key(self, application_installation_key):
        """
        Sets the application_installation_key of this DeployedApplicationInstallationUsageSummary.
        The internal identifier of the deployed application installation.


        :param application_installation_key: The application_installation_key of this DeployedApplicationInstallationUsageSummary.
        :type: str
        """
        self._application_installation_key = application_installation_key

    @property
    def application_key(self):
        """
        **[Required]** Gets the application_key of this DeployedApplicationInstallationUsageSummary.
        The internal identifier of the deployed application.
        ApplicationKey will be identical for deployed applications with different applicationSourcePaths.


        :return: The application_key of this DeployedApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._application_key

    @application_key.setter
    def application_key(self, application_key):
        """
        Sets the application_key of this DeployedApplicationInstallationUsageSummary.
        The internal identifier of the deployed application.
        ApplicationKey will be identical for deployed applications with different applicationSourcePaths.


        :param application_key: The application_key of this DeployedApplicationInstallationUsageSummary.
        :type: str
        """
        self._application_key = application_key

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this DeployedApplicationInstallationUsageSummary.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this DeployedApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this DeployedApplicationInstallationUsageSummary.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this DeployedApplicationInstallationUsageSummary.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def application_name(self):
        """
        **[Required]** Gets the application_name of this DeployedApplicationInstallationUsageSummary.
        The name of the deployed application.


        :return: The application_name of this DeployedApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """
        Sets the application_name of this DeployedApplicationInstallationUsageSummary.
        The name of the deployed application.


        :param application_name: The application_name of this DeployedApplicationInstallationUsageSummary.
        :type: str
        """
        self._application_name = application_name

    @property
    def application_type(self):
        """
        Gets the application_type of this DeployedApplicationInstallationUsageSummary.
        The type of the deployed application.


        :return: The application_type of this DeployedApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """
        Sets the application_type of this DeployedApplicationInstallationUsageSummary.
        The type of the deployed application.


        :param application_type: The application_type of this DeployedApplicationInstallationUsageSummary.
        :type: str
        """
        self._application_type = application_type

    @property
    def application_source_path(self):
        """
        Gets the application_source_path of this DeployedApplicationInstallationUsageSummary.
        The full path to source WAR or EAR file for deployed application.


        :return: The application_source_path of this DeployedApplicationInstallationUsageSummary.
        :rtype: str
        """
        return self._application_source_path

    @application_source_path.setter
    def application_source_path(self, application_source_path):
        """
        Sets the application_source_path of this DeployedApplicationInstallationUsageSummary.
        The full path to source WAR or EAR file for deployed application.


        :param application_source_path: The application_source_path of this DeployedApplicationInstallationUsageSummary.
        :type: str
        """
        self._application_source_path = application_source_path

    @property
    def is_clustered(self):
        """
        Gets the is_clustered of this DeployedApplicationInstallationUsageSummary.
        Whether or not the deployed application is clustered.


        :return: The is_clustered of this DeployedApplicationInstallationUsageSummary.
        :rtype: bool
        """
        return self._is_clustered

    @is_clustered.setter
    def is_clustered(self, is_clustered):
        """
        Sets the is_clustered of this DeployedApplicationInstallationUsageSummary.
        Whether or not the deployed application is clustered.


        :param is_clustered: The is_clustered of this DeployedApplicationInstallationUsageSummary.
        :type: bool
        """
        self._is_clustered = is_clustered

    @property
    def approximate_java_server_instance_count(self):
        """
        Gets the approximate_java_server_instance_count of this DeployedApplicationInstallationUsageSummary.
        The approximate count of Java Server instances running the deployed application installations.


        :return: The approximate_java_server_instance_count of this DeployedApplicationInstallationUsageSummary.
        :rtype: int
        """
        return self._approximate_java_server_instance_count

    @approximate_java_server_instance_count.setter
    def approximate_java_server_instance_count(self, approximate_java_server_instance_count):
        """
        Sets the approximate_java_server_instance_count of this DeployedApplicationInstallationUsageSummary.
        The approximate count of Java Server instances running the deployed application installations.


        :param approximate_java_server_instance_count: The approximate_java_server_instance_count of this DeployedApplicationInstallationUsageSummary.
        :type: int
        """
        self._approximate_java_server_instance_count = approximate_java_server_instance_count

    @property
    def approximate_library_count(self):
        """
        Gets the approximate_library_count of this DeployedApplicationInstallationUsageSummary.
        The approximate count of libraries in the deployed application.


        :return: The approximate_library_count of this DeployedApplicationInstallationUsageSummary.
        :rtype: int
        """
        return self._approximate_library_count

    @approximate_library_count.setter
    def approximate_library_count(self, approximate_library_count):
        """
        Sets the approximate_library_count of this DeployedApplicationInstallationUsageSummary.
        The approximate count of libraries in the deployed application.


        :param approximate_library_count: The approximate_library_count of this DeployedApplicationInstallationUsageSummary.
        :type: int
        """
        self._approximate_library_count = approximate_library_count

    @property
    def time_start(self):
        """
        Gets the time_start of this DeployedApplicationInstallationUsageSummary.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this DeployedApplicationInstallationUsageSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this DeployedApplicationInstallationUsageSummary.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this DeployedApplicationInstallationUsageSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this DeployedApplicationInstallationUsageSummary.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this DeployedApplicationInstallationUsageSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this DeployedApplicationInstallationUsageSummary.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_end: The time_end of this DeployedApplicationInstallationUsageSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this DeployedApplicationInstallationUsageSummary.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this DeployedApplicationInstallationUsageSummary.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this DeployedApplicationInstallationUsageSummary.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this DeployedApplicationInstallationUsageSummary.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this DeployedApplicationInstallationUsageSummary.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this DeployedApplicationInstallationUsageSummary.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this DeployedApplicationInstallationUsageSummary.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this DeployedApplicationInstallationUsageSummary.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
