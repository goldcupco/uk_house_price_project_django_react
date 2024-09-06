from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import HousePrice, Region
import json
from datetime import date

class HousePriceModelTests(TestCase):
    def setUp(self):
        self.house_price = HousePrice.objects.create(
            date=date(2023, 1, 1),
            average_price=200000,
            detached_price=300000,
            semi_detached_price=250000,
            terraced_price=180000,
            flat_price=150000
        )

    def test_average_price(self):
        self.assertEqual(self.house_price.average_price, 200000)

    def test_string_representation(self):
        self.assertEqual(str(self.house_price), "House Price on 2023-01-01")

class RegionModelTests(TestCase):
    def setUp(self):
        self.region = Region.objects.create(name="London", average_price=500000)

    def test_region_name(self):
        self.assertEqual(self.region.name, "London")

    def test_region_string_representation(self):
        self.assertEqual(str(self.region), "London")

class APIViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.house_price = HousePrice.objects.create(
            date=date(2023, 1, 1),
            average_price=200000
        )
        self.region = Region.objects.create(name="London", average_price=500000)

    def test_get_house_prices_status(self):
        response = self.client.get(reverse('houseprice-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_house_prices_count(self):
        response = self.client.get(reverse('houseprice-list'))
        self.assertEqual(len(response.data), 1)

    def test_get_regions_status(self):
        response = self.client.get(reverse('region-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_regions_count(self):
        response = self.client.get(reverse('region-list'))
        self.assertEqual(len(response.data), 1)
class PriceTrendChartViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        HousePrice.objects.create(date=date(2023, 1, 1), average_price=200000)
        HousePrice.objects.create(date=date(2023, 2, 1), average_price=210000)

    def test_price_trend_chart_view_status(self):
        response = self.client.get(reverse('price-trend-chart'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_price_trend_chart_view_content(self):
        response = self.client.get(reverse('price-trend-chart'))
        content = json.loads(response.content)
        self.assertIn('dates', content)
        self.assertIn('average_prices', content)

    def test_price_trend_chart_view_data_types(self):
        response = self.client.get(reverse('price-trend-chart'))
        content = json.loads(response.content)
        self.assertIsInstance(content['dates'], list)
        self.assertIsInstance(content['average_prices'], list)

    def test_price_trend_chart_view_data_values(self):
        response = self.client.get(reverse('price-trend-chart'))
        content = json.loads(response.content)
        self.assertEqual(len(content['dates']), 2)
        self.assertEqual(len(content['average_prices']), 2)
        self.assertAlmostEqual(content['average_prices'][0], 200.0, places=1)
        self.assertAlmostEqual(content['average_prices'][1], 210.0, places=1)

    def test_price_trend_chart_view_no_data(self):
        HousePrice.objects.all().delete()
        response = self.client.get(reverse('price-trend-chart'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        content = json.loads(response.content)
        self.assertIn('error', content)
        self.assertEqual(content['error'], "No data available")
        