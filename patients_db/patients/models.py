from django.db import models
from typing import List

class MedicalRecord(models.Model):
    date = models.DateField()
    content = models.TextField()

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_records = models.JSONField(default=list)
    
    def __str__(self):
        return self.name



    