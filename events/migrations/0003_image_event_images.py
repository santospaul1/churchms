# Generated by Django 4.2.9 on 2024-05-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_meeting_service"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="images",
            field=models.ManyToManyField(blank=True, to="events.image"),
        ),
    ]
