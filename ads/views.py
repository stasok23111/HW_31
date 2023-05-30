from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.permissions import IsOwner, IsStaff
from ads.serializers import *


def root(request):
    return JsonResponse({
        "status": "ok"
    })


class CategoryVieSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdSerializer
    serializers = {
        'list': AdListSerializer,
        'retrieve': AdDetailSerializer,

    }

    permissions = {
        'retrieve': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner | IsStaff],
        'partial_update': [IsAuthenticated, IsOwner | IsStaff],
        'destroy': [IsAuthenticated, IsOwner | IsStaff],
    }
    default_permissions = [AllowAny]

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permissions)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        category = request.GET.getlist('cat')
        if category:
            self.queryset = self.queryset.filter(category_id__in=category)

        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        price_from = request.GET.get('price_from')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get('price_to')
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({
            'id': self.object.pk,
            'name': self.object.name,
            'price': self.object.price,
            'author': self.object.author.username,
            'description': self.object.description,
            'category': self.object.category.name,
            'is_published': self.object.is_published,
            'image': self.object.image.url
        })


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer = SelectionSerializer
    serializers = {
        'list': SelectionListSerializer,
        'retrieve': SelectionDetailSerializer,
        'create': SelectionCreateSerializer

    }

    permissions = {
        'create': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner],
        'partial_update': [IsAuthenticated, IsOwner],
        'destroy': [IsAuthenticated, IsOwner],

    }
    default_permissions = [AllowAny]

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permissions)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
