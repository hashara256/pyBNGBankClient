# OAuthMetaDataConfigurationResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | The name of the issuer. | [optional] 
**authorization_endpoint** | **str** | The URI of the authorization endpoint. | [optional] 
**token_endpoint** | **str** | The URI of the token endpoint. | [optional] 
**scopes_supported** | **list[str]** | &lt;p&gt;A list of scopes supported.&lt;/p&gt;  &lt;p&gt;The following scopes are supported:&lt;ul&gt;&lt;li&gt;PIS:{paymentId} &#x3D; Review and/or authorise a payment initiation&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**response_types_supported** | **list[str]** | &lt;p&gt;A list of response types supported.&lt;/p&gt;  &lt;p&gt;The following response types are supported:&lt;ul&gt;&lt;li&gt;code &#x3D; An authorization code is returned after a successful SCA Redirect using OAuth2&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**grant_types_supported** | **list[str]** | &lt;p&gt;A list of grant types supported.&lt;/p&gt;  &lt;p&gt;The following grant types are supported:&lt;ul&gt;&lt;li&gt;authorization_code &#x3D; An authorization code is used to retrieve an access token&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**code_challenge_methods_supported** | **list[str]** | &lt;p&gt;A list of code challenge methods supported.&lt;/p&gt;  &lt;p&gt;The following code challenge methods are supported:&lt;ul&gt;&lt;li&gt;plain &#x3D; a code verifier is send in the same form in the authorization request and token request&lt;/li&gt;&lt;li&gt;S256 &#x3D; a code verifier is send in SHA-256 in the authorization request and in plain form in the token request&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**service_documentation** | **str** | The URI to the service documentation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


