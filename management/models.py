from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  #blank=True, creation of a customer without a user not necessarily being attched to it 
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, null=True)
    email =models.CharField(max_length=30, null=True)
    profile_pic = models.ImageField(default="",null=True, blank=True)# if no prof pic, creates a silhouette
    date =models.DateTimeField(auto_now_add=True, null=True)

def __str__(self):
    return self.name

class Tag(models.Model):
    name = models.CharField(max_length=15, null=True)

def __str__(self):
    return self.name

class Product(models.Model):
    CATEGORY=(
        ('indoor','indoor'),
        ('outdoor','outdoor')
    )
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=15, null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    description = models.CharField(max_length=255, null=True)
    Date = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

def __str__(self):
    return self.category



class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('Delivered','Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=255, null=True, choices=STATUS)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)
    note = models.CharField(max_length=1000, null=True)

def __str__(self):
    return self.product.name