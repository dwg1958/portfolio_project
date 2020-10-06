"""
This is the urls.py for the blog section of the portfolio project ONLY
"""

from django.urls import path

from .import views   # not blog.views because we're in it


urlpatterns = [

    path( '', views.allblogs, name = "allblogs"),
    path( '1', views.oneblog, name = "oneblog"),

]
