# TrendsResultAggregations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**issue** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**product** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**sub_issue** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**sub_product** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**tags** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 

## Example

```python
from openapi_client.models.trends_result_aggregations import TrendsResultAggregations

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsResultAggregations from a JSON string
trends_result_aggregations_instance = TrendsResultAggregations.from_json(json)
# print the JSON string representation of the object
print(TrendsResultAggregations.to_json())

# convert the object into a dict
trends_result_aggregations_dict = trends_result_aggregations_instance.to_dict()
# create an instance of TrendsResultAggregations from a dict
trends_result_aggregations_from_dict = TrendsResultAggregations.from_dict(trends_result_aggregations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


