from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.RolesListCreate.as_view(), name='roles-view-create'),
    path('roles/<int:pk>/', views.RolesRetriveUpdateDestroy.as_view(), name='update-roles'),

    path('users/', views.UsersListCreate.as_view(), name='users-view-create'),
    path('users/<int:pk>/', views.UsersRetriveUpdateDestroy.as_view(), name='update-users'),

    path('points/', views.PointsListCreate.as_view(), name='points-view-create'),
    path('points/<int:pk>/', views.PointsRetriveUpdateDestroy.as_view(), name='update-points'),

    path('workers/', views.WorkersListCreate.as_view(), name='workers-view-create'),
    path('workers/<int:pk>/', views.WorkersRetriveUpdateDestroy.as_view(), name='update-workers'),

    path('from-order/', views.FromOrderListCreate.as_view(), name='from-order-view-create'),
    path('from-order/<int:pk>/', views.FromOrderRetriveUpdateDestroy.as_view(), name='update-from-order'),

    path('orders/', views.OrdersListCreate.as_view(), name='orders-view-create'),
    path('orders/<int:pk>/', views.OrdersRetriveUpdateDestroy.as_view(), name='update-orders'),

    path('igredients/', views.IngredientsListCreate.as_view(), name='igredients-view-create'),
    path('igredients/<int:pk>/', views.IngredientsRetriveUpdateDestroy.as_view(), name='update-igredients'),

    path('kebabs/', views.KebabsListCreate.as_view(), name='kebabs-view-create'),
    path('kebabs/<int:pk>/', views.KebabsRetriveUpdateDestroy.as_view(), name='update-kebabs'),

    path('kebab-ingradient/', views.KebabIngredientsListCreate.as_view(), name='kebab-ingradient-view-create'),
    path('kebab-ingradient/<int:pk>/', views.KebabIngredientsRetriveUpdateDestroy.as_view(), name='update-kebab-ingradient'),

    path('kebab-ordered/', views.KebabsOrderedListCreate.as_view(), name='kebab-ordered-view-create'),
    path('kebab-ordered/<int:pk>/', views.KebabsOrderedRetriveUpdateDestroy.as_view(), name='update-kebab-ordered'),

    path('order-feedback/', views.OrderFeedbacksListCreate.as_view(), name='order-feedback-view-create'),
    path('order-feedback/<int:pk>/', views.OrderFeedbacksRetriveUpdateDestroy.as_view(), name='update-order-feedback'),

    path('profiles/', views.ProfilesListCreate.as_view(), name='profiles-view-create'),
    path('profiles/<int:pk>/', views.ProfilesRetriveUpdateDestroy.as_view(), name='update-profiles'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logut'),
]
