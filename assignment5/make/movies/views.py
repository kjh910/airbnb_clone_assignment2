from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class MoviesView(ListView):
    template_name='movies.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)