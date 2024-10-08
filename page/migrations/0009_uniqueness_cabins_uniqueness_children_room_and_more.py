# Generated by Django 5.0.3 on 2024-04-15 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_remove_restaurant_check_dish_averagecheck_restaurant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniqueness',
            name='cabins',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Кабинки'),
        ),
        migrations.AddField(
            model_name='uniqueness',
            name='children_room',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Детская комнатка'),
        ),
        migrations.AddField(
            model_name='uniqueness',
            name='display_brewery',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='uniqueness',
            name='display_cabins',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='uniqueness',
            name='display_children_room',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='uniqueness',
            name='display_vegetarian_menu',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='uniqueness',
            name='own_brewery',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Своя Пивоварня'),
        ),
        migrations.AddField(
            model_name='uniqueness',
            name='vegetarian_menu',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Вегетарианское меню'),
        ),
        migrations.AlterField(
            model_name='uniqueness',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Связь с рестораном'),
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(upload_to='gallery/', verbose_name='Фото')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.restaurant')),
            ],
        ),
    ]
