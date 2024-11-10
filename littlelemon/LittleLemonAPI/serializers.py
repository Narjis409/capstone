from rest_framework import serializers
from .models import User, MenuItem, Category, Order, Cart, DeliveryCrewAssignment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'status', 'assigned_delivery_crew']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['customer', 'items']

class DeliveryCrewAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCrewAssignment
        fields = ['order', 'delivery_crew', 'status']
