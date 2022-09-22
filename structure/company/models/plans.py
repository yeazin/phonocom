'''
This file contains database 
Plans 
'''

from django.db import models
from mainConfig.models import InitModels


class Plans(InitModels):
    planName = models.CharField(
        max_length=100,null=True,verbose_name="Plan Name"
        )
    price = models.FloatField(
        default=0,null=True,verbose_name="Price"
        )
    duration = models.CharField(
        max_length=50,null=True,verbose_name="Duration"
    )

    def __str__(self):
        return self.planName

    class Meta:
        verbose_name_plural = " Plans "


### Database of Plan Subscription between customer and plans

class PlanSubscription(InitModels):

    plan = models.ForeignKey(
        'company.Plans',on_delete=models.CASCADE,null=True,
        verbose_name="Plan Name"
        )
    customer = models.ForeignKey(
        'accounts.Customer',on_delete=models.CASCADE,
        null=True,verbose_name="Customer Name"
    )
    registered_sim = models.ForeignKey(
        'company.CompanySubscription',on_delete=models.CASCADE,
        null=True,verbose_name="Customer Registered Sim"
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Plan Subscription"
        indexes = [models.Index(fields = ['id','plan','customer'])]