# TokenResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token bound to the scope as requested in the authorisation request and confirmed by the PSU. | [optional] 
**token_type** | **str** | The token type, in this case \&quot;Bearer\&quot; as is supported. | [optional] 
**expires_in** | **str** | The lifetime of the access token in seconds. | [optional] 
**refresh_token** | **str** | Refresh Token, which can be utilised to obtain a fresh access tokens in case the previous access token expired or was revoked. Especially useful in the context of AIS. | [optional] 
**scope** | **str** | The scope of the access token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


