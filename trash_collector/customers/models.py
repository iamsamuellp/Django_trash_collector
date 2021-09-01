from django.db import models
import django.utils.timezone 
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    street_address = models.CharField(blank=True, max_length=50)
    zip_code = models.CharField(default=True, max_length=5)
    balance = models.IntegerField(null=True)
    weekly_pickup = models.CharField(null=True, max_length=50)
    one_time_pickup = models.DateField(null=True, blank=True)
    suspend_start = models.DateField(null=True, blank=True)
    suspend_end = models.DateField(null=True, blank=True)
 
    def __str__(self):
        return self.name
