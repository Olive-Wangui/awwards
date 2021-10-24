from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def project(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'project.html', context)