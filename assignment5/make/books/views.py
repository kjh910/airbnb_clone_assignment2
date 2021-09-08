from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class BooksView(ListView):
    template_name='books.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)