'''
This file contains the 
Accounts  URl 
'''

from django.urls import path

# imporing views 
from structure.accounts.views.initUser import (
    RegisterView
)

urlpatterns = [
    path('',RegisterView.as_view())
]