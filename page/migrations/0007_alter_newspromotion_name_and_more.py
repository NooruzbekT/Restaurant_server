# Generated by Django 5.0.3 on 2024-04-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_alter_newspromotion_subheading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspromotion',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='newspromotion',
            name='subheading',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Подзаголовок'),
        ),
    ]
