from django.urls import path
from rest_framework import routers

from ads.views import AdUploadImageView, AdViewSet

urlpatterns = [
    path('<int:pk>/up_image/', AdUploadImageView.as_view()),
]

router = routers.SimpleRouter()
router.register('', AdViewSet)
urlpatterns += router.urls
