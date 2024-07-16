from .models import Ticket, Payment, Invoice, Receipt
from rest_framework import serializers

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields ='__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields ='__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields ='__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields ='__all__'