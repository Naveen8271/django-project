
from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
        
    def __str__(self): 
        return  f"{self.name}-{self.rollno}"
from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    photo = models.ImageField(upload_to='student_photos/',blank=True,null=True)
        
    def __str__(self): 
        return f"{self.name} - {self.patient_id}"
