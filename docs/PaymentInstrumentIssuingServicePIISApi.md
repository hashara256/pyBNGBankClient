# swagger_client.PaymentInstrumentIssuingServicePIISApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_confirmation_of_funds_consent**](PaymentInstrumentIssuingServicePIISApi.md#add_confirmation_of_funds_consent) | **POST** /api/v1/consents/confirmation-of-funds | Create confirmation of funds consent
[**add_confirmation_of_funds_consent_authorisation**](PaymentInstrumentIssuingServicePIISApi.md#add_confirmation_of_funds_consent_authorisation) | **POST** /api/v1/consents/confirmation-of-funds/{consentId}/authorisations | Start the authorisation process for a confirmation of funds consent
[**delete_confirmation_of_funds_consent**](PaymentInstrumentIssuingServicePIISApi.md#delete_confirmation_of_funds_consent) | **DELETE** /api/v1/consents/confirmation-of-funds/{consentId} | Delete Confirmation Of Funds Consent
[**get_confirmation_of_funds_consent**](PaymentInstrumentIssuingServicePIISApi.md#get_confirmation_of_funds_consent) | **GET** /api/v1/consents/confirmation-of-funds/{consentId} | Get Confirmation Of Funds Consent Request
[**get_confirmation_of_funds_consent_authorisation_status**](PaymentInstrumentIssuingServicePIISApi.md#get_confirmation_of_funds_consent_authorisation_status) | **GET** /api/v1/consents/confirmation-of-funds/{consentId}/authorisations/{authorisationId} | Read the SCA Status of the confirmation of funds consent authorisation
[**get_confirmation_of_funds_consent_authorisations**](PaymentInstrumentIssuingServicePIISApi.md#get_confirmation_of_funds_consent_authorisations) | **GET** /api/v1/consents/confirmation-of-funds/{consentId}/authorisations | Get Confirmation Of Funds Consent Initiation Authorisation Sub-Resources Request
[**get_confirmation_of_funds_consent_status**](PaymentInstrumentIssuingServicePIISApi.md#get_confirmation_of_funds_consent_status) | **GET** /api/v1/consents/confirmation-of-funds/{consentId}/status | Get Confirmation Of Funds Consent Status Request
[**post**](PaymentInstrumentIssuingServicePIISApi.md#post) | **POST** /api/v1/funds-confirmations | Checks whether a specific amount is available at point of time of the request on an account.


# **add_confirmation_of_funds_consent**
> AddConsentResponseDto add_confirmation_of_funds_consent(_date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, body, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_uri=tpp_redirect_uri)

Create confirmation of funds consent

<p>This method creates a confirmation of funds consent resource, defining access rights to a dedicated account. The PSU is determined after authorization of the consent using SCA. The account is addressed explicitly in the method as parameters as a core function.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentIssuingServicePIISApi()
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.
body = swagger_client.ConfirmationOfFundsConsentData() # ConfirmationOfFundsConsentData | Requestbody for a consents request
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this consent.</p> (optional)

try:
    # Create confirmation of funds consent
    api_response = api_instance.add_confirmation_of_funds_consent(_date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, body, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_uri=tpp_redirect_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentIssuingServicePIISApi->add_confirmation_of_funds_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | 
 **body** | [**ConfirmationOfFundsConsentData**](ConfirmationOfFundsConsentData.md)| Requestbody for a consents request | 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id** | **str**| Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id_type** | **str**| Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **tpp_redirect_uri** | **str**| &lt;p&gt;URI of the TPP, where the transaction flow shall be redirected to after a Redirect.&lt;/p&gt;  &lt;p&gt;This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this consent.&lt;/p&gt; | [optional] 

### Return type

[**AddConsentResponseDto**](AddConsentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_confirmation_of_funds_consent_authorisation**
> AddConsentAuthorisationResponseDto add_confirmation_of_funds_consent_authorisation(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, tpp_redirect_uri=tpp_redirect_uri)

Start the authorisation process for a confirmation of funds consent

<p>Create an authorisation sub-resource and start the authorisation process. The message might in addition transmit authentication and authorisation related data.</p>  <p>The usage of this access method is unnecessary since only one SCA process is needed, and the related authorisation resource is automatically created by the ASPSP after the submission of the consent data with the first POST consent call.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentIssuingServicePIISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent initiation resource.
_date = '_date_example' # str | Date of the request.
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request.
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this consent authorisation.</p> (optional)

try:
    # Start the authorisation process for a confirmation of funds consent
    api_response = api_instance.add_confirmation_of_funds_consent_authorisation(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, tpp_redirect_uri=tpp_redirect_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentIssuingServicePIISApi->add_confirmation_of_funds_consent_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Resource identification of the generated consent initiation resource. | 
 **_date** | **str**| Date of the request. | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. | 
 **tpp_redirect_uri** | **str**| &lt;p&gt;URI of the TPP, where the transaction flow shall be redirected to after a Redirect.&lt;/p&gt;  &lt;p&gt;This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this consent authorisation.&lt;/p&gt; | [optional] 

### Return type

[**AddConsentAuthorisationResponseDto**](AddConsentAuthorisationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_confirmation_of_funds_consent**
> delete_confirmation_of_funds_consent(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Delete Confirmation Of Funds Consent

<p>The TPP can delete an account information consent object if needed.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentIssuingServicePIISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Delete Confirmation Of Funds Consent
    api_instance.delete_confirmation_of_funds_consent(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
except ApiException as e:
    print("Exception when calling PaymentInstrumentIssuingServicePIISApi->delete_confirmation_of_funds_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Resource identification of the generated consent resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_confirmation_of_funds_consent**
> GetConsentStatusResponseDto get_confirmation_of_funds_consent(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Confirmation Of Funds Consent Request

<p>Returns the content of an account information consent object. This is returning the data for the TPP especially in cases, where the consent was directly managed between ASPSP and PSU e.g. in a re-direct SCA Approach.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentIssuingServicePIISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Confirmation Of Funds Consent Request
    api_response = api_instance.get_confirmation_of_funds_consent(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentIssuingServicePIISApi->get_confirmation_of_funds_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Resource identification of the generated consent resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetConsentStatusResponseDto**](GetConsentStatusResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_confirmation_of_funds_consent_authorisation_status**
> GetConsentAuthorisationResponseDto get_confirmation_of_funds_consent_authorisation_status(consent_id, authorisation_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Read the SCA Status of the confirmation of funds consent authorisation

This method returns the SCA status of a consent's authorisation sub-resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentIssuingServicePIISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent initiation resource.
authorisation_id = 'authorisation_id_example' # str | Resource identification of the generated authorisation sub-resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Read the SCA Status of the confirmation of funds consent authorisation
    api_response = api_instance.get_confirmation_of_funds_consent_authorisation_status(consent_id, authorisation_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentIssuingServicePIISApi->get_confirmation_of_funds_consent_authorisation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Resource identification of the generated consent initiation resource. | 
 **authorisation_id** | **str**| Resource identification of the generated authorisation sub-resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetConsentAuthorisationResponseDto**](GetConsentAuthorisationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_confirmation_of_funds_consent_authorisations**
> GetConsentAuthorisationsResponseDto get_confirmation_of_funds_consent_authorisations(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Confirmation Of Funds Consent Initiation Authorisation Sub-Resources Request

<p>Read a list of all authorisation subresources IDs which have been created.</p>  <p>This function returns an array of hyperlinks to all generated authorisation sub-resources.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentIssuingServicePIISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Confirmation Of Funds Consent Initiation Authorisation Sub-Resources Request
    api_response = api_instance.get_confirmation_of_funds_consent_authorisations(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentIssuingServicePIISApi->get_confirmation_of_funds_consent_authorisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Resource identification of the generated consent initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetConsentAuthorisationsResponseDto**](GetConsentAuthorisationsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_confirmation_of_funds_consent_status**
> GetConsentStatusResponseDto get_confirmation_of_funds_consent_status(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Confirmation Of Funds Consent Status Request

<p>Read the status of a confirmation of funds consent resource.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentIssuingServicePIISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Confirmation Of Funds Consent Status Request
    api_response = api_instance.get_confirmation_of_funds_consent_status(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentIssuingServicePIISApi->get_confirmation_of_funds_consent_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Resource identification of the generated consent resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetConsentStatusResponseDto**](GetConsentStatusResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> FundsConfirmationResponseDto post(_date, x_request_id, digest, signature, tpp_signature_certificate, authorization, body)

Checks whether a specific amount is available at point of time of the request on an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentIssuingServicePIISApi()
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.
body = swagger_client.FundsConfirmationDto() # FundsConfirmationDto | <p>JSON request body for a confirmation of funds request</p>

try:
    # Checks whether a specific amount is available at point of time of the request on an account.
    api_response = api_instance.post(_date, x_request_id, digest, signature, tpp_signature_certificate, authorization, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentIssuingServicePIISApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 
 **body** | [**FundsConfirmationDto**](FundsConfirmationDto.md)| &lt;p&gt;JSON request body for a confirmation of funds request&lt;/p&gt; | 

### Return type

[**FundsConfirmationResponseDto**](FundsConfirmationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

