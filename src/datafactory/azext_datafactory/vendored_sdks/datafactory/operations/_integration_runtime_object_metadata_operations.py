# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Iterator, Optional, Type, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_refresh_request(
    resource_group_name: str, factory_name: str, integration_runtime_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/refreshObjectMetadata",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "factoryName": _SERIALIZER.url(
            "factory_name",
            factory_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
        "integrationRuntimeName": _SERIALIZER.url(
            "integration_runtime_name",
            integration_runtime_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, factory_name: str, integration_runtime_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/getObjectMetadata",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "factoryName": _SERIALIZER.url(
            "factory_name",
            factory_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
        "integrationRuntimeName": _SERIALIZER.url(
            "integration_runtime_name",
            integration_runtime_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class IntegrationRuntimeObjectMetadataOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.datafactory.DataFactoryManagementClient`'s
        :attr:`integration_runtime_object_metadata` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def _refresh_initial(
        self, resource_group_name: str, factory_name: str, integration_runtime_name: str, **kwargs: Any
    ) -> Iterator[bytes]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        _request = build_refresh_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            integration_runtime_name=integration_runtime_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def begin_refresh(
        self, resource_group_name: str, factory_name: str, integration_runtime_name: str, **kwargs: Any
    ) -> LROPoller[_models.SsisObjectMetadataStatusResponse]:
        """Refresh a SSIS integration runtime object metadata.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :return: An instance of LROPoller that returns either SsisObjectMetadataStatusResponse or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.datafactory.models.SsisObjectMetadataStatusResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SsisObjectMetadataStatusResponse] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._refresh_initial(
                resource_group_name=resource_group_name,
                factory_name=factory_name,
                integration_runtime_name=integration_runtime_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("SsisObjectMetadataStatusResponse", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: PollingMethod = cast(PollingMethod, ARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[_models.SsisObjectMetadataStatusResponse].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[_models.SsisObjectMetadataStatusResponse](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @overload
    def get(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        get_metadata_request: Optional[_models.GetSsisObjectMetadataRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SsisObjectMetadataListResponse:
        """Get a SSIS integration runtime object metadata by specified path. The return is pageable
        metadata list.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param get_metadata_request: The parameters for getting a SSIS object metadata. Default value
         is None.
        :type get_metadata_request: ~azure.mgmt.datafactory.models.GetSsisObjectMetadataRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SsisObjectMetadataListResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.SsisObjectMetadataListResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def get(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        get_metadata_request: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SsisObjectMetadataListResponse:
        """Get a SSIS integration runtime object metadata by specified path. The return is pageable
        metadata list.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param get_metadata_request: The parameters for getting a SSIS object metadata. Default value
         is None.
        :type get_metadata_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SsisObjectMetadataListResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.SsisObjectMetadataListResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        get_metadata_request: Optional[Union[_models.GetSsisObjectMetadataRequest, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.SsisObjectMetadataListResponse:
        """Get a SSIS integration runtime object metadata by specified path. The return is pageable
        metadata list.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param get_metadata_request: The parameters for getting a SSIS object metadata. Is either a
         GetSsisObjectMetadataRequest type or a IO[bytes] type. Default value is None.
        :type get_metadata_request: ~azure.mgmt.datafactory.models.GetSsisObjectMetadataRequest or
         IO[bytes]
        :return: SsisObjectMetadataListResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.SsisObjectMetadataListResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SsisObjectMetadataListResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(get_metadata_request, (IOBase, bytes)):
            _content = get_metadata_request
        else:
            if get_metadata_request is not None:
                _json = self._serialize.body(get_metadata_request, "GetSsisObjectMetadataRequest")
            else:
                _json = None

        _request = build_get_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            integration_runtime_name=integration_runtime_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SsisObjectMetadataListResponse", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
