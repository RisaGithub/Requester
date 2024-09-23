# Generated by Django 5.1.1 on 2024-09-23 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(max_length=1000)),
                ("is_active", models.BooleanField()),
                ("time_interval", models.TimeField()),
                ("request_method", models.CharField(max_length=10)),
                ("next_request_time", models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sent_at", models.DateTimeField()),
                ("http_status_code", models.CharField(max_length=10)),
                ("request_method", models.CharField(max_length=10)),
                ("error_message", models.CharField(max_length=1000)),
                (
                    "url",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="requests_data.url",
                    ),
                ),
            ],
        ),
    ]
