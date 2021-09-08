from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class FavsView(ListView):
    template_name='favs.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)