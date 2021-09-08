from django.urls import path
from people import views as people_view

urlpatterns = [
    path('', people_view.PeopleView.as_view(), name='people'),
]
