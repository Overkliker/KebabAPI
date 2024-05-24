from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import * 
import jwt, datetime

class SetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class RegisterView(APIView):

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self, request):
        login = request.data['login']
        password = request.data['password']

        user = Users.objects.filter(login=login).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='token', value=token, httponly=True)
        response.data = {
            'token': token
        }
        
        return response
    


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie(key='token')

        response.data = {
            "message": 'logout'
        }

        return response


class RolesListCreate(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    pagination_class = SetPagination

    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed("Unauthenticated")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")
        
        user = Users.objects.filter(id=payload['id']).first()

        serializer = UsersSerializer(user)

        return Response(serializer.data)
    


class RolesRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    lookup_field = 'pk'



class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    pagination_class = SetPagination


class UsersRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'pk'



class PointsListCreate(generics.ListCreateAPIView):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer
    pagination_class = SetPagination


class PointsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer
    lookup_field = 'pk'



class WorkersListCreate(generics.ListCreateAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
    pagination_class = SetPagination


class WorkersRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
    lookup_field = 'pk'



class FromOrderListCreate(generics.ListCreateAPIView):
    queryset = FromOrder.objects.all()
    serializer_class =FromOrderSerializer
    pagination_class = SetPagination


class FromOrderRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FromOrder.objects.all()
    serializer_class = FromOrderSerializer
    lookup_field = 'pk'



class OrdersListCreate(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class =OrdersSerializer
    pagination_class = SetPagination


class OrdersRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    lookup_field = 'pk'



class IngredientsListCreate(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    pagination_class = SetPagination


class IngredientsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    lookup_field = 'pk'



class KebabsListCreate(generics.ListCreateAPIView):
    queryset = Kebabs.objects.all()
    serializer_class = KebabsSerializer
    pagination_class = SetPagination


class KebabsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kebabs.objects.all()
    serializer_class = KebabsSerializer
    lookup_field = 'pk'



class KebabIngredientsListCreate(generics.ListCreateAPIView):
    queryset = KebabIngredients.objects.all()
    serializer_class = KebabIngredientsSerializer
    pagination_class = SetPagination


class KebabIngredientsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = KebabIngredients.objects.all()
    serializer_class = KebabIngredientsSerializer
    lookup_field = 'pk'



class KebabsOrderedListCreate(generics.ListCreateAPIView):
    queryset = KebabsOrdered.objects.all()
    serializer_class = KebabsOrderedSerializer
    pagination_class = SetPagination


class KebabsOrderedRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = KebabsOrdered.objects.all()
    serializer_class = KebabsOrderedSerializer
    lookup_field = 'pk'



class OrderFeedbacksListCreate(generics.ListCreateAPIView):
    queryset = OrderFeedbacks.objects.all()
    serializer_class = OrderFeedbacksSerializer
    pagination_class = SetPagination


class OrderFeedbacksRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderFeedbacks.objects.all()
    serializer_class = OrderFeedbacksSerializer
    lookup_field = 'pk'



class ProfilesListCreate(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    pagination_class = SetPagination


class ProfilesRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = 'pk'
