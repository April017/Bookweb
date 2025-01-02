from django.db import models
from django.urls import reverse


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)  
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.username  
    
class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='authored_books',default=1  # Replace 1 with the ID of a valid user in your database
                               )
    def __str__(self):
        return f"Author: {self.user.username}"

    
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=600)
    author = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True) 
    description = models.TextField()
    body = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')
    tags = models.ManyToManyField(Tag, related_name='books', blank=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})



