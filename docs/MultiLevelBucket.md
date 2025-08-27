# MultiLevelBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_count** | **int** | The number of complaints that match this key | [optional] 
**field_raw** | [**MultiLevelBucketFieldRaw**](MultiLevelBucketFieldRaw.md) |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.multi_level_bucket import MultiLevelBucket

# TODO update the JSON string below
json = "{}"
# create an instance of MultiLevelBucket from a JSON string
multi_level_bucket_instance = MultiLevelBucket.from_json(json)
# print the JSON string representation of the object
print(MultiLevelBucket.to_json())

# convert the object into a dict
multi_level_bucket_dict = multi_level_bucket_instance.to_dict()
# create an instance of MultiLevelBucket from a dict
multi_level_bucket_from_dict = MultiLevelBucket.from_dict(multi_level_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


