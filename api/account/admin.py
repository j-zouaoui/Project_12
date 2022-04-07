from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SalesContact, SupportContact

class EmployeeAdmin(UserAdmin):
    pass

admin.site.register(User, EmployeeAdmin)
admin.site.register(SalesContact)
admin.site.register(SupportContact)


"""
from django.contrib.auth.admin import UserAdmin
from .models import Employee

class EmployeeAdmin(UserAdmin):
    pass

admin.site.register(Employee, EmployeeAdmin)

"""