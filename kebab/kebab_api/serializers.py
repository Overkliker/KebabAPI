from rest_framework import serializers
from .models import *



class RolesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Roles
        fields = ['id', 'role_name']


class UsersSerializer(serializers.ModelSerializer):
    role = Roles.objects.all()
    class Meta: 
        model = Users
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance



class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = '__all__'


class WorkersSerializer(serializers.ModelField):
    user = Users.objects.all()
    point = Points.objects.all()

    class Meta:
        model = Workers
        fields = ['id', 'user', 'point']


class FromOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FromOrder
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    user = Users.objects.all()
    from_order = FromOrder.objects.all()

    class Meta:
        model = Orders
        fields = ['id', 'user', 'from_order', 'where_eat', 'when_ordering']


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'


class KebabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kebabs
        fields = '__all__'


class KebabIngredientsSerializer(serializers.ModelSerializer):
    kebab = Kebabs.objects.all()
    ingredient = Ingredients.objects.all()

    class Meta:
        model = Workers
        fields = ['id', 'kebab', 'ingredient']


class KebabsOrderedSerializer(serializers.ModelSerializer):
    kebab = Kebabs.objects.all()
    order = Orders.objects.all()

    class Meta:
        model = Workers
        fields = ['id', 'kebab', 'order']


class OrderFeedbacksSerializer(serializers.ModelSerializer):
    user = Users.objects.all()
    order = Orders.objects.all()

    class Meta:
        model = OrderFeedbacks
        fields = ['id', 'user', 'order', 'score', 'description']


class ProfilesSerializer(serializers.ModelSerializer):
    user = Users.objects.all()

    class Meta:
        model = Profiles
        fields = ['id', 'user', 'photo_path', 'description']
