from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import InstructorProfile, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + \
        (('Rol personalizado', {
         'fields': ('is_instructor',)}),)  # type: ignore
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('is_instructor',)}),
    )


admin.site.register(InstructorProfile)
