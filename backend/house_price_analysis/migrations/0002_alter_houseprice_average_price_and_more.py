# Generated by Django 5.1.1 on 2024-09-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_price_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseprice',
            name='average_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='houseprice',
            name='detached_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='houseprice',
            name='flat_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='houseprice',
            name='semi_detached_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='houseprice',
            name='terraced_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='average_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
