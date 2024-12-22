from django.contrib import admin
from .models import MenuItem, Table, Order, Reservation, Staff, Payment

admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Reservation)
admin.site.register(Staff)
admin.site.register(Payment)