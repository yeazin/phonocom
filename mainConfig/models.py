'''
This file is a init models of 
every models 
'''

from django.db import models




'''
Initial Models for every models 

'''

class InitModels(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    class Meta:
        abstract = True