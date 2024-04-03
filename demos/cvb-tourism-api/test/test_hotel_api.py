# coding: utf-8

"""
    CVB Tourism API

    API for accessing information about points of interest, hotels, restaurants, and landmarks.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.hotel_api import HotelApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHotelApi(unittest.TestCase):
    """HotelApi unit test stubs"""

    def setUp(self):
        self.api = HotelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_hotels(self):
        """Test case for list_hotels

        List all hotels  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
