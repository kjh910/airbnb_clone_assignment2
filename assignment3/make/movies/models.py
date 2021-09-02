from django.db import models
from core import models as core_models
# from categories import models as categories_models

class Movie(core_models.TimeStampedModel):
      title = models.TextField(max_length=128)
      year = models.TextField(max_length=4)
      cover_images = models.ImageField(upload_to="movie_photos")
      rating = models.IntegerField()
      category = models.ManyToManyField("categories.Category", related_name='movie' ,blank=True)
      director = models.ForeignKey("people.Person",on_delete=models.PROTECT)
      # cast = models.ManyToManyField("people.Person", blank=True)

"""
Here are the models you have to create:
- Movie:
  title
  year
  cover_image
  rating
  category (ManyToMany => categories.Category)
  director (ForeignKey => people.Person)
  cast (ManyToMany => people.Person)
"""