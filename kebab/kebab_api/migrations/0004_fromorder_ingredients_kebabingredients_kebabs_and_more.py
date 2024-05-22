# Generated by Django 5.0.6 on 2024-05-21 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kebab_api', '0003_delete_fromorder_delete_ingredients_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FromOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_or_street', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'from_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'ingredients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KebabIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'kebab_ingredients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kebabs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kebab_name', models.CharField(blank=True, max_length=128, null=True)),
                ('kebab_price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'kebabs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KebabsOrdered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'kebabs_ordered',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderFeedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'order_feedbacks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where_eat', models.BooleanField(blank=True, null=True)),
                ('when_ordering', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'points',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('photo_path', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'profiles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'workers',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(verbose_name=64)),
                ('password', models.CharField(verbose_name=256)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kebab_api.roles')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]