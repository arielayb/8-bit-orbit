from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Satellite

# Create your views here.

class IndexView(generic.ListView):
    template_name = "satorbit/index.html"
    context_object_name = "latest_satellite_list"
    
    def get_queryset(self):
        return Satellite.objects.order_by("-pub_date")[:50]

class DetailView(generic.DetailView):
    model = Satellite
    template_name = "satorbit/detail.html"
    

class ResultsView(generic.DetailView):
    model = Satellite
    template_name = "satorbit/results.html"
