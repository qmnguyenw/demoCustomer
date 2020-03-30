from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'age', 'active']}),
    ]
    list_display = ('name', 'age', 'active')
    list_filter = ['id']
    search_fields = ['name']
    # list_per_page = 3

# add Customer field into admin page
admin.site.register(Customer, CustomerAdmin)