# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from books.models import Book, Person

# Create your views here.
def index(request):
    return render(request, "index.html", { 'books' : Book.objects.all() })

def book(request,id):
    book = get_object_or_404(Book, pk=id)
    errormessage = None

    if not book.available:
        errormessage = "Denna bok är redan tagen!"
    elif request.method == 'POST':
        if len(request.POST['name']) == 0:
            errormessage = "Du måste fylla i ett namn!"
        else:
            person = Person()
            person.name = request.POST['name']
            person.book_claimed = Book.objects.get(pk=id)

            person.save()
            return HttpResponseRedirect(reverse("books:book", args=[id]))

    return render(request, "book.html", { 'book' : book, 'errormessage' : errormessage })
