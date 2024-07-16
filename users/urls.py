
from django.urls import path
from .views import Register,Login

urlpatterns = [
    path('register/',Register, name = 'register-list'),
    path('register/<int:pk>/', Register, name='register-detail'),
    path('login/', Login)
    
]