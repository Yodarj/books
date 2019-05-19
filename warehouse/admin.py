from django.contrib import admin

from warehouse.models import Book

class BookAdmin(admin.ModelAdmin):
    """ModelAdmin class for Book model"""
    fieldsets =[
        ("Title, authors, date, categories", {"fields": ["title", "authors", "publishedDate", "categories"]}),
        ("Description", {"fields": ["description"]})
    ]


    # list_display = ('pk', 'title', 'authors', 'publishedDate',)
    # search_fields = ('title',)
    # ordering = ('publishedDate', 'title',)

admin.site.register(Book, BookAdmin)