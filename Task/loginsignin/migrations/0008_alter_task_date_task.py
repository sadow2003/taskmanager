# Generated by Django 5.0.4 on 2024-05-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsignin', '0007_task_date_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_task',
            field=models.DateTimeField(max_length=100, null=True),
        ),
    ]
