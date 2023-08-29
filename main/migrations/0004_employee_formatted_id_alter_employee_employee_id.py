# Generated by Django 4.2.4 on 2023-08-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_employee_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='formatted_id',
            field=models.CharField(default=1, max_length=8, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]