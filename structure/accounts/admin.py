from django.contrib import admin

# Register your models here.
from structure.accounts.models.usersetup import (
    User
)
from structure.accounts.models.customer import (
    Customer
)

admin.site.register(User)
admin.site.register(Customer)