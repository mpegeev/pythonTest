"""https://api.openbrewerydb.org/ tests"""
import pytest
import requests
from jsonschema import validate


def endpoint_url(query_string="", value=""):
    uri = "https://api.openbrewerydb.org/breweries"
    if query_string and value:
        uri += f"?{query_string}={value}"
    return uri


def test_brewery_status_code():
    response = requests.get(endpoint_url())
    assert response.ok


def test_brewery_content_type():
    response = requests.get(endpoint_url())
    assert response.headers["content-type"].startswith("application/json")


def test_brewery_schema():
    response = requests.get(endpoint_url())
    response_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
            },
            "required": ["id", "name", "brewery_type"],
        },
    }
    validate(response.json(), response_schema)


@pytest.mark.parametrize(
    "brewery_type",
    [
        "micro",
        "nano",
        "regional",
        "brewpub",
        "large",
        "planning",
        "bar",
        "contract",
        "proprieter",
        "closed",
    ],
)
def test_brewery_types(brewery_type):
    response = requests.get(endpoint_url("by_type", brewery_type))
    breweries = response.json()
    assert len(breweries) == 0 or all(
        map(lambda brewery: brewery["brewery_type"] == brewery_type, breweries)
    )


@pytest.mark.parametrize("per_page", [1, 2, 5, 10, 20])
def test_brewery_page_size(per_page):
    response = requests.get(endpoint_url("per_page", per_page))
    assert len(response.json()) == per_page
