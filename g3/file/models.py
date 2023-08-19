from django.db import models


class student(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='student')
# Create your models here.
