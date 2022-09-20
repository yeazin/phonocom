'''
This file contains the database 
setup of 
Customer '''


from django.db import models

## importing init models
from mainConfig.models import InitModels


## Customer Models

class Customer(InitModels):
    
    user = models.OneToOneField(
        'accounts.User',on_delete=models.CASCADE,
        verbose_name="Customer Name", related_name="customer"
    )
    firstName = models.CharField(
        max_length=200,null=True,verbose_name="First Name"
        )
    lastName = models.CharField(
        max_length=200,null=True,verbose_name="Last Name"
    )
    phoneNumber = models.IntegerField(
        unique=True
    )
    
    