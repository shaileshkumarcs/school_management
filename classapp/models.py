from django.db import models

from common.models import BaseAbstract
from mainapp.models import Sessions, User
from teachersapp.models import TeacherProfile

# Create your models here.
class Class(BaseAbstract):
    sessions    = models.ForeignKey(Sessions, related_name="class_year")
    teacher     = models.OneToOneField(TeacherProfile,on_delete=models.CASCADE)
    classname   = models.CharField(max_length=50)
    classcode   = models.CharField(max_length=20)
    created_by  = models.ForeignKey(User, related_name="class_createdby")

    def __str__(self):
        return self.classname
