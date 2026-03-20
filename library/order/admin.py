from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'created_at', 'plated_end_at')
    list_filter = ('plated_end_at',)         
    
admin.site.register(Order, OrderAdmin)
