from django.contrib import admin
from .models import  Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'languege', 'genre')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death',)