from __future__ import unicode_literals
from django.db import models

class book_issue(models.Model):
  bookname = models.CharField(max_length = 40)  
  author = models.CharField(max_length = 30)
  book_id = models.IntegerField(default=0)
  issue_date = models.DateTimeField()
  return_date = models.DateTimeField()