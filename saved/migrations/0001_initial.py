# Generated by Django 4.1.7 on 2023-10-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Saved",
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
                ("user", models.TextField()),
                ("text", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
    ]
