# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._volume_quota_rules_operations import build_create_request_initial, build_delete_request_initial, build_get_request, build_list_by_volume_request, build_update_request_initial
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class VolumeQuotaRulesOperations:
    """VolumeQuotaRulesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.netapp.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_volume(
        self,
        resource_group_name: str,
        account_name: str,
        pool_name: str,
        volume_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.VolumeQuotaRulesList"]:
        """Get all quota rules for a volume.

        List all quota rules associated with the volume.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param account_name: The name of the NetApp account.
        :type account_name: str
        :param pool_name: The name of the capacity pool.
        :type pool_name: str
        :param volume_name: The name of the volume.
        :type volume_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either VolumeQuotaRulesList or the result of
         cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.netapp.models.VolumeQuotaRulesList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-01-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VolumeQuotaRulesList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_volume_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    pool_name=pool_name,
                    volume_name=volume_name,
                    api_version=api_version,
                    template_url=self.list_by_volume.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_volume_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    pool_name=pool_name,
                    volume_name=volume_name,
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("VolumeQuotaRulesList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_volume.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        account_name: str,
        pool_name: str,
        volume_name: str,
        volume_quota_rule_name: str,
        **kwargs: Any
    ) -> "_models.VolumeQuotaRule":
        """Describe a quota rule.

        Get details of the specified quota rule.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param account_name: The name of the NetApp account.
        :type account_name: str
        :param pool_name: The name of the capacity pool.
        :type pool_name: str
        :param volume_name: The name of the volume.
        :type volume_name: str
        :param volume_quota_rule_name: The name of volume quota rule.
        :type volume_quota_rule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VolumeQuotaRule, or the result of cls(response)
        :rtype: ~azure.mgmt.netapp.models.VolumeQuotaRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VolumeQuotaRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            account_name=account_name,
            pool_name=pool_name,
            volume_name=volume_name,
            volume_quota_rule_name=volume_quota_rule_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('VolumeQuotaRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules/{volumeQuotaRuleName}"}  # type: ignore


    async def _create_initial(
        self,
        resource_group_name: str,
        account_name: str,
        pool_name: str,
        volume_name: str,
        volume_quota_rule_name: str,
        body: "_models.VolumeQuotaRule",
        **kwargs: Any
    ) -> "_models.VolumeQuotaRule":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VolumeQuotaRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(body, 'VolumeQuotaRule')

        request = build_create_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            account_name=account_name,
            pool_name=pool_name,
            volume_name=volume_name,
            volume_quota_rule_name=volume_quota_rule_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._create_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('VolumeQuotaRule', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('VolumeQuotaRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules/{volumeQuotaRuleName}"}  # type: ignore


    @distributed_trace_async
    async def begin_create(
        self,
        resource_group_name: str,
        account_name: str,
        pool_name: str,
        volume_name: str,
        volume_quota_rule_name: str,
        body: "_models.VolumeQuotaRule",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.VolumeQuotaRule"]:
        """Create a quota rule.

        Create the specified quota rule within the given volume.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param account_name: The name of the NetApp account.
        :type account_name: str
        :param pool_name: The name of the capacity pool.
        :type pool_name: str
        :param volume_name: The name of the volume.
        :type volume_name: str
        :param volume_quota_rule_name: The name of volume quota rule.
        :type volume_quota_rule_name: str
        :param body: Quota rule object supplied in the body of the operation.
        :type body: ~azure.mgmt.netapp.models.VolumeQuotaRule
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VolumeQuotaRule or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.netapp.models.VolumeQuotaRule]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-01-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VolumeQuotaRule"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_initial(
                resource_group_name=resource_group_name,
                account_name=account_name,
                pool_name=pool_name,
                volume_name=volume_name,
                volume_quota_rule_name=volume_quota_rule_name,
                body=body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('VolumeQuotaRule', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules/{volumeQuotaRuleName}"}  # type: ignore

    async def _update_initial(
        self,
        resource_group_name: str,
        account_name: str,
        pool_name: str,
        volume_name: str,
        volume_quota_rule_name: str,
        body: "_models.VolumeQuotaRulePatch",
        **kwargs: Any
    ) -> Optional["_models.VolumeQuotaRule"]:
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.VolumeQuotaRule"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(body, 'VolumeQuotaRulePatch')

        request = build_update_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            account_name=account_name,
            pool_name=pool_name,
            volume_name=volume_name,
            volume_quota_rule_name=volume_quota_rule_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._update_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('VolumeQuotaRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules/{volumeQuotaRuleName}"}  # type: ignore


    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        account_name: str,
        pool_name: str,
        volume_name: str,
        volume_quota_rule_name: str,
        body: "_models.VolumeQuotaRulePatch",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.VolumeQuotaRule"]:
        """Update a quota rule.

        Patch a quota rule.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param account_name: The name of the NetApp account.
        :type account_name: str
        :param pool_name: The name of the capacity pool.
        :type pool_name: str
        :param volume_name: The name of the volume.
        :type volume_name: str
        :param volume_quota_rule_name: The name of volume quota rule.
        :type volume_quota_rule_name: str
        :param body: Quota rule object supplied in the body of the operation.
        :type body: ~azure.mgmt.netapp.models.VolumeQuotaRulePatch
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VolumeQuotaRule or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.netapp.models.VolumeQuotaRule]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-01-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VolumeQuotaRule"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                account_name=account_name,
                pool_name=pool_name,
                volume_name=volume_name,
                volume_quota_rule_name=volume_quota_rule_name,
                body=body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('VolumeQuotaRule', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules/{volumeQuotaRuleName}"}  # type: ignore

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        account_name: str,
        pool_name: str,
        volume_name: str,
        volume_quota_rule_name: str,
        **kwargs: Any
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01")  # type: str

        
        request = build_delete_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            account_name=account_name,
            pool_name=pool_name,
            volume_name=volume_name,
            volume_quota_rule_name=volume_quota_rule_name,
            api_version=api_version,
            template_url=self._delete_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules/{volumeQuotaRuleName}"}  # type: ignore


    @distributed_trace_async
    async def begin_delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        account_name: str,
        pool_name: str,
        volume_name: str,
        volume_quota_rule_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete a quota rule.

        Delete quota rule.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param account_name: The name of the NetApp account.
        :type account_name: str
        :param pool_name: The name of the capacity pool.
        :type pool_name: str
        :param volume_name: The name of the volume.
        :type volume_name: str
        :param volume_quota_rule_name: The name of volume quota rule.
        :type volume_quota_rule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-01-01")  # type: str
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                account_name=account_name,
                pool_name=pool_name,
                volume_name=volume_name,
                volume_quota_rule_name=volume_quota_rule_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/volumeQuotaRules/{volumeQuotaRuleName}"}  # type: ignore
