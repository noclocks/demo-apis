import connexion
import six

from swagger_server.models.hotel import Hotel  # noqa: E501
from swagger_server import util


def list_hotels(stars=None):  # noqa: E501
    """List all hotels

     # noqa: E501

    :param stars: Filter hotels by star rating
    :type stars: int

    :rtype: List[Hotel]
    """
    return 'do some magic!'
