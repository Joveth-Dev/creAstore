import pytest
from django.contrib.auth import get_user_model
from model_bakery import baker
from store_app.models import Store, StoreType

User = get_user_model()


@pytest.mark.django_db
class TestStoreTypeModel:
    def test_if__str__returns_store_type_name(self):
        store_type = baker.make(StoreType)

        assert store_type.__str__() == store_type.name


@pytest.mark.django_db
class TestStoreModel:
    def test_if__str__returns_store_name(self):
        user = baker.make(User)
        store = baker.make(Store, user=user)

        assert store.__str__() == store.name
