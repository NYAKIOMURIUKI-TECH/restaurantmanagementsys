from rest_framework import serializers
from .models import MenuItem, Table, Order, Reservation, Staff, Payment

# Serializer for MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

# Serializer for Table
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

# Serializer for Order
class OrderSerializer(serializers.ModelSerializer):
    menu_items = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), many=True) 

    class Meta:
        model = Order
        fields = ['id', 'table', 'menu_items', 'total_amount', 'completed']

    def update(self, instance, validated_data):
        # You might want to add custom logic here to handle updates
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance

# Serializer for Reservation
class ReservationSerializer(serializers.ModelSerializer):
    table = TableSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'

# Serializer for Staff
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

# Serializer for Payment
class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Payment
        fields = '__all__'