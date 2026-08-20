from django.contrib import admin
from django.urls import path
from PlacementOfficer import views
urlpatterns = [
    path('POLogin/',views.po_login,name="po_login"),
    path('POSignUp/',views.po_signup,name="po_signup"),
    path('POHome/',views.po_home,name="po_home"),
   
    path('POPlacementStats/',views.po_placement_stats,name="po_placement_stats"),
    path('Company/<int:pk>/', views.view_company, name='view_company'),
    path('Company/<int:pk>/delete/', views.delete_company, name='delete_company'),
    path('StudentDetails/<int:job_id>',views.view_student,name="view_student"),
    path('AddCompany/', views.add_company, name='add_company'),
   
]