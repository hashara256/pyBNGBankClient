# GetConsentStatusResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_status** | **str** | &lt;p&gt;This is the overall lifecycle status of the consent.&lt;/p&gt;  &lt;p&gt;Valid values are:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;&#39;received&#39;: The consent data have been received and are technically correct.The data is not authorised yet.&lt;/li&gt;    &lt;li&gt;&#39;rejected&#39;: The consent data have been rejected e.g. since no successful authorisation has taken place.&lt;/li&gt;    &lt;li&gt;&#39;valid&#39;: The consent is accepted and valid for GET account data calls and others as specified in the consent object.&lt;/li&gt;    &lt;li&gt;&#39;revokedByPsu&#39;: The consent has been revoked by the PSU towards the ASPSP.&lt;/li&gt;    &lt;li&gt;&#39;expired&#39;: The consent expired.&lt;/li&gt;    &lt;li&gt;&#39;terminatedByTpp&#39;: The corresponding TPP has terminated the consent by applying the DELETE method to the consent resource.&lt;/li&gt;  &lt;/ul&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


