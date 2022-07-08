from django.urls import path, include
# from Advertisement.views import AdvertiserList, AdvertiserDetail
# from .views import AdvertiserViewSet
from rest_framework.routers import DefaultRouter
from Advertisement.views import AdvertiserViewSet, AdViewSet, ViewViewSet, ClickViewSet


router = DefaultRouter()
router.register(r'advertiser', AdvertiserViewSet, basename="advertisement")
router.register(r'ads', AdViewSet)
router.register(r'views', ViewViewSet)
router.register(r'clicks', ClickViewSet)


urlpatterns = [
    path('', include(router.urls))
]

