
from django.db import models

# 1. Menu Item Model (already discussed)
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# 2. Table Model (already discussed)
class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.number}"

# 3. Order Model (already discussed)
class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for Table {self.table.number} - {'Completed' if self.completed else 'Pending'}"

# 4. Reservation Model
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"Reservation by {self.customer_name} at Table {self.table.number}"

# 5. Staff Model
class Staff(models.Model):
    ROLE_CHOICES = (
        ('waiter', 'Waiter'),
        ('chef', 'Chef'),
        ('manager', 'Manager'),
        ('cleaner', 'Cleaner'),
        ('bartender', 'Bartender'),
    )

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.role}"

# 6. Payment Model
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20, choices=[('cash', 'Cash'), ('card', 'Card'), ('mobile', 'Mobile Payment')])
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {'Paid' if self.paid else 'Pending'}"
