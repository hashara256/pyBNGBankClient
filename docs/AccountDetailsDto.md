# AccountDetailsDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | This shall be filled, if addressable resource are created by the ASPSP on the /accounts endpoint. | [optional] 
**iban** | **str** | IBAN of an account. | [optional] 
**currency** | **str** | ISO 4217 Alpha 3 currency code. | [optional] 
**name** | **str** | Name of the account given by the bank or the PSU in online-banking. | [optional] 
**product** | **str** | Product name of the bank for this account, proprietary definition. | [optional] 
**cash_account_type** | **str** | ExternalCashAccountType1Code from ISO 20022. | [optional] 
**status** | **str** | &lt;p&gt;Account status. The value is one of the following:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;\&quot;enabled\&quot;: account is available&lt;/li&gt;    &lt;li&gt;\&quot;deleted\&quot;: account is terminated&lt;/li&gt;    &lt;li&gt;\&quot;blocked\&quot;: account is blocked e.g. for legal reasons. If this field is not used, than the account is available in the sense of this specification.&lt;/li&gt;  &lt;/ul&gt; | [optional] 
**bic** | **str** | BICFI. | [optional] 
**linked_accounts** | **str** | Case of a set of pending card transactions, the APSP will provide the relevant cash account the card is set up on. | [optional] 
**usage** | **str** | &lt;p&gt;Specifies the usage of the account&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;PRIV: private personal account&lt;/li&gt;    &lt;li&gt;ORGA: professional account&lt;/li&gt;  &lt;/ul&gt; | [optional] 
**details** | **str** | &lt;p&gt;Specifications that might be provided by the ASPSP&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;characteristics of the account&lt;/li&gt;    &lt;li&gt;characteristics of the relevant card&lt;/li&gt;  &lt;/ul&gt; | [optional] 
**balances** | [**list[BalanceDto]**](BalanceDto.md) | A list of balances regarding this account, e.g. the current balance, the last booked balance. The list migght be restricted to the current ballance. | [optional] 
**links** | [**ReadAccountListResponseLinksDto**](ReadAccountListResponseLinksDto.md) | &lt;p&gt;Links to the account, which can be directly used for retrieving account information from this dedicated account.&lt;/p&gt;  &lt;p&gt;Links to \&quot;balances\&quot; and/or \&quot;transactions\&quot;&lt;/p&gt;  &lt;p&gt;These links are only supported, when the corresponding consent has been already granted.&lt;/p&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


