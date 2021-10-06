from django.db import models

# Create your models here.
class department(models.Model):
    branch=models.CharField(max_length=50)
    
    def __str__(self):
        return self.branch

class student(models.Model):
    dep=models.ForeignKey(department,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=30)
def __str__(self):
        return self.dep

class lecture(models.Model):
    name=models.CharField(max_length=30)
    depart=models.ManyToManyField(department)
    

    def __str__(self):
        return self.name

