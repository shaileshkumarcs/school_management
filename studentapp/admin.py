from django.contrib import admin
from .models import StudentProfile


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name','image', 'rollno']


# Register your models here.
admin.site.register(StudentProfile, StudentProfileAdmin)
