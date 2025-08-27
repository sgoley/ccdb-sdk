# openapi_client.ComplaintsApi

All URIs are relative to *https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complaint_id_get**](ComplaintsApi.md#complaint_id_get) | **GET** /{complaintId} | Find consumer complaint by ID
[**geo_states_get**](ComplaintsApi.md#geo_states_get) | **GET** /geo/states | Get the state-by-state information
[**root_get**](ComplaintsApi.md#root_get) | **GET** / | Search consumer complaints


# **complaint_id_get**
> Complaint complaint_id_get(complaint_id)

Find consumer complaint by ID

Get complaint details for a specific ID

### Example


```python
import openapi_client
from openapi_client.models.complaint import Complaint
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ComplaintsApi(api_client)
    complaint_id = 56 # int | ID of the complaint

    try:
        # Find consumer complaint by ID
        api_response = api_instance.complaint_id_get(complaint_id)
        print("The response of ComplaintsApi->complaint_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplaintsApi->complaint_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complaint_id** | **int**| ID of the complaint | 

### Return type

[**Complaint**](Complaint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**404** | Complaint not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_states_get**
> StatesResult geo_states_get(search_term=search_term, var_field=var_field, company=company, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, has_narrative=has_narrative, issue=issue, product=product, state=state, submitted_via=submitted_via, tags=tags, timely=timely, zip_code=zip_code)

Get the state-by-state information

Get complaint information broken down by states

### Example


```python
import openapi_client
from openapi_client.models.states_result import StatesResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ComplaintsApi(api_client)
    search_term = 'search_term_example' # str | Return results containing specific term (optional)
    var_field = complaint_what_happened # str | If the parameter \"search_term\" has a value, use \"field\" to specify which field is searched. If not specified, \"complaint_what_happened\" will be searched. (optional) (default to complaint_what_happened)
    company = ['company_example'] # List[str] | Filter the results to only return these companies (optional)
    company_public_response = ['company_public_response_example'] # List[str] | Filter the results to only return these types of public response by the company (optional)
    company_received_max = '2013-10-20' # date | Return results with date < company_received_max (i.e. 2017-03-04) (optional)
    company_received_min = '2013-10-20' # date | Return results with date >= company_received_min (i.e. 2017-03-04) (optional)
    company_response = ['company_response_example'] # List[str] | Filter the results to only return these types of response by the company (optional)
    consumer_consent_provided = ['consumer_consent_provided_example'] # List[str] | Filter the results to only return these types of consent consumer provided (optional)
    consumer_disputed = ['consumer_disputed_example'] # List[str] | Filter the results to only return the specified state of consumer disputed, i.e. yes, no (optional)
    date_received_max = '2013-10-20' # date | Return results with date < date_received_max (i.e. 2017-03-04) (optional)
    date_received_min = '2013-10-20' # date | Return results with date >= date_received_min (i.e. 2017-03-04) (optional)
    has_narrative = ['has_narrative_example'] # List[str] | Filter the results to only return the specified state of whether it has narrative in the complaint or not, i.e. yes, no (optional)
    issue = ['issue_example'] # List[str] | Filter the results to only return these types of issue and subissue, i.e. product-only: Getting a Loan, subproduct needs to include product, separated by '•', Getting a Loan•Can't qualify for a loan (optional)
    product = ['product_example'] # List[str] | Filter the results to only return these types of product and subproduct, i.e. product-only: Mortgage, subproduct needs to include product, separated by '•', Mortgage•FHA mortgage (optional)
    state = ['state_example'] # List[str] | Filter the results to only return these states (use abbreviation, i.e. CA, VA) (optional)
    submitted_via = ['submitted_via_example'] # List[str] | Filter the results to only return these types of way consumers submitted their complaints (optional)
    tags = ['tags_example'] # List[str] | Filter the results to only return these types of tag (optional)
    timely = ['timely_example'] # List[str] | Filter the results to show whether a response was timely (optional)
    zip_code = ['zip_code_example'] # List[str] | Filter the results to only return these zip codes (optional)

    try:
        # Get the state-by-state information
        api_response = api_instance.geo_states_get(search_term=search_term, var_field=var_field, company=company, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, has_narrative=has_narrative, issue=issue, product=product, state=state, submitted_via=submitted_via, tags=tags, timely=timely, zip_code=zip_code)
        print("The response of ComplaintsApi->geo_states_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplaintsApi->geo_states_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Return results containing specific term | [optional] 
 **var_field** | **str**| If the parameter \&quot;search_term\&quot; has a value, use \&quot;field\&quot; to specify which field is searched. If not specified, \&quot;complaint_what_happened\&quot; will be searched. | [optional] [default to complaint_what_happened]
 **company** | [**List[str]**](str.md)| Filter the results to only return these companies | [optional] 
 **company_public_response** | [**List[str]**](str.md)| Filter the results to only return these types of public response by the company | [optional] 
 **company_received_max** | **date**| Return results with date &lt; company_received_max (i.e. 2017-03-04) | [optional] 
 **company_received_min** | **date**| Return results with date &gt;&#x3D; company_received_min (i.e. 2017-03-04) | [optional] 
 **company_response** | [**List[str]**](str.md)| Filter the results to only return these types of response by the company | [optional] 
 **consumer_consent_provided** | [**List[str]**](str.md)| Filter the results to only return these types of consent consumer provided | [optional] 
 **consumer_disputed** | [**List[str]**](str.md)| Filter the results to only return the specified state of consumer disputed, i.e. yes, no | [optional] 
 **date_received_max** | **date**| Return results with date &lt; date_received_max (i.e. 2017-03-04) | [optional] 
 **date_received_min** | **date**| Return results with date &gt;&#x3D; date_received_min (i.e. 2017-03-04) | [optional] 
 **has_narrative** | [**List[str]**](str.md)| Filter the results to only return the specified state of whether it has narrative in the complaint or not, i.e. yes, no | [optional] 
 **issue** | [**List[str]**](str.md)| Filter the results to only return these types of issue and subissue, i.e. product-only: Getting a Loan, subproduct needs to include product, separated by &#39;•&#39;, Getting a Loan•Can&#39;t qualify for a loan | [optional] 
 **product** | [**List[str]**](str.md)| Filter the results to only return these types of product and subproduct, i.e. product-only: Mortgage, subproduct needs to include product, separated by &#39;•&#39;, Mortgage•FHA mortgage | [optional] 
 **state** | [**List[str]**](str.md)| Filter the results to only return these states (use abbreviation, i.e. CA, VA) | [optional] 
 **submitted_via** | [**List[str]**](str.md)| Filter the results to only return these types of way consumers submitted their complaints | [optional] 
 **tags** | [**List[str]**](str.md)| Filter the results to only return these types of tag | [optional] 
 **timely** | [**List[str]**](str.md)| Filter the results to show whether a response was timely | [optional] 
 **zip_code** | [**List[str]**](str.md)| Filter the results to only return these zip codes | [optional] 

### Return type

[**StatesResult**](StatesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> SearchResult root_get(search_term=search_term, var_field=var_field, frm=frm, size=size, sort=sort, format=format, no_aggs=no_aggs, no_highlight=no_highlight, company=company, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, has_narrative=has_narrative, issue=issue, product=product, search_after=search_after, state=state, submitted_via=submitted_via, tags=tags, timely=timely, zip_code=zip_code)

Search consumer complaints

Search the contents of the consumer complaint database

### Example


```python
import openapi_client
from openapi_client.models.search_result import SearchResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ComplaintsApi(api_client)
    search_term = 'search_term_example' # str | Return results containing specific term (optional)
    var_field = complaint_what_happened # str | If the parameter \"search_term\" has a value, use \"field\" to specify which field is searched. If not specified, \"complaint_what_happened\" will be searched. (optional) (default to complaint_what_happened)
    frm = 0 # int | Return results starting from a specific index, only if format parameter is not specified, ignore otherwise (optional) (default to 0)
    size = 10 # int | Limit the size of the results (optional) (default to 10)
    sort = relevance_desc # str | Return results sort in a particular order (optional) (default to relevance_desc)
    format = json # str | Format to be returned, if this parameter is not specified, frm/size parameters can be used properly, but if a format is specified for exporting, frm/size will be ignored (optional) (default to json)
    no_aggs = False # bool | Include aggregations in result or not, True means no aggregations will be included, False means aggregations will be included. (optional) (default to False)
    no_highlight = False # bool | Include highlight of search term in result or not, True means no highlighting will be included, False means highlighting will be included. (optional) (default to False)
    company = ['company_example'] # List[str] | Filter the results to only return these companies (optional)
    company_public_response = ['company_public_response_example'] # List[str] | Filter the results to only return these types of public response by the company (optional)
    company_received_max = '2013-10-20' # date | Return results with date < company_received_max (i.e. 2017-03-04) (optional)
    company_received_min = '2013-10-20' # date | Return results with date >= company_received_min (i.e. 2017-03-04) (optional)
    company_response = ['company_response_example'] # List[str] | Filter the results to only return these types of response by the company (optional)
    consumer_consent_provided = ['consumer_consent_provided_example'] # List[str] | Filter the results to only return these types of consent consumer provided (optional)
    consumer_disputed = ['consumer_disputed_example'] # List[str] | Filter the results to only return the specified state of consumer disputed, i.e. yes, no (optional)
    date_received_max = '2013-10-20' # date | Return results with date < date_received_max (i.e. 2017-03-04) (optional)
    date_received_min = '2013-10-20' # date | Return results with date >= date_received_min (i.e. 2017-03-04) (optional)
    has_narrative = ['has_narrative_example'] # List[str] | Filter the results to only return the specified state of whether it has narrative in the complaint or not, i.e. yes, no (optional)
    issue = ['issue_example'] # List[str] | Filter the results to only return these types of issue and subissue, i.e. product-only: Getting a Loan, subproduct needs to include product, separated by '•', Getting a Loan•Can't qualify for a loan (optional)
    product = ['product_example'] # List[str] | Filter the results to only return these types of product and subproduct, i.e. product-only: Mortgage, subproduct needs to include product, separated by '•', Mortgage•FHA mortgage (optional)
    search_after = 'search_after_example' # str | Used in conjunction with frm parameter to paginate results. This value is calculated by combining the values from the break_points object in the _meta key from the api response. For instance to paginate to the nth page, use the value from the break_points n:[k, id] to pass to the API the value page=n&frm=25&search_after=k_id Please see https://github.com/cfpb/cfpb.github.io/issues/292 for more detailed examples (optional)
    state = ['state_example'] # List[str] | Filter the results to only return these states (use abbreviation, i.e. CA, VA) (optional)
    submitted_via = ['submitted_via_example'] # List[str] | Filter the results to only return these types of way consumers submitted their complaints (optional)
    tags = ['tags_example'] # List[str] | Filter the results to only return these types of tag (optional)
    timely = ['timely_example'] # List[str] | Filter the results to show whether a response was timely (optional)
    zip_code = ['zip_code_example'] # List[str] | Filter the results to only return these zip codes (optional)

    try:
        # Search consumer complaints
        api_response = api_instance.root_get(search_term=search_term, var_field=var_field, frm=frm, size=size, sort=sort, format=format, no_aggs=no_aggs, no_highlight=no_highlight, company=company, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, has_narrative=has_narrative, issue=issue, product=product, search_after=search_after, state=state, submitted_via=submitted_via, tags=tags, timely=timely, zip_code=zip_code)
        print("The response of ComplaintsApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplaintsApi->root_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Return results containing specific term | [optional] 
 **var_field** | **str**| If the parameter \&quot;search_term\&quot; has a value, use \&quot;field\&quot; to specify which field is searched. If not specified, \&quot;complaint_what_happened\&quot; will be searched. | [optional] [default to complaint_what_happened]
 **frm** | **int**| Return results starting from a specific index, only if format parameter is not specified, ignore otherwise | [optional] [default to 0]
 **size** | **int**| Limit the size of the results | [optional] [default to 10]
 **sort** | **str**| Return results sort in a particular order | [optional] [default to relevance_desc]
 **format** | **str**| Format to be returned, if this parameter is not specified, frm/size parameters can be used properly, but if a format is specified for exporting, frm/size will be ignored | [optional] [default to json]
 **no_aggs** | **bool**| Include aggregations in result or not, True means no aggregations will be included, False means aggregations will be included. | [optional] [default to False]
 **no_highlight** | **bool**| Include highlight of search term in result or not, True means no highlighting will be included, False means highlighting will be included. | [optional] [default to False]
 **company** | [**List[str]**](str.md)| Filter the results to only return these companies | [optional] 
 **company_public_response** | [**List[str]**](str.md)| Filter the results to only return these types of public response by the company | [optional] 
 **company_received_max** | **date**| Return results with date &lt; company_received_max (i.e. 2017-03-04) | [optional] 
 **company_received_min** | **date**| Return results with date &gt;&#x3D; company_received_min (i.e. 2017-03-04) | [optional] 
 **company_response** | [**List[str]**](str.md)| Filter the results to only return these types of response by the company | [optional] 
 **consumer_consent_provided** | [**List[str]**](str.md)| Filter the results to only return these types of consent consumer provided | [optional] 
 **consumer_disputed** | [**List[str]**](str.md)| Filter the results to only return the specified state of consumer disputed, i.e. yes, no | [optional] 
 **date_received_max** | **date**| Return results with date &lt; date_received_max (i.e. 2017-03-04) | [optional] 
 **date_received_min** | **date**| Return results with date &gt;&#x3D; date_received_min (i.e. 2017-03-04) | [optional] 
 **has_narrative** | [**List[str]**](str.md)| Filter the results to only return the specified state of whether it has narrative in the complaint or not, i.e. yes, no | [optional] 
 **issue** | [**List[str]**](str.md)| Filter the results to only return these types of issue and subissue, i.e. product-only: Getting a Loan, subproduct needs to include product, separated by &#39;•&#39;, Getting a Loan•Can&#39;t qualify for a loan | [optional] 
 **product** | [**List[str]**](str.md)| Filter the results to only return these types of product and subproduct, i.e. product-only: Mortgage, subproduct needs to include product, separated by &#39;•&#39;, Mortgage•FHA mortgage | [optional] 
 **search_after** | **str**| Used in conjunction with frm parameter to paginate results. This value is calculated by combining the values from the break_points object in the _meta key from the api response. For instance to paginate to the nth page, use the value from the break_points n:[k, id] to pass to the API the value page&#x3D;n&amp;frm&#x3D;25&amp;search_after&#x3D;k_id Please see https://github.com/cfpb/cfpb.github.io/issues/292 for more detailed examples | [optional] 
 **state** | [**List[str]**](str.md)| Filter the results to only return these states (use abbreviation, i.e. CA, VA) | [optional] 
 **submitted_via** | [**List[str]**](str.md)| Filter the results to only return these types of way consumers submitted their complaints | [optional] 
 **tags** | [**List[str]**](str.md)| Filter the results to only return these types of tag | [optional] 
 **timely** | [**List[str]**](str.md)| Filter the results to show whether a response was timely | [optional] 
 **zip_code** | [**List[str]**](str.md)| Filter the results to only return these zip codes | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

