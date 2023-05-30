from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserSerializer, UserCreateUpdateSerializer, UserListSerializer, LocationSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserListView(ListAPIView):
    queryset = User.objects.annotate(total_ads=Count('ad', filter=Q(ad__is_published=True))).order_by('username')
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer