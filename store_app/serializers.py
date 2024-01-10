from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        user_id = self.context["user_id"]
        return Store.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = Store
        fields = [
            "id",
            "name",
            "user_id",
            "type",
            "description",
            "address",
            "contact_number",
            "open_from",
            "open_to",
        ]
