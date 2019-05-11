from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
# import datetime as dt 
import .models import Location,Photo,Category

# Create your views here.

def welcomen(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categorys = Category.objects.all()
    return render(request, 'index.html',{'images':images,'locations':locations,'categorys':categorys})



def search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_location = Image.search_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'photo/search.html',{"message":message,"location": searched_location})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photo/search.html',{"message":message})  


