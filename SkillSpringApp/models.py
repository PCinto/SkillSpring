from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname+" "+self.lastname

class Products(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50, default="Data Science")
    phone = models.IntegerField(default=0)
    email = models.EmailField()
    origin = models.CharField(max_length=50, default="Kenya")
    time = models.CharField(max_length=30, default="white")

    def __str__(self):
        return self.name
