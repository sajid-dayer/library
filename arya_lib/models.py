from __future__ import unicode_literals

from django.db import models
class User_Login_List(models.Model):
  """Stores Info of user login.
  """
  username = models.CharField(max_length = 30)  
  password = models.CharField(max_length = 30)