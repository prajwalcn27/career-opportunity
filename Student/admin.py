from django.contrib import admin
from Student.models import *
from PlacementOfficer.models import *
# Register your models here.
admin.site.register(PlacementDetails)
admin.site.register(OnCampusJobs)
admin.site.register(StudentOnCampusJobs)