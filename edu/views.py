from django.shortcuts import render

# Create your views here.
def skill(request):
    return render(request,'edu/skill.html')
def certificate(request):
    return render(request,'edu/certificate.html')
def resume(request):
    return render(request,'edu/resume.html')
def projects(request):
    return render(request,'edu/projects.html')