from django.urls import path
from .views import TicketView, PaymentView, InvoiceView, ReceiptView


urlpatterns = [
    path('ticket/',TicketView.as_view({'get':'list', 'post': 'create'})),
    path('ticket/<int:pk>/',TicketView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('payment/', PaymentView.as_view({'get':'list', 'post':'create'})),
    path('payment/<int:pk>/', PaymentView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('invoice/',InvoiceView.as_view({'get':'list', 'post': 'create'})),
    path('invoice/<int:pk>/',InvoiceView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('receipt/', ReceiptView.as_view({'get':'list', 'post':'create'})),
    path('receipt/<int:pk>/', ReceiptView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
]