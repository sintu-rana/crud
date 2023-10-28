from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    mobile=models.CharField(max_length=10)
    city=models.TextField()
    pic=models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name