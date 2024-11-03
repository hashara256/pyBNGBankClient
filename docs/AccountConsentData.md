# AccountConsentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AccountConsentAccess**](AccountConsentAccess.md) | Requested access services for a consent. | 
**combined_service_indicator** | **bool** | If \&quot;true\&quot; indicates that a payment initiation service will be addressed in the same \&quot;session\&quot;. | 
**recurring_indicator** | **bool** | \&quot;true\&quot;, if the consent is for recurring access to the account data.&lt;br /&gt;\&quot;false\&quot;, if the consent is for one access to the account data. | 
**valid_until** | **str** | &lt;p&gt;This parameter is requesting a valid until date for the requested consent.&lt;br /&gt;The content is the local ASPSP date in ISO-Date Format, e.g. 2017-10-30.&lt;/p&gt;  &lt;p&gt;Future dates might get adjusted by ASPSP.&lt;/p&gt;  &lt;p&gt;If a maximal available date is requested, a date in far future is to be used: \&quot;9999-12-31\&quot;.&lt;/p&gt;  &lt;p&gt;In both cases the consent object to be retrieved by the GET Consent Request will contain the adjusted date.&lt;/p&gt; | 
**frequency_per_day** | **int** | &lt;p&gt;This field indicates the requested maximum frequency for an access without PSU involvement per day.&lt;br /&gt;For a one-off access, this attribute is set to \&quot;1\&quot;.&lt;/p&gt;  &lt;p&gt;The frequency needs to be greater equal to one.&lt;/p&gt; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


