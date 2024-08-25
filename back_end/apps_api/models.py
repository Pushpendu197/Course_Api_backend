from django.db import models

# Create your models here.
class Course(models.Model):
    course_id= models.BigAutoField(primary_key=True)
    course_title= models.CharField(max_length=100)
    course_code= models.CharField(max_length=100)
    course_desc= models.TextField()

class Instances(models.Model):
    instances_id= models.BigAutoField(primary_key=True)
    instances_title= models.CharField(max_length=100)
    instances_year= models.CharField(max_length=100)
    instances_sem= models.CharField(max_length=100)



    def __str__(self) -> str:
        return self.course_title