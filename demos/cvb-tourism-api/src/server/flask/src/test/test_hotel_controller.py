# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.hotel import Hotel  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHotelController(BaseTestCase):
    """HotelController integration test stubs"""

    def test_list_hotels(self):
        """Test case for list_hotels

        List all hotels
        """
        query_string = [('stars', 5)]
        response = self.client.open(
            '/noclocks/CVBTouismAPI/1.0.0/hotels',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
