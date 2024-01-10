from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Store
from .permissions import IsOwnerOrReadOnly, IsSuperUser
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["user", "type"]
    ordering_fields = ["name", "type__name"]
    search_fields = ["name", "type__name", "description"]
    serializer_class = StoreSerializer
    queryset = Store.objects.select_related("user", "type")

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action in ("retrieve", "update", "partial_update", "delete"):
            permission_classes += [IsOwnerOrReadOnly | IsSuperUser]
        elif self.action == "list":
            if not self.request.user.is_superuser:
                self.queryset = self.queryset.filter(user=self.request.user.id)
        return [permission() for permission in permission_classes]
