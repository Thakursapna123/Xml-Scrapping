from django.contrib import admin
from .models import Student,User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id','email','first_name','city','last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Details', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','city')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name','city', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('id','email',)
 
    filter_horizontal = ()

    
admin.site.register(User, UserModelAdmin)
admin.site.register(Student)