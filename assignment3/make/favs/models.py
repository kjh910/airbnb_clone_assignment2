from django.db import models
from core import models as core_models

class FavList(core_models.TimeStampedModel):
      created_by = models.OneToOneField("users.User", on_delete=models.PROTECT)
      books = models.ManyToManyField("books.Book", blank=True)
      movies = models.ManyToManyField("movies.Movie", blank=True)
"""
Here are the models you have to create:
- FavList
  created_by (OneToOne => users.User)
  books (ManyToMany => books.Book)
  movies (ManyToMany => movies.Movie)
"""
