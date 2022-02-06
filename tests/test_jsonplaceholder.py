"""https://jsonplaceholder.typicode.com/ tests"""
import pytest
import requests


def endpoint_url(user_id=""):
    return f"https://jsonplaceholder.typicode.com/users/{user_id}"


def test_jsp_users_get():
    response = requests.get(endpoint_url(1))
    assert response.ok


@pytest.mark.parametrize("name", ["Jonh Doe", "Ivan the Terrible", "D'Artagnan"])
def test_jsp_users_create(name):
    response = requests.post(endpoint_url(), {"name": name})
    user = response.json()
    assert user["name"] == name


@pytest.mark.parametrize(
    "user_id, name", [(1, "Jonh Doe"), (2, "Ivan the Terrible"), (3, "D'Artagnan")]
)
def test_jsp_users_update(user_id, name):
    response = requests.put(endpoint_url(user_id), {"name": name})
    user = response.json()
    assert user["id"] == user_id
    assert user["name"] == name


@pytest.mark.parametrize(
    "user_id, name", [(1, "Jonh Doe"), (2, "Ivan the Terrible"), (3, "D'Artagnan")]
)
def test_jsp_users_patch(user_id, name):
    response = requests.patch(endpoint_url(user_id), {"name": name})
    assert response.json()["name"] == name


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_jsp_users_delete(user_id):
    response = requests.delete(endpoint_url(user_id))
    assert response.ok
