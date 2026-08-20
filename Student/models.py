from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class JobDetails(models.Model):
    role=models.CharField(max_length=1500,blank=True,null=True)
    company_name=models.CharField(max_length=1500,blank=True,null=True)
    experience=models.CharField(max_length=1500,blank=True,null=True)
    ctc=models.CharField(max_length=1500,blank=True,null=True)
    link=models.CharField(max_length=1500,blank=True,null=True)
    location=models.CharField(max_length=1500,blank=True,null=True)
    def __str__(self):
        return self.company_name
class PlacementDetails(models.Model):
    name=models.CharField(max_length=30)
    company_name=models.CharField(max_length=150)
    department=models.CharField(max_length=50)
    ctc=models.FloatField(default=0)
    batch=models.CharField(max_length=50)
    def __str__(self):
        return self.name+"("+self.batch+")"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(blank=False,max_length=30,null=False,default="WYD")
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True,default=settings.DEFAULT_PROFILE_PIC)
    cgpa = models.FloatField(null=True, blank=True)
    batch = models.CharField(max_length=20, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    def __str__(self):
        return self.user.username

