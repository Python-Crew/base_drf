from django.contrib import admin
from .models import *

admin.site.site_header = 'FAQ Dashboard'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # readonly_fields = ['',]
    list_display = ('name','parent')
    list_filter = ['name', 'parent']
    list_per_page = 20
    actions_selection_counter = True
    # date_hierarchy = 'name'
    search_fields = ('name','parent')
    ordering = ('name', )