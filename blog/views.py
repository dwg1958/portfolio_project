from django.shortcuts import render, get_object_or_404

# go get the data model
from .models import Blog

# Create your views here.
def allblogs(request):
    # Collect data from db via the data model to the page
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {"blogs":blogs})

def oneblog(request, blog_id):
    blogpost = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/oneblog.html', {"blogpost":blogpost})
