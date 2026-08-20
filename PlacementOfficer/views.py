from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User,auth
from PlacementOfficer.models import *
# Create your views here.

def po_login(request):
    message=""
    if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']
     user=auth.authenticate(username=username,password=password)
     if user is not None:
       auth.login(request,user)
       print("user verified",user.username)
       return redirect('po_home')
     else:
       message="Invalid credentials"
    return render(request,'PlacementOfficer/login.html',{'message':message}) 

def po_logout(request):
  auth.logout(request)
  print("logged out")
  return redirect('po_login')  

def po_signup(request):
   if(request.method=="POST"):
    first_name=request.POST['firstName']
    last_name=request.POST['lastName']
    username=request.POST['username']
    password1=request.POST['password1']
    password2=request.POST['password2']
    email=request.POST['email']
    user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
    profile=ProfilePO.objects.create(username=username,user=user,name=first_name+" "+last_name)
    print("User saved")
    return redirect('po_login')
   else:
    return render(request,'PlacementOfficer/signup.html')
def po_home(request):
    oncampus_jobs=OnCampusJobs.objects.all()
    return render(request,'PlacementOfficer/PlacementOfficerHome.html',{'oncampus_jobs':oncampus_jobs})


def view_company(request, pk):
    company = get_object_or_404(OnCampusJobs, pk=pk)
    return render(request, 'PlacementOfficer/view_company.html', {'company': company})

def view_student(request,job_id):
    student_jobs = StudentOnCampusJobs.objects.filter(company_id_id=job_id)
    # Extract the student IDs associated with the filtered jobs
    student_ids = student_jobs.values_list('student_id', flat=True)
    # Retrieve profiles whose IDs are in student_ids
    profiles = Profile.objects.filter(id__in=student_ids)
    '''for p in profiles:
       print(p.name," ",p.cgpa," ",p.email)'''
    return render(request, 'PlacementOfficer/StudentDetails.html',{'profiles': profiles})
    
    

def delete_company(request, pk):
    company = get_object_or_404(OnCampusJobs, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('po_home')
    return render(request, 'PlacementOfficer/confirm_delete.html', {'company': company})

def add_company(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        role = request.POST.get('role')
        ctc = request.POST.get('ctc')
        description = request.POST.get('description')
        
        # Create a new OnCampusJobs instance and save it
        new_company = OnCampusJobs(company_name=company_name, role=role, ctc=ctc, description=description)
        new_company.save()
        
        return redirect('po_home')  # Redirect to company list page after adding
    return render(request, 'PlacementOfficer/AddCompany.html')


    
def po_placement_stats (request):
    return HttpResponse("POPlacementStats")

