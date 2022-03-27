from django.shortcuts import render
from .models import Image, Location, Category

# Create your views here.
def home(request):
    images=Image.get_images()

    return render(request, 'home.html', {"images":images})

def search_by_category(request):
    if 'image_category' in request.GET and request.GET["image_category"]:
        search_term=request.GET.get("image_category")
        searched_images=Image.search_by_category(search_term)
        return render(request, 'search.html', {"images":searched_images})
    
    else:
        message="No search term added"
        return render(request, 'search.html', {"message":message})