from django.contrib import admin
from .models import *
from shop.models import UserData
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class UserDataInline(admin.StackedInline):
    model = UserData
    can_delete = False
    verbose_name_plural = 'app_users'
    
class UserAdmin(BaseUserAdmin):
    inlines = (UserDataInline,)

   
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

   
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональні дані', {'fields': ('first_name', 'last_name')}),
        ('Права доступу', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Важливі дати', {'fields': ('last_login', 'date_joined')}),
    )

  
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'first_name', 'last_name',
                'is_staff', 'is_active'
            ),
        }),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(CustomUser, UserAdmin)
