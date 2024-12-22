from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import MenuItem, Table, Order, Reservation, Staff, Payment
from .serializers import MenuItemSerializer, TableSerializer, OrderSerializer, ReservationSerializer, StaffSerializer, PaymentSerializer


from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("Welcome to the Restaurant Management System!")
# Viewset for MenuItem
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Viewset for Table
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

# Viewset for Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Viewset for Reservation
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# Viewset for Staff
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

# Viewset for Payment
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer