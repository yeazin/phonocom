'''
This file contains the following 
    - singals will go when Subscription created 
    - '''

import random
from django.dispatch import receiver
from django.db.models.signals import post_save

from mainConfig.scripts.numbergenerate import unique_Pnumber_generate
# importing models 
from structure.company.models.company import (
    CompanySubscription
)


## Phone number will be automated 
# when subscription created 

@receiver(post_save, sender=CompanySubscription)
def PhoneNumberCreate(sender,instance,created,*args,**kwargs):
    try:
        if created:
            instance.phoneNumber = f"{instance.company.digitprefix}{unique_Pnumber_generate(instance)}"
            instance.save()
    except Exception as e:
        print(e)

        