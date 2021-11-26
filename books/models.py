from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(verbose_name="Nombres", max_length=50)
    last_name = models.CharField(verbose_name="Apellidos", max_length=50)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    name = models.CharField(verbose_name="Nombre del libro", max_length=50)
    author = models.ForeignKey(Author, related_name="books",verbose_name="Autor", on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="Precio")
    preview = models.FileField(upload_to="books/", verbose_name="Adjunto del libro")

    def __str__(self):
        return self.name

class Reader(models.Model):
    first_name = models.CharField(verbose_name="Nombres", max_length=50)
    last_name = models.CharField(verbose_name="Apellidos", max_length=50)
    readed_books = models.ManyToManyField(Book, related_name="readers")
    

    def __str__(self):
        return self.first_name + " " + self.last_name
