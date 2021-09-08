from django.urls import path
from categories import views as categories_view

urlpatterns = [
    path('', categories_view.CategoriesView.as_view(), name='categories'),
]
