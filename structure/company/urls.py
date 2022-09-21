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
from structure.company.views.company import (
    SimSubscriptionCreateView
)

urlpatterns = []

plans_URL = [
    path('plan/subscription/',PlanSubscriptionView.as_view())
]

company_URL = [
    path('company/subscription',SimSubscriptionCreateView.as_view())
]

urlpatterns += plans_URL
urlpatterns += company_URL