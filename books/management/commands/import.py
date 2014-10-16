from django.core.management.base import BaseCommand, CommandError
from books.models import Book
from django.core.files import File
import os

class Command(BaseCommand):
    def handle(self, *args, **options):

        for filename in os.listdir('files'):
            filename = os.path.join('files',filename)
            if os.path.isfile(filename):
                with open(filename, "rb") as f:
                    b = Book()
                    b.image = File(f)
                    thumbnail = os.path.join(os.path.dirname(filename),
                    'thumbnails', os.path.basename(filename))
                    with open(thumbnail, "rb") as tn:
                        b.thumbnail = File(tn)
                        b.save()
