from django.core.management.base import BaseCommand
from house_price_analysis.models import HousePrice, Region
import pandas as pd
from datetime import datetime
import numpy as np

class Command(BaseCommand):
    help = 'Import house price data'

    def handle(self, *args, **options):
        # Update this path to the actual location of your CSV file
        df = pd.read_csv('UK-HPI-full-file-2020-06.csv')

        for _, row in df.iterrows():
            # Convert date from DD/MM/YYYY to YYYY-MM-DD
            date_obj = datetime.strptime(row['Date'], '%d/%m/%Y')
            formatted_date = date_obj.strftime('%Y-%m-%d')

            # Function to handle 'nan' values
            def clean_price(value):
                return value if pd.notna(value) else None

            try:
                HousePrice.objects.create(
                    date=formatted_date,
                    average_price=clean_price(row['AveragePrice']),
                    detached_price=clean_price(row['DetachedPrice']),
                    semi_detached_price=clean_price(row['SemiDetachedPrice']),
                    terraced_price=clean_price(row['TerracedPrice']),
                    flat_price=clean_price(row['FlatPrice'])
                )

                # Optionally, you can also create Region objects if needed
                if pd.notna(row['RegionName']) and pd.notna(row['AveragePrice']):
                    Region.objects.get_or_create(
                        name=row['RegionName'],
                        defaults={'average_price': row['AveragePrice']}
                    )
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Error processing row: {row['Date']} - {str(e)}"))

        self.stdout.write(self.style.SUCCESS('Successfully imported house price data'))