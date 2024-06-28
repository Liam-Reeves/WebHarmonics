from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

from interface.models import Education, Profile



# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    context = {'profile': Profile.objects.all()}
    context['education'] = Education.objects.all()
 
    return render(request, "about.html", context)


def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def resume(request):
    return render(request, "resume.html")

















