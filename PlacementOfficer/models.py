from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from Student.models import *
# Create your models here.
class ProfilePO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(blank=False,max_length=30,null=False,default="WYD")
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True,default=settings.DEFAULT_PROFILE_PIC)

class OnCampusJobs(models.Model):
    company_name=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    ctc=models.FloatField()
    description=models.TextField(max_length=5500)
    def __str__(self):
        return self.company_name
    
class StudentOnCampusJobs(models.Model):
    company_id=models.ForeignKey(OnCampusJobs,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Profile, on_delete=models.CASCADE)
