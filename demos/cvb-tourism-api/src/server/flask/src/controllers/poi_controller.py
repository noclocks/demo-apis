import connexion
import six

from swagger_server.models.point_of_interest import PointOfInterest  # noqa: E501
from swagger_server import util


def list_pois(category=None):  # noqa: E501
    """List all points of interest

     # noqa: E501

    :param category: Filter by category of interest
    :type category: str

    :rtype: List[PointOfInterest]
    """
    return 'do some magic!'
