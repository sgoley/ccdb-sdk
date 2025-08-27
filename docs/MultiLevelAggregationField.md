# MultiLevelAggregationField

The name of the field being aggregated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**List[MultiLevelBucket]**](MultiLevelBucket.md) |  | [optional] 
**doc_count_error_upper_bound** | **int** | The number of possible errors that occurred when searching the shards | [optional] 
**sum_other_doc_count** | **int** | The number of complaints that were not included in this aggregation. | [optional] 

## Example

```python
from openapi_client.models.multi_level_aggregation_field import MultiLevelAggregationField

# TODO update the JSON string below
json = "{}"
# create an instance of MultiLevelAggregationField from a JSON string
multi_level_aggregation_field_instance = MultiLevelAggregationField.from_json(json)
# print the JSON string representation of the object
print(MultiLevelAggregationField.to_json())

# convert the object into a dict
multi_level_aggregation_field_dict = multi_level_aggregation_field_instance.to_dict()
# create an instance of MultiLevelAggregationField from a dict
multi_level_aggregation_field_from_dict = MultiLevelAggregationField.from_dict(multi_level_aggregation_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


