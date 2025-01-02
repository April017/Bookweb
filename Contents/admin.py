from django.contrib import admin
from .models import User, Author, Genre, Tag, Book

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Book)
