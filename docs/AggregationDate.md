# AggregationDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_as_string** | **datetime** | ISO-8601 formatted date (yyyy-mm-ddTHH:MM:SSZZ) | [optional] 
**value** | **float** | Seconds since 1970 (Unix Epoch) | [optional] 

## Example

```python
from openapi_client.models.aggregation_date import AggregationDate

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationDate from a JSON string
aggregation_date_instance = AggregationDate.from_json(json)
# print the JSON string representation of the object
print(AggregationDate.to_json())

# convert the object into a dict
aggregation_date_dict = aggregation_date_instance.to_dict()
# create an instance of AggregationDate from a dict
aggregation_date_from_dict = AggregationDate.from_dict(aggregation_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


