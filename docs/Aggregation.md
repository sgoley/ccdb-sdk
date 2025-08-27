# Aggregation

An Elasticsearch aggregation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_count** | **int** | The total number of complaints covered in this aggregation | [optional] 
**var_field** | [**AggregationField**](AggregationField.md) |  | [optional] 

## Example

```python
from openapi_client.models.aggregation import Aggregation

# TODO update the JSON string below
json = "{}"
# create an instance of Aggregation from a JSON string
aggregation_instance = Aggregation.from_json(json)
# print the JSON string representation of the object
print(Aggregation.to_json())

# convert the object into a dict
aggregation_dict = aggregation_instance.to_dict()
# create an instance of Aggregation from a dict
aggregation_from_dict = Aggregation.from_dict(aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


