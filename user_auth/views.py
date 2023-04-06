from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    """
    Registers a new user.

    If the request method is POST, this function retrieves the user's first name, email, and password
    from the request.POST dictionary, creates a new user object with the retrieved data, saves the user
    object to the database, and then redirects the user to the 'manage_players' page. If the request
    method is not POST, this function simply renders the signup.html template.

    :param request: The HttpRequest object containing the user's registration data.
    :type request: HttpRequest

    :returns: If the request method is POST, this function returns an HttpResponseRedirect object
    that redirects the user to the 'manage_players' page. If the request method is not POST, this
    function returns an HttpResponse object that renders the signup.html template.
    :rtype: HttpResponse or HttpResponseRedirect
    """
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
    """
    Displays the login page.

    This function renders the signin.html template, which displays a form that allows the user to log in.

    :param request: The HttpRequest object for the current request.
    :type request: HttpRequest

    :return: The rendered HTML response for the signin.html template.
    :rtype: HttpResponse
    """
    return render(request, 'signin.html')

def authenticate_user(request):
    """
    Authenticates a user and logs them in.

    This function retrieves the user's username and password from the request.POST dictionary, then
    attempts to authenticate the user with those credentials. If the authentication is successful,
    the function logs the user in by calling the login() function with the HttpRequest object and the
    authenticated user object. The function then redirects the user to the 'manage_players' page.
    If the authentication is not successful, the function redirects the user to the 'login' page.

    :param request: The HttpRequest object containing the user's login credentials.
    :type request: HttpRequest

    :returns: An HttpResponseRedirect object that redirects the user to either the 'manage_players'
    page (if the authentication was successful) or the 'login' page (if the authentication was not
    successful).
    :rtype: HttpResponse
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('playerTrainingSystem:manage_players'))
