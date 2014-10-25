from django.db import models

# Create your models here.
class Book(models.Model):
    available = models.BooleanField(default=True)
    image = models.FileField(upload_to='books')
    thumbnail = models.FileField(upload_to='books/thumbnail')

class Person(models.Model):
    name = models.CharField(max_length = 255)
    added = models.DateTimeField(auto_now_add = True)
    book_claimed = models.ForeignKey("Book", related_name = "claimed_by")

#    class Meta:
#            order_with_respect_to = 'added'
