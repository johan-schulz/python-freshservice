import pytest
import responses

from freshservice.v2.api import API
from freshservice.v2.errors import (
    FreshserviceBadRequest,
    FreshserviceAccessDenied,
    FreshserviceNotFound,
    FreshserviceError,
    FreshserviceRateLimited,
    FreshserviceServerError,
)
from freshservice.v2.tests.conftest import DOMAIN


def test_custom_cname():
    with pytest.raises(AttributeError):
        API("custom_cname_domain", "invalid_api_key")


def test_api_prefix():
    api = API("test_domain.freshservice.com", "test_key")
    assert api._api_prefix == "https://test_domain.freshservice.com/api/v2/"
    api = API("test_domain.freshservice.com/", "test_key")
    assert api._api_prefix == "https://test_domain.freshservice.com/api/v2/"


@responses.activate
@pytest.mark.parametrize(
    ("status_code", "exception"),
    [
        (400, FreshserviceBadRequest),
        (403, FreshserviceAccessDenied),
        (404, FreshserviceNotFound),
        (418, FreshserviceError),
        (429, FreshserviceRateLimited),
        (502, FreshserviceServerError),
    ],
)
def test_errors(status_code, exception):
    responses.add(responses.GET, "https://{}/api/v2/tickets/1".format(DOMAIN), status=status_code)

    api = API("pythonfreshservice.freshservice.com", "test_key")
    with pytest.raises(exception):
        api.tickets.get_ticket(1)
