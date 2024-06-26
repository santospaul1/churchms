# Generated by Django 4.2.9 on 2024-05-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meeting",
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
                ("name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("location", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("location", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
        ),
    ]
