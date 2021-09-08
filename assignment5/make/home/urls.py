from django.urls import path
from home import views as home_view

urlpatterns = [
    path('', home_view.HomeView.as_view(), name='home'),
    path('search/', home_view.SearchView.as_view(), name='search'),
    path('genres/', home_view.GenresView.as_view(), name='genres'),
]
