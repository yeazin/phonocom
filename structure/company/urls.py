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
    PlanSubscriptionView,
    PlanSubsListView,
    PlanSubSingleView
)
from structure.company.views.company import (
    CompanyView,
    CompanySingleView,
    SimSubscriptionCreateView,
    SimSubsListView,
    SimSubsSingleView
)
from structure.company.views.tracking_views import (
    ActiveTrackingViews,
    CanceledTrackingViews
)

urlpatterns = []

tracking_URL = [
    path('tracking/activate/',ActiveTrackingViews.as_view()),
    path('tracking/canceled/',CanceledTrackingViews.as_view()),
]

plans_URL = [
    path('plan/',PlansView.as_view()), 
    path('plan/<int:pk>/',PlanSingleView.as_view()),
    path('plan/subscription/',PlanSubscriptionView.as_view()),
    path('plan/subscription/',PlanSubsListView.as_view()),
    path('plan/subscription/<int:pk>/', PlanSubSingleView.as_view())
]

company_URL = [
    path('company/',CompanyView.as_view()),
    path('company/<int:pk>/',CompanySingleView.as_view()),
    path('company/subscription/',SimSubscriptionCreateView.as_view()),
    path('company/subscription/',SimSubsListView.as_view()),
    path('company/subscription/<int:pk>/',SimSubsSingleView.as_view())
]


urlpatterns += tracking_URL
urlpatterns += plans_URL
urlpatterns += company_URL