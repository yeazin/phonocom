'''
This file contains the followings 
    - Tracking Views 
    - Active Tracking Views
    - Cancel Tracking views
'''

# importing initials 

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# importing models 
from structure.company.models.tracking import (
    TrackingCustomer
)
# importing API
from structure.company.serializer import (
    TrackingAPI
)


'''
Tracking Views Activate 
'''

class ActiveTrackingViews (generics.ListAPIView):
    queryset = TrackingCustomer.objects.filter(
        is_active=True,
        status='1'
    )
    serializer_class = TrackingAPI


'''
Cancel Tracking Views
'''

class CanceledTrackingViews (generics.ListAPIView):
    queryset = TrackingCustomer.objects.filter(
        is_active=True,
        status='2'
    )
    serializer_class = TrackingAPI
