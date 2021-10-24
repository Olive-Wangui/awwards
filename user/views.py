from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def project(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'project.html', context)

@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')