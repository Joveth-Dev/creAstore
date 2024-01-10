import pytest
from django.contrib.auth import get_user_model
from model_bakery import baker
from rest_framework import status
from store_app.models import Store, StoreType


User = get_user_model()


@pytest.mark.django_db
class TestListStore:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.get("/store_app/store/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_authenticated_returns_200(self, authenticate, api_client):
        authenticate()

        response = api_client.get("/store_app/store/")

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestRetrieveStore:
    def test_if_store_exists_returns_200(self, authenticate, api_client):
        authenticate()
        store = baker.make(Store)
        response = api_client.get(f"/store_app/store/{store.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": store.id,
            "name": store.name,
            "user_id": store.user_id,
            "type": store.type.id,
            "description": store.description,
            "address": store.address,
            "contact_number": store.contact_number,
            "open_from": store.open_from,
            "open_to": store.open_to,
        }

    def test_if_store_does_not_exists_returns_404(self, authenticate, api_client):
        authenticate()
        response = api_client.get("/store_app/store/0/")

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestCreateStore:
    def test_if_user_is_authenticated_returns_201(self, authenticate, api_client):
        user = baker.make(User)
        store_type = baker.make(StoreType)
        authenticate(user=user)
        response = api_client.post(
            "/store_app/store/",
            {
                "name": "Test store 5",
                "user_id": user.id,
                "type": store_type.id,
                "description": "+",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0


@pytest.mark.django_db
class TestUpdateStore:
    def test_if_user_is_authenticated_returns_200(self, authenticate, api_client):
        user = baker.make(User)
        authenticate(user=user)
        store = baker.make(Store, user=user)
        response = api_client.put(
            f"/store_app/store/{store.id}/",
            {
                "id": store.id,
                "name": store.name,
                "user_id": store.user.id,
                "type": store.type.id,
                "description": "+",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": store.id,
            "name": store.name,
            "user_id": store.user.id,
            "type": store.type.id,
            "description": "+",
            "address": None,
            "contact_number": None,
            "open_from": None,
            "open_to": None,
        }
