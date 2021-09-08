from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class PeopleView(ListView):
    template_name='people.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)