from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class CategoriesView(ListView):
    template_name='categories.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)