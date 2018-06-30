import datetime
from django.db import models

class BaseAbstract(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, editable=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, editable=False)
    published  = models.BooleanField(default=True)

    class Meta:
        abstract =True