# Generated by Django 4.2.9 on 2024-07-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("volunteers", "0007_remove_volunteer_volunteer_volunteer_volunteer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volunteer",
            name="interests",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="skills",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
