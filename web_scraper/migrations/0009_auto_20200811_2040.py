# Generated by Django 3.1 on 2020-08-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraper', '0008_auto_20200811_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articledetail',
            name='url',
            field=models.CharField(max_length=3062, unique=True),
        ),
    ]