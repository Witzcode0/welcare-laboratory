# Generated by Django 4.2.4 on 2023-09-22 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("profile", models.ImageField(upload_to="doctor_profiles/")),
                ("name", models.CharField(max_length=100)),
                ("designation", models.CharField(max_length=100)),
                ("summary", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
