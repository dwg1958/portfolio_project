####################################
# PICTURES APP VIEWS FILE ##########
####################################

from django.shortcuts import render

# go get the data model
from .models import Picture

# Create your views here.
def home(request):
    # Collect data from db via the data model to the page
    pictures = Picture.objects

    # Now fire up the HTML page with data..
    return render(request, 'pictures/home.html', {"pictures": pictures} )
    # (notice the extra 'pictures sub-folder so we can see
    # where it is and avoid name clash across apps..)
