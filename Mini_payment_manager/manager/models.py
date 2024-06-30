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
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default="Male")

    def __str__(self):
        return self.name

class Services(models.Model):
    SERVICES_TYPE = [
        ('Mobile Recharge', 'Mobile Recharge'),
        ('DTH Recharge', 'DTH Recharge'),
        ('Insurance payment', 'Insurance payment'),

    ]
    MODE_OF_PAYMENT = [
        ('UPI', 'UPI'),
        ('internet banking', 'internet banking'),
        ('card payment', 'card payment'),

    ]
    type = models.CharField(max_length=40,choices=SERVICES_TYPE)
    payment_type =models.CharField(max_length=40,choices=MODE_OF_PAYMENT)
    company = models.CharField(max_length=100)
    def __str__(self):
        return self.company
    
class Subscription(models.Model):
    user = models.ForeignKey(ServiceUser,on_delete=models.CASCADE)
    services = models.ForeignKey(Services,on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.name


