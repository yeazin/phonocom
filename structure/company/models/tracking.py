'''
This file contains the following 
    - Database of Tracking Customer 
        when the Buy an offer and 
        Cancel the offer 
'''

from django.db import models
from mainConfig.models import InitModels


## Tracking Database 

select_status = (
    ('1','Activate'),
    ('2','Cancel')
)

class TrackingCustomer(InitModels):

    customer = models.ForeignKey(
        'accounts.Customer',on_delete= models.SET_NULL,
        null=True,verbose_name="Customer Name"
    )
    phoneNumber = models.CharField(
        max_length=11,null=True,verbose_name="Phone Number"
    )
    offerName = models.CharField(
        max_length=100, null=True,
        verbose_name="Offer Name"
    )
    offerPrice = models.FloatField(default=0,null=True)
    offerDuration = models.CharField(
        max_length=100, null=True,
        verbose_name="Offer Duration"
    )
    status = models.CharField(
        max_length=15,null=True,
        choices=select_status,
        verbose_name="Offer Status"
    )


    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Customer Offer Tracking"
        indexes = [models.Index(fields=['id','customer'])]