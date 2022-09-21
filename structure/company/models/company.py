'''
This file contains the followings
    - Company database
    - Company register with user 
'''

from django.db import models 
from mainConfig.models import InitModels


## Company Database 
class Company(InitModels):

    name = models.CharField(
        max_length=100,null=True,
        verbose_name="Company Name"
    )
    digitprefix = models.CharField(
        max_length=3,null=True,
        verbose_name="Digit Prefix"
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = " Company "
        # indexes = [models.indexes(fields = ['id'])]



## The database of 
# Customer Register to Company 
# with their 

class CompanySubscription(InitModels):
    company = models.ForeignKey(
        'company.Company',null=True,
        on_delete= models.CASCADE,
        verbose_name=" Company Name",
        related_name="subscription"
    )
    customer = models.ForeignKey(
        'accounts.Customer',null=True,
        on_delete= models.CASCADE,
        verbose_name="Customer",
        related_name="company"
    )
    phoneNumber = models.CharField(
        max_length=11,null=True,
        unique=True,verbose_name="Phone Number",
        blank=True
    )

    def __str__(self):
        return str(self.phoneNumber)

    
    class Meta:
        verbose_name_plural = "Sim Subscription"
        indexes = [models.Index(fields = ['id','company','customer'])]