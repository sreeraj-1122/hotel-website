from django.db import models
from datetime import date
# Create your models here.

class room(models.Model):
    image=models.ImageField(max_length=5000)
    room_name=models.CharField(max_length=200)
    details=models.TextField()
    cost=models.FloatField()

    def __str__(self):
        return self.room_name
    
class roombooking(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    check_in=models.DateField()
    check_out=models.DateField()
    room=models.ForeignKey(room,on_delete=models.CASCADE)
    adults=models.IntegerField()
    childs=models.IntegerField()
    request=models.TextField()

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    

