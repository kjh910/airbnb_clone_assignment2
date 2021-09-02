from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):
      
      created_by = models.OneToOneField("users.User", on_delete=models.PROTECT)
      text = models.TextField()
      movie = models.ForeignKey("movies.Movie",null=True,blank=True,on_delete=models.PROTECT)
      book = models.ForeignKey("books.Book",null=True,blank=True,on_delete=models.PROTECT)
      rating = models.IntegerField()

"""
Here are the models you have to create:
- Review
  created_by (ForeignKey => users.User)
  text
  movie (ForeignKey => movies.Movie, null,blank)
  book (ForeignKey => movies.Movie, null,blank)
  rating
"""
