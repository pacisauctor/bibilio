from django.shortcuts import render
from django.urls import reverse_lazy
from books.models import Book, Reader
from books.forms import BookForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class ReaderList(ListView):
    model = Reader
    
class ReaderDetail(DetailView):
    model = Reader
    
class ReaderCreation(CreateView):
    model = Reader
    success_url = reverse_lazy("readers:list")
    fields = '__all__'
    
class ReaderUpdate(UpdateView):
    model = Reader
    success_url = reverse_lazy("readers:list")
    fields = '__all__'
    
class ReaderDelete(DeleteView):
    model = Reader
    success_url = reverse_lazy("readers:list")
    
    