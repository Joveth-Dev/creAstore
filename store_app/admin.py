from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http.request import HttpRequest
from .models import Store, StoreType


@admin.register(StoreType)
class StoreTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "store_count", "created_at"]
    list_filter = ["created_at"]
    ordering = ["-created_at"]
    search_fields = ["name"]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return (
            super()
            .get_queryset(request)
            .prefetch_related("store_set")
            .annotate(store_count=Count("store"))
        )

    @admin.display(ordering="store_count", description="Stores with this type")
    def store_count(self, instance: StoreType):
        return instance.store_count


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "user",
        "type",
        "address",
        "contact_number",
        "open_from",
        "open_to",
        "created_at",
    ]
    list_filter = ["open_to", "open_from", "created_at", "type", "user"]
    list_per_page = 20
    list_select_related = ["user", "type"]
    ordering = ["-created_at"]
    search_fields = ["user__username", "name", "description"]
