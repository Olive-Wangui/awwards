from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from user.forms import ProjectForm
from .models import *
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    projects = Project.get_projects()
    context = {
        'projects': projects,
    }
    return render(request, 'home.html', context)

def project(request):
    current_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = ProjectForm(request.POST, request.FILES)
                if form.is_valid():
                    new_project = form.save(commit=False)
                    new_project.author = current_user
                    new_project.profile = profile
                    new_project.save()
                    return redirect('home')
            else:
                form = ProjectForm()
            
            context = {
                'user': current_user,
            }
    return render(request, 'project.html', context)

@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')