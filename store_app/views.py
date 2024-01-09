from rest_framework import generics
from .models import Store
from .permissions import IsOwnerOrReadOnly, IsSuperUser
from .serializers import StoreSerializer


class StoreList(generics.ListCreateAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        # return all stores for superusers
        if self.request.user.is_superuser:
            queryset = Store.objects.select_related("user")
        # return user's own stores
        else:
            queryset = Store.objects.select_related("user").filter(
                user=self.request.user.id
            )
        return queryset

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.select_related("user")
    serializer_class = StoreSerializer
    # here I used bitwise OR (|) to allow owners to update or delete thier store
    # while superusers can update or delete any store
    permission_classes = [IsOwnerOrReadOnly | IsSuperUser]
