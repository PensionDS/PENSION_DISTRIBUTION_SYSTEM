# Generated by Django 3.2.10 on 2022-01-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pension_user_dashboard', '0007_bookverification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookverification',
            name='Slot_time',
        ),
        migrations.AddField(
            model_name='bookverification',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
