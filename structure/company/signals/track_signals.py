'''
This file contains the followings
    - Obj will be created via Plan subscription 
    - obj will status will be changed via plan subscription 
'''

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

# importing models 
from structure.company.models.plans import (
    PlanSubscription
)
from structure.company.models.tracking import (
    TrackingCustomer
)

## Tracking subscription will be created when 
#  Plans Subscription / a customer buy new offer

@receiver(post_save, sender=PlanSubscription)
def ActivateTrackingOBJ(sender,instance,created,*args,**kwargs):
    if created:
        tracking_obj = TrackingCustomer(
            customer = instance.customer,
            phoneNumber = instance.registered_sim,
            offerName = instance.plan.planName,
            offerPrice= instance.plan.price,
            offerDuration = instance.plan.duration,
            status = '1'
        )
        tracking_obj.save()


## Tracking subscription status will show Deactivated when 
#  Plans Subscription / a customer  Cancel its offer

@receiver(pre_delete, sender=PlanSubscription)
def DeactivateTrackObj(sender,instance,using,*arg,**kwargs):

    tracking_obj = TrackingCustomer(
        customer = instance.customer,
        phoneNumber = instance.registered_sim,
        offerName = instance.plan.planName,
        offerPrice= instance.plan.price,
        offerDuration = instance.plan.duration,
        status = '2'
    )
    tracking_obj.save()