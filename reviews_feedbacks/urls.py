from django.urls import path
from .views import ReviewView


urlpatterns = [
    path('review/',ReviewView.as_view({'get':'list', 'post': 'create'})),
    path('review/<int:pk>/',ReviewView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
   
]