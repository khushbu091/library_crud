from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=50)

    # class Meta:
    #     db_table='Student'

    # def __str__(self):
    #     return self.Name

class Query(models.Model):
    Tittle=models.CharField(max_length=100)
    Dec=models.CharField(max_length=200)
    Email=models.EmailField()
    Password=models.CharField(max_length=50, null=True)
    # class Meta:
    #     db_table='User'
    # def __str__(self):
    #     return self.Tittle
