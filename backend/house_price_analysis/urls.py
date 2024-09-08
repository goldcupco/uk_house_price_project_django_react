
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HousePriceViewSet, RegionViewSet, house_prices_view, price_trend_chart
from . import views 
router = DefaultRouter()
router.register(r'house-prices', HousePriceViewSet)
router.register(r'regions', RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/house-prices/<str:area>/', house_prices_view, name='house-prices-area'),
    path('api/price-trend-chart/<str:area>/', views.price_trend_chart, name='price-trend-chart'),
]

urlpatterns += router.urls
