# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

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


class ObjectModelWithRefProps(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    a model that includes properties which should stay primitive (String + Boolean) and one which is defined as a class, NumberWithValidations
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def myNumber() -> typing.Type['NumberWithValidations']:
                return NumberWithValidations
        
            @staticmethod
            def myString() -> typing.Type['String']:
                return String
        
            @staticmethod
            def myBoolean() -> typing.Type['Boolean']:
                return Boolean
            __annotations__ = {
                "myNumber": myNumber,
                "myString": myString,
                "myBoolean": myBoolean,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["myNumber"]) -> 'NumberWithValidations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["myString"]) -> 'String': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["myBoolean"]) -> 'Boolean': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["myNumber", "myString", "myBoolean", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["myNumber"]) -> typing.Union['NumberWithValidations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["myString"]) -> typing.Union['String', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["myBoolean"]) -> typing.Union['Boolean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["myNumber", "myString", "myBoolean", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        myNumber: typing.Union['NumberWithValidations', schemas.Unset] = schemas.unset,
        myString: typing.Union['String', schemas.Unset] = schemas.unset,
        myBoolean: typing.Union['Boolean', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjectModelWithRefProps':
        return super().__new__(
            cls,
            *args,
            myNumber=myNumber,
            myString=myString,
            myBoolean=myBoolean,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.boolean import Boolean
from petstore_api.model.number_with_validations import NumberWithValidations
from petstore_api.model.string import String
