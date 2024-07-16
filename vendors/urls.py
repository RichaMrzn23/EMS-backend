from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServiceView.as_view({'get':'list', 'post': 'create'})),
    path('services/<int:pk>/', ServiceView.as_view({'get':'retrieve', 'put':'update', 'delete': 'destroy'})),
    path('vendors/', VendorView.as_view({'get':'list', 'post': 'create'})),
    path('vendors/<int:pk>/', VendorView.as_view({'get':'retrieve', 'put':'update', 'delete': 'destroy'}))
    
]