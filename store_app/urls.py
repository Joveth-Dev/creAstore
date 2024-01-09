from django.urls import path
from . import views


urlpatterns = [
    path("store/", views.StoreList.as_view()),
    path("store/<int:pk>/", views.StoreDetail.as_view()),
]
