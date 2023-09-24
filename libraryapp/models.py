from django.db import models
from django.contrib import admin

class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    date_published = models.DateField(auto_now_add=True)
    authors = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class PhysicalBook(models.Model):
    shelfLocation = models.CharField(max_length=50)
    isAvailable = models.BooleanField(default=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='physical_books')

    def __str__(self):
        return f'{self.shelfLocation}, {self.isAvailable} {self.book.title}'

    # @admin.display(ordering='book__title')
    def title(self):
        return self.book.title


    class Meta:
        ordering = ['shelfLocation']

class DigitalBook(models.Model):
    fileSize = models.FloatField()
    download_link = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='digital_books')

    def __str__(self):
        return {self.book}

class Member(models.Model):
    memberId = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    borrowed_books = models.OneToOneField(PhysicalBook, related_name='borrowers', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.memberId}, {self.name} {self.borrowed_books.bulk_create}'


class Library(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='libraries')
    members = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='libraries')

    def __str__(self):
        return f'Library: {self.pk}'