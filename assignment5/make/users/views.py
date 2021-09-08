from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class UsersView(ListView):
    template_name='users.html'
    queryset=""
    
    def get(self, request):
        return super().get(request)