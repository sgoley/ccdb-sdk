# MultiLevelAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_count** | **int** | The total number of complaints covered in this aggregation | [optional] 
**var_field** | [**MultiLevelAggregationField**](MultiLevelAggregationField.md) |  | [optional] 

## Example

```python
from openapi_client.models.multi_level_aggregation import MultiLevelAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of MultiLevelAggregation from a JSON string
multi_level_aggregation_instance = MultiLevelAggregation.from_json(json)
# print the JSON string representation of the object
print(MultiLevelAggregation.to_json())

# convert the object into a dict
multi_level_aggregation_dict = multi_level_aggregation_instance.to_dict()
# create an instance of MultiLevelAggregation from a dict
multi_level_aggregation_from_dict = MultiLevelAggregation.from_dict(multi_level_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


