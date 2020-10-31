from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Projects, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from django.http import JsonResponse
#from .forms import EventLetterForm, NewEventForm


# Create your views here.

def registerPage(request):
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('page.html')
     else:
        form = SignUpForm()
        return render(request, 'registration/registration_form.html', {'form': form})
def page(request):
   return render(request, 'page.html')

@login_required(login_url='/accounts/login/')
def search_results(request):
    
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'online/search.html',{"message":message,"projects": searched_projects})

    else:
     message = "Stay home and remember to sanitize"
     return render(request, 'online/search.html',{"message":message})

