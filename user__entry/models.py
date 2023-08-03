from django.db import models

# Create your models here.
class Member(models.Model):
    username=models.CharField(max_length=20)
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    password=models.CharField(max_length=30)

    def __str__(self):
        #to display specific details on the database interface do this ---call the required items...
       return self.Fname+'  '+ self.Lname

