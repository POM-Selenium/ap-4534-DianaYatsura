from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    list_filter = ('surname',)
    
    fields = [('name', 'surname'), 'patronymic', 'id']
    readonly_fields = ('id',)

admin.site.register(Author, AuthorAdmin)
