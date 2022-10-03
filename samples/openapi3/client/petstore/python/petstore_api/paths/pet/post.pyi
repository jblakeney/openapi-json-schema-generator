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

from petstore_api.model.pet import Pet

# body param
SchemaForRequestBodyApplicationJson = Pet
SchemaForRequestBodyApplicationXml = Pet


class BaseApi(api_client.Api):

    @typing.overload
    def _add_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[ApiResponseFor200,api_client.ApiResponse]:
        ...

    @typing.overload
    def _add_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def _add_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def _add_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add a new pet to the store
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_pet.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        host = self._get_host_oapg('add_pet', _servers, host_index)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            host=host,
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


class AddPet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def add_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[ApiResponseFor200,api_client.ApiResponse]:
        ...

    @typing.overload
    def add_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def add_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def add_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        return self._add_pet_oapg(
            body=body,
            content_type=content_type,
            host_index=host_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[ApiResponseFor200,api_client.ApiResponse]:
        ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        return self._add_pet_oapg(
            body=body,
            content_type=content_type,
            host_index=host_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


