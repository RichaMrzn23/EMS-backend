from django.urls import path
from .views import AttendeeView, RegistrationView, CommunicationView


urlpatterns = [
    path('attendee/',AttendeeView.as_view({'get':'list', 'post': 'create'})),
    path('attendee/<int:pk>/',AttendeeView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('register/', RegistrationView.as_view(), name ="registration_create"),
    path('list', RegistrationView.as_view(), name ="registration_list"),
    path('communication/', CommunicationView.as_view({'get':'list', 'post':'create'})),
    path('communication/<int:pk>/', CommunicationView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
]