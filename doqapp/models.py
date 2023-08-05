from django.db import models

class task(models.Model):
     Title=models.CharField(max_length=50)
     description=models.CharField(max_length=200)
     due_date=models.DateField()
     completion_status=models.CharField(max_length=50)

     
    
