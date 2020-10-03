from django.contrib import admin

# Register your models here so admin screen can see them.
from .models import Blog

admin.site.register(Blog)
