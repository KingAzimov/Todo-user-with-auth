from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    fullname=models.CharField(max_length=50)
    guruh=models.CharField(max_length=50, blank=True)
    st_raqam=models.CharField(max_length=50, blank=True)
    tel=models.CharField(max_length=50, blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self): return self.fullname

class TODO (models.Model):
    title=models.CharField(max_length=50)
    time=models.DateField()
    description=models.CharField(max_length=150)
    status=models.CharField(max_length=50)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    def __str__(self): return self.title