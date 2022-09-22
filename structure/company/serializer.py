'''
This file contains the followings 
    - Plans API 
    - Plan subscription API
    - Company API 
    - Sim API
    - Tracking API
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
from structure.company.models.tracking import (
    TrackingCustomer
)
from structure.accounts.models.customer import (
    Customer
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
        fields = ['company','customer']



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


## Tracking API
class TrackingAPI(serializers.ModelSerializer):

    customer = serializers.SlugRelatedField(queryset=Customer.objects.filter(is_active=True),
    slug_field='firstName')

    class Meta:
        model = TrackingCustomer
        fields = [
            'id','customer','phoneNumber','offerName',
            'offerPrice','offerDuration','status'
            ]