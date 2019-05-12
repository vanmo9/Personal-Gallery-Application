from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
# import datetime as dt 
from .models import Location,Photo,Category

# Create your views here.

def welcomen(request):
    photos = Photo.objects.all()
    locations = Location.objects.all()
    categorys = Category.objects.all()
    return render(request, 'index.html',{'photos':photos,'locations':locations,'categorys':categorys})



def search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_locations = Photo.search_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'photo/search.html',{"message":message,"location": searched_locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photo/search.html',{"message":message})  


