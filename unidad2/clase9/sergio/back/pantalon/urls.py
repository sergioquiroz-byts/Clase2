from rest_framework.routers import DefaultRouter
from pantalon.views.pantalon_viewset import PantalonViewSet
router = DefaultRouter()
router.register("pantalones", PantalonViewSet, basename="pantalon")
urlpatterns = router.urls
