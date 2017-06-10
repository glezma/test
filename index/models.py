# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class SignUp(models.Model):
    """ sign up model """
    email_signup = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email_signup + ' - ' + self.first_name
#
class LogIn(models.Model):
    """ Login model """
    email_login = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    date_login = models.DateTimeField()
    def __str__(self):
        return self.email_login.email_signup + ' - ' + str(self.date_login)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_login = timezone.now()
        return super(LogIn, self).save(*args, **kwargs)

# class User(models.Model):
#     created     = models.DateTimeField(editable=False)
#     modified    = models.DateTimeField()

#     def save(self, *args, **kwargs):
#         ''' On save, update timestamps '''
#         if not self.id:
#             self.created = timezone.now()
#         self.modified = timezone.now()
#         return super(User, self).save(*args, **kwargs)
    
    
