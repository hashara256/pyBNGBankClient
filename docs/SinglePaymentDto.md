# SinglePaymentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_to_end_identification** | **str** |  | [optional] 
**debtor_account** | [**AccountReferenceDto**](AccountReferenceDto.md) |  | 
**instructed_amount** | [**EuroAmountFieldDto**](EuroAmountFieldDto.md) |  | 
**creditor_account** | [**AccountReferenceDto**](AccountReferenceDto.md) |  | 
**creditor_agent** | **str** | BICFI | [optional] 
**creditor_name** | **str** | Creditor Name | 
**creditor_address** | [**AddressDto**](AddressDto.md) |  | [optional] 
**remittance_information_unstructured** | **str** | Unstructured remittance information | [optional] 
**remittance_information_structured** | [**RemittanceDto**](RemittanceDto.md) | Not allowed for urgent payments | [optional] 
**urgent** | **bool** | Can not be used when creating a recurring payment | [optional] 
**requested_execution_date** | **str** | ISO Date yyyy-MM-dd, Business day, not-holiday. Required for non-periodic payments. Not allowed for periodic payments | [optional] 
**frequency** | **str** | Required for periodic payments, not allowed for other payments | [optional] 
**start_date** | **str** | Required for periodic payments, not allowed for other payments | [optional] 
**end_date** | **str** | Optional for periodic payments, not allowed for other payments | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


