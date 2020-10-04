from django.contrib import admin

# Register your models here.
from .models import Picture

# Tell admin site to show it for editing
admin.site.register(Picture)
