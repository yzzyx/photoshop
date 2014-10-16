# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'books')),
                ('thumbnail', models.FileField(upload_to=b'books/thumbnail')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('book_claimed', models.ForeignKey(related_name=b'claimed_by', to='books.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
