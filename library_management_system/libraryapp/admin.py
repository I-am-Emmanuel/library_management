from django.contrib import admin

from . import models
from . models import Book, Member, DigitalBook, PhysicalBook, Library

# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'isbn', 'date_published']
    search_fields = ['title', 'authors', 'isbn']
    list_editable = ['authors', 'isbn']

@admin.register(models.PhysicalBook)
class PhysicalBookAdmin(admin.ModelAdmin):
    list_display = ['shelfLocation', 'isAvailable', 'title']
    search_fields = ['book__title', 'book__isbn']
    list_select_related = ['book']



@admin.register(models.DigitalBook)
class DigitalAdmin(admin.ModelAdmin):
    list_display = ['fileSize', 'download_link', 'book']
    search_fields = ['book__title', 'book__isbn']


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'memberId', ]


admin.site.register(Library)

