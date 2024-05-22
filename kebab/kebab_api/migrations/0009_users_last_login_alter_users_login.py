# Generated by Django 5.0.6 on 2024-05-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kebab_api', '0008_rename_role_id_users_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='users',
            name='login',
            field=models.CharField(unique=True, verbose_name=64),
        ),
    ]
