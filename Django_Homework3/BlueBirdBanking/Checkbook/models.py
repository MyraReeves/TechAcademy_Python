from django.db import models


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_length=15, decimal_places=2)

    # Model manager:
    object = models.Manager()

    # Refers accounts as a string of the owner's full name:
    def __str__(self):
        return self.first_name + " " + self.last_name