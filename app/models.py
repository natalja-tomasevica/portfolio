from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    age = models.IntegerField(null=True, blank=True)
    languages = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.full_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    