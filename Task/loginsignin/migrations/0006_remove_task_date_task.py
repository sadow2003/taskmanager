# Generated by Django 5.0.4 on 2024-05-21 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsignin', '0005_task_date_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_task',
        ),
    ]