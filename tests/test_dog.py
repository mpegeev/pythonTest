"""https://dog.ceo/dog-api/ tests"""
import pytest
import requests
from jsonschema import validate


def endpoint_url(breed, count=""):
    return f"https://dog.ceo/api/breed/{breed}/images/random/{count}"


@pytest.mark.parametrize("breed", ["pug", "ovcharka"])
def test_breeds_random_status_code(breed):
    response = requests.get(endpoint_url(breed))
    assert response.ok


@pytest.mark.parametrize("breed", ["pug", "ovcharka"])
def test_breeds_random_content_type(breed):
    response = requests.get(endpoint_url(breed))
    assert response.headers["content-type"].startswith("application/json")


@pytest.mark.parametrize("breed", ["pug", "ovcharka"])
def test_breeds_random_schema(breed):
    response = requests.get(endpoint_url(breed, 3))
    response_schema = {
        "type": "object",
        "properties": {"message": {"type": "array"}, "status": {"type": "string"}},
    }
    validate(response.json(), response_schema)


@pytest.mark.parametrize("breed", ["pug", "ovcharka"])
def test_breeds_random_https_image(breed):
    response = requests.get(endpoint_url(breed, 3))
    images = response.json()["message"]

    assert len(list(filter(lambda img: img.startswith("https://"), images))) == len(
        images
    )


@pytest.mark.parametrize("breed", ["pug", "ovcharka"])
@pytest.mark.parametrize("count", [3, 2])
def test_breeds_random_count(breed, count):
    response = requests.get(endpoint_url(breed, count))
    assert len(response.json()["message"]) == count
