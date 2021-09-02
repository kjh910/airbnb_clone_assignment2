from django.contrib import admin
from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "cover_images",
        "rating",
        "writer",
    )

    list_filter = (
        "title",
        "year",
        "cover_images",
        "rating",
        "writer",
    )
