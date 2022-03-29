from django.shortcuts import render
from .models import Image, Location, Category

# Create your views here.
def home(request):
    images=Image.get_images()
    locations=Location.objects.all()


    return render(request, 'home.html', {"images":images, "locations":locations})

def search_by_category(request):
    if 'image_category' in request.GET and request.GET["image_category"]:
        search_term=request.GET.get("image_category")
        searched_images=Image.search_by_category(search_term)
        return render(request, 'search.html', {"images":searched_images})
    
    else:
        message="No search term added"
        return render(request, 'search.html', {"message":message})

def photos_by_location(request, location_id):
    images=Image.filter_by_location(location_id)
    return render(request, 'locations.html', {"images":images})