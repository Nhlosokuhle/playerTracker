from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['username']
        username = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        user.save()
        return HttpResponseRedirect(reverse('playerTrainingSystem:manage_players'))
    else:
        return render(request, 'signup.html')

def user_login(request):
    return render(request, 'signin.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('playerTrainingSystem:manage_players'))
