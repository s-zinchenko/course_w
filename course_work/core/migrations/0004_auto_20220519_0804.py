# Generated by Django 3.2 on 2022-05-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_notification"),
    ]

    operations = [
        migrations.AddField(
            model_name="bb",
            name="views",
            field=models.IntegerField(default=0, verbose_name="Views amount"),
        ),
        migrations.AddField(
            model_name="historicalbb",
            name="views",
            field=models.IntegerField(default=0, verbose_name="Views amount"),
        ),
    ]
