from django.shortcuts import render
from books.models import Book
from books.forms import BookForm
# Create your views here.
def index(request):
    formulario = BookForm()
    if request.method =="GET":
        print("GET method")
    else:
        print(request.POST)
        formulario = BookForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            print("Algo pasó")


        print("POST method")

    context = {
        "formulario": formulario,
        "books": Book.objects.all() # select * from book
    }
    return render(request, 'books/index.html', context)
