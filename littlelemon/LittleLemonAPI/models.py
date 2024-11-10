from django.db import models
from django.contrib.auth.models import User, Group, Permission

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', related_name='menu_items', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')
    assigned_delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_orders')

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)

class DeliveryCrewAssignment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_assignments')
    status = models.CharField(max_length=20, default='assigned')