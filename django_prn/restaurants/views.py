from django.db.models import Q
from django.shortcuts import render
from .models import Restaurants
from django.views.generic import TemplateView, ListView

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Restaurants 
    template_name = 'search_results.html'

    def get_queryset(self):  
        query = self.request.GET.get("q")
        object_list = Restaurants.objects.filter(
            Q(name__icontains=query))
        return object_list