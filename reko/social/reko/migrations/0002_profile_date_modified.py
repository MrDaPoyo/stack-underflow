# Generated by Django 5.0.1 on 2024-01-05 12:51

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reko", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name=django.contrib.auth.models.User
            ),
        ),
    ]
