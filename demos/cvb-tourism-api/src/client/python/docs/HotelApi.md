# swagger_client.HotelApi

All URIs are relative to *https://virtserver.swaggerhub.com/noclocks/CVBTouismAPI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_hotels**](HotelApi.md#list_hotels) | **GET** /hotels | List all hotels

# **list_hotels**
> list[Hotel] list_hotels(stars=stars)

List all hotels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HotelApi()
stars = 56 # int | Filter hotels by star rating (optional)

try:
    # List all hotels
    api_response = api_instance.list_hotels(stars=stars)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HotelApi->list_hotels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stars** | **int**| Filter hotels by star rating | [optional] 

### Return type

[**list[Hotel]**](Hotel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

