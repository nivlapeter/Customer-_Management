from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer

def customer_profile(sender,instance,created,**kwargs):
    if created:
        group = Group.objects.get(name='customer')  #querying the customer group,automatically associates a group (customer) with the regitered user 
        instance.groups.add(group)


        Customer.objects.create(    # Creating the customer
            user=instance,
            name=instance.username,
        )

post_save.connect(customer_profile, sender=User)