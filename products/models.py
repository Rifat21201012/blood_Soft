from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    age = models.IntegerField(default=0)
    national_number = models.CharField(max_length=20)
    present_address = models.CharField(max_length=200, default="")


    def __str__(self):
        return self.name
