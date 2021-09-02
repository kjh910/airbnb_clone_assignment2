from django.db import models
from core import models as core_models

class Book(core_models.TimeStampedModel):
      title=models.TextField(max_length=138)
      year = models.TextField(max_length=4)
      category = models.ManyToManyField("categories.Category", related_name='book', blank=True)
      cover_images = models.ImageField(upload_to="book_photos")
      rating = models.IntegerField()
      writer = models.ForeignKey("people.Person",on_delete=models.PROTECT)
"""
Here are the models you have to create:
- Book:
  title
  year
  category (ForeignKey => categories.Category)
  cover_image
  rating
  writer (ForeignKey => people.Person)
"""
