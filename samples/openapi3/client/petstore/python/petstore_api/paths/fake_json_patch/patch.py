# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from petstore_api.model.json_patch_request import JSONPatchRequest

from . import path

# body param
SchemaForRequestBodyApplicationJsonPatchjson = JSONPatchRequest


request_body_json_patch_request = api_client.RequestBody(
    content={
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
    },
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
)
_status_code_to_response = {
    '200': _response_for_200,
}


class BaseApi(api_client.Api):

    @typing.overload
    def _json_patch_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[ApiResponseFor200,api_client.ApiResponse]:
        ...

    @typing.overload
    def _json_patch_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def _json_patch_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def _json_patch_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        json patch
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_json_patch_request.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='patch'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class JsonPatch(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def json_patch(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[ApiResponseFor200,api_client.ApiResponse]:
        ...

    @typing.overload
    def json_patch(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def json_patch(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def json_patch(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        return self._json_patch_oapg(
            body=body,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def patch(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[ApiResponseFor200,api_client.ApiResponse]:
        ...

    @typing.overload
    def patch(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def patch(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def patch(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson,schemas.Unset] = schemas.unset,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        return self._json_patch_oapg(
            body=body,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


