from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Registration_Model(models.Model):
    User_Forgn=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    User_Contact=models.CharField(max_length=15)
    User_Address=models.CharField(max_length=100)
    User_Gender=models.CharField(max_length=10)
    User_Photo=models.ImageField(upload_to='image/',null=True,blank=True)
    status=models.CharField(max_length=255,default="")


class Course_Model(models.Model):
    Course_Name=models.CharField(max_length=20)
    Course_Fee=models.IntegerField()
    About_Course=models.CharField(max_length=1000)
    Duration=models.CharField(max_length=100)
    BG_Image=models.ImageField(upload_to='image/',null=True,blank=True)

class Course_Joining_Model(models.Model):
    Course_Joining_Forgn=models.ForeignKey(Course_Model,on_delete=models.CASCADE,null=True)
    User_Course_Joining_Forgn=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Joining_Date=models.DateField(auto_now_add=True)

class Course_Notes_Model(models.Model):
    Course_Forgn=models.ForeignKey(Course_Model,on_delete=models.CASCADE,null=True)
    Course_Discription=models.CharField(max_length=3000)
    Bg_Image=models.ImageField(upload_to='image/')
    PDF_Note=models.FileField(null=True,blank=True,upload_to='document/')


class Teacher_Model(models.Model):
    Name=models.CharField(max_length=30)
    Gender=models.CharField(max_length=10)
    Teacher_Course_Name=models.ForeignKey(Course_Model,on_delete=models.CASCADE,null=True)



