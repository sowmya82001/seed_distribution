from django.contrib import admin
from .models import Farmer, Seed, Distribution, Contact  # Import Contact model

# Register models to appear in Django admin panel
admin.site.register(Farmer)
admin.site.register(Seed)
admin.site.register(Distribution)
admin.site.register(Contact)  # Add Contact model
