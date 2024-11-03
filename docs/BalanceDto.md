# BalanceDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_amount** | [**EuroAmountFieldDto**](EuroAmountFieldDto.md) |  | [optional] 
**balance_type** | **str** | &lt;p&gt;The following balance types are defined:&lt;/p&gt;  &lt;ul&gt;    &lt;li&gt;      &lt;p&gt;\&quot;closingBooked\&quot;:Balance of the account at the end of the pre-agreed account reporting period.It is the sum of the opening booked balance at the beginning of the period and all entries bookedto the account during the pre-agreed account reporting period.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;      &lt;p&gt;\&quot;expected\&quot;:Balance composed of booked entries and pending items known at the time of calculation,which projects the end of day balance if everything is booked on the account and no other entry is posted.&lt;/p&gt;    &lt;/li&gt;  &lt;/ul&gt; | [optional] 
**credit_limit_included** | **bool** | A flag indicating if the credit limit of the corresponding account is included in the calculation of the balance, where applicable. | [optional] 
**last_change_date_time** | **str** | This data element might be used to indicate e.g. with the expected or booked balance that no action is known on the account, which is not yet booked. | [optional] 
**reference_date** | **str** | Reference date of the balance. | [optional] 
**last_committed_transaction** | **str** | EntryReference of the last commited transaction to support the TPP in identifying whether all PSU transactions are already known. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


