from rest_framework.routers import DefaultRouter
from cartas.views import CartaViewSet

router = DefaultRouter()
router.register(r"cartas", CartaViewSet)

urlpatterns = router.urls
