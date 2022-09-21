'''
This file contains the following 
    - user registrations
    - check user
'''


from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status

# importing models
from structure.accounts.models.usersetup import(
    User
)
from structure.accounts.models.customer import (
    Customer
)
# importing API
from structure.accounts.serializer import (
    CustomerAPI
)


## Register View 

class RegisterView(GenericAPIView):
    serializer_class = CustomerAPI
    queryset = Customer.objects.filter(is_active=True)

    def post(self,request):

        apifetch = CustomerAPI(data=request.data)
        if apifetch.is_valid():
            '''
            Apifetch will return 
                - Password Validataion 
                - validated customer will be saved
            '''
            password1 = apifetch.validated_data['password']
            password2 = apifetch.validated_data['confirm_password']

            if password1 != password2:
                return Response({
                    'Error':'Password & Confirm Password Didn`t match'
                },status=status.HTTP_406_NOT_ACCEPTABLE)

            else :
                apifetch.save()
                return Response(
                    {'Success':'User Created'},
                    status=status.HTTP_201_CREATED
                )
        else:
            return Response(apifetch.error_messages)
