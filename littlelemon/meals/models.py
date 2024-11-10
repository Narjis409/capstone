from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Meals(models.Model):
    name= models.CharField(max_length=55)
    description = models.TextField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def str(self):
        return self.name