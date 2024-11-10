from django.db import models

# Create your models here.
from django.db import models
from meals.models import Meals

class Orders(models.Model):
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )

    def __str__(self):
        return f"Order of {self.quantity} {self.meal.name}(s)"

    def get_total_price(self):
        return self.quantity * self.meal.price
