from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=50)
    weekly_pickup = models.CharField(max_length=50)
    one-time_pickup = models.DateField(max_length=50, null = True)
    nonsuspended = models.DateField(max_length=50, null = True)

    