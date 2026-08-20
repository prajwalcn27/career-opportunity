from django.shortcuts import render,HttpResponse,redirect
from Alumni.models import *
from Student.models import *

def alumni_home(request):
    return HttpResponse("Ahome")

def interview_exp(request):
    msg=""
    if request.method == 'POST':
        name = request.POST.get('name')
        batch = request.POST.get('batch')
        linkedin = request.POST.get('linkedin')
        company = request.POST.get('company')
        experience = request.POST.get('experience')
        interview_exp=InterviewExperience(name=name,batch=batch,linkedin=linkedin,company=company,experience=experience)
        msg="Thank your experience is recorded"
        interview_exp.save()
        return redirect('alumni_home')
       
    return render(request,'Alumni/InterviewExperience.html',{"msg":msg})
