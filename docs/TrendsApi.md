# openapi_client.TrendsApi

All URIs are relative to *https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trends_get**](TrendsApi.md#trends_get) | **GET** /trends | List trends


# **trends_get**
> TrendsResult trends_get(lens, trend_interval, search_term=search_term, var_field=var_field, company=company, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, focus=focus, has_narrative=has_narrative, issue=issue, product=product, state=state, submitted_via=submitted_via, sub_lens=sub_lens, sub_lens_depth=sub_lens_depth, tags=tags, timely=timely, trend_depth=trend_depth, zip_code=zip_code)

List trends

Return specific aggregations for a search

### Example


```python
import openapi_client
from openapi_client.models.trends_result import TrendsResult
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
    api_instance = openapi_client.TrendsApi(api_client)
    lens = overview # str | The data lens through which to view complaint trends over time. (default to overview)
    trend_interval = 'trend_interval_example' # str | The interval of time to use for trends aggregations histograms. When using day intervals, we recommend querying for date_received_min / max periods of less than one year.
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
    focus = ['focus_example'] # List[str] | The name of the product or company on which to focus charts for products and issues (optional)
    has_narrative = ['has_narrative_example'] # List[str] | Filter the results to only return the specified state of whether it has narrative in the complaint or not, i.e. yes, no (optional)
    issue = ['issue_example'] # List[str] | Filter the results to only return these types of issue and subissue, i.e. product-only: Getting a Loan, subproduct needs to include product, separated by '•', Getting a Loan•Can't qualify for a loan (optional)
    product = ['product_example'] # List[str] | Filter the results to only return these types of product and subproduct, i.e. product-only: Mortgage, subproduct needs to include product, separated by '•', Mortgage•FHA mortgage (optional)
    state = ['state_example'] # List[str] | Filter the results to only return these states (use abbreviation, i.e. CA, VA) (optional)
    submitted_via = ['submitted_via_example'] # List[str] | Filter the results to only return these types of way consumers submitted their complaints (optional)
    sub_lens = 'sub_lens_example' # str | The sub-lens through which to view complaint trends over time. (optional)
    sub_lens_depth = 10 # int | The top X trend sub aggregations will be returned, where X is the supplied sub_lens_depth. (optional) (default to 10)
    tags = ['tags_example'] # List[str] | Filter the results to only return these types of tag (optional)
    timely = ['timely_example'] # List[str] | Filter the results to show whether a response was timely (optional)
    trend_depth = 10 # int | The top X trend aggregations will be returned, where X is the supplied trend_depth. (optional) (default to 10)
    zip_code = ['zip_code_example'] # List[str] | Filter the results to only return these zip codes (optional)

    try:
        # List trends
        api_response = api_instance.trends_get(lens, trend_interval, search_term=search_term, var_field=var_field, company=company, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, focus=focus, has_narrative=has_narrative, issue=issue, product=product, state=state, submitted_via=submitted_via, sub_lens=sub_lens, sub_lens_depth=sub_lens_depth, tags=tags, timely=timely, trend_depth=trend_depth, zip_code=zip_code)
        print("The response of TrendsApi->trends_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrendsApi->trends_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lens** | **str**| The data lens through which to view complaint trends over time. | [default to overview]
 **trend_interval** | **str**| The interval of time to use for trends aggregations histograms. When using day intervals, we recommend querying for date_received_min / max periods of less than one year. | 
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
 **focus** | [**List[str]**](str.md)| The name of the product or company on which to focus charts for products and issues | [optional] 
 **has_narrative** | [**List[str]**](str.md)| Filter the results to only return the specified state of whether it has narrative in the complaint or not, i.e. yes, no | [optional] 
 **issue** | [**List[str]**](str.md)| Filter the results to only return these types of issue and subissue, i.e. product-only: Getting a Loan, subproduct needs to include product, separated by &#39;•&#39;, Getting a Loan•Can&#39;t qualify for a loan | [optional] 
 **product** | [**List[str]**](str.md)| Filter the results to only return these types of product and subproduct, i.e. product-only: Mortgage, subproduct needs to include product, separated by &#39;•&#39;, Mortgage•FHA mortgage | [optional] 
 **state** | [**List[str]**](str.md)| Filter the results to only return these states (use abbreviation, i.e. CA, VA) | [optional] 
 **submitted_via** | [**List[str]**](str.md)| Filter the results to only return these types of way consumers submitted their complaints | [optional] 
 **sub_lens** | **str**| The sub-lens through which to view complaint trends over time. | [optional] 
 **sub_lens_depth** | **int**| The top X trend sub aggregations will be returned, where X is the supplied sub_lens_depth. | [optional] [default to 10]
 **tags** | [**List[str]**](str.md)| Filter the results to only return these types of tag | [optional] 
 **timely** | [**List[str]**](str.md)| Filter the results to show whether a response was timely | [optional] 
 **trend_depth** | **int**| The top X trend aggregations will be returned, where X is the supplied trend_depth. | [optional] [default to 10]
 **zip_code** | [**List[str]**](str.md)| Filter the results to only return these zip codes | [optional] 

### Return type

[**TrendsResult**](TrendsResult.md)

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

