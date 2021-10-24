from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from user.forms import ProjectForm
from .models import *
from .forms import *
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    projects = Project.get_projects()
    context = {
        'projects': projects,
    }
    return render(request, 'home.html', context)

@login_required
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
                'form': form,
            }
    return render(request, 'project.html', context)

@login_required
def profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    Project = Project.objects.filter(profile_id=profile).all()
    
    context = {
        'profile': profile,
        'project': project,
    }
    return render(request, 'profile.html', context)

@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/')

@login_required
def new_profile(request):
    project = Project.objects.filter(author=request.user).order_by('-date_posted')
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'project' : project
    }
    return render(request, 'profile/profile.html', context)




