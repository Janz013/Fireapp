from django.shortcuts import render
from django.views.generic.list import ListView
from fire.models import Locations, Incident, FireStation

def map_station(request):
    # Fetch fire station data with name, latitude, and longitude
    fireStations = FireStation.objects.values('name', 'latitude', 'longitude')

    # Convert latitude and longitude to float for each fire station
    for fs in fireStations:
        fs['latitude'] = float(fs['latitude'])
        fs['longitude'] = float(fs['longitude'])

    # Convert QuerySet to a list
    fireStations_list = list(fireStations)

    # Context to pass to the template
    context = {
        'fireStations': fireStations_list,
    }

    # Render the template with context
    return render(request, 'map_station.html', context)

class HomePageView(ListView):
    model = Locations
    context_object_name = 'home'
    template_name = "home.html"
