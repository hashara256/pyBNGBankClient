# CrossBorderPaymentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_to_end_identification** | **str** |  | [optional] 
**debtor_account** | [**AccountReferenceDto**](AccountReferenceDto.md) |  | 
**instructed_amount** | [**AmountFieldDto**](AmountFieldDto.md) |  | 
**creditor_account** | [**CrossBorderAccountReferenceDto**](CrossBorderAccountReferenceDto.md) |  | 
**creditor_agent** | **str** | BICFI required if no bankcode | [optional] 
**creditor_name** | **str** | Creditor Name | 
**creditor_address** | [**AddressDto**](AddressDto.md) |  | 
**charge_bearer** | **str** | The charge bearer of the payment transaction (for this environment not all charge bearer types might be enabled).  Supported values are:&lt;ul&gt;&lt;li&gt;DEBT, CRED, SHAR and SLEV&lt;/li&gt;&lt;/ul&gt; | 
**remittance_information_unstructured** | **str** | Unstructured remittance information, the description. For urgent Cross-Border payments, the max length is 128 | [optional] 
**requested_execution_date** | **str** | ISO Date yyyy-MM-dd, Business day, not-holiday. | 
**bankcode** | **str** | Bankcode required if no creditorAgent (BICFI) | [optional] 
**contra_bank_name** | **str** |  | 
**contra_bank_city** | **str** |  | 
**contra_bank_country_code** | **str** | ContraBankCountryCode required and a valid country | 
**urgent** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


