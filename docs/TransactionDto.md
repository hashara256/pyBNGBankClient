# TransactionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | This shall be filled, if addressable resource are created by the ASPSP on the /accounts endpoint. | [optional] 
**entry_reference** | **str** | Is the identification of the transaction as used e.g. for reference for deltafunction on application level. The same identification as for example used within camt.05x messages. | [optional] 
**end_to_end_id** | **str** | Unique end to end identity. | [optional] 
**mandate_id** | **str** | Identification of Mandates, e.g. a SEPA Mandate ID | [optional] 
**check_id** | **str** | Identification of a Cheque | [optional] 
**creditor_id** | **str** | Identification of Creditors, e.g. a SEPA Creditor ID | [optional] 
**booking_date** | **str** | The Date when an entry is posted to an account on the ASPSPs books. | [optional] 
**value_date** | **str** | The Date at which assets become available to the account owner in case of a credit. | [optional] 
**transaction_amount** | [**AmountFieldDto**](AmountFieldDto.md) | The amount of the transaction as billed to the account. | [optional] 
**currency_exchange** | [**ReportExchangeRateDto**](ReportExchangeRateDto.md) |  | [optional] 
**creditor_name** | **str** | Name of the creditor if a \&quot;Debited\&quot; transaction. | [optional] 
**creditor_account** | [**AccountReferenceDto**](AccountReferenceDto.md) |  | [optional] 
**ultimate_creditor** | **str** |  | [optional] 
**debtor_name** | **str** | Name of the debtor if a \&quot;Credited\&quot; transaction. | [optional] 
**debtor_account** | [**AccountReferenceDto**](AccountReferenceDto.md) |  | [optional] 
**ultimate_debtor** | **str** |  | [optional] 
**remittance_information_unstructured** | **str** |  | [optional] 
**remittance_information_structured** | **str** | Reference as contained in the structured remittance reference structure (without the surrounding XML structure). | [optional] 
**purpose_code** | **str** |  | [optional] 
**bank_transaction_code** | **str** | Bank transaction code as used by the ASPSP and using the sub elements of this structured code defined by ISO20022 | [optional] 
**proprietary_bank_transaction_code** | **str** | proprietary bank transaction code as used within a community or within an ASPSP e.g. for MT94x based transaction reports | [optional] 
**links** | [**TransactionResponseLinksDto**](TransactionResponseLinksDto.md) | &lt;p&gt;Links to transaction details, which can be directly used for retrieving transaction details.&lt;/p&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


