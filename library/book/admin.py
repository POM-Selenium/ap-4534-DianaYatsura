from django.contrib import admin
from .models import Book
from order.models import Order
from django.contrib.admin import RelatedOnlyFieldListFilter


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_authors', 'count')
    list_filter = ('id', 'name', ('authors', RelatedOnlyFieldListFilter),)
    search_fields = ('id', 'name', 'authors__name', 'authors__surname')
    
    fieldsets = (
        ('Book Data', {
            'fields': ('name', 'authors', 'id')
        }),
        ('Inventory', {
            'fields': ('count', 'description'),
        }),
        ('Orders Data', {
            'fields': ('get_status', 'get_last_end_at')
        }),
    )
    readonly_fields = ('id', 'get_status', 'get_last_end_at')

    
    def display_authors(self, obj):
        authors_list = []
        for author in obj.authors.all():
            full_name = f'{author.name} {author.surname}'
            authors_list.append(full_name)
        return ', '.join(authors_list)
            
    display_authors.short_description = 'Authors'

    def get_status(self, obj):
        last_order = Order.objects.filter(book=obj, end_at__isnull=True).last()
        if last_order:
            return "On Hands"
        return "Available"
        
    get_status.short_description = 'Current Status'

    def get_last_end_at(self, obj):
        last_order = Order.objects.filter(book=obj).order_by('-created_at').first()
        if last_order:
            if not last_order.end_at:
                return f"Due: {last_order.plated_end_at.strftime('%m/%d/%Y')}"
            return f"Returned: {last_order.end_at.strftime('%m/%d/%Y')}"
        return "No history"
        
    get_last_end_at.short_description = 'Last Transaction Date'
    

admin.site.register(Book, BookAdmin)
