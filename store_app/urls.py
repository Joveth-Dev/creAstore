from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("store", views.StoreViewSet, basename="store")

urlpatterns = router.urls
