# Generated by Django 5.0.3 on 2024-04-18 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchedulingApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
    ]
