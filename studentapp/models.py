from django.db import models

from mainapp.models import User

# Create your models here.

def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    #extension = filename.split(".")
    return "%s/%s" % (instance.id, filename)

class StudentProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender')
    )
    user            = models.ForeignKey(User, related_name='student_userid')
    rollno          = models.IntegerField()
    first_name      = models.CharField(max_length=100,blank=True)
    middle_name     = models.CharField(max_length=100,blank=True)
    last_name       = models.CharField(max_length=100, blank=True)
    gender          = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dateofbirth     = models.DateField(max_length=10, blank=True, auto_now_add=False, auto_now=False)
    phone           = models.CharField(max_length=15, blank=True)
    email           = models.EmailField(max_length=100, blank=True)
    religion        = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field    = models.IntegerField(default=0)
    width_field     = models.IntegerField(default=0)
    created_at      = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.first_name
