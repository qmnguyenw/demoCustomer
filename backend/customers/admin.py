from django.contrib import admin
from .models import Customer

# add Customer field into admin page
admin.site.register(Customer)