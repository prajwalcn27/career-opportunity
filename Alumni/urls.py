from django.contrib import admin
from django.urls import path
from Alumni import views
urlpatterns = [
    path('AlumniHome/',views.alumni_home,name="alumni_home"),
    path('AlumniInterviewExperience/',views.interview_exp,name="interview_exp"),
    
    
]