from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(verbose_name="Nombre del libro", max_length=50)
    author = models.CharField(verbose_name="Autor del libro", max_length=75)
    price = models.FloatField(verbose_name="Precio")
    preview = models.FileField(upload_to="books/", verbose_name="Adjunto del libro")

    def __str__(self):
        return self.name
