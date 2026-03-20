from django.contrib import admin
from .models import CustomUser



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')

    list_filter = ('last_name', 'is_superuser')

admin.site.register(CustomUser, CustomUserAdmin)
