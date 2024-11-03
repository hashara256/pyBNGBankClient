# AddConsentAuthorisationResponseLinksDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sca_o_auth** | [**HrefTypeDto**](HrefTypeDto.md) | A link to the OAuth2 configuration endpoint. When this link is present, one of the next steps is to redirect the PSU to the OAuth2 authorization endpoint.  Note that the creation of consent authorisation sub-resources at this ASPSP are created implicitly. Explicitly creation of such sub-resources do not have any follow-up actions.  Use scope PIS to redirect the PSU to the OAuth2 authorization endpoint for authorisation, instead. | [optional] 
**sca_status** | [**HrefTypeDto**](HrefTypeDto.md) | A link to retrieve status information of the SCA method for this consent authorisation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


