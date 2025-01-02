from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy

class FrontPagePageView(TemplateView):
    template_name = 'app/frontpage.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class SearchPageView(TemplateView):
    template_name = 'app/search.html'

class AccountPageView(TemplateView):
    template_name = 'app/account.html'

class RegisterPageView(TemplateView):
    template_name = 'app/register.html'

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'app/book_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'app/book_detail.html'

class BooksCreateView(CreateView):
     model = Book
     fields = ['title','description', 'body', 'genre', 'author', 'tags'] 
     template_name = 'app/book_create.html'

class BookUpdateView(UpdateView):
     model = Book
     fields = ['title','description', 'body', 'genre', 'author', 'tags'] 
     template_name = 'app/book_update.html'

class BookDeleteView(DeleteView):
     model = Book
     template_name = 'app/book_delete.html'
     success_url = reverse_lazy('book')
