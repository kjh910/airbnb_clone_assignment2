from django.urls import path
from movies import views as movies_view

urlpatterns = [
    path('', movies_view.MoviesView.as_view(), name='movies'),
]
