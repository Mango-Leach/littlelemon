from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by("id")
    serializer_class = MenuItemSerializer
    # TODO: Choose permissions appropriate for the assignment.
    # For example, allow reads publicly but require authentication for writes.

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by("booking_date")
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_user(request):
    # TODO: Validate username/password, handle duplicate usernames, create user,
    # and return an appropriate status code and response.
    return Response(
        {"detail": "Implement registration validation and user creation."},
        status=501,
    )

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def obtain_token(request):
    # TODO: Validate credentials and return a DRF token for the authenticated user.
    return Response(
        {"detail": "Implement credential validation and token creation."},
        status=501,
    )
