from django.db import models

# Create your models here.

class LoginUser(models.Model):
    user_name       = models.CharField(max_length=120)
    user_email      = models.EmailField(max_length=254,unique=True, null=False, blank=True)
    user_phone      = models.CharField(max_length=15,unique=True)
    user_password   = models.CharField(PasswordInput)