from django.contrib import admin
from models import Book, Person

class PersonInline(admin.TabularInline):
    model = Person

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'available', 'claimed_by_list')
    ordering = ('id',)
    inlines = [ PersonInline, ]

    def claimed_by_list(self, obj):
        return ",".join([k.name for k in obj.claimed_by.all()])

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Person, PersonAdmin)
