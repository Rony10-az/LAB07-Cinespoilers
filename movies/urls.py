from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet  # CAMBIO

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)  # NUEVO

urlpatterns = router.urls