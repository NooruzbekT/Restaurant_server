# Generated by Django 5.0.3 on 2024-04-13 11:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_restaurant_restaurant_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspromotion',
            name='image_url',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='news_promotion/', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
