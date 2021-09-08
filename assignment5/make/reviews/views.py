from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class ReviewsView(ListView):
    template_name='reviews.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)