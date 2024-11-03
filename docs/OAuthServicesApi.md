# swagger_client.OAuthServicesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](OAuthServicesApi.md#get) | **GET** /oauth/.well-known/oauth-authorization-server | OAuth configuration metadata
[**post**](OAuthServicesApi.md#post) | **POST** /token | Retrieve bearer access token


# **get**
> OAuthMetaDataConfigurationResponseDto get(api_version=api_version)

OAuth configuration metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OAuthServicesApi()
api_version = 'api_version_example' # str | The requested API version (optional)

try:
    # OAuth configuration metadata
    api_response = api_instance.get(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthServicesApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The requested API version | [optional] 

### Return type

[**OAuthMetaDataConfigurationResponseDto**](OAuthMetaDataConfigurationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> TokenResponseDto post(grant_type, client_id, code, redirect_uri, code_verifier, api_version=api_version)

Retrieve bearer access token

<p>This method is used to request a bearer access token in exchange for an authorization code</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OAuthServicesApi()
grant_type = 'grant_type_example' # str | The grant type used to request an access token.
client_id = 'client_id_example' # str | The client id used during an authorization request.
code = 'code_example' # str | The authorization code to exchange for a bearer access token.
redirect_uri = 'redirect_uri_example' # str | The redirect uri used during an authorization request.
code_verifier = 'code_verifier_example' # str | The code verifier in plain format used during an authorization request.
api_version = 'api_version_example' # str | The requested API version (optional)

try:
    # Retrieve bearer access token
    api_response = api_instance.post(grant_type, client_id, code, redirect_uri, code_verifier, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthServicesApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The grant type used to request an access token. | 
 **client_id** | **str**| The client id used during an authorization request. | 
 **code** | **str**| The authorization code to exchange for a bearer access token. | 
 **redirect_uri** | **str**| The redirect uri used during an authorization request. | 
 **code_verifier** | **str**| The code verifier in plain format used during an authorization request. | 
 **api_version** | **str**| The requested API version | [optional] 

### Return type

[**TokenResponseDto**](TokenResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

