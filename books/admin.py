from django.contrib import admin
from books.models import Book, Reader, Author
# Register your models here.
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Author)
