# AddBulkPaymentInitiationResponseDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_status** | **str** | The transaction status of the bulk payment initiation created. | [optional] 
**payment_id** | **str** | This is the identifier of the bulk payment initiation created. This identifier will be used later to reference this bulk payment initiation. | [optional] 
**payment_initiation_batch_group_id** | **str** | This is the group identifier of the bulk payment initiation created. This identifier will be used later to reference this bulk payment initiation. This paymentInitiationBatchGroupId is used to group the batches in a posted multi batch file. | [optional] 
**payment_initiation_initiations** | [**list[AddBulkPaymentInitiationResponsePaymentInitiationDto]**](AddBulkPaymentInitiationResponsePaymentInitiationDto.md) | This is a list of bulk payment initiation identifiers created for a bulk payment initiation request. If a multi batch file was posted, multiple payment initiation identifiers will be present. | [optional] 
**links** | [**AddBulkPaymentInitiationResponseLinksDto**](AddBulkPaymentInitiationResponseLinksDto.md) | This is a list of links containing possible next actions that can be performed after the this bulk payment initiation request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


