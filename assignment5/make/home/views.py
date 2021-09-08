from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class HomeView(ListView):
    template_name='home.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)
    
class SearchView(ListView):
    template_name='search.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)
    
class GenresView(ListView):
    template_name='genres.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)