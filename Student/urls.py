from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    
    path('',views.main_page,name="main_page"),
    path('StudentLogin/',views.s_login,name="s_login"),
    path('s_logout/',views.s_logout,name="s_logout"),
    path('StudentSignUp/',views.s_signup,name="s_signup"),
    path('StudentHome/',views.s_home,name="s_home"),
    path('StudentOnCampus/',views.s_oncampus,name="s_oncampus"),
    path('StudentPlacementStats/',views.splacement_stats,name="splacement_stats"),
    path('StudentOffcampus/',views.off_campus,name="off_campus"),
    path('StudentResumeBuilder/',views.resume_builder,name="resume_builder"),
    path('StudentProfile/<str:username>/',views.s_profile,name="s_profile"),
    path('EditProfile/<str:username>/',views.s_edit_profile,name="s_edit_profile"),
    path('StudentInterviewExperience/',views.student_interview_exp,name="student_interview_exp"),
    path('StudentRoadmapAndResources/',views.roadmap_resources,name="roadmap_resources"),
    path('PlacedStudents/', views.placed_students, name='placed_students'),
    path('StudentOnCampus/<int:pk>/',views.job_details,name="job_details"),
    path('StudentAddPlacement/', views.add_placement, name='add_placement'),
]