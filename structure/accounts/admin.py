from django.contrib import admin

# Register your models here.
from structure.accounts.models.usersetup import (
    User
)

admin.site.register(User)