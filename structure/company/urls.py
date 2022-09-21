'''
This file contains the followings
    - Plans URL 
    - Plans Subscription URL 
'''

from django.urls import path

# importing views
from structure.company.views.plans import (
    PlansView,
    PlanSingleView,
    PlanSubscriptionView
)
from structure.company.views.company import (
    CompanyView,
    CompanySingleView,
    SimSubscriptionCreateView
)

urlpatterns = []

plans_URL = [
    path('plan/',PlansView.as_view()),
    path('plan/<int:pk>/',PlanSingleView.as_view()),
    path('plan/subscription/',PlanSubscriptionView.as_view())
]

company_URL = [
    path('company',CompanyView.as_view()),
    path('company/,<int:pk>/',CompanySingleView.as_view()),
    path('company/subscription',SimSubscriptionCreateView.as_view())
]

urlpatterns += plans_URL
urlpatterns += company_URL