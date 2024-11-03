# swagger_client.PaymentInitiationServicePISApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bulk_payment_for_direct_debit_transfer**](PaymentInitiationServicePISApi.md#add_bulk_payment_for_direct_debit_transfer) | **POST** /api/v1/bulk-payments/pain.008-sepa-direct-debits | Bulk Payment Initiation request for SepaDirectDebit
[**add_bulk_payment_for_sepa_credit_transfer**](PaymentInitiationServicePISApi.md#add_bulk_payment_for_sepa_credit_transfer) | **POST** /api/v1/bulk-payments/pain.001-sepa-credit-transfers | Bulk Payment Initiation request for SepaCreditTransfer
[**add_payment_authorisation**](PaymentInitiationServicePISApi.md#add_payment_authorisation) | **POST** /api/v1/{payment-service}/{payment-product}/{paymentId}/authorisations | Start the authorisation process for a payment initiation
[**add_payment_cancellation_authorisation**](PaymentInitiationServicePISApi.md#add_payment_cancellation_authorisation) | **POST** /api/v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations | Start the authorisation process for a payment cancellation
[**add_payment_for_cross_border_credit_transfer**](PaymentInitiationServicePISApi.md#add_payment_for_cross_border_credit_transfer) | **POST** /api/v1/payments/cross-border-credit-transfers | Payment Initiation request for CrossBorderCreditTransfer
[**add_payment_for_sepa_credit_transfer**](PaymentInitiationServicePISApi.md#add_payment_for_sepa_credit_transfer) | **POST** /api/v1/payments/sepa-credit-transfers | Payment Initiation request for SepaCreditTransfer
[**delete**](PaymentInitiationServicePISApi.md#delete) | **DELETE** /api/v1/{payment-service}/{payment-product}/{paymentId} | Delete Payment
[**get_bulk_payment_for_direct_debit_transfer**](PaymentInitiationServicePISApi.md#get_bulk_payment_for_direct_debit_transfer) | **GET** /api/v1/bulk-payments/pain.008-sepa-direct-debits/{paymentId} | Get Bulk Payment for Direct Debit Information
[**get_bulk_payment_for_sepa_credit_transfer**](PaymentInitiationServicePISApi.md#get_bulk_payment_for_sepa_credit_transfer) | **GET** /api/v1/bulk-payments/pain.001-sepa-credit-transfers/{paymentId} | Get Bulk Payment Information
[**get_payment_authorisation_status**](PaymentInitiationServicePISApi.md#get_payment_authorisation_status) | **GET** /api/v1/{payment-service}/{payment-product}/{paymentId}/authorisations/{authorisationId} | Read the SCA Status of the payment authorisation
[**get_payment_authorisations**](PaymentInitiationServicePISApi.md#get_payment_authorisations) | **GET** /api/v1/{payment-service}/{payment-product}/{paymentId}/authorisations | Get Payment Initiation Authorisation Sub-Resources Request
[**get_payment_cancellation_authorisation_status**](PaymentInitiationServicePISApi.md#get_payment_cancellation_authorisation_status) | **GET** /api/v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations/{authorisationId} | Read the SCA Status of the payment authorisation
[**get_payment_cancellation_authorisations**](PaymentInitiationServicePISApi.md#get_payment_cancellation_authorisations) | **GET** /api/v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations | Get Payment Initiation Authorisation Sub-Resources Request
[**get_payment_for_cross_border_credit_transfer**](PaymentInitiationServicePISApi.md#get_payment_for_cross_border_credit_transfer) | **GET** /api/v1/payments/cross-border-credit-transfers/{paymentId} | Get Cross-Border Payment Information
[**get_payment_for_sepa_credit_transfer**](PaymentInitiationServicePISApi.md#get_payment_for_sepa_credit_transfer) | **GET** /api/v1/payments/sepa-credit-transfers/{paymentId} | Get Payment Information
[**get_status**](PaymentInitiationServicePISApi.md#get_status) | **GET** /api/v1/{payment-service}/{payment-product}/{paymentId}/status | Payment initiation status request


# **add_bulk_payment_for_direct_debit_transfer**
> AddBulkPaymentInitiationResponseDto add_bulk_payment_for_direct_debit_transfer(content_type, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, consent_id=consent_id, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location, tpp_redirect_uri=tpp_redirect_uri, tpp_redirect_preferred=tpp_redirect_preferred, body=body)

Bulk Payment Initiation request for SepaDirectDebit

<p>This method is used to initiate a bulk-direct debit at the ASPSP.</p>  <h2>Variants of Bulk Direct Debit Initiation Requests</h2>  <p>This method to initiate a bulk direct debit initiation at the ASPSP can be sent with a pain.008.001.02 XML body or using a file stream.</p>  <p>There are the following <strong>payment products</strong> that are currently supported:</p>  <ul>    <li>Payment products with payment information in <em>pain.008.001.02 XML</em> format:<ul><li><strong><em>pain.008-sepa-direct-debits</em></strong><br />Pain 008.001.02 XML can be posted using  two different methods:<ul><li>application/xml<br />The XML posted in the body of the request.</li><li>application/octet-stream<br />The XML posted in an XML file or as XML file in a ZIP file using a file stream (recommended for large batch files)</li></ul></li></ul></li>  </ul>  <p>Furthermore the request body depends on the <strong>payment-service</strong></p>  <ul>    <li>      <p>        <strong>          <em>bulk-payments</em>        </strong>: A bulk direct debit initiation request.</p>    </li>  </ul>  <p>This is the first step in the API to initiate a direct debit.</p>  <h2>Single and mulitilevel SCA Processes</h2>  <p>The Direct Debit Initiation Requests are independent from the need of one ore multilevel SCA processing, i.e. independent from the number of authorisations needed for the execution of direct debits.</p>  <p>Payment Initiations (for each direct debit a payment initiation is created) submitted will receive the 'PDNG' status initially, since the Direct Debit has not been reviewed and confirmed by a PSU yet. In order to proceed with the Payment Initiation, a redirect to the 'scaOAuth' authorization endpoint with scope PIS:{paymentId or paymentInitiationBatchGroupId}is required. During this redirect the PSU enters their username and reviews the transaction details for authorization and can authorize the bulk direct debits if the user has enough privileges. If mulitilevel SCA is required, the status will change to 'PATC' meaning the direct debit is partially authorised. A different PSU will then need to be redirected the same way to make the final authorisation. After which the status will change to 'ACTC'.</p>  <p>For multibatch files it is recommended to use the {paymentInitiationBatchGroupId} when redirecting to the authorization endpoint for processing. A multibatch file is always processed at once. After it is processed, the separate payment initiation identifiers received from this API can be used to authorise specific batches. These can then be used in a redirect to the authorization endpoint.</p>  <p>Funds confirmations are not supported by the ASPSP for this service.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
content_type = 'content_type_example' # str | <p>The content type of the request.</p>
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.
consent_id = 'consent_id_example' # str | This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. Currently this field can be provided, but it does not do anything extra, since the payment initiation always needs to be reviewed by the PSU using the SCA Redirect OAuth approach. (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment initiation. Note that this URI should not be PSU specific, incase of multilevel SCA required for this payment initiation, another PSU also needs to be able to be redirected to the OAuth authorization endpoint with the same redirect URI.</p> (optional)
tpp_redirect_preferred = true # bool | This field is ignored, since a redirect approach is always used by the ASPSP. (optional)
body = 'body_example' # str | <p>Pain 008.001.02 XML as request body or of a file stream of an Pain 008.001.02 XML file or zip file containing such a file.</p> (optional)

try:
    # Bulk Payment Initiation request for SepaDirectDebit
    api_response = api_instance.add_bulk_payment_for_direct_debit_transfer(content_type, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, consent_id=consent_id, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location, tpp_redirect_uri=tpp_redirect_uri, tpp_redirect_preferred=tpp_redirect_preferred, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->add_bulk_payment_for_direct_debit_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| &lt;p&gt;The content type of the request.&lt;/p&gt; | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | 
 **consent_id** | **str**| This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. Currently this field can be provided, but it does not do anything extra, since the payment initiation always needs to be reviewed by the PSU using the SCA Redirect OAuth approach. | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id** | **str**| Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id_type** | **str**| Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available. | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available. | [optional] 
 **tpp_redirect_uri** | **str**| &lt;p&gt;URI of the TPP, where the transaction flow shall be redirected to after a Redirect.&lt;/p&gt;  &lt;p&gt;This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment initiation. Note that this URI should not be PSU specific, incase of multilevel SCA required for this payment initiation, another PSU also needs to be able to be redirected to the OAuth authorization endpoint with the same redirect URI.&lt;/p&gt; | [optional] 
 **tpp_redirect_preferred** | **bool**| This field is ignored, since a redirect approach is always used by the ASPSP. | [optional] 
 **body** | **str**| &lt;p&gt;Pain 008.001.02 XML as request body or of a file stream of an Pain 008.001.02 XML file or zip file containing such a file.&lt;/p&gt; | [optional] 

### Return type

[**AddBulkPaymentInitiationResponseDto**](AddBulkPaymentInitiationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bulk_payment_for_sepa_credit_transfer**
> AddBulkPaymentInitiationResponseDto add_bulk_payment_for_sepa_credit_transfer(content_type, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, consent_id=consent_id, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location, tpp_redirect_uri=tpp_redirect_uri, tpp_redirect_preferred=tpp_redirect_preferred, body=body)

Bulk Payment Initiation request for SepaCreditTransfer

<p>This method is used to initiate a bulk-payment at the ASPSP.</p>  <h2>Variants of Bulk Payment Initiation Requests</h2>  <p>This method to initiate a bulk payment initiation at the ASPSP can be sent with a pain.001.001.03 XML body or using a file stream.</p>  <p>There are the following <strong>payment products</strong> that are currently supported:</p>  <ul>    <li>Payment products with payment information in <em>pain.001.001.03 XML</em> format:<ul><li><strong><em>pain.001-sepa-credit-transfers</em></strong><br />Pain 001.001.03 XML can be posted using  two different methods:<ul><li>application/xml<br />The XML posted in the body of the request.</li><li>application/octet-stream<br />The XML posted in an XML file or as XML file in a ZIP file using a file stream (recommended for large batch files)</li></ul></li></ul></li>  </ul>  <p>Furthermore the request body depends on the <strong>payment-service</strong></p>  <ul>    <li>      <p>        <strong>          <em>bulk-payments</em>        </strong>: A bulk payment initiation request.</p>    </li>  </ul>  <p>This is the first step in the API to initiate a payment.</p>  <h2>Single and mulitilevel SCA Processes</h2>  <p>The Payment Initiation Requests are independent from the need of one ore multilevel SCA processing, i.e. independent from the number of authorisations needed for the execution of payments.</p>  <p>Payment Initiations submitted will receive the 'PDNG' status initially, since the Payment Initiation has not been reviewed and confirmed by a PSU yet. In order to proceed with the Payment Initiation, a redirect to the 'scaOAuth' authorization endpoint with scope PIS:{paymentId or paymentInitiationBatchGroupId}is required. During this redirect the PSU enters their username and reviews the transaction details for authorization and can authorize the bulk payments if the user has enough privileges. If mulitilevel SCA is required, the status will change to 'PATC' meaning the bulk payment is partially authorised. A different PSU will then need to be redirected the same way to make the final authorisation. After which the status will change to 'ACTC'.</p>  <p>For multibatch files it is recommended to use the {paymentInitiationBatchGroupId} when redirecting to the authorization endpoint for processing. A multibatch file is always processed at once. After it is processed, the separate payment initiation identifiers received from this API can be used to authorise specific batches. These can then be used in a redirect to the authorization endpoint.</p>  <p>Funds confirmations are not supported by the ASPSP for this service.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
content_type = 'content_type_example' # str | <p>The content type of the request.</p>
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.
consent_id = 'consent_id_example' # str | This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. Currently this field can be provided, but it does not do anything extra, since the payment initiation always needs to be reviewed by the PSU using the SCA Redirect OAuth approach. (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment initiation. Note that this URI should not be PSU specific, incase of multilevel SCA required for this payment initiation, another PSU also needs to be able to be redirected to the OAuth authorization endpoint with the same redirect URI.</p> (optional)
tpp_redirect_preferred = true # bool | This field is ignored, since a redirect approach is always used by the ASPSP. (optional)
body = 'body_example' # str | <p>Pain 001.001.03 XML as request body or of a file stream of an Pain 001.001.03 XML file or zip file containing such a file.</p> (optional)

try:
    # Bulk Payment Initiation request for SepaCreditTransfer
    api_response = api_instance.add_bulk_payment_for_sepa_credit_transfer(content_type, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, consent_id=consent_id, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location, tpp_redirect_uri=tpp_redirect_uri, tpp_redirect_preferred=tpp_redirect_preferred, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->add_bulk_payment_for_sepa_credit_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| &lt;p&gt;The content type of the request.&lt;/p&gt; | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | 
 **consent_id** | **str**| This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. Currently this field can be provided, but it does not do anything extra, since the payment initiation always needs to be reviewed by the PSU using the SCA Redirect OAuth approach. | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id** | **str**| Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id_type** | **str**| Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available. | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available. | [optional] 
 **tpp_redirect_uri** | **str**| &lt;p&gt;URI of the TPP, where the transaction flow shall be redirected to after a Redirect.&lt;/p&gt;  &lt;p&gt;This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment initiation. Note that this URI should not be PSU specific, incase of multilevel SCA required for this payment initiation, another PSU also needs to be able to be redirected to the OAuth authorization endpoint with the same redirect URI.&lt;/p&gt; | [optional] 
 **tpp_redirect_preferred** | **bool**| This field is ignored, since a redirect approach is always used by the ASPSP. | [optional] 
 **body** | **str**| &lt;p&gt;Pain 001.001.03 XML as request body or of a file stream of an Pain 001.001.03 XML file or zip file containing such a file.&lt;/p&gt; | [optional] 

### Return type

[**AddBulkPaymentInitiationResponseDto**](AddBulkPaymentInitiationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_payment_authorisation**
> AddPaymentAuthorisationResponseDto add_payment_authorisation(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, tpp_redirect_uri=tpp_redirect_uri)

Start the authorisation process for a payment initiation

<p>Create an authorisation sub-resource and start the authorisation process. The message might in addition transmit authentication and authorisation related data.</p>  <p>The usage of this access method is unnecessary since only one SCA process is needed, and the related authorisation resource is automatically created by the ASPSP after the submission of the consent data with the first POST consent/{payment-product} call.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>sepa-credit-transfers</li>    <li>cross-border-credit-transfers</li>  </ul>
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | Date of the request.
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request.
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment authorisation.</p> (optional)

try:
    # Start the authorisation process for a payment initiation
    api_response = api_instance.add_payment_authorisation(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, tpp_redirect_uri=tpp_redirect_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->add_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;sepa-credit-transfers&lt;/li&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| Date of the request. | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. | 
 **tpp_redirect_uri** | **str**| &lt;p&gt;URI of the TPP, where the transaction flow shall be redirected to after a Redirect.&lt;/p&gt;  &lt;p&gt;This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment authorisation.&lt;/p&gt; | [optional] 

### Return type

[**AddPaymentAuthorisationResponseDto**](AddPaymentAuthorisationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_payment_cancellation_authorisation**
> AddPaymentAuthorisationResponseDto add_payment_cancellation_authorisation(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, tpp_redirect_uri=tpp_redirect_uri)

Start the authorisation process for a payment cancellation

<p>Create an authorisation sub-resource and start the authorisation process. The message might in addition transmit authentication and authorisation related data.</p>  <p>The usage of this access method is unnecessary since only one SCA process is needed, and the related authorisation resource is automatically created by the ASPSP after the submission of the consent data with the first POST consent/{payment-product} call.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>sepa-credit-transfers</li>    <li>cross-border-credit-transfers</li>  </ul>
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | Date of the request.
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Is contained if and only if the \"Signature\" element is contained in the header of the request.
signature = 'signature_example' # str | A signature of the request by the TPP on application level. This might be mandated by ASPSP.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment authorisation.</p> (optional)

try:
    # Start the authorisation process for a payment cancellation
    api_response = api_instance.add_payment_cancellation_authorisation(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, tpp_redirect_uri=tpp_redirect_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->add_payment_cancellation_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;sepa-credit-transfers&lt;/li&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| Date of the request. | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | 
 **signature** | **str**| A signature of the request by the TPP on application level. This might be mandated by ASPSP. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. | 
 **tpp_redirect_uri** | **str**| &lt;p&gt;URI of the TPP, where the transaction flow shall be redirected to after a Redirect.&lt;/p&gt;  &lt;p&gt;This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment authorisation.&lt;/p&gt; | [optional] 

### Return type

[**AddPaymentAuthorisationResponseDto**](AddPaymentAuthorisationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_payment_for_cross_border_credit_transfer**
> AddPaymentInitiationResponseDto add_payment_for_cross_border_credit_transfer(payment_service, payment_product, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, body, consent_id=consent_id, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location, tpp_redirect_uri=tpp_redirect_uri, tpp_redirect_preferred=tpp_redirect_preferred)

Payment Initiation request for CrossBorderCreditTransfer

<p>This method is used to initiate a cross-border payment at the ASPSP.</p>  <h2>Variants of Payment Initiation Requests</h2>  <p>This method to initiate a payment initiation at the ASPSP can be sent with a JSON body.</p>  <p>There are the following <strong>payment products</strong> that are currently supported:</p>  <ul>    <li> Payment products with payment information in <em>JSON</em> format: <ul><li><strong><em>cross-border-credit-transfers</em></strong></li></ul></li>  </ul>  <p>Furthermore the request body depends on the <strong>payment-service</strong></p>  <ul>    <li>      <p>        <strong>          <em>payments</em>        </strong>: A single payment initiation request.</p>    </li>  </ul>  <p>This is the first step in the API to initiate a payment.</p>  <h2>Single and mulitilevel SCA Processes</h2>  <p>The Payment Initiation Requests are independent from the need of one ore multilevel SCA processing, i.e. independent from the number of authorisations needed for the execution of payments.</p>  <p>Payment Initiations submitted will receive the 'PDNG' status initially, since the Payment has not been reviewed and confirmed by a PSU yet. In order to proceed with the Payment Initiation, a redirect to the 'scaOAuth' authorization endpoint with scope PIS:{paymentId}is required. During this redirect the PSU can review and choose one of the following options: 1. allow the payment to be created or 2. allow the payment to be created and authorise the payment. If the PSU chooses the first option, the status will change to 'RCVD' and further authorisations will be required. Then a new redirect to the same endpoint is required again, where the PSU can then choose option 2. If mulitilevel SCA is required, the status will change to 'PATC' meaning the payment is partially authorised. A different PSU will then need to be redirected the same way to make the final authorisation. After which the status will change to 'ACTC'.</p>  <p>Funds confirmations are not supported by the ASPSP for this service.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>cross-border-credit-transfers</li>  </ul>
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.
body = swagger_client.CrossBorderPaymentDto() # CrossBorderPaymentDto | <p>JSON request body for a payment inition request message</p>  <p>There are the following payment-products currently supported:</p>  <ul>    <li>\"cross-border-credit-transfers\" with JSON-Body</li>  </ul>  <p>There are the following payment-services currently supported:</p>  <ul>    <li>\"payments\"</li>  </ul>
consent_id = 'consent_id_example' # str | This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. Currently this field can be provided, but it does not do anything extra, since the payment initiation always needs to be reviewed by the PSU using the SCA Redirect OAuth approach. (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment initiation. Note that this URI should not be PSU specific, incase of multilevel SCA required for this payment initiation, another PSU also needs to be able to be redirected to the OAuth authorization endpoint with the same redirect URI.</p> (optional)
tpp_redirect_preferred = true # bool | This field is ignored, since a redirect approach is always used by the ASPSP. (optional)

try:
    # Payment Initiation request for CrossBorderCreditTransfer
    api_response = api_instance.add_payment_for_cross_border_credit_transfer(payment_service, payment_product, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, body, consent_id=consent_id, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location, tpp_redirect_uri=tpp_redirect_uri, tpp_redirect_preferred=tpp_redirect_preferred)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->add_payment_for_cross_border_credit_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | 
 **body** | [**CrossBorderPaymentDto**](CrossBorderPaymentDto.md)| &lt;p&gt;JSON request body for a payment inition request message&lt;/p&gt;  &lt;p&gt;There are the following payment-products currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;\&quot;cross-border-credit-transfers\&quot; with JSON-Body&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;There are the following payment-services currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;\&quot;payments\&quot;&lt;/li&gt;  &lt;/ul&gt; | 
 **consent_id** | **str**| This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. Currently this field can be provided, but it does not do anything extra, since the payment initiation always needs to be reviewed by the PSU using the SCA Redirect OAuth approach. | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id** | **str**| Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id_type** | **str**| Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available. | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available. | [optional] 
 **tpp_redirect_uri** | **str**| &lt;p&gt;URI of the TPP, where the transaction flow shall be redirected to after a Redirect.&lt;/p&gt;  &lt;p&gt;This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment initiation. Note that this URI should not be PSU specific, incase of multilevel SCA required for this payment initiation, another PSU also needs to be able to be redirected to the OAuth authorization endpoint with the same redirect URI.&lt;/p&gt; | [optional] 
 **tpp_redirect_preferred** | **bool**| This field is ignored, since a redirect approach is always used by the ASPSP. | [optional] 

### Return type

[**AddPaymentInitiationResponseDto**](AddPaymentInitiationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_payment_for_sepa_credit_transfer**
> AddPaymentInitiationResponseDto add_payment_for_sepa_credit_transfer(payment_service, payment_product, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, body, consent_id=consent_id, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location, tpp_redirect_uri=tpp_redirect_uri, tpp_redirect_preferred=tpp_redirect_preferred)

Payment Initiation request for SepaCreditTransfer

<p>This method is used to initiate a payment at the ASPSP.</p>  <h2>Variants of Payment Initiation Requests</h2>  <p>This method to initiate a payment initiation at the ASPSP can be sent with a JSON body.</p>  <p>There are the following <strong>payment products</strong> that are currently supported:</p>  <ul>    <li> Payment products with payment information in <em>JSON</em> format: <ul><li><strong><em>sepa-credit-transfers</em></strong></li></ul></li>  </ul>  <p>Furthermore the request body depends on the <strong>payment-service</strong></p>  <ul>    <li>      <p>        <strong>          <em>payments</em>        </strong>: A single payment initiation request.</p>    </li>  </ul>  <p>This is the first step in the API to initiate a payment.</p>  <h2>Single and mulitilevel SCA Processes</h2>  <p>The Payment Initiation Requests are independent from the need of one ore multilevel SCA processing, i.e. independent from the number of authorisations needed for the execution of payments.</p>  <p>Payment Initiations submitted will receive the 'PDNG' status initially, since the Payment has not been reviewed and confirmed by a PSU yet. In order to proceed with the Payment Initiation, a redirect to the 'scaOAuth' authorization endpoint with scope PIS:{paymentId}is required. During this redirect the PSU can review and choose one of the following options: 1. allow the payment to be created or 2. allow the payment to be created and authorise the payment. If the PSU chooses the first option, the status will change to 'RCVD' and further authorisations will be required. Then a new redirect to the same endpoint is required again, where the PSU can then choose option 2. If mulitilevel SCA is required, the status will change to 'PATC' meaning the payment is partially authorised. A different PSU will then need to be redirected the same way to make the final authorisation. After which the status will change to 'ACTC'.</p>  <p>Funds confirmations are not supported by the ASPSP for this service.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>cross-border-credit-transfers</li>  </ul>
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.
body = swagger_client.SinglePaymentDto() # SinglePaymentDto | <p>JSON request body for a payment inition request message</p>  <p>There are the following payment-products currently supported:</p>  <ul>    <li>\"sepa-credit-transfers\" with JSON-Body</li>  </ul>  <p>There are the following payment-services currently supported:</p>  <ul>    <li>\"payments\"</li>  </ul>
consent_id = 'consent_id_example' # str | This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. Currently this field can be provided, but it does not do anything extra, since the payment initiation always needs to be reviewed by the PSU using the SCA Redirect OAuth approach. (optional)
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. (optional)
tpp_redirect_uri = 'tpp_redirect_uri_example' # str | <p>URI of the TPP, where the transaction flow shall be redirected to after a Redirect.</p>  <p>This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment initiation. Note that this URI should not be PSU specific, incase of multilevel SCA required for this payment initiation, another PSU also needs to be able to be redirected to the OAuth authorization endpoint with the same redirect URI.</p> (optional)
tpp_redirect_preferred = true # bool | This field is ignored, since a redirect approach is always used by the ASPSP. (optional)

try:
    # Payment Initiation request for SepaCreditTransfer
    api_response = api_instance.add_payment_for_sepa_credit_transfer(payment_service, payment_product, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, body, consent_id=consent_id, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location, tpp_redirect_uri=tpp_redirect_uri, tpp_redirect_preferred=tpp_redirect_preferred)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->add_payment_for_sepa_credit_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | 
 **body** | [**SinglePaymentDto**](SinglePaymentDto.md)| &lt;p&gt;JSON request body for a payment inition request message&lt;/p&gt;  &lt;p&gt;There are the following payment-products currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;\&quot;sepa-credit-transfers\&quot; with JSON-Body&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;There are the following payment-services currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;\&quot;payments\&quot;&lt;/li&gt;  &lt;/ul&gt; | 
 **consent_id** | **str**| This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. Currently this field can be provided, but it does not do anything extra, since the payment initiation always needs to be reviewed by the PSU using the SCA Redirect OAuth approach. | [optional] 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id** | **str**| Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id_type** | **str**| Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available. | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available. | [optional] 
 **tpp_redirect_uri** | **str**| &lt;p&gt;URI of the TPP, where the transaction flow shall be redirected to after a Redirect.&lt;/p&gt;  &lt;p&gt;This URI is checked against during the SCA Redirect OAuth approach, where this URI is matched against the redirect_uri used in the OAuth redirect for this payment initiation. Note that this URI should not be PSU specific, incase of multilevel SCA required for this payment initiation, another PSU also needs to be able to be redirected to the OAuth authorization endpoint with the same redirect URI.&lt;/p&gt; | [optional] 
 **tpp_redirect_preferred** | **bool**| This field is ignored, since a redirect approach is always used by the ASPSP. | [optional] 

### Return type

[**AddPaymentInitiationResponseDto**](AddPaymentInitiationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, authorization, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location)

Delete Payment

<p>Deletes or cancels a payment.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>sepa-credit-transfers</li>    <li>cross-border-credit-transfers</li>  </ul>
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
psu_ip_address = 'psu_ip_address_example' # str | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.
psu_id = 'psu_id_example' # str | Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_id_type = 'psu_id_type_example' # str | Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_corporate_id_type = 'psu_corporate_id_type_example' # str | Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. (optional)
psu_user_agent = 'psu_user_agent_example' # str | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. (optional)
psu_geo_location = 'psu_geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. (optional)

try:
    # Delete Payment
    api_instance.delete(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, psu_ip_address, authorization, psu_id=psu_id, psu_id_type=psu_id_type, psu_corporate_id=psu_corporate_id, psu_corporate_id_type=psu_corporate_id_type, psu_user_agent=psu_user_agent, psu_geo_location=psu_geo_location)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;sepa-credit-transfers&lt;/li&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **psu_ip_address** | **str**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 
 **psu_id** | **str**| Client ID of the PSU in the ASPSP client interface. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_id_type** | **str**| Type of the PSU-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id** | **str**| Corporate ID of the PSU. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_corporate_id_type** | **str**| Type of the Corporate-ID. This field is optional and is not used to identify the PSU, this is done using the SCA Redirect OAuth approach. | [optional] 
 **psu_user_agent** | **str**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available. | [optional] 
 **psu_geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_payment_for_direct_debit_transfer**
> GetPaymentInitiationForBulkPaymentResponseDto get_bulk_payment_for_direct_debit_transfer(payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Bulk Payment for Direct Debit Information

<p>Returns the content of a bulk payment for direct debit object</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Bulk Payment for Direct Debit Information
    api_response = api_instance.get_bulk_payment_for_direct_debit_transfer(payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_bulk_payment_for_direct_debit_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentInitiationForBulkPaymentResponseDto**](GetPaymentInitiationForBulkPaymentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_payment_for_sepa_credit_transfer**
> GetPaymentInitiationForBulkPaymentResponseDto get_bulk_payment_for_sepa_credit_transfer(payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Bulk Payment Information

<p>Returns the content of a bulk payment object</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Bulk Payment Information
    api_response = api_instance.get_bulk_payment_for_sepa_credit_transfer(payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_bulk_payment_for_sepa_credit_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentInitiationForBulkPaymentResponseDto**](GetPaymentInitiationForBulkPaymentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_authorisation_status**
> GetPaymentAuthorisationResponseDto get_payment_authorisation_status(payment_service, payment_product, payment_id, authorisation_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Read the SCA Status of the payment authorisation

This method returns the SCA status of a payment initiation's authorisation sub-resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>sepa-credit-transfers</li>    <li>cross-border-credit-transfers</li>  </ul>
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
authorisation_id = 'authorisation_id_example' # str | Resource identification of the generated authorisation sub-resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Read the SCA Status of the payment authorisation
    api_response = api_instance.get_payment_authorisation_status(payment_service, payment_product, payment_id, authorisation_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_authorisation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;sepa-credit-transfers&lt;/li&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **authorisation_id** | **str**| Resource identification of the generated authorisation sub-resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentAuthorisationResponseDto**](GetPaymentAuthorisationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_authorisations**
> GetPaymentAuthorisationsResponseDto get_payment_authorisations(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Payment Initiation Authorisation Sub-Resources Request

<p>Read a list of all authorisation subresources IDs which have been created.</p>  <p>This function returns an array of hyperlinks to all generated authorisation sub-resources.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>sepa-credit-transfers</li>    <li>cross-border-credit-transfers</li>  </ul>
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Payment Initiation Authorisation Sub-Resources Request
    api_response = api_instance.get_payment_authorisations(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_authorisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;sepa-credit-transfers&lt;/li&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentAuthorisationsResponseDto**](GetPaymentAuthorisationsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_cancellation_authorisation_status**
> GetPaymentAuthorisationResponseDto get_payment_cancellation_authorisation_status(payment_service, payment_product, payment_id, authorisation_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Read the SCA Status of the payment authorisation

This method returns the SCA status of a payment initiation's authorisation sub-resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>sepa-credit-transfers</li>    <li>cross-border-credit-transfers</li>  </ul>
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
authorisation_id = 'authorisation_id_example' # str | Resource identification of the generated authorisation sub-resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Read the SCA Status of the payment authorisation
    api_response = api_instance.get_payment_cancellation_authorisation_status(payment_service, payment_product, payment_id, authorisation_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_cancellation_authorisation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;sepa-credit-transfers&lt;/li&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **authorisation_id** | **str**| Resource identification of the generated authorisation sub-resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentAuthorisationResponseDto**](GetPaymentAuthorisationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_cancellation_authorisations**
> GetPaymentAuthorisationsResponseDto get_payment_cancellation_authorisations(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Payment Initiation Authorisation Sub-Resources Request

<p>Read a list of all authorisation subresources IDs which have been created.</p>  <p>This function returns an array of hyperlinks to all generated authorisation sub-resources.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>sepa-credit-transfers</li>    <li>cross-border-credit-transfers</li>  </ul>
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Payment Initiation Authorisation Sub-Resources Request
    api_response = api_instance.get_payment_cancellation_authorisations(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_cancellation_authorisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;sepa-credit-transfers&lt;/li&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentAuthorisationsResponseDto**](GetPaymentAuthorisationsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_for_cross_border_credit_transfer**
> GetPaymentInitiationForCrossBorderPaymentResponseDto get_payment_for_cross_border_credit_transfer(payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Cross-Border Payment Information

<p>Returns the content of a cross-border payment object</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Cross-Border Payment Information
    api_response = api_instance.get_payment_for_cross_border_credit_transfer(payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_for_cross_border_credit_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentInitiationForCrossBorderPaymentResponseDto**](GetPaymentInitiationForCrossBorderPaymentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_for_sepa_credit_transfer**
> GetPaymentInitiationResponseDto get_payment_for_sepa_credit_transfer(payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Get Payment Information

<p>Returns the content of a payment object</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Get Payment Information
    api_response = api_instance.get_payment_for_sepa_credit_transfer(payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_payment_for_sepa_credit_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentInitiationResponseDto**](GetPaymentInitiationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> GetPaymentInitiationStatusResponseDto get_status(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)

Payment initiation status request

<p>Returns the content of a payment object</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInitiationServicePISApi()
payment_service = 'payment_service_example' # str | <p>The following payment services are currently supported:</p>  <ul>    <li>payments</li>  </ul>
payment_product = 'payment_product_example' # str | <p>The following payment products are currently supported:</p>  <ul>    <li>sepa-credit-transfers</li>    <li>cross-border-credit-transfers</li>  </ul>
payment_id = 'payment_id_example' # str | Resource identification of the generated payment initiation resource.
_date = '_date_example' # str | <p>The date of the request.</p>
x_request_id = 'x_request_id_example' # str | ID of the request, unique to the call, as determined by the initiating party.
digest = 'digest_example' # str | Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature.
signature = 'signature_example' # str | A signature of the request. The ASPSP mandates the use of a signature.
tpp_signature_certificate = 'tpp_signature_certificate_example' # str | The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature.
authorization = 'authorization_example' # str | The bearer access token of the OAuth2 process required for accessing this API.

try:
    # Payment initiation status request
    api_response = api_instance.get_status(payment_service, payment_product, payment_id, _date, x_request_id, digest, signature, tpp_signature_certificate, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_service** | **str**| &lt;p&gt;The following payment services are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;payments&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_product** | **str**| &lt;p&gt;The following payment products are currently supported:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;sepa-credit-transfers&lt;/li&gt;    &lt;li&gt;cross-border-credit-transfers&lt;/li&gt;  &lt;/ul&gt; | 
 **payment_id** | **str**| Resource identification of the generated payment initiation resource. | 
 **_date** | **str**| &lt;p&gt;The date of the request.&lt;/p&gt; | 
 **x_request_id** | **str**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **str**| Digest of the body of the request. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **signature** | **str**| A signature of the request. The ASPSP mandates the use of a signature. | 
 **tpp_signature_certificate** | **str**| The certificate used for signing the request, in base64 encoding. This field is mandatory, because the ASPSP mandates the use of a signature. | 
 **authorization** | **str**| The bearer access token of the OAuth2 process required for accessing this API. | 

### Return type

[**GetPaymentInitiationStatusResponseDto**](GetPaymentInitiationStatusResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

