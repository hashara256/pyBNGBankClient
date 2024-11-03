# AddPaymentInitiationResponseLinksDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sca_o_auth** | [**HrefTypeDto**](HrefTypeDto.md) | A link to the OAuth2 configuration endpoint. When this link is present, one of the next steps is to redirect the PSU to the OAuth2 authorization endpoint.  Use scope PIS during the redirect. The PSU can then review the payment initiation and also choose to authorise it. | [optional] 
**_self** | [**HrefTypeDto**](HrefTypeDto.md) | A link to the payment initiation resource created, with this link information of the payment initiation can be retrieved. | [optional] 
**status** | [**HrefTypeDto**](HrefTypeDto.md) | A link to the payment initiation resource created, with this link status information of the payment initiation can be retrieved. | [optional] 
**start_authorisation** | [**HrefTypeDto**](HrefTypeDto.md) | A link to create or retrieve payment authorisation sub-resources of the payment initiation created.  When this link is present, to start the authorisation of the payment initiation, this link might be present.  Note that the ASPSP requires a SCA Redirect OAuth2 approach to authorise the payment initiation.  Use the scaOAuth link with the scope PIS instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


