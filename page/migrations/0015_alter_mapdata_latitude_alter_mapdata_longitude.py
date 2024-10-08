# Generated by Django 5.0.3 on 2024-04-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_alter_mapdata_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapdata',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='mapdata',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True, verbose_name='Долгота'),
        ),
    ]
