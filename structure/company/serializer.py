'''
This file contains the followings 
    - Plans API 
    - Plan subscription API
    - Company API 
    - Sim API
'''

from rest_framework import serializers

## importing models 
from structure.company.models.company import (
    Company,
    CompanySubscription
)
from structure.company.models.plans import (
    Plans,
    PlanSubscription
)

## Company API
class CompanyAPI(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name','digitprefix','description']
    
## Company Subscription 
class SimSubscriptionAPI(serializers.ModelSerializer):
    class Meta:
        model = CompanySubscription
        fields = ['company','customer','phoneNumber']



## Plans API

class PlansAPI(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ['planName','price','duration']


## Plans Subscription

class PlanSubscriptionAPI(serializers.ModelSerializer):
    class Meta:
        model = PlanSubscription
        fields = ['plan','customer','registered_sim']
