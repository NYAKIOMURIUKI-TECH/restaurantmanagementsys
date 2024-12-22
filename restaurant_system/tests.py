from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import MenuItem, Table, Order, Reservation, Staff, Payment
from django.utils import timezone

class RestaurantAPITests(APITestCase):

    def setUp(self):
        # Create test data
        self.table = Table.objects.create(number=1, seats=4)
        self.menu_item = MenuItem.objects.create(name='Pizza', description='Cheese Pizza', price=8.99)
        self.staff = Staff.objects.create(name='John Doe', role='waiter', phone='1234567890', hire_date=timezone.now())
        self.order = Order.objects.create(table=self.table, total_amount=50.00, completed=False)
        self.reservation = Reservation.objects.create(customer_name="Jane Doe", customer_phone="0987654321", table=self.table, reservation_time=timezone.now(), number_of_people=2)
        self.payment = Payment.objects.create(order=self.order, payment_type='cash', amount=50.00, paid=True)

    # Test GET method for MenuItems
    def test_get_menu_items(self):
        response = self.client.get('/restaurant/api/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test POST method for Order creation
    def test_create_order(self):
        data = {
            'table': self.table.id,
            'menu_items': [self.menu_item.id],
            'total_amount': 30.00,
            'completed': False
        }
        response = self.client.post('/restaurant/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test PUT method to update Order
    def test_update_order(self):
        data = {'completed': True}
        response = self.client.put(f'/restaurant/api/orders/{self.order.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test DELETE method to delete a Reservation
    def test_delete_reservation(self):
        response = self.client.delete(f'/restaurant/api/reservations/{self.reservation.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)