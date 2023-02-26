from django.db import models

# Create your models here.

class FatherAccount(models.Model):
    full_name= models.CharField(max_length=1024)
    id_nummber=models.IntegerField()
    age=models.IntegerField()
    date_of_birth=models.DateField()
    email=models.EmailField()

