from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Places
from math import ceil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,'web/index2.html')

def about(request):
	return render(request,'web/about.html')

def search(request):
	
	return render(request,'web/test.html')

def index(request):
    places= Places.objects.all()
    n= len(places)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'place': places}
    return render(request,"web/index.html", params)


def register(request):
	if request.method =="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			return redirect("web:home")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = UserCreationForm
	return render(request,
				  "web/register.html",
				  context = {"form":form})