# Generated by Django 3.2.10 on 2022-01-21 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pension_user_notification', '0002_alter_usernotification_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usernotification',
            options={'ordering': ['-notification']},
        ),
    ]