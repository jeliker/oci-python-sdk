# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class ManagedInstanceClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.os_management_hub.ManagedInstanceClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new ManagedInstanceClientCompositeOperations object

        :param ManagedInstanceClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def attach_software_sources_to_managed_instance_and_wait_for_state(self, managed_instance_id, attach_software_sources_to_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.attach_software_sources_to_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.AttachSoftwareSourcesToManagedInstanceDetails attach_software_sources_to_managed_instance_details: (required)
            Details of software sources to be attached to a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.attach_software_sources_to_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.attach_software_sources_to_managed_instance(managed_instance_id, attach_software_sources_to_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def detach_software_sources_from_managed_instance_and_wait_for_state(self, managed_instance_id, detach_software_sources_from_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.detach_software_sources_from_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.DetachSoftwareSourcesFromManagedInstanceDetails detach_software_sources_from_managed_instance_details: (required)
            Details of software sources to be detached from a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.detach_software_sources_from_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.detach_software_sources_from_managed_instance(managed_instance_id, detach_software_sources_from_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def disable_module_stream_on_managed_instance_and_wait_for_state(self, managed_instance_id, disable_module_stream_on_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.disable_module_stream_on_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.DisableModuleStreamOnManagedInstanceDetails disable_module_stream_on_managed_instance_details: (required)
            The details of the module stream to be disabled on a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.disable_module_stream_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.disable_module_stream_on_managed_instance(managed_instance_id, disable_module_stream_on_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def enable_module_stream_on_managed_instance_and_wait_for_state(self, managed_instance_id, enable_module_stream_on_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.enable_module_stream_on_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.EnableModuleStreamOnManagedInstanceDetails enable_module_stream_on_managed_instance_details: (required)
            The details of the module stream to be enabled on a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.enable_module_stream_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.enable_module_stream_on_managed_instance(managed_instance_id, enable_module_stream_on_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_module_stream_profile_on_managed_instance_and_wait_for_state(self, managed_instance_id, install_module_stream_profile_on_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.install_module_stream_profile_on_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.InstallModuleStreamProfileOnManagedInstanceDetails install_module_stream_profile_on_managed_instance_details: (required)
            The details of the module stream profile to be installed on a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.install_module_stream_profile_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_module_stream_profile_on_managed_instance(managed_instance_id, install_module_stream_profile_on_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def install_packages_on_managed_instance_and_wait_for_state(self, managed_instance_id, install_packages_on_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.install_packages_on_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.InstallPackagesOnManagedInstanceDetails install_packages_on_managed_instance_details: (required)
            Details about packages to be installed on a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.install_packages_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.install_packages_on_managed_instance(managed_instance_id, install_packages_on_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def list_managed_instance_modules_and_wait_for_state(self, managed_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.list_managed_instance_modules` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.list_managed_instance_modules`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.list_managed_instance_modules(managed_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def manage_module_streams_on_managed_instance_and_wait_for_state(self, managed_instance_id, manage_module_streams_on_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.manage_module_streams_on_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.ManageModuleStreamsOnManagedInstanceDetails manage_module_streams_on_managed_instance_details: (required)
            A description of an operation to perform against the modules, streams, and profiles of a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.manage_module_streams_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.manage_module_streams_on_managed_instance(managed_instance_id, manage_module_streams_on_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def refresh_software_on_managed_instance_and_wait_for_state(self, managed_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.refresh_software_on_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.refresh_software_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.refresh_software_on_managed_instance(managed_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def remove_module_stream_profile_from_managed_instance_and_wait_for_state(self, managed_instance_id, remove_module_stream_profile_from_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.remove_module_stream_profile_from_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.RemoveModuleStreamProfileFromManagedInstanceDetails remove_module_stream_profile_from_managed_instance_details: (required)
            The details of the module stream profile to be removed from a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.remove_module_stream_profile_from_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.remove_module_stream_profile_from_managed_instance(managed_instance_id, remove_module_stream_profile_from_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def remove_packages_from_managed_instance_and_wait_for_state(self, managed_instance_id, remove_packages_from_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.remove_packages_from_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.RemovePackagesFromManagedInstanceDetails remove_packages_from_managed_instance_details: (required)
            Details about packages to be removed on a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.remove_packages_from_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.remove_packages_from_managed_instance(managed_instance_id, remove_packages_from_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def switch_module_stream_on_managed_instance_and_wait_for_state(self, managed_instance_id, switch_module_stream_on_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.switch_module_stream_on_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.SwitchModuleStreamOnManagedInstanceDetails switch_module_stream_on_managed_instance_details: (required)
            The details of the module stream to be switched on a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.switch_module_stream_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.switch_module_stream_on_managed_instance(managed_instance_id, switch_module_stream_on_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_all_packages_on_managed_instances_in_compartment_and_wait_for_state(self, update_all_packages_on_managed_instances_in_compartment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.update_all_packages_on_managed_instances_in_compartment` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param oci.os_management_hub.models.UpdateAllPackagesOnManagedInstancesInCompartmentDetails update_all_packages_on_managed_instances_in_compartment_details: (required)
            The details about package types are to be updated on all managed instances in a compartment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.update_all_packages_on_managed_instances_in_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_all_packages_on_managed_instances_in_compartment(update_all_packages_on_managed_instances_in_compartment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_packages_on_managed_instance_and_wait_for_state(self, managed_instance_id, update_packages_on_managed_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.ManagedInstanceClient.update_packages_on_managed_instance` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param oci.os_management_hub.models.UpdatePackagesOnManagedInstanceDetails update_packages_on_managed_instance_details: (required)
            Details about packages to be updated on a managed instance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.ManagedInstanceClient.update_packages_on_managed_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_packages_on_managed_instance(managed_instance_id, update_packages_on_managed_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
