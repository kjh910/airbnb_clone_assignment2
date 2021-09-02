from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class PersonAdmin(admin.ModelAdmin):

    list_display = (
        "created_by",
        "text",
        "movie",
        "book",
        "rating",
    )
    
    list_filter = (
        "created_by",
        "text",
        "movie",
        "book",
        "rating",
    )

