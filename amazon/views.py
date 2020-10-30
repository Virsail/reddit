from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
#from .models import Event, NewsLetterRecipients
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
            return redirect('today-events.html')
     else:
        form = SignUpForm()
        return render(request, 'registration/registration_form.html', {'form': form})


