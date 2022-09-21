'''
This file contains the followings 
    - Plan Views 
    - plan Subscription
'''

# importing initials 

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


# importing models 
from structure.company.models.plans import (
    Plans,
    PlanSubscription
)
from structure.accounts.models.customer import (
    Customer
)
# importing APIs 
from structure.company.serializer import (
    PlansAPI,
    PlanSubscriptionAPI
)



## Plans Subsciption View 
class PlanSubscriptionView(GenericAPIView):
    queryset = PlanSubscription.objects.filter(is_active=True)
    serializer_class = PlanSubscriptionAPI

    def post(self,request):
        apifetch = PlanSubscriptionAPI(data= request.data)
        if apifetch.is_valid():

            ## getting sim number
            getSim = apifetch.validated_data['registered_sim']
            ## getting customer ID 
            getCustomer = apifetch.validated_data['customer']
            customerObj = Customer.objects.filter(id=getCustomer.id).first()

            ## getting Plans ID 
            getPlans = apifetch.validated_data['plan']
            planObj = Plans.objects.filter(id=getPlans.id).first()

            ## checking if the customer Already Registered to the plan
            if PlanSubscription.objects.filter(
                plan = getPlans,
                customer = getCustomer,
                registered_sim = getSim 
            ):
                return Response({
                    'Error':'Customer Already Registered with this Number'
                },status=status.HTTP_206_PARTIAL_CONTENT)

            ## Checking if the customer wallet is sufficient for buying the Plan
            elif customerObj.wallet < planObj.price:
                return Response({
                    'Sufficient Error':'Customer`s wallet not Sufficient'
                },status=status.HTTP_406_NOT_ACCEPTABLE)

            ## If above everything is OK then we register the Customer to the plan
            else:
                # we need to deduct the money after buying the Plan from 
                # customer wallet
                deduction = customerObj.wallet - planObj.price
                customerObj.wallet = deduction
                customerObj.save()
                # saving the Data
                apifetch.save()

                return Response({
                    'Success':'Customer Registration Success'
                },status=status.HTTP_201_CREATED)

        else:
            return Response(apifetch.errors)


'''
Plans Functional View s
    Create
    Update
    view 
    list
    delete
'''

# Create  & list view 

class PlansView(generics.ListCreateAPIView):
    queryset = Plans.objects.filter(is_active=True)
    serializer_class = PlansAPI

# Update , view , delete 

class PlanSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plans.objects.filter(is_active=True)
    serializer_class = PlansAPI

    