from django.db import models

# Create your models here.

class Student(models.Model):
    roll_number = models.IntegerField()
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name
