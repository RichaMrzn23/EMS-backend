from django.urls import path
from .views import LogisticsView


urlpatterns = [
    path('logistics/',LogisticsView.as_view({'get':'list', 'post': 'create'})),
    path('logistics/<int:pk>/',LogisticsView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
   
]