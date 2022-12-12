from rest_framework.routers import DefaultRouter

from applications.movie import views


router = DefaultRouter()
router.register('', views.MovieViewSet)

urlpatterns = router.urls
