from django.http import JsonResponse
from rest_framework import viewsets
import pandas as pd
from .models import HousePrice, Region
from .serializers import HousePriceSerializer, RegionSerializer

class HousePriceViewSet(viewsets.ModelViewSet):
    queryset = HousePrice.objects.all()
    serializer_class = HousePriceSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

def house_prices_view(request, area=None):
    try:
        # Fetch data
        if area:
            data = HousePrice.objects.filter(area=area).order_by('date')
        else:
            data = HousePrice.objects.all().order_by('date')
        
        if not data.exists():
            return JsonResponse({"error": "No data available"}, status=404)

        df = pd.DataFrame(list(data.values()))

        # Convert prices to thousands for better readability
        price_columns = ['average_price', 'detached_price', 'semi_detached_price', 'terraced_price', 'flat_price']
        for column in price_columns:
            if column in df.columns:
                df[column] = df[column].astype(float) / 1000

        # Prepare data for JSON
        chart_data = {
            'dates': df['date'].astype(str).tolist(),
            'average_prices': df['average_price'].tolist()
        }

        # Add other price types if available
        for column in ['detached_price', 'semi_detached_price', 'terraced_price', 'flat_price']:
            if column in df.columns:
                chart_data[column] = df[column].tolist()

        # Return JSON response with numeric data
        return JsonResponse(chart_data)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def price_trend_chart(request,area):
    return house_prices_view(request,area)