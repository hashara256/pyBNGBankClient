# swagger_client.AccountInformationServiceAISApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_consent**](AccountInformationServiceAISApi.md#add_consent) | **POST** /api/v1/consents | Create consent
[**add_consent_authorisation**](AccountInformationServiceAISApi.md#add_consent_authorisation) | **POST** /api/v1/consents/{consentId}/authorisations | Start the authorisation process for a consent
[**delete_consent**](AccountInformationServiceAISApi.md#delete_consent) | **DELETE** /api/v1/consents/{consentId} | Delete Consent
[**get**](AccountInformationServiceAISApi.md#get) | **GET** /api/v1/accounts | Read Account List
[**get_account_balances**](AccountInformationServiceAISApi.md#get_account_balances) | **GET** /api/v1/accounts/{account-id}/balances | Read Balance
[**get_account_details**](AccountInformationServiceAISApi.md#get_account_details) | **GET** /api/v1/accounts/{account-id} | Read Account Details
[**get_consent**](AccountInformationServiceAISApi.md#get_consent) | **GET** /api/v1/consents/{consentId} | Get Consent Request
[**get_consent_authorisation_status**](AccountInformationServiceAISApi.md#get_consent_authorisation_status) | **GET** /api/v1/consents/{consentId}/authorisations/{authorisationId} | Read the SCA Status of the consent authorisation
[**get_consent_authorisations**](AccountInformationServiceAISApi.md#get_consent_authorisations) | **GET** /api/v1/consents/{consentId}/authorisations | Get Consent Initiation Authorisation Sub-Resources Request
[**get_consent_status**](AccountInformationServiceAISApi.md#get_consent_status) | **GET** /api/v1/consents/{consentId}/status | Consent status request
[**get_statements**](AccountInformationServiceAISApi.md#get_statements) | **GET** /api/v1/accounts/{account-id}/statements | Read Account Statements
[**get_transaction_details**](AccountInformationServiceAISApi.md#get_transaction_details) | **GET** /api/v1/accounts/{account-id}/transactions/{transaction-id} | Read Transaction Details
[**get_transactions**](AccountInformationServiceAISApi.md#get_transactions) | **GET** /api/v1/accounts/{account-id}/transactions | Read Transactions


# **add_consent**
> AddConsentResponseDto add_consent(_date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, body, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_uri=tpp_redirect_uri)

Create consent

<p>This method creates a consent resource, defining access rights to dedicated accounts. The PSU is determined after authorization of the consent using SCA. These accounts are addressed explicitly in the method as parameters as a core function.</p>  <p>Side Effects When this Consent Request is a request where the \"recurringIndicator\" equals \"true\", and if it exists already a former consent for recurring access on account information for the addressed PSU, then the former consent automatically expires as soon as the new consent request is authorised by the PSU.</p>  <p>Optional Extension: As an option, an ASPSP might optionally accept a specific access right on the access on all psd2 related services for all available accounts.</p>  <p>    <ul>      <li>to see the list of available payment accounts or</li>      <li>to see the list of available payment accounts with balances.</li>    </ul>  </p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.
body = swagger_client.AccountConsentData() # AccountConsentData | Requestbody for a consents request
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this consent.</p> (optional)

try:
    # Create consent
    api_response = api_instance.add_consent(_date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, body, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, tpp_redirect_uri=tpp_redirect_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->add_consent: %s\n" % e)
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
 **body** | [**AccountConsentData**](AccountConsentData.md)| Requestbody for a consents request | 
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

# **add_consent_authorisation**
> AddConsentAuthorisationResponseDto add_consent_authorisation(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, tpp_redirect_uri=tpp_redirect_uri)

Start the authorisation process for a consent

<p>Create an authorisation sub-resource and start the authorisation process. The message might in addition transmit authentication and authorisation related data.</p>  <p>The usage of this access method is unnecessary since only one SCA process is needed, and the related authorisation resource is automatically created by the ASPSP after the submission of the consent data with the first POST consent call.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent initiation resource.
_date = '_date_example' # str | Date of the request.
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request.
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this consent authorisation.</p> (optional)

try:
    # Start the authorisation process for a consent
    api_response = api_instance.add_consent_authorisation(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, tpp_redirect_uri=tpp_redirect_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->add_consent_authorisation: %s\n" % e)
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

# **delete_consent**
> delete_consent(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Delete Consent

<p>The TPP can delete an account information consent object if needed.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Delete Consent
    api_instance.delete_consent(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->delete_consent: %s\n" % e)
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

# **get**
> ReadAccountListResponseDto get(_date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, with_balance=with_balance, psu_ip_address=psu_ip_address)

Read Account List

<p>Read the identifiers of the available payment account together with booking balance information, depending on the consent granted.</p>  <p>It is assumed that a consent of the PSU to this access is already given and stored on the ASPSP system.The addressed list of accounts depends then on the PSU ID and the stored consent addressed by consentId, respectively the OAuth2 access token.</p>  <p>Returns all identifiers of the accounts, to which an account access has been granted to through the /consents endpoint by the PSU. In addition, relevant information about the accounts and hyperlinks to corresponding account information resources are provided if a related consent has been already granted.</p>  <p>Remark: Note that the /consents endpoint optionally offers to grant an access on all available payment accounts of a PSU. In this case, this endpoint will deliver the information about all available payment accounts of the PSU at this ASPSP.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
consent_id = 'consent_id_example' # str | ID of the consent, which was retrieved using the /consents endpoint.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.
with_balance = true # bool | If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. (optional)

try:
    # Read Account List
    api_response = api_instance.get(_date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, with_balance=with_balance, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consent_id** | **str**| ID of the consent, which was retrieved using the /consents endpoint. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 
 **with_balance** | **bool**| If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | [optional] 

### Return type

[**ReadAccountListResponseDto**](ReadAccountListResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_balances**
> ReadBalanceResponseDto get_account_balances(account_id, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, psu_ip_address=psu_ip_address)

Read Balance

<p>Reads account data from a given account addressed by \"account-id\".</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
account_id = 'account_id_example' # str | Resource identification of the generated account resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
consent_id = 'consent_id_example' # str | ID of the consent, which was retrieved using the /consents endpoint.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. (optional)

try:
    # Read Balance
    api_response = api_instance.get_account_balances(account_id, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_account_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Resource identification of the generated account resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consent_id** | **str**| ID of the consent, which was retrieved using the /consents endpoint. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | [optional] 

### Return type

[**ReadBalanceResponseDto**](ReadBalanceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_details**
> ReadAccountDetailsResponseDto get_account_details(account_id, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, with_balance=with_balance, psu_ip_address=psu_ip_address)

Read Account Details

<p>Reads details about an account, with balances where required. It is assumed that a consent of the PSU to this access is already given and stored on the ASPSP system. The addressed details of this account depends then on the stored consent addressed by consentId, respectively the OAuth2 access token.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
account_id = 'account_id_example' # str | Resource identification of the generated account resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
consent_id = 'consent_id_example' # str | ID of the consent, which was retrieved using the /consents endpoint.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.
with_balance = true # bool | If contained, this function reads the details of the accessible payment account including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. (optional)

try:
    # Read Account Details
    api_response = api_instance.get_account_details(account_id, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, with_balance=with_balance, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_account_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Resource identification of the generated account resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consent_id** | **str**| ID of the consent, which was retrieved using the /consents endpoint. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 
 **with_balance** | **bool**| If contained, this function reads the details of the accessible payment account including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | [optional] 

### Return type

[**ReadAccountDetailsResponseDto**](ReadAccountDetailsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent**
> GetConsentStatusResponseDto get_consent(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Consent Request

<p>Returns the content of an account information consent object. This is returning the data for the TPP especially in cases, where the consent was directly managed between ASPSP and PSU e.g. in a re-direct SCA Approach.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Consent Request
    api_response = api_instance.get_consent(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_consent: %s\n" % e)
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

# **get_consent_authorisation_status**
> GetConsentAuthorisationResponseDto get_consent_authorisation_status(consent_id, authorisation_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Read the SCA Status of the consent authorisation

This method returns the SCA status of a consent's authorisation sub-resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent initiation resource.
authorisation_id = 'authorisation_id_example' # str | Resource identification of the generated authorisation sub-resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Read the SCA Status of the consent authorisation
    api_response = api_instance.get_consent_authorisation_status(consent_id, authorisation_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_consent_authorisation_status: %s\n" % e)
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

# **get_consent_authorisations**
> GetConsentAuthorisationsResponseDto get_consent_authorisations(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Consent Initiation Authorisation Sub-Resources Request

<p>Read a list of all authorisation subresources IDs which have been created.</p>  <p>This function returns an array of hyperlinks to all generated authorisation sub-resources.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Consent Initiation Authorisation Sub-Resources Request
    api_response = api_instance.get_consent_authorisations(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_consent_authorisations: %s\n" % e)
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

# **get_consent_status**
> GetConsentStatusResponseDto get_consent_status(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Consent status request

<p>Read the status of an account information consent resource.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
consent_id = 'consent_id_example' # str | Resource identification of the generated consent resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Consent status request
    api_response = api_instance.get_consent_status(consent_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_consent_status: %s\n" % e)
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

# **get_statements**
> get_statements(account_id, date_from, booking_status, accept, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, start_date=start_date, date_to=date_to, end_date=end_date, booking_status_enum=booking_status_enum, psu_ip_address=psu_ip_address)

Read Account Statements

<p>Reads booked camt.053 statements from a given account addressed by \"account-id\".</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
account_id = 'account_id_example' # str | Resource identification of the generated account resource.
date_from = 'date_from_example' # str | Starting date (inclusive the date dateFrom) of the transaction list.
booking_status = 'booking_status_example' # str | Permitted codes are \"booked\".
accept = 'accept_example' # str | <p>The TPP can indicate the formats of account reports supported together with a priorisation following the HTTP header definition.</p>  <p>The formats supported by this specification are:<br /><ul><li>xml, CAMT053</li></ul></p>
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
consent_id = 'consent_id_example' # str | ID of the consent, which was retrieved using the /consents endpoint.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_to = 'date_to_example' # str | End date (inclusive the data dateTo) of the transaction list, default is \"now\" if not given. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
booking_status_enum = 'booking_status_enum_example' # str |  (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. (optional)

try:
    # Read Account Statements
    api_instance.get_statements(account_id, date_from, booking_status, accept, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, start_date=start_date, date_to=date_to, end_date=end_date, booking_status_enum=booking_status_enum, psu_ip_address=psu_ip_address)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Resource identification of the generated account resource. | 
 **date_from** | **str**| Starting date (inclusive the date dateFrom) of the transaction list. | 
 **booking_status** | **str**| Permitted codes are \&quot;booked\&quot;. | 
 **accept** | **str**| &lt;p&gt;The TPP can indicate the formats of account reports supported together with a priorisation following the HTTP header definition.&lt;/p&gt;  &lt;p&gt;The formats supported by this specification are:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;xml, CAMT053&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consent_id** | **str**| ID of the consent, which was retrieved using the /consents endpoint. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 
 **start_date** | **datetime**|  | [optional] 
 **date_to** | **str**| End date (inclusive the data dateTo) of the transaction list, default is \&quot;now\&quot; if not given. | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **booking_status_enum** | **str**|  | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_details**
> ReadTransactionDetailsResponseDto get_transaction_details(account_id, transaction_id, accept, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, psu_ip_address=psu_ip_address)

Read Transaction Details

<p>Reads transaction details from a given account addressed by \"account-id\" and by a \"transaction-id\".</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
account_id = 'account_id_example' # str | Resource identification of the generated account resource.
transaction_id = 'transaction_id_example' # str | Resource identification of the transaction resource.
accept = 'accept_example' # str | <p>The TPP can indicate the formats of account reports supported together with a priorisation following the HTTP header definition.</p>  <p>The formats supported by this specification are:<br /><ul><li>JSON</li></ul></p>
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
consent_id = 'consent_id_example' # str | ID of the consent, which was retrieved using the /consents endpoint.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. (optional)

try:
    # Read Transaction Details
    api_response = api_instance.get_transaction_details(account_id, transaction_id, accept, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_transaction_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Resource identification of the generated account resource. | 
 **transaction_id** | **str**| Resource identification of the transaction resource. | 
 **accept** | **str**| &lt;p&gt;The TPP can indicate the formats of account reports supported together with a priorisation following the HTTP header definition.&lt;/p&gt;  &lt;p&gt;The formats supported by this specification are:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;JSON&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consent_id** | **str**| ID of the consent, which was retrieved using the /consents endpoint. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | [optional] 

### Return type

[**ReadTransactionDetailsResponseDto**](ReadTransactionDetailsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> ReadTransactionsResponseDto get_transactions(account_id, date_from, booking_status, accept, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, start_date=start_date, date_to=date_to, end_date=end_date, booking_status_enum=booking_status_enum, with_balance=with_balance, page=page, download=download, psu_ip_address=psu_ip_address)

Read Transactions

<p>Reads transactions from a given account addressed by \"account-id\".</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceAISApi()
account_id = 'account_id_example' # str | Resource identification of the generated account resource.
date_from = 'date_from_example' # str | Starting date (inclusive the date dateFrom) of the transaction list.
booking_status = 'booking_status_example' # str | Permitted codes are \"booked\", \"pending\" and \"both\".
accept = 'accept_example' # str | <p>The TPP can indicate the formats of account reports supported together with a priorisation following the HTTP header definition.</p>  <p>The formats supported by this specification are:<br /><ul><li>JSON</li></ul></p>
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
consent_id = 'consent_id_example' # str | ID of the consent, which was retrieved using the /consents endpoint.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_to = 'date_to_example' # str | End date (inclusive the data dateTo) of the transaction list, default is \"now\" if not given. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
booking_status_enum = 'booking_status_enum_example' # str |  (optional)
with_balance = true # bool | If contained, this function reads the list of transactions including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. (optional)
page = 56 # int | The page to request (used in pagination). (optional)
download = true # bool | Indicates if the request is to download a file. (optional)
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. (optional)

try:
    # Read Transactions
    api_response = api_instance.get_transactions(account_id, date_from, booking_status, accept, _date, x_request_id, consent_id, digest, signature, tpp_signature_certificate, authorization, start_date=start_date, date_to=date_to, end_date=end_date, booking_status_enum=booking_status_enum, with_balance=with_balance, page=page, download=download, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Resource identification of the generated account resource. | 
 **date_from** | **str**| Starting date (inclusive the date dateFrom) of the transaction list. | 
 **booking_status** | **str**| Permitted codes are \&quot;booked\&quot;, \&quot;pending\&quot; and \&quot;both\&quot;. | 
 **accept** | **str**| &lt;p&gt;The TPP can indicate the formats of account reports supported together with a priorisation following the HTTP header definition.&lt;/p&gt;  &lt;p&gt;The formats supported by this specification are:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;JSON&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consent_id** | **str**| ID of the consent, which was retrieved using the /consents endpoint. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 
 **start_date** | **datetime**|  | [optional] 
 **date_to** | **str**| End date (inclusive the data dateTo) of the transaction list, default is \&quot;now\&quot; if not given. | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **booking_status_enum** | **str**|  | [optional] 
 **with_balance** | **bool**| If contained, this function reads the list of transactions including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. | [optional] 
 **page** | **int**| The page to request (used in pagination). | [optional] 
 **download** | **bool**| Indicates if the request is to download a file. | [optional] 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | [optional] 

### Return type

[**ReadTransactionsResponseDto**](ReadTransactionsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

