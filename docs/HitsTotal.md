# HitsTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The count of matching hits, accurate in our code even above 10,000 hits | [optional] 
**relation** | **str** | Indicates the accuracy of the default ES response, whether the value is accurate (eq) or a lower bound (gte) | [optional] 

## Example

```python
from openapi_client.models.hits_total import HitsTotal

# TODO update the JSON string below
json = "{}"
# create an instance of HitsTotal from a JSON string
hits_total_instance = HitsTotal.from_json(json)
# print the JSON string representation of the object
print(HitsTotal.to_json())

# convert the object into a dict
hits_total_dict = hits_total_instance.to_dict()
# create an instance of HitsTotal from a dict
hits_total_from_dict = HitsTotal.from_dict(hits_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


