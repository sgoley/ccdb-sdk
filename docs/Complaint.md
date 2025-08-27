# Complaint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** | The complaint is about this company | [optional] 
**company_public_response** | **str** | The company&#39;s optional, public-facing response to a consumer&#39;s complaint | [optional] 
**company_response** | **str** | The response from the company about this complaint | [optional] 
**complaint_id** | **int** | The unique identification number for a complaint | [optional] 
**complaint_what_happened** | **str** | A description of the complaint provided by the consumer | [optional] 
**consumer_consent_provided** | **str** | Identifies whether the consumer opted in to publish their complaint narrative | [optional] 
**consumer_disputed** | **str** | Whether the consumer disputed the company&#39;s response | [optional] 
**date_received** | **date** | The date the CFPB received the complaint | [optional] 
**date_sent_to_company** | **str** | The date the CFPB sent the complaint to the company | [optional] 
**has_narrative** | **bool** | Indicates this complaint has a narrative | [optional] 
**issue** | **str** | The issue the consumer identified in the complaint | [optional] 
**product** | **str** | The type of product the consumer identified in the complaint | [optional] 
**state** | **str** | The state of the mailing address provided by the consumer | [optional] 
**sub_issue** | **str** | The sub-issue the consumer identified in the complaint | [optional] 
**sub_product** | **str** | The type of sub-product the consumer identified in the complaint | [optional] 
**submitted_via** | **str** | How the complaint was submitted to the CFPB | [optional] 
**tags** | **str** | Data that supports easier searching and sorting of complaints | [optional] 
**timely** | **str** | Indicates whether the company gave a timely response or not | [optional] 
**zip_code** | **str** | The mailing ZIP code provided by the consumer | [optional] 

## Example

```python
from openapi_client.models.complaint import Complaint

# TODO update the JSON string below
json = "{}"
# create an instance of Complaint from a JSON string
complaint_instance = Complaint.from_json(json)
# print the JSON string representation of the object
print(Complaint.to_json())

# convert the object into a dict
complaint_dict = complaint_instance.to_dict()
# create an instance of Complaint from a dict
complaint_from_dict = Complaint.from_dict(complaint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


