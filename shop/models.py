from django.db import models

# Create your models here.
class policy(models.Model):
    policy_id = models.IntegerField()
    policy_name=models.CharField(max_length=50)
    policy_period=models.IntegerField()
    policy_price=models.IntegerField()
    policy_description=models.TextField()
    image1=models.ImageField(upload_to='pics')
class customer(models.Model):
    aadhar_card_number = models.IntegerField(unique=True,default=1)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Email_address = models.EmailField(default='insuranceex@gmail.com')
    Address = models.CharField(max_length=200)
    Postal_Code = models.IntegerField(default=0)
    Password = models.IntegerField(default=0)
    Phone_number = models.IntegerField(default=0)
class user_policy(models.Model):
    Aadhar_card_number = models.ForeignKey(customer, on_delete=models.CASCADE)
    policy_id=models.ForeignKey(policy,on_delete=models.CASCADE)
    transaction_no=models.IntegerField()