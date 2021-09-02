from django.db import models
from core import models as core_models

class Person(core_models.TimeStampedModel):
      
      PER_ACTOR = "actor"
      PER_DIRECTOR = "director"
      PER_WRITER = "writer"
      PER_CHOICES = (
        (PER_ACTOR, "Actor"), 
        (PER_DIRECTOR, "Director"),
        (PER_WRITER, "Writer"),
      )
      
      name = models.TextField(max_length=128)
      kind = models.CharField(
        max_length=20, choices=PER_CHOICES
      )
      photo = models.ImageField(upload_to="person_photos")
      

"""
- Person
  name
  kind (choice=Actor/Director/Writer)
  photo
"""
