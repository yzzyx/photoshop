from django.contrib import admin
from models import Book, Person

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'available')
    ordering = ('id',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Person, PersonAdmin)
