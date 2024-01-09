from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("store", views.StoreViewSet, basename="store")

urlpatterns = router.urls


# urlpatterns = [
#     path("store/<int:pk>/", views.StoreDetail.as_view()),
#     path("", include(router.urls)),
# ]
