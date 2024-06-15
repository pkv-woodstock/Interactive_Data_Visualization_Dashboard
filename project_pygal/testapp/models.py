from django.db import models

# Create your models here.
class Employee(models.Model):
    department = models.CharField(max_length=255)
    strength = models.IntegerField()

    def __str__(self):
        return self.department
