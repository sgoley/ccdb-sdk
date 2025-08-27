# Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_points** | **object** | Contains key value pairs of page and arrays. Used to paginate elasticsearch results in list view | [optional] 
**has_data_issue** | **bool** | Indicates there has been an issue with the most recent data load | [optional] 
**is_data_stale** | **bool** | Indicates the most recent data is over 5 business days old | [optional] 
**is_narrative_stale** | **bool** | Indicates the most recent narratives are over 5 business days old | [optional] 
**last_indexed** | **str** | The timestamp of the most recently indexed complaint | [optional] 
**last_updated** | **str** | The timestamp of the most recent complaint | [optional] 
**license** | **str** | The open source license under which the API operates | [optional] 
**total_record_count** | **int** | The total number of complaints currently indexed | [optional] 

## Example

```python
from openapi_client.models.meta import Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Meta from a JSON string
meta_instance = Meta.from_json(json)
# print the JSON string representation of the object
print(Meta.to_json())

# convert the object into a dict
meta_dict = meta_instance.to_dict()
# create an instance of Meta from a dict
meta_from_dict = Meta.from_dict(meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


