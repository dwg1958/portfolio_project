from django.shortcuts import render

# go get the data model
from .models import Blog

# Create your views here.
def allblogs(request):
    # Collect data from db via the data model to the page
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {"blogs":blogs})

def oneblog(request):
    return render(request, 'blog/oneblog.html')
