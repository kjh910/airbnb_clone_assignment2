from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "cover_images",
        "rating",
        "director",
    )
    
    list_filter = (
        "title",
        "year",
        "cover_images",
        "rating",
        "director",
    )

