import pytest
from model_bakery import baker
from rest_framework import status
from core.models import User


@pytest.mark.django_db
class TestListUser:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.get("/auth/users/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_authenticated_returns_200(self, authenticate, api_client):
        authenticate()
        response = api_client.get("/auth/users/")

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestRetrieveUser:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.get("/auth/users/me/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_authenticated_returns_200(self, authenticate, api_client):
        authenticate()
        response = api_client.get("/auth/users/me/")

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestCreateUser:
    def test_if_user_is_anonymous_returns_201(self, api_client):
        response = api_client.post(
            "/auth/users/",
            {
                "email": "sampleuser@domain.com",
                "username": "sampleuser",
                "password": "_jsWq.Pra-8mZga",
                "first_name": "",
                "last_name": "",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == {
            "email": "sampleuser@domain.com",
            "username": "sampleuser",
            "first_name": "",
            "last_name": "",
        }


@pytest.mark.django_db
class TestUpdateUser:
    def test_if_user_is_authenticated_returns_200(self, authenticate, api_client):
        user = baker.make(User)
        authenticate(user=user)
        response = api_client.put(
            "/auth/users/me/",
            {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "first_name": "Test",
                "last_name": "User",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "first_name": "Test",
            "last_name": "User",
        }
