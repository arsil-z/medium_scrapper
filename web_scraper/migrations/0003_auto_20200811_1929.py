# Generated by Django 3.1 on 2020-08-11 19:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraper', '0002_auto_20200811_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=2048, null=True), size=None), size=None),
        ),
    ]