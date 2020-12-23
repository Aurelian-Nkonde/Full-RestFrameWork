from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    LANGUEGES = (
        ('E', 'English'),
        ('S', 'Spanish'),
        ('F', 'French'),
        ('M', 'Mandarin'),
        ('G', 'Germany'),
    )

    GENRES = (
        ('T', 'Thriller'),
        ('R', 'Romantic'),
        ('A', 'Action'),
        ('C', 'Cooking'),
        ('E', 'Education'),
    )

    title = models.CharField(max_length=200)
    published_date = models.DateField()
    summary = models.TextField()
    ISBN = models.CharField(max_length=20)
    languege = models.CharField(max_length=1, choices=LANGUEGES,  default='English')
    genre = models.CharField(max_length=1, choices=GENRES, default='Education')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name