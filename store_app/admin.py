from django.contrib import admin
from .models import Store, StoreType


@admin.register(StoreType)
class StoreTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]


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
    search_fields = ["user__username", "name"]
    list_per_page = 20
    list_select_related = ["user", "type"]
