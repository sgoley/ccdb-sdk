# SearchResultAggregations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_public_response** | [**Aggregation**](Aggregation.md) |  | [optional] 
**company_response** | [**Aggregation**](Aggregation.md) |  | [optional] 
**consumer_consent_provided** | [**Aggregation**](Aggregation.md) |  | [optional] 
**consumer_disputed** | [**Aggregation**](Aggregation.md) |  | [optional] 
**has_narrative** | [**Aggregation**](Aggregation.md) |  | [optional] 
**issue** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**product** | [**MultiLevelAggregation**](MultiLevelAggregation.md) |  | [optional] 
**state** | [**Aggregation**](Aggregation.md) |  | [optional] 
**submitted_via** | [**Aggregation**](Aggregation.md) |  | [optional] 
**tags** | [**Aggregation**](Aggregation.md) |  | [optional] 
**timely** | [**Aggregation**](Aggregation.md) |  | [optional] 
**zip_code** | [**Aggregation**](Aggregation.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_result_aggregations import SearchResultAggregations

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultAggregations from a JSON string
search_result_aggregations_instance = SearchResultAggregations.from_json(json)
# print the JSON string representation of the object
print(SearchResultAggregations.to_json())

# convert the object into a dict
search_result_aggregations_dict = search_result_aggregations_instance.to_dict()
# create an instance of SearchResultAggregations from a dict
search_result_aggregations_from_dict = SearchResultAggregations.from_dict(search_result_aggregations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


