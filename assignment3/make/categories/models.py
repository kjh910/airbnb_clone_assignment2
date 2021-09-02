from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):
      
      PREF_BOOKS = "books"
      PREF_MOVIES = "movies"
      PREF_BOTH = "both"
      PREF_CHOICES = (
        (PREF_BOOKS, "Books"), 
        (PREF_MOVIES, "Movies"),
        (PREF_BOTH, "both"),
      )
      
      name = models.TextField(max_length=128)
      kind = models.CharField(
        max_length=20, choices=PREF_CHOICES
      )
      
      
"""
Here are the models you have to create:
- Category
  name
  kind (book/movie/both)
"""
