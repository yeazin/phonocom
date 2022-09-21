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
        # indexes = [models.indexes(fields=['id'])]