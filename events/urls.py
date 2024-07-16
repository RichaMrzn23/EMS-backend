from django.urls import path
from .views import EventView, CategoryView


urlpatterns = [
    path('event/',EventView.as_view({'get':'list', 'post': 'create'})),
    path('event/<int:pk>/',EventView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('category/',CategoryView.as_view({'get':'list', 'post': 'create'})),
    path('category/<int:pk>/',CategoryView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    
]