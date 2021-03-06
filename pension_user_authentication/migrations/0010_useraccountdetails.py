# Generated by Django 3.2.10 on 2022-01-03 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pension_user_authentication', '0009_auto_20211229_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=251, unique=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=16)),
                ('confirm_password', models.CharField(max_length=16)),
                ('otp', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
