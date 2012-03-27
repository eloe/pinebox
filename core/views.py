from django.shortcuts import render_to_response
from core.models import Brewery, Beer

def index(request):
    
    breweries = list(Brewery.objects.all().order_by('name'))
    beers = list(Beer.objects.all().order_by('name'))
    
    return render_to_response("core/index.html", {
        "breweries" : breweries,
        "beers" : beers
    })