from django.db import models

# a. ServiceUser (having name, email, age, gender as necessary fields, use field Types accordingly, Keep gender as choices/select tag)

# b. Services (should have type where choices: Mobile Recharge, DTH Recharge, Insurance payment, mode_of_payment where choices: UPI, internet banking, card payment, and company as fields)

# Establish a many-to-many relationship between User and Service for managing subscriptions.
# Create your models here.
class ServiceUser(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F', 'Female'),
        ('O','Other')
    ]
    name = models.CharField(max_length=100)
    email =models.EmailField()
    age = models.IntegerField()
    choices = GENDER_CHOICES

    def __str__(self):
        return self.name

class Services(models.Model):


