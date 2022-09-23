'''
This file contains 
    - Plans URL Test
    - Company URL Test
    - Tracking URL test
'''

from django.test import SimpleTestCase
from django.urls import (
    resolve
)
# importing views
from structure.company.views.plans import (
    PlansView,
    PlanSingleView,
    PlanSubscriptionView,
    PlanSubSingleView
)
from structure.company.views.company import (
    CompanyView,
    CompanySingleView,
    SimSubscriptionCreateView,
    SimSubsSingleView
)
from structure.company.views.tracking_views import (
    ActiveTrackingViews,
    CanceledTrackingViews
)

## Test case for Tracking Module
class TrackTestCase(SimpleTestCase):

    def test_activate(self):
        resolver = resolve('/tracking/activate/')
        self.assertEqual(resolver.func.__name__, ActiveTrackingViews.as_view().__name__)

    
    def test_Cancel(self):
        resolver = resolve('/tracking/canceled/')
        self.assertEqual(resolver.func.__name__, CanceledTrackingViews.as_view().__name__)

    
## Test Case for Plans Module
class PlanTestCase(SimpleTestCase):
    
    def test_plan_view(self):
        resolver = resolve('/plan/')
        self.assertEqual(resolver.func.__name__, PlansView.as_view().__name__)

    
    def test_plan_single(self):
        resolver = resolve('/plan/1/',)
        self.assertEqual(resolver.func.__name__, PlanSingleView.as_view().__name__)

    def test_plan_subscription(self):
        resolver = resolve('/plan/subscription/')
        self.assertEqual(resolver.func.__name__,PlanSubscriptionView.as_view().__name__)
    
    def test_plan_subscription_single(self):
        resolver = resolve('/plan/subscription/1/')
        self.assertEqual(resolver.func.__name__, PlanSubSingleView.as_view().__name__)

## Test Case for Company Module
class CompanyTest(SimpleTestCase):

    def test_company_view(self):
        resolver = resolve('/company/')
        self.assertEqual(resolver.func.__name__, CompanyView.as_view().__name__)

    def test_company_single(self):
        resolver = resolve('/company/1/')
        self.assertEqual(resolver.func.__name__, CompanySingleView.as_view().__name__)

    def test_sim_create_view(self):
        resolver = resolve('/company/subscription/')
        self.assertEqual(resolver.func.__name__, SimSubscriptionCreateView.as_view().__name__)

    def test_sim_single_view(self):
        resolver = resolve('/company/subscription/1/')
        self.assertEqual(resolver.func.__name__, SimSubsSingleView.as_view().__name__)

