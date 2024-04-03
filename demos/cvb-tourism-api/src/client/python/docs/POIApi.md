# swagger_client.POIApi

All URIs are relative to *https://virtserver.swaggerhub.com/noclocks/CVBTouismAPI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_pois**](POIApi.md#list_pois) | **GET** /points-of-interest | List all points of interest

# **list_pois**
> list[PointOfInterest] list_pois(category=category)

List all points of interest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.POIApi()
category = 'category_example' # str | Filter by category of interest (optional)

try:
    # List all points of interest
    api_response = api_instance.list_pois(category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POIApi->list_pois: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by category of interest | [optional] 

### Return type

[**list[PointOfInterest]**](PointOfInterest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

