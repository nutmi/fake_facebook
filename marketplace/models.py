from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Type(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
class Condition(models.Model):
    condition = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.condition

class Place(models.Model):
    place_name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.place_name

class Product(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    body = models.TextField(max_length=500)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    price = models.IntegerField(max_length=100)

    def __str__(self) -> str:
        return self.name


