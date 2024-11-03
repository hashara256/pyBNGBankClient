# AddConsentResponseLinksDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sca_o_auth** | [**HrefTypeDto**](HrefTypeDto.md) | A link to the OAuth2 configuration endpoint. When this link is present, one of the next steps is to redirect the PSU to the OAuth2 authorization endpoint.  Use scope AIS during the redirect. The PSU can then review and approve the consent. | [optional] 
**_self** | [**HrefTypeDto**](HrefTypeDto.md) | A link to the consent resource created, with this link information of the consent can be retrieved. | [optional] 
**status** | [**HrefTypeDto**](HrefTypeDto.md) | A link to the consent resource created, with this link status information of the consent can be retrieved. | [optional] 
**start_authorisation** | [**HrefTypeDto**](HrefTypeDto.md) | A link to create or retrieve consent authorisation sub-resources of the consent created.  When this link is present, to start the authorisation of the consent, this link might be present.  Note that the ASPSP requires a SCA Redirect OAuth2 approach to authorise the consent.  Use the scaOAuth link with the scope AIS instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


