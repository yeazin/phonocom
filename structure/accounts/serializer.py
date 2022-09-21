'''
This file contains the api 
'''


from rest_framework import serializers
from django.contrib.auth.hashers import make_password

# importing models 
from structure.accounts.models.customer import Customer
from structure.accounts.models.usersetup import User


## Customer Serializer 
class CustomerAPI(serializers.ModelSerializer):

    # define password and confirm password 
    password = serializers.CharField(style={'input_type':'password'})
    confirm_password = serializers.CharField(style={'input_type':'password'})

    class Meta:
        model = Customer
        fields = ['user','firstName','lastName','password','confirm_password']

    def create(self,validated_data):
        password1 = validated_data.pop('password')
        password2 = validated_data.pop('confirm_password')

        auth_info = {
            'password':make_password(password1),
            'confirm_password':make_password(password2)
        }
        userobj = User(**auth_info)
        userobj.save()
        
        customer_obj = Customer.objects.create(**validated_data)
        customer_obj.user = userobj

        return customer_obj
        

