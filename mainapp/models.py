from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import BaseAbstract

# Create your models here.

class User(AbstractUser):
    is_admin    = models.BooleanField(default=False)
    is_student  = models.BooleanField(default=False)
    is_teacher  = models.BooleanField(default=False)

class School(BaseAbstract):
    name        = models.CharField(max_length=255)
    establish   = models.DateField(auto_now=False, auto_now_add=False)
    affliated_by= models.CharField(max_length=120, default=False)
    board_type  = models.CharField(max_length=100, default=False)
    address     = models.CharField(max_length=255)
    city        = models.CharField(max_length=255)
    state       = models.CharField(max_length=255)
    country     = models.CharField(max_length=255)
    zip         = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Sessions(BaseAbstract):
    schoolid        = models.ForeignKey(School, related_name='school_session')
    session_years   = models.CharField(max_length=50)
    comments        = models.CharField(max_length=250)

    def __str__(self):
        return self.session_years







