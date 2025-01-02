from django.urls import path
from .views import FrontPagePageView, AboutPageView, SearchPageView, AccountPageView, RegisterPageView, BookListView, BookDetailView, BooksCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('', FrontPagePageView.as_view(), name = 'frontpage'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('search/', SearchPageView.as_view(), name = 'search'),
    path('account/', AccountPageView.as_view(), name = 'account'),   
    path('register/', RegisterPageView.as_view(), name = 'register'),   

    path('book/', BookListView.as_view(), name = 'book'),   
    path('book/<int:pk>', BookDetailView.as_view(), name = 'book_detail'),   
    path('books/create', BooksCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete')


]
