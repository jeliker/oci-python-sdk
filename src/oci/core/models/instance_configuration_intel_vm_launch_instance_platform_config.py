# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .instance_configuration_launch_instance_platform_config import InstanceConfigurationLaunchInstancePlatformConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationIntelVmLaunchInstancePlatformConfig(InstanceConfigurationLaunchInstancePlatformConfig):
    """
    The platform configuration used when launching a virtual machine instance with the Intel platform.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationIntelVmLaunchInstancePlatformConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceConfigurationIntelVmLaunchInstancePlatformConfig.type` attribute
        of this class is ``INTEL_VM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
            Allowed values for this property are: "AMD_MILAN_BM", "AMD_MILAN_BM_GPU", "AMD_ROME_BM", "AMD_ROME_BM_GPU", "GENERIC_BM", "INTEL_ICELAKE_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM"
        :type type: str

        :param is_secure_boot_enabled:
            The value to assign to the is_secure_boot_enabled property of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        :type is_secure_boot_enabled: bool

        :param is_trusted_platform_module_enabled:
            The value to assign to the is_trusted_platform_module_enabled property of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        :type is_trusted_platform_module_enabled: bool

        :param is_measured_boot_enabled:
            The value to assign to the is_measured_boot_enabled property of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        :type is_measured_boot_enabled: bool

        :param is_memory_encryption_enabled:
            The value to assign to the is_memory_encryption_enabled property of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        :type is_memory_encryption_enabled: bool

        :param is_symmetric_multi_threading_enabled:
            The value to assign to the is_symmetric_multi_threading_enabled property of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        :type is_symmetric_multi_threading_enabled: bool

        """
        self.swagger_types = {
            'type': 'str',
            'is_secure_boot_enabled': 'bool',
            'is_trusted_platform_module_enabled': 'bool',
            'is_measured_boot_enabled': 'bool',
            'is_memory_encryption_enabled': 'bool',
            'is_symmetric_multi_threading_enabled': 'bool'
        }
        self.attribute_map = {
            'type': 'type',
            'is_secure_boot_enabled': 'isSecureBootEnabled',
            'is_trusted_platform_module_enabled': 'isTrustedPlatformModuleEnabled',
            'is_measured_boot_enabled': 'isMeasuredBootEnabled',
            'is_memory_encryption_enabled': 'isMemoryEncryptionEnabled',
            'is_symmetric_multi_threading_enabled': 'isSymmetricMultiThreadingEnabled'
        }
        self._type = None
        self._is_secure_boot_enabled = None
        self._is_trusted_platform_module_enabled = None
        self._is_measured_boot_enabled = None
        self._is_memory_encryption_enabled = None
        self._is_symmetric_multi_threading_enabled = None
        self._type = 'INTEL_VM'

    @property
    def is_symmetric_multi_threading_enabled(self):
        """
        Gets the is_symmetric_multi_threading_enabled of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
        called simultaneous multithreading (SMT) or Intel Hyper-Threading.

        Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
        independent threads of execution, to better use the resources and increase the efficiency
        of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
        can provide higher or more predictable performance for some workloads.


        :return: The is_symmetric_multi_threading_enabled of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        :rtype: bool
        """
        return self._is_symmetric_multi_threading_enabled

    @is_symmetric_multi_threading_enabled.setter
    def is_symmetric_multi_threading_enabled(self, is_symmetric_multi_threading_enabled):
        """
        Sets the is_symmetric_multi_threading_enabled of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
        called simultaneous multithreading (SMT) or Intel Hyper-Threading.

        Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
        independent threads of execution, to better use the resources and increase the efficiency
        of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
        can provide higher or more predictable performance for some workloads.


        :param is_symmetric_multi_threading_enabled: The is_symmetric_multi_threading_enabled of this InstanceConfigurationIntelVmLaunchInstancePlatformConfig.
        :type: bool
        """
        self._is_symmetric_multi_threading_enabled = is_symmetric_multi_threading_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
