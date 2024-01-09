from django.contrib import admin
from .models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name"]
    search_fields = ["user__username", "name"]
