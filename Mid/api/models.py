from django.db import models

class BookJournalBase (models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    created_at=models.CharField(max_length=100)

class Book(BookJournalBase):
    num_pages=models.IntegerField()
    janre=models.CharField(max_length=100)

class Journal(BookJournalBase):
    type=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
