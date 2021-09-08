from django.urls import path
from reviews import views as reviews_view

urlpatterns = [
    path('', reviews_view.ReviewsView.as_view(), name='reviews'),
]
