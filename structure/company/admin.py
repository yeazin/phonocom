from django.contrib import admin
from structure.company.models.plans import (
    Plans
)
from structure.company.models.company import (
    Company,
    CompanySubscription
)

## Company admin
class CompanyAdmin(admin.ModelAdmin):

    list_display = ['id','name','digitprefix']

admin.site.register(Company,CompanyAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id','company','customer','phoneNumber']

admin.site.register(CompanySubscription,SubscriptionAdmin)

