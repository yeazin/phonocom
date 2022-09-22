from django.contrib import admin
from structure.company.models.plans import (
    Plans,
    PlanSubscription
)
from structure.company.models.company import (
    Company,
    CompanySubscription
)
from structure.company.models.tracking import (
    TrackingCustomer
)

## Company admin
class CompanyAdmin(admin.ModelAdmin):

    list_display = ['id','name','digitprefix']

admin.site.register(Company,CompanyAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id','company','customer','phoneNumber']

admin.site.register(CompanySubscription,SubscriptionAdmin)
admin.site.register(Plans)

class PlansAdmin(admin.ModelAdmin):
    list_display = ['id','plan','customer','registered_sim']

admin.site.register(PlanSubscription,PlansAdmin)

class TrackingAdmin(admin.ModelAdmin):
    list_display = ['id','customer','offerName','status']

admin.site.register(TrackingCustomer, TrackingAdmin)

