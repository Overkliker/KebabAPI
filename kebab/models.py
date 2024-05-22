# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FromOrder(models.Model):
    app_or_street = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'from_order'


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class KebabIngredients(models.Model):
    kebab = models.ForeignKey('Kebabs', models.DO_NOTHING, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredients, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kebab_ingredients'


class Kebabs(models.Model):
    kebab_name = models.CharField(max_length=128, blank=True, null=True)
    kebab_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kebabs'


class KebabsOrdered(models.Model):
    id = models.AutoField()
    kebab = models.ForeignKey(Kebabs, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kebabs_ordered'


class OrderFeedbacks(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_feedbacks'


class Orders(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    where_eat = models.BooleanField(blank=True, null=True)
    when_ordering = models.DateTimeField(blank=True, null=True)
    from_order = models.ForeignKey(FromOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Points(models.Model):
    adress = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'points'


class Profiles(models.Model):
    description = models.CharField(max_length=128, blank=True, null=True)
    photo_path = models.CharField(max_length=128, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class Roles(models.Model):
    role_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Users(models.Model):
    login = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Workers(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    point = models.ForeignKey(Points, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workers'
