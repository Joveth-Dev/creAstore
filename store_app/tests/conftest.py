from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
import pytest

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(user=None):
        if user:
            return api_client.force_authenticate(user=user)
        return api_client.force_authenticate(user=User())

    return do_authenticate
