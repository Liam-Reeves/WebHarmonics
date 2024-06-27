from django.db import models

# Create your models here.
class Education(models.Model):
    level = models.CharField(max_length=100, blank= False)
    course_name= models.CharField(max_length=100, blank=False)
    institution = models.CharField(max_length=100, blank= False)

def __str__(self):
    return self.level
    
class Meta:
    verbose_name_plural = "Education"





   


