from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Projects, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime as dt
from .serializers import ProfileSerializer, ProjectSerializer
from django.http import JsonResponse
from .forms import SignUpForm, NewProjectForm, ProfileUpdateForm
from rest_framework import status


# Create your views here.

def page(request):
    
    projects = Projects.get_projects()
    

    return render(request, 'page.html', {"projects":projects})


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
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Owner = current_user
            project.save()
        return redirect('page')

    else:
        form = NewProjectForm()
    return render(request, 'online/new-project.html', {"form": form})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Projects.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
        

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

#class ProjectDescription(APIView):
#    permission_classes = (IsAdminOrReadOnly,)
#    def get_merch(self, pk):
#        try:
#            return ProjectMerch.objects.get(pk=pk)
#        except ProjectMerch.DoesNotExist:
#            return Http404

#    def get(self, request, pk, format=None):
#        merch = self.get_merch(pk)
#        serializers = ProjectSerializer(merch)
#        return Response(serializers.data)

@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    Owner = current_user
    projects = Projects.get_by_owner(Owner)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'profiles/profile.html', {"form":form, "projects":projects})






@login_required(login_url='/accounts/login/')
def search_results(request):
    
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'online/search.html',{"message":message,"projects": searched_projects})

    else:
     message = ",Have an amazing website you want to showcase ,post it here"
     return render(request, 'online/search.html',{"message":message})

def get_project(request, id):

    try:
        project = Projects.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()
    
    
    return render(request, "online/projects.html", {"project":project})

