# Generated by Django 5.0.3 on 2024-04-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_newspromotion_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspromotion',
            name='subheading',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Подзаголовок'),
        ),
    ]
