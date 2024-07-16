from django.shortcuts import render
from .models import Ticket, Payment, Invoice, Receipt
from rest_framework.viewsets import ModelViewSet
from .serializers import TicketSerializer, PaymentSerializer, InvoiceSerializer, ReceiptSerializer
import stripe
# Create your views here.

stripe.api_key = 'sk_test_51PSamKE9LJc7ltvuVBt1fkDJol6Z6y8guEtp7B9PH96FxNgiHBPLvQO6A4vkDtbYeiu99MTxlxVgCI8g2HlsR1os00ns9Tbgxc'
class TicketView(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class PaymentView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer



class InvoiceView(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    

class ReceiptView(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer