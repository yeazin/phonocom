'''
This file is the Root URL file
'''

from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions

## DRF ysgh settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="PhonoCom",
      default_version='v1',
      description="Phonocom Backend API",
      contact=openapi.Contact(email="contact@test.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # adding APP url 
    path('customer/',include('structure.accounts.urls')),
    path('',include('structure.company.urls')),


    # Redoc URL config 
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


### Admin panel Configure 
admin.site.site_header = "PhonoCom Admin Panel"
admin.site.site_title = "PhonoCom Backend"
admin.site.index_title = "Welcome to PhonoCom Dashboard"