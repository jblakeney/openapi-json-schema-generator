<a name="__pageTop"></a>
# petstore_api.apis.tags.pet_api.PetApi

All URIs are relative to *http://petstore.swagger.io:80/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pet**](#add_pet) | **post** /pet | Add a new pet to the store
[**delete_pet**](#delete_pet) | **delete** /pet/{petId} | Deletes a pet
[**get_pet_by_id**](#get_pet_by_id) | **get** /pet/{petId} | Find pet by ID
[**update_pet**](#update_pet) | **put** /pet | Update an existing pet
[**update_pet_with_form**](#update_pet_with_form) | **post** /pet/{petId} | Updates a pet in the store with form data

# **add_pet**
<a name="add_pet"></a>

Add a new pet to the store

Add a new pet to the store

### Example

* Api Key Authentication (aws_sigv4):
```python
import petstore_api
from petstore_api.apis.tags import pet_api
from petstore_api.components.schema.pet import Pet
from pprint import pprint
# Defining the host is optional and defaults to http://petstore.swagger.io:80/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://petstore.swagger.io:80/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: aws_sigv4
configuration.api_key['aws_sigv4'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aws_sigv4'] = 'Bearer'
# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)

    # example passing only required values which don't have defaults set
    body = Pet(
        id=1,
        category=Category(
            id=1,
            name="default-name",
        ),
        name="doggie",
        photo_urls=[
            "photo_urls_example"
        ],
        tags=[
            Tag(
                id=1,
                name="name_example",
            )
        ],
        status="available",
    )
    try:
        # Add a new pet to the store
        api_response = api_instance.add_pet(
            body=body,
        )
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->add_pet: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#add_pet.request_body) | typing.Union[[request_body.application_json](#add_pet.request_body.application_json), [request_body.application_xml](#add_pet.request_body.application_xml)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
host_index | typing.Optional[int] | default is None | Allows one to select a different host
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="add_pet.request_body" >body</a>

# <a id="add_pet.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Pet**](../../components/schema/Pet.md) |  | 


# <a id="add_pet.request_body.application_xml" >request_body.application_xml</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Pet**](../../components/schema/Pet.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#add_pet.response_for_200.ApiResponse) | Ok
405 | [response_for_405.ApiResponse](#add_pet.response_for_405.ApiResponse) | Invalid input

#### <a id="add_pet.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### <a id="add_pet.response_for_405.ApiResponse" >response_for_405.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[aws_sigv4](../../../README.md#aws_sigv4)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_pet**
<a name="delete_pet"></a>

Deletes a pet

### Example

* Api Key Authentication (aws_sigv4):
```python
import petstore_api
from petstore_api.apis.tags import pet_api
from pprint import pprint
# Defining the host is optional and defaults to http://petstore.swagger.io:80/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://petstore.swagger.io:80/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: aws_sigv4
configuration.api_key['aws_sigv4'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aws_sigv4'] = 'Bearer'
# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'petId': 1,
    }
    header_params = {
    }
    try:
        # Deletes a pet
        api_response = api_instance.delete_pet(
            path_params=path_params,
            header_params=header_params,
        )
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->delete_pet: %s\n" % e)

    # example passing only optional values
    path_params = {
        'petId': 1,
    }
    header_params = {
        'api_key': "api_key_example",
    }
    try:
        # Deletes a pet
        api_response = api_instance.delete_pet(
            path_params=path_params,
            header_params=header_params,
        )
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->delete_pet: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[header_params](#delete_pet.RequestHeaderParameters) | [RequestHeaderParameters.Params](#delete_pet.RequestHeaderParameters.Params) | |
[path_params](#delete_pet.RequestPathParameters) | [RequestPathParameters.Params](#delete_pet.RequestPathParameters.Params) | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="delete_pet.RequestHeaderParameters" >header_params</a>
#### <a id="delete_pet.RequestHeaderParameters.Params" >RequestHeaderParameters.Params</a>

Key | Input Type | Description  | Notes
------------- | ------------- | ------------- | -------------
api_key | [parameter_0.schema](#delete_pet.parameter_0.schema) | | optional

# <a id="delete_pet.parameter_0.schema" >parameter_0.schema</a>

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### <a id="delete_pet.RequestPathParameters" >path_params</a>
#### <a id="delete_pet.RequestPathParameters.Params" >RequestPathParameters.Params</a>

Key | Input Type | Description  | Notes
------------- | ------------- | ------------- | -------------
petId | [parameter_1.schema](#delete_pet.parameter_1.schema) | | 

# <a id="delete_pet.parameter_1.schema" >parameter_1.schema</a>

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [response_for_400.ApiResponse](#delete_pet.response_for_400.ApiResponse) | Invalid pet value

#### <a id="delete_pet.response_for_400.ApiResponse" >response_for_400.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[aws_sigv4](../../../README.md#aws_sigv4)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pet_by_id**
<a name="get_pet_by_id"></a>

Find pet by ID

Returns a single pet

### Example

* Api Key Authentication (aws_sigv4):
```python
import petstore_api
from petstore_api.apis.tags import pet_api
from pprint import pprint
# Defining the host is optional and defaults to http://petstore.swagger.io:80/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://petstore.swagger.io:80/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: aws_sigv4
configuration.api_key['aws_sigv4'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aws_sigv4'] = 'Bearer'
# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'petId': 1,
    }
    try:
        # Find pet by ID
        api_response = api_instance.get_pet_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->get_pet_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[path_params](#get_pet_by_id.RequestPathParameters) | [RequestPathParameters.Params](#get_pet_by_id.RequestPathParameters.Params) | |
accept_content_types | typing.Tuple[str] | default is ('application/xml', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="get_pet_by_id.RequestPathParameters" >path_params</a>
#### <a id="get_pet_by_id.RequestPathParameters.Params" >RequestPathParameters.Params</a>

Key | Input Type | Description  | Notes
------------- | ------------- | ------------- | -------------
petId | [parameter_0.schema](#get_pet_by_id.parameter_0.schema) | | 

# <a id="get_pet_by_id.parameter_0.schema" >parameter_0.schema</a>

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#get_pet_by_id.response_for_200.ApiResponse) | successful operation
400 | [response_for_400.ApiResponse](#get_pet_by_id.response_for_400.ApiResponse) | Invalid ID supplied
404 | [response_for_404.ApiResponse](#get_pet_by_id.response_for_404.ApiResponse) | Pet not found

#### <a id="get_pet_by_id.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_xml](#get_pet_by_id.response_for_200.application_xml), [response_for_200.application_json](#get_pet_by_id.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="get_pet_by_id.response_for_200.application_xml" >response_for_200.application_xml</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Pet**](../../components/schema/Pet.md) |  | 


# <a id="get_pet_by_id.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Pet**](../../components/schema/Pet.md) |  | 


#### <a id="get_pet_by_id.response_for_400.ApiResponse" >response_for_400.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### <a id="get_pet_by_id.response_for_404.ApiResponse" >response_for_404.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[aws_sigv4](../../../README.md#aws_sigv4)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_pet**
<a name="update_pet"></a>

Update an existing pet

### Example

* Api Key Authentication (aws_sigv4):
```python
import petstore_api
from petstore_api.apis.tags import pet_api
from petstore_api.components.schema.pet import Pet
from pprint import pprint
# Defining the host is optional and defaults to http://petstore.swagger.io:80/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://petstore.swagger.io:80/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: aws_sigv4
configuration.api_key['aws_sigv4'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aws_sigv4'] = 'Bearer'
# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)

    # example passing only required values which don't have defaults set
    body = Pet(
        id=1,
        category=Category(
            id=1,
            name="default-name",
        ),
        name="doggie",
        photo_urls=[
            "photo_urls_example"
        ],
        tags=[
            Tag(
                id=1,
                name="name_example",
            )
        ],
        status="available",
    )
    try:
        # Update an existing pet
        api_response = api_instance.update_pet(
            body=body,
        )
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->update_pet: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#update_pet.request_body) | typing.Union[[request_body.application_json](#update_pet.request_body.application_json), [request_body.application_xml](#update_pet.request_body.application_xml)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
host_index | typing.Optional[int] | default is None | Allows one to select a different host
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="update_pet.request_body" >body</a>

# <a id="update_pet.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Pet**](../../components/schema/Pet.md) |  | 


# <a id="update_pet.request_body.application_xml" >request_body.application_xml</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Pet**](../../components/schema/Pet.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [response_for_400.ApiResponse](#update_pet.response_for_400.ApiResponse) | Invalid ID supplied
404 | [response_for_404.ApiResponse](#update_pet.response_for_404.ApiResponse) | Pet not found
405 | [response_for_405.ApiResponse](#update_pet.response_for_405.ApiResponse) | Validation exception

#### <a id="update_pet.response_for_400.ApiResponse" >response_for_400.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### <a id="update_pet.response_for_404.ApiResponse" >response_for_404.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### <a id="update_pet.response_for_405.ApiResponse" >response_for_405.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[aws_sigv4](../../../README.md#aws_sigv4)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_pet_with_form**
<a name="update_pet_with_form"></a>

Updates a pet in the store with form data

### Example

* Api Key Authentication (aws_sigv4):
```python
import petstore_api
from petstore_api.apis.tags import pet_api
from pprint import pprint
# Defining the host is optional and defaults to http://petstore.swagger.io:80/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = petstore_api.Configuration(
    host = "http://petstore.swagger.io:80/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: aws_sigv4
configuration.api_key['aws_sigv4'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aws_sigv4'] = 'Bearer'
# Enter a context with an instance of the API client
with petstore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'petId': 1,
    }
    try:
        # Updates a pet in the store with form data
        api_response = api_instance.update_pet_with_form(
            path_params=path_params,
        )
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->update_pet_with_form: %s\n" % e)

    # example passing only optional values
    path_params = {
        'petId': 1,
    }
    body = dict(
        name="name_example",
        status="status_example",
    )
    try:
        # Updates a pet in the store with form data
        api_response = api_instance.update_pet_with_form(
            path_params=path_params,
            body=body,
        )
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->update_pet_with_form: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#update_pet_with_form.request_body) | typing.Union[[request_body.application_x_www_form_urlencoded](#update_pet_with_form.request_body.application_x_www_form_urlencoded), Unset] | optional, default is unset |
[path_params](#update_pet_with_form.RequestPathParameters) | [RequestPathParameters.Params](#update_pet_with_form.RequestPathParameters.Params) | |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="update_pet_with_form.request_body" >body</a>

# <a id="update_pet_with_form.request_body.application_x_www_form_urlencoded" >request_body.application_x_www_form_urlencoded</a>

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Updated name of the pet | [optional] 
**status** | str,  | str,  | Updated status of the pet | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### <a id="update_pet_with_form.RequestPathParameters" >path_params</a>
#### <a id="update_pet_with_form.RequestPathParameters.Params" >RequestPathParameters.Params</a>

Key | Input Type | Description  | Notes
------------- | ------------- | ------------- | -------------
petId | [parameter_0.schema](#update_pet_with_form.parameter_0.schema) | | 

# <a id="update_pet_with_form.parameter_0.schema" >parameter_0.schema</a>

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
405 | [response_for_405.ApiResponse](#update_pet_with_form.response_for_405.ApiResponse) | Invalid input

#### <a id="update_pet_with_form.response_for_405.ApiResponse" >response_for_405.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[aws_sigv4](../../../README.md#aws_sigv4)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

