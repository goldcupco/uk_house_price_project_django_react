from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HousePriceViewSet, RegionViewSet, price_trend_chart

router = DefaultRouter()
router.register(r'house-prices', HousePriceViewSet)
router.register(r'regions', RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('price-trend-chart/', price_trend_chart, name='price-trend-chart'),
]