from django.http import JsonResponse
from rest_framework import viewsets
import pandas as pd

from house_price_analysis.models import HousePrice, Region
from house_price_analysis.serializers import HousePriceSerializer, RegionSerializer

class HousePriceViewSet(viewsets.ModelViewSet):
    queryset = HousePrice.objects.all()
    serializer_class = HousePriceSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

def price_trend_chart(request):
    try:
        # Fetch data
        data = HousePrice.objects.all().order_by('date')
        
        if not data.exists():
            return JsonResponse({"error": "No data available"}, status=404)

        df = pd.DataFrame(list(data.values()))

        # Convert prices to thousands for better readability
        price_columns = ['average_price', 'detached_price', 'semi_detached_price', 'terraced_price', 'flat_price']
        for column in price_columns:
            if column in df.columns:
                df[column] = df[column] / 1000

        # Prepare data for JSON
        chart_data = df.to_dict(orient='records')

        # Return JSON response
        return JsonResponse(chart_data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)