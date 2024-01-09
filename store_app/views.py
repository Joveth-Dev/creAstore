from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Store
from .permissions import IsOwnerOrReadOnly, IsSuperUser
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.select_related("user")

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action in ("retrieve", "update", "partial_update", "delete"):
            permission_classes += [IsOwnerOrReadOnly | IsSuperUser]
        elif self.action == "list":
            if not self.request.user.is_superuser:
                # if not superuser filter list showing only their own stores
                self.queryset = super().get_queryset().filter(user=self.request.user.id)
        return [permission() for permission in permission_classes]
