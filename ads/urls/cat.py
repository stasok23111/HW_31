from rest_framework import routers
from ads.views import CategoryVieSet

router = routers.SimpleRouter()
router.register('', CategoryVieSet)


urlpatterns = router.urls