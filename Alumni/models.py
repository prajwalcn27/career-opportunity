from django.db import models

# Create your models here.
class InterviewExperience(models.Model):
    name =models.CharField(max_length=30)
    batch =models.IntegerField()
    linkedin =models.CharField(max_length=300)
    company =models.CharField(max_length=30)
    experience =models.TextField(max_length=3500)
    def __str__(self):
        return self.name