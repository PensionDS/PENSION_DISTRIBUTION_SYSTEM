# Generated by Django 3.2.10 on 2021-12-28 05:56

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pension_user_authentication', '0002_alter_useraccount_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
