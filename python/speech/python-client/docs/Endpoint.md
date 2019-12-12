# Endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrent_recognitions** | **int** | The number of concurrent recognitions the endpoint supports | [optional] 
**id** | **str** | The identifier of this entity | 
**endpoint_urls** | **dict(str, str)** | The list of endpoint urls | [optional] 
**endpoint_kind** | **str** | The kind of this endpoint (e.g. custom speech, custom voice ...) | 
**last_action_date_time** | **datetime** | The time-stamp when the current status was entered | [optional] 
**status** | **str** | The status of the object | [optional] 
**created_date_time** | **datetime** | The time-stamp when the object was created | [optional] 
**models** | [**list[Model]**](Model.md) | Information about the deployed models | 
**content_logging_enabled** | **bool** | A value indicating whether content logging (audio &amp;amp; transcriptions) is being used for a deployment.  Suppressing content logging will result in a higher cost for the deployment.  Free subscriptions can only deploy true | [optional] 
**name** | **str** | The name of the object | 
**description** | **str** | The description of the object | [optional] 
**properties** | **dict(str, str)** | The custom properties of this entity | [optional] 
**locale** | **str** | The locale of the contained data | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


