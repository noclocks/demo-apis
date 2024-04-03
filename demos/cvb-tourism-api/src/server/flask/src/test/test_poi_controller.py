# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.point_of_interest import PointOfInterest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPOIController(BaseTestCase):
    """POIController integration test stubs"""

    def test_list_pois(self):
        """Test case for list_pois

        List all points of interest
        """
        query_string = [('category', 'category_example')]
        response = self.client.open(
            '/noclocks/CVBTouismAPI/1.0.0/points-of-interest',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
