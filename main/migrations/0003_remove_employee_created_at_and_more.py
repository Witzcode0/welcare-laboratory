# Generated by Django 4.2.4 on 2023-08-26 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_employee_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='updated_at',
        ),
    ]
