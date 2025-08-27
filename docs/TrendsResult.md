# TrendsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | [**TrendsResultAggregations**](TrendsResultAggregations.md) |  | [optional] 

## Example

```python
from openapi_client.models.trends_result import TrendsResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsResult from a JSON string
trends_result_instance = TrendsResult.from_json(json)
# print the JSON string representation of the object
print(TrendsResult.to_json())

# convert the object into a dict
trends_result_dict = trends_result_instance.to_dict()
# create an instance of TrendsResult from a dict
trends_result_from_dict = TrendsResult.from_dict(trends_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


