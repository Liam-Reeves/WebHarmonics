from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models

from interface.models import Education, Profile

from  .forms import ContactForm



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
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            email= form.cleaned_data['email']
            message= form.cleaned_data['message']

            return redirect ('contact_success')

        else:
            form = ContactForm()

    return render(request, "contact.html",{'form': form} )



def contact_success(request):
    return render(request, 'contact_success.html')

def resume(request):
    return render(request, "resume.html")

















