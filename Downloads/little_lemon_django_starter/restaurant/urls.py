from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, register_user, obtain_token

router = DefaultRouter()
router.register("menu", MenuItemViewSet, basename="menu")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
    path("users/", register_user, name="register-user"),
    path("token/", obtain_token, name="obtain-token"),
]
