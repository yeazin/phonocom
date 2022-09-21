'''
This file contains 
    - Company Views Logic
    - Company subscription logic
'''

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# importing models 
from structure.company.models.company import (
    Company,
    CompanySubscription
)

# importing APIs
from structure.company.serializer import (
    CompanyAPI,
    SimSubscriptionAPI
)

## Company Sim Subscription Create View 
class SimSubscriptionCreateView(GenericAPIView):
    queryset = CompanySubscription.objects.filter(is_active=True)
    serializer_class = SimSubscriptionAPI

    def post(self,request):

        apifetch = SimSubscriptionAPI(data=request.data)

        if apifetch.is_valid():
            apifetch.save()
            return Response({
                'success':'Customer Registered'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'Error':'Submission data not Valid'
            },status=status.HTTP_406_NOT_ACCEPTABLE)


'''
Comapny Functional Logic
    create
    delete 
    update 
    list
'''

# list , create
class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanyAPI


# update, view ,delete 
class CompanySingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanyAPI