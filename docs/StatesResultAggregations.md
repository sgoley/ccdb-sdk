# StatesResultAggregations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**product** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**state** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 

## Example

```python
from openapi_client.models.states_result_aggregations import StatesResultAggregations

# TODO update the JSON string below
json = "{}"
# create an instance of StatesResultAggregations from a JSON string
states_result_aggregations_instance = StatesResultAggregations.from_json(json)
# print the JSON string representation of the object
print(StatesResultAggregations.to_json())

# convert the object into a dict
states_result_aggregations_dict = states_result_aggregations_instance.to_dict()
# create an instance of StatesResultAggregations from a dict
states_result_aggregations_from_dict = StatesResultAggregations.from_dict(states_result_aggregations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


