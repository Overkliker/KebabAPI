from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.role_name
    

    class Meta:
        managed = False
        db_table = 'roles'


class Users(AbstractBaseUser):
    login = models.CharField(64, unique=True)
    password = models.CharField(256)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    username = None

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login

    class Meta:
        db_table = 'users'


class Points(models.Model):
    adress = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'points'



class Workers(models.Model):
    user = models.ForeignKey(Users, blank=True, null=True, on_delete=models.CASCADE)
    point = models.ForeignKey(Points, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.login

    class Meta:
        managed = False
        db_table = 'workers'


class FromOrder(models.Model):
    app_or_street = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.app_or_street

    class Meta:
        managed = False
        db_table = 'from_order'



class Orders(models.Model):
    user = models.ForeignKey(Users, blank=True, null=True, on_delete=models.CASCADE)
    where_eat = models.BooleanField(blank=True, null=True)
    when_ordering = models.DateTimeField(blank=True, null=True)
    from_order = models.ForeignKey(FromOrder, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.user.login} - {self.when_ordering}'

    class Meta:
        managed = False
        db_table = 'orders'


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        managed = False
        db_table = 'ingredients'


class KebabIngredients(models.Model):
    kebab = models.ForeignKey('Kebabs', models.DO_NOTHING, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredients, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.kebab.kebab_name} - {self.ingredient.ingredient_name}'

    class Meta:
        managed = False
        db_table = 'kebab_ingredients'


class Kebabs(models.Model):
    kebab_name = models.CharField(max_length=128, blank=True, null=True)
    kebab_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.kebab_name

    class Meta:
        managed = False
        db_table = 'kebabs'


class KebabsOrdered(models.Model):
    kebab = models.ForeignKey(Kebabs, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(Orders, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order.id} - {self.kebab.kebab_name}'

    class Meta:
        managed = False
        db_table = 'kebabs_ordered'



class OrderFeedbacks(models.Model):
    user = models.ForeignKey('Users', blank=True, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey('Orders', blank=True, null=True, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)


    def __str__(self):
        return f'{self.score} - {self.user.login}'

    class Meta:
        managed = False
        db_table = 'order_feedbacks'
        

class Profiles(models.Model):
    description = models.CharField(max_length=128, blank=True, null=True)
    photo_path = models.CharField(max_length=128, blank=True, null=True)
    user = models.ForeignKey('Users', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.login
    
    class Meta:
        managed = False
        db_table = 'profiles'