from django.contrib import admin
from Student.models import *
from Alumni.models import *
from PlacementOfficer.models import *
# Register your models here.
admin.site.register(JobDetails)
admin.site.register(Profile)
admin.site.register(InterviewExperience)