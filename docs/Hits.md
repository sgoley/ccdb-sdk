# Hits

A set of complaints that matched the query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | [**List[Hit]**](Hit.md) |  | [optional] 
**max_score** | **float** | The highest score in the results | [optional] 
**total** | [**HitsTotal**](HitsTotal.md) |  | [optional] 

## Example

```python
from openapi_client.models.hits import Hits

# TODO update the JSON string below
json = "{}"
# create an instance of Hits from a JSON string
hits_instance = Hits.from_json(json)
# print the JSON string representation of the object
print(Hits.to_json())

# convert the object into a dict
hits_dict = hits_instance.to_dict()
# create an instance of Hits from a dict
hits_from_dict = Hits.from_dict(hits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


