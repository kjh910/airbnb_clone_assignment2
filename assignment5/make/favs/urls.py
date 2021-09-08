from django.urls import path
from favs import views as favs_view

urlpatterns = [
    path('', favs_view.FavsView.as_view(), name='favs'),
]
