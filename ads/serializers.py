from rest_framework.fields import SerializerMethodField, BooleanField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Category, Selection
from ads.validator import is_published_not_tru
from users.models import User


class AdSerializer(ModelSerializer):

    is_published = BooleanField(validators=[is_published_not_tru], required=False)

    class Meta:
        fields = '__all__'
        model = Ad


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        exclude = ('description',)
        model = Ad


class AdAuthorSerializer(ModelSerializer):
    total_ads = SerializerMethodField()

    def get_total_ads(self, obj):
        return obj.ad_set.count()

    class Meta:
        exclude = ('password', 'role')
        model = User


class AdDetailSerializer(ModelSerializer):
    author = AdAuthorSerializer()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        fields = '__all__'
        model = Ad


class CategoryListSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ad


class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ad


class CategorySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class SelectionSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Selection


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field='username', required=False, read_only=True)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user

        return super().create(validated_data)

    class Meta:
        fields = '__all__'
        model = Selection


class SelectionListSerializer(ModelSerializer):
    class Meta:
        fields = ['pk', 'name']
        model = Selection


class SelectionDetailSerializer(ModelSerializer):
    items = AdSerializer(many=True)
    owner = SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Selection
