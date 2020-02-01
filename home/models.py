from django.db import models
from django.utils import timezone  #above one is to get current date and time
from django.contrib.auth.models import User #inbuilt user class derieved by Django!!!!!!

# Create your models here.
#class Author(models.Model):
   # username=models.CharField(max_length=25,unique=True) # for every Charfield we need to specify maximum length....
   # fname=models.CharField(max_length=20)
   # lname=models.CharField(max_length=20)
   # email=models.EmailField() #It dont Require maximum length
   # timestamp=models.DateTimeField(default=timezone.now()) #default attribute can be used everywhere 
   # def __str__(self):
   #    return self.username+" "+self.fname+" " # For returning multiple values to the response....


class post(models.Model):
   title=models.CharField(max_length=150)
   content=models.TextField() # for large text content
   posted_on=models.DateTimeField(default=timezone.now())
   posted_by=models.ForeignKey(User,on_delete=models.CASCADE) #we need foreign key as we need reference from another table...
   def __str__(self):
      return self.title+" by "+str(self.posted_by)
    # on_delete is used..when...if entry from one table will get deleted then other fiels depended upon it should be affect soo on_delete is used...


class contactus(models.Model):
   name=models.CharField(max_length=20)
   email=models.EmailField()
   message=models.TextField()
   timestamp=models.DateTimeField(default=timezone.now)
   def __str__(self):
      return self.name