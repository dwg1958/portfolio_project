####################################
# PICTURES APP VIEWS FILE ##########
####################################

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pictures/home.html') #extra folder so we can see where it is and avoid name clash across apps
