'''
This file contains the database 
setup of 
Customer '''


from django.db import models
from django.db.models.signals import pre_save

## importing init models
from mainConfig.models import InitModels
# importing scripts 
from mainConfig.scripts.numbergenerate import unique_Pnumber_generate
## Customer Models

class Customer(InitModels):
    
    user = models.OneToOneField(
        'accounts.User',on_delete=models.CASCADE,null=True,
        verbose_name="Customer Name", related_name="customer"
    )
    firstName = models.CharField(
        max_length=200,null=True,verbose_name="First Name"
        )
    lastName = models.CharField(
        max_length=200,null=True,verbose_name="Last Name"
    )
    phoneNumber = models.CharField(
        max_length=11,unique=True,
        null=True,verbose_name="Phone Number",
        blank=True
    )
    wallet = models.FloatField(default=0,null=True,verbose_name="Wallet")


    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name_plural = "Customer"
        indexes = [models.Index(fields=['id','user','phoneNumber'])]

## Creating Unique phone number in creating customer instance 
def make_customer_ID(sender,instance,*args,**kwargs):
    if not instance.phoneNumber:
        instance.phoneNumber =f"011{unique_Pnumber_generate(instance)}" 

pre_save.connect(make_customer_ID,sender=Customer)
    