# Generated by Django 4.2.4 on 2023-09-09 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="email",
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="mobile",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]