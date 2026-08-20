from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User,auth
from Student.models import *
from django.db.models import Count
from django.template import loader
import pdfkit
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from Alumni.models import *
from PlacementOfficer.models import *
import logging
# Create your views here.
def main_page(request):
    return HttpResponse("hello")

def s_login(request):
    message=""
    if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']
     user=auth.authenticate(username=username,password=password)
     if user is not None:
       auth.login(request,user)
       print("user verified",user.username)
       return redirect('/StudentHome')
     else:
       message="Invalid credentials"
    return render(request,'Student/login.html',{'message':message}) 

def s_logout(request):
  auth.logout(request)
  print("logged out")
  return redirect('/StudentLogin')  

def s_signup(request):
   if(request.method=="POST"):
    first_name=request.POST['firstName']
    last_name=request.POST['lastName']
    username=request.POST['username']
    password1=request.POST['password1']
    password2=request.POST['password2']
    email=request.POST['email']
    department=request.POST['department']
    batch=request.POST['batch']
    user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
    profile=Profile.objects.create(username=username,user=user,name=first_name+" "+last_name,email=email,batch=batch,department=department)
    print("User saved")
    return redirect('/StudentLogin')
   else:
    return render(request,'Student/signup.html')

def s_profile(request,username):
   profile =Profile.objects.get(username=username)
   user_profile={}
   return render(request, 'Student/profile.html', {'profile': profile})

def s_edit_profile(request,username):
   profile =Profile.objects.get(username=username)
   if request.method=='POST':
      name=request.POST['name']
      email=request.POST['email']
      cgpa=request.POST['cgpa']
      if 'profile_picture' in request.FILES:#check if profile picture is passed or not in the form
            profile_picture = request.FILES['profile_picture']
            profile.profile_picture = profile_picture #save the profile picture
      profile.name=name
      profile.cgpa=cgpa
      profile.email=email
      profile.save()#creating object
      return redirect('s_profile',profile.username)
   
   return render(request, 'Student/editprofile.html', {'profile': profile})

def s_home(request):
    return render(request,'Student/StudentHomePage.html')

def s_oncampus(request):
    jobs = OnCampusJobs.objects.all()
    return render(request, 'Student/StudentOnCampus.html', {'jobs': jobs})

def job_details(request,pk):
    job = get_object_or_404(OnCampusJobs, pk=pk)
    
    if request.method == 'POST':
        # Assuming you have the current student logged in and stored in `request.user.profile`
        student = request.user.profile
        # Create a new StudentOnCampusJobs object
        student_job = StudentOnCampusJobs(company_id=job, student_id=student)
        student_job.save()
        return redirect('s_oncampus')
    return render(request, 'Student/JobDetails.html', {'job': job})

def roadmap_resources(request):
    return render(request,'Student/roadmap.html')

def resume_builder(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        linkedin=request.POST.get("linkedin","")
        skills=request.POST.get("skills","")
        summary=request.POST.get("summary","")
        phone=request.POST.get("phone","")
        university=request.POST.get("university","")
        degree=request.POST.get("degree","")
        cgpa_degree=request.POST.get("cgpa_degree","")
        school_12=request.POST.get("school_12","")
        cgpa_12=request.POST.get("cgpa_12","")
        school_10=request.POST.get("school_10","")
        cgpa_10=request.POST.get("cgpa_10","")
        project1_name=request.POST.get("project1_name","")
        project1_link=request.POST.get("project1_link","")
        project2_name=request.POST.get("project2_name","")
        project2_link=request.POST.get("project2_link","")
        profile={"name":name,"email":email,'linkedin':linkedin,"skills":skills,"summary":summary,"phone":phone,"university":university,"degree":degree,
                 "school_10":school_10,"school_12":school_12,"cgpa_degree":cgpa_degree,"cgpa_12":cgpa_12,"cgpa_10":cgpa_10,
                 "project1_name":project1_name,"project2_name":project2_name,"project1_link":project1_link,"project2_link":project2_link
                 }
        return build_resume(request,profile)
        
        #return render(request,'Student/resume.html',{'profile':profile,'sk_list':sk_list})
    return render(request,'Student/accept.html')

def build_resume(request,profile):
    skill_string=profile['skills']
    sk_list=skill_string.split(",")
    for s in sk_list:
        print(s)
    template=loader.get_template('Student/trial.html')
    html=template.render({'profile':profile,'sk_list':sk_list})
    options={
        'page-size':'Letter',
        'encoding':"UTF-8",
        'enable-local-file-access': "",
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename="resume.pdf"
    return response

def splacement_stats (request):
    result1= PlacementDetails.objects.values('department').annotate(total=Count('department'))
    result2= PlacementDetails.objects.values('batch').annotate(total=Count('batch'))
    result3= PlacementDetails.objects.values('company_name').annotate(total=Count('company_name'))
    dept = []
    dept_count= []
    for item in result1:
      dept.append(item['department'])
      dept_count.append(item['total'])
    dept_data=zip(dept,dept_count)
    company=[]
    company_count=[]
    for item in result3:
       company.append(item['company_name'])
       company_count.append(item['total'])
    company_data=zip(company,company_count)
    batch=[]
    batch_count=[]
    for item in result2:
       batch.append(item['batch'])
       batch_count.append(item['total'])
    batch_data=zip(batch,batch_count)
    return render(request,'Student/placementstats.html',{'dept':dept,'dept_count':dept_count,'company':company,
                  'company_count':company_count,'batch':batch,'batch_count':batch_count,'dept_data':dept_data,
                  'company_data':company_data,'batch_data':batch_data})
 


def off_campus(request):
    page=requests.get('https://www.placementindia.com/job-search/search.php?seeker_search_keyword=developer+engineer&seeker_search_city=&seeker_search_experience=0')
    soup=BeautifulSoup(page.text,'html.parser')
    role_list=[]
    company_list=[]
    exp_list=[]
    ctc_list=[]
    l_list=[]
    jd=JobDetails.objects.all()
    if(jd!=None):
       jd.delete()
    for link in soup.find_all('a',class_='job-name'):
        role=link.text
        role_list.append(role)
    for link in soup.find_all('a',class_='job-name'):
        lnk=link.get('href')
        l_list.append(lnk)  
    cmpnylst=soup.find_all('p',class_='job-cname')#get the company name in list
    for cl in cmpnylst:
        c_name=cl.text
        company_list.append(c_name)
    lst=soup.find_all('ul',class_='sjci-need')
    li1=[]
    li2=[]
    li3=[]
    for l in lst:
        li_tag=l.find_all('li')
        if(len(li_tag)==2):
          for i in range(0,2):
              if(i==0):
                li1.append(li_tag[i].text)
              else:
                li3.append(li_tag[i].text)
          li2.append("Not disclosed")      
        else:
          for i in range(0,3):
             if(i==0):
                li1.append(li_tag[i].text)
             elif(i==1):
                li2.append(li_tag[i].text)
             else:
                li3.append(li_tag[i].text)   
    for i in range(0,len(company_list)):
        role=role_list[i]
        c_name=company_list[i]
        lnk=l_list[i]
        exp=li1[i]
        ctc=li2[i]
        loc=li3[i]
        JobDetails.objects.create(company_name=c_name,role=role,link=lnk,ctc=ctc,location=loc,experience=exp)
    role=request.GET.get('name')
    if role:
       jd=JobDetails.objects.filter(role__icontains=role)
    else:
       jd=JobDetails.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(jd,8)
    jd=paginator.page(page)
    return render(request,'Student/offcampus.html',{'jd':jd})

def student_interview_exp(request):
   interviews=InterviewExperience.objects.all()
   return render(request,'Student/InterviewExperience.html',{'interviews':interviews})

def placed_students(request):
    students = PlacementDetails.objects.all()
    if 'batch' in request.GET:
        batch = request.GET['batch']
        students = students.filter(batch=batch)
    return render(request, 'Student/PlacedStudents.html', {'students': students})

def add_placement(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        department = request.POST.get('department')
        ctc = request.POST.get('ctc')
        batch = request.POST.get('batch')
        
        new_placement = PlacementDetails(name=name, company_name=company_name, department=department, ctc=ctc, batch=batch)
        new_placement.save()
        
        return redirect('placed_students')  # Redirect to placement list page after adding
    return render(request, 'Student/AddPlacement.html')