import pytest

from django.urls import reverse
from ..django_assertions import assertion_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('base:home'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assertion_contains(resp, '<title> Python Pro </title>')


def test_link(resp):
    assertion_contains(resp, f'href="{reverse("base:home")}"> Python Pro </a>')
