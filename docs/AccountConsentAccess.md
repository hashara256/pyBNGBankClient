# AccountConsentAccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**list[AccountAccess]**](AccountAccess.md) | &lt;p&gt;Is asking for detailed account information.&lt;/p&gt;  &lt;p&gt;If the array is empty, the TPP is asking for an accessible account list.&lt;br /&gt;This may be restricted in a PSU/ASPSP authorization dialogue.&lt;br /&gt;If the array is empty, also the arrays for balances or transactions shall be empty, if used.&lt;/p&gt; | [optional] 
**balances** | [**list[AccountAccess]**](AccountAccess.md) | &lt;p&gt;Is asking for balances of the addressed accounts.&lt;/p&gt;  &lt;p&gt;If the array is empty, the TPP is asking for the balances of all accessible account lists.&lt;br /&gt;This may be restricted in a PSU/ASPSP authorization dialogue.&lt;br /&gt;If the array is empty, also the arrays for accounts or transactions shall be empty, if used.&lt;/p&gt; | [optional] 
**transactions** | [**list[AccountAccess]**](AccountAccess.md) | &lt;p&gt;Is asking for transactions of the addressed accounts.&lt;/p&gt;  &lt;p&gt;If the array is empty, the TPP is asking for the transactions of all accessible account lists.&lt;br /&gt;This may be restricted in a PSU/ASPSP authorization dialogue.&lt;br /&gt;If the array is empty, also the arrays for accounts or balances shall be empty, if used.&lt;/p&gt; | [optional] 
**available_accounts** | **str** | &lt;p&gt;Only the value \&quot;allAccounts\&quot; is admitted.&lt;/p&gt; | [optional] 
**available_accounts_with_balances** | **str** | &lt;p&gt;Only the value \&quot;allAccounts\&quot; is admitted.&lt;/p&gt; | [optional] 
**all_psd2** | **str** | &lt;p&gt;Only the value \&quot;allAccounts\&quot; is admitted.&lt;/p&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


