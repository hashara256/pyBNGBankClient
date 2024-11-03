# AccountReportDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booked** | [**list[TransactionDto]**](TransactionDto.md) | List of booked transactions. | [optional] 
**pending** | [**list[TransactionDto]**](TransactionDto.md) | List of pending transactions. | [optional] 
**links** | [**AccountReportLinksDto**](AccountReportLinksDto.md) | &lt;p&gt;Links to the account, which can be directly used for retrieving account information from this dedicated account.&lt;/p&gt;  &lt;p&gt;Links to \&quot;balances\&quot; and/or \&quot;transactions\&quot;&lt;/p&gt;  &lt;p&gt;These links are only supported, when the corresponding consent has been already granted.&lt;/p&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


