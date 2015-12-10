from django.db import models
from django.contrib.auth.models import User

"""
class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    dbname = models.CharField(max_length=30)
    plan = models.CharField(default="free",max_length=30)
    

    #other fields here

    def __str__(self):  
          return "%s's profile" % self.user  
"""

