# openapi_client.TypeaheadApi

All URIs are relative to *https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suggest_company_get**](TypeaheadApi.md#suggest_company_get) | **GET** /_suggest_company | Suggest possible companies
[**suggest_get**](TypeaheadApi.md#suggest_get) | **GET** /_suggest | Suggest possible searches
[**suggest_zip_get**](TypeaheadApi.md#suggest_zip_get) | **GET** /_suggest_zip | Suggest possible zip codes


# **suggest_company_get**
> List[str] suggest_company_get(text, size=size, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, has_narrative=has_narrative, issue=issue, product=product, state=state, submitted_via=submitted_via, tags=tags, timely=timely, zip_code=zip_code)

Suggest possible companies

Provide a list of companies that match the input text

### Example


```python
import openapi_client
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
    api_instance = openapi_client.TypeaheadApi(api_client)
    text = 'text_example' # str | text to use for suggestions
    size = 10 # int | Limit the size of the results (optional) (default to 10)
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
        # Suggest possible companies
        api_response = api_instance.suggest_company_get(text, size=size, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, has_narrative=has_narrative, issue=issue, product=product, state=state, submitted_via=submitted_via, tags=tags, timely=timely, zip_code=zip_code)
        print("The response of TypeaheadApi->suggest_company_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypeaheadApi->suggest_company_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| text to use for suggestions | 
 **size** | **int**| Limit the size of the results | [optional] [default to 10]
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

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest_get**
> List[str] suggest_get(text, size=size)

Suggest possible searches

The endpoint for the main search box in the UI

### Example


```python
import openapi_client
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
    api_instance = openapi_client.TypeaheadApi(api_client)
    text = 'text_example' # str | text to use for suggestions
    size = 10 # int | Limit the size of the results (optional) (default to 10)

    try:
        # Suggest possible searches
        api_response = api_instance.suggest_get(text, size=size)
        print("The response of TypeaheadApi->suggest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypeaheadApi->suggest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| text to use for suggestions | 
 **size** | **int**| Limit the size of the results | [optional] [default to 10]

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest_zip_get**
> List[str] suggest_zip_get(text, size=size, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, has_narrative=has_narrative, issue=issue, product=product, state=state, submitted_via=submitted_via, tags=tags, timely=timely, zip_code=zip_code)

Suggest possible zip codes

Provide a list of zip codes that match the input text

### Example


```python
import openapi_client
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
    api_instance = openapi_client.TypeaheadApi(api_client)
    text = 'text_example' # str | text to use for suggestions
    size = 10 # int | Limit the size of the results (optional) (default to 10)
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
        # Suggest possible zip codes
        api_response = api_instance.suggest_zip_get(text, size=size, company_public_response=company_public_response, company_received_max=company_received_max, company_received_min=company_received_min, company_response=company_response, consumer_consent_provided=consumer_consent_provided, consumer_disputed=consumer_disputed, date_received_max=date_received_max, date_received_min=date_received_min, has_narrative=has_narrative, issue=issue, product=product, state=state, submitted_via=submitted_via, tags=tags, timely=timely, zip_code=zip_code)
        print("The response of TypeaheadApi->suggest_zip_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypeaheadApi->suggest_zip_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| text to use for suggestions | 
 **size** | **int**| Limit the size of the results | [optional] [default to 10]
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

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

