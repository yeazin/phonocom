'''
This file contains the followings
    - Plans URL 
    - Plans Subscription URL 
'''

from django.urls import path

# importing views
from structure.company.views.plans import (
    PlanSubscriptionView
)

urlpatterns = [
    path('plan/subscription/',PlanSubscriptionView.as_view())
]