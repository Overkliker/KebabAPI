# Generated by Django 5.0.6 on 2024-05-24 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kebab_api', '0009_users_last_login_alter_users_login'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'managed': False},
        ),
    ]